#!/usr/bin/env python3
"""
Database utility module for Supabase PostgreSQL operations.
Includes comprehensive logging for all database actions.
"""
import os
import psycopg2
from psycopg2 import pool
from typing import Dict, List, Optional, Any
from datetime import datetime
from dotenv import load_dotenv

from .logger import setup_logger, log_operation, log_error, log_url_action, log_separator, get_emoji

# Load environment variables
load_dotenv()

# Setup logger
logger = setup_logger('gnews.db')

# Connection pool
connection_pool = None


def get_connection_pool():
    """
    Get or create database connection pool.

    Returns:
        Connection pool instance
    """
    global connection_pool

    if connection_pool is None:
        try:
            logger.info("Initializing database connection pool")
            log_operation(logger, 'db_pool_init', status='starting')

            connection_pool = psycopg2.pool.SimpleConnectionPool(
                1,  # minconn
                10,  # maxconn
                host=os.getenv('SUPABASE_HOST'),
                port=os.getenv('SUPABASE_PORT', '5432'),
                database=os.getenv('SUPABASE_DATABASE', 'postgres'),
                user=os.getenv('SUPABASE_USER'),
                password=os.getenv('SUPABASE_PASSWORD')
            )

            log_operation(logger, 'db_pool_init', status='success', min_conn=1, max_conn=10)
            logger.info("Database connection pool initialized successfully")

        except Exception as e:
            log_error(logger, 'db_pool_init', e, status='failed')
            raise

    return connection_pool


def get_db_connection():
    """
    Get a database connection from the pool.

    Returns:
        Database connection
    """
    try:
        pool = get_connection_pool()
        conn = pool.getconn()
        log_operation(logger, 'db_connection_get', status='success')
        return conn
    except Exception as e:
        log_error(logger, 'db_connection_get', e, status='failed')
        raise


def release_db_connection(conn):
    """
    Release a database connection back to the pool.

    Args:
        conn: Database connection to release
    """
    try:
        pool = get_connection_pool()
        pool.putconn(conn)
        log_operation(logger, 'db_connection_release', status='success')
    except Exception as e:
        log_error(logger, 'db_connection_release', e, status='failed')


def transform_category(category: str) -> str:
    """
    Transform category to title case format.

    Args:
        category: Original category string

    Returns:
        Title-cased category (e.g., 'artificial intelligence' -> 'Artificial Intelligence')
    """
    if not category:
        return ''

    # Title case each word
    transformed = ' '.join(word.capitalize() for word in category.split())

    logger.debug(f"Category transformed: '{category}' -> '{transformed}'")
    return transformed


def transform_authors(authors: List[str]) -> str:
    """
    Transform authors list to comma-separated string.

    Args:
        authors: List of author names

    Returns:
        Comma-separated author string
    """
    if not authors:
        return ''

    author_str = ', '.join(authors)
    logger.debug(f"Authors transformed: {authors} -> '{author_str}'")
    return author_str


def insert_article(article: Dict[str, Any], table_name: str = 'sources') -> Dict[str, Any]:
    """
    Insert a single article into the database with smart duplicate handling.

    Args:
        article: Article dictionary with fields to insert
        table_name: Name of the table (default: 'sources')

    Returns:
        Dict with status info: {'status': 'success'|'duplicate'|'failed', 'url': str, 'title': str, 'reason': str}
    """
    conn = None
    cursor = None

    # Extract title and URL early for logging
    title = article.get('title', '')
    url = article.get('url', '')

    try:
        # Extract and transform data according to mappings
        # Parse published date
        published_date = article.get('published date', '')
        utc = None
        if published_date:
            try:
                # Try parsing common date formats
                for fmt in ['%a, %d %b %Y %H:%M:%S %Z', '%Y-%m-%d %H:%M:%S.%f%z', '%Y-%m-%d %H:%M:%S%z']:
                    try:
                        utc = datetime.strptime(published_date, fmt)
                        break
                    except ValueError:
                        continue

                if utc is None:
                    logger.debug(f"Could not parse date: {published_date}")
            except Exception as e:
                logger.debug(f"Date parse error: {e}")

        # Extract publisher/source
        publisher = article.get('publisher', {})
        if isinstance(publisher, dict):
            source = publisher.get('title', '')
        else:
            source = str(publisher) if publisher else ''

        # Transform category to title case
        category = transform_category(article.get('category', ''))

        # Get full text
        text = article.get('full_text', '')

        # Transform authors to comma-separated string
        authors = article.get('authors', [])
        author = transform_authors(authors)

        # Prepare insert query with ON CONFLICT handling
        insert_query = f"""
            INSERT INTO {table_name} (title, utc, url, source, category, text, author)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (url) DO NOTHING
            RETURNING url
        """

        # Get connection and execute
        conn = get_db_connection()
        cursor = conn.cursor()

        logger.debug(f"Executing insert for article: {title[:100]}")
        cursor.execute(insert_query, (title, utc, url, source, category, text, author))

        # Check if row was inserted
        result = cursor.fetchone()
        conn.commit()

        if result:
            # Successfully inserted
            log_url_action(
                logger,
                'success',
                url,
                title,
                category=category,
                text_length=len(text) if text else 0
            )
            return {
                'status': 'success',
                'url': url,
                'title': title
            }
        else:
            # Duplicate URL - skipped
            log_url_action(
                logger,
                'duplicate',
                url,
                title,
                reason='URL already exists in database'
            )
            return {
                'status': 'duplicate',
                'url': url,
                'title': title
            }

    except Exception as e:
        if conn:
            conn.rollback()

        log_url_action(
            logger,
            'failed',
            url,
            title,
            error=str(e)
        )

        return {
            'status': 'failed',
            'url': url,
            'title': title,
            'reason': str(e)
        }

    finally:
        if cursor:
            cursor.close()
        if conn:
            release_db_connection(conn)


def insert_articles_batch(articles: List[Dict[str, Any]], table_name: str = 'sources') -> Dict[str, Any]:
    """
    Insert multiple articles into the database with detailed tracking.

    Args:
        articles: List of article dictionaries
        table_name: Name of the table (default: 'sources')

    Returns:
        Dictionary with counts and URL lists: {
            'success': int, 'duplicate': int, 'failed': int,
            'success_urls': list, 'duplicate_urls': list, 'failed_urls': list
        }
    """
    logger.info("")
    logger.info(f"{get_emoji('insert')} Inserting {len(articles)} articles into database table '{table_name}'...")
    logger.info("─────────────────────────────────────────")

    success_count = 0
    duplicate_count = 0
    failed_count = 0

    success_list = []
    duplicate_list = []
    failed_list = []

    for idx, article in enumerate(articles, 1):
        logger.info(f"{get_emoji('article')} [Article {idx}/{len(articles)}] Processing...")

        result = insert_article(article, table_name)

        if result['status'] == 'success':
            success_count += 1
            success_list.append({'url': result['url'], 'title': result['title']})
        elif result['status'] == 'duplicate':
            duplicate_count += 1
            duplicate_list.append({'url': result['url'], 'title': result['title']})
        else:  # failed
            failed_count += 1
            failed_list.append({
                'url': result['url'],
                'title': result['title'],
                'reason': result.get('reason', 'Unknown error')
            })

        logger.info("")  # Blank line for readability

    # Log comprehensive summary
    total = len(articles)
    logger.info("")
    log_separator(logger)
    logger.info(f"{get_emoji('summary')} BATCH INSERT SUMMARY")
    log_separator(logger)
    logger.info(f"{get_emoji('package')} Total Processed: {total}")
    logger.info(f"{get_emoji('success')} Successfully Inserted: {success_count} ({success_count/total*100:.1f}%)" if total > 0 else f"{get_emoji('success')} Successfully Inserted: 0 (0.0%)")
    logger.info(f"{get_emoji('duplicate')} Duplicates Skipped: {duplicate_count} ({duplicate_count/total*100:.1f}%)" if total > 0 else f"{get_emoji('duplicate')} Duplicates Skipped: 0 (0.0%)")
    logger.info(f"{get_emoji('failed')} Failed: {failed_count} ({failed_count/total*100:.1f}%)" if total > 0 else f"{get_emoji('failed')} Failed: 0 (0.0%)")
    logger.info("")

    # Log successful insertions
    if success_list:
        logger.info(f"{get_emoji('success')} Successful Insertions ({len(success_list)}):")
        for i, item in enumerate(success_list[:10], 1):  # Show first 10
            logger.info(f"  {i}. {get_emoji('url')} {item['url']}")
            logger.info(f"     {get_emoji('article')} {item['title'][:60]}...")
        if len(success_list) > 10:
            logger.info(f"  ... and {len(success_list) - 10} more")
        logger.info("")

    # Log duplicates
    if duplicate_list:
        logger.info(f"{get_emoji('duplicate')} Duplicates Skipped ({len(duplicate_list)}):")
        for i, item in enumerate(duplicate_list[:10], 1):  # Show first 10
            logger.info(f"  {i}. {get_emoji('url')} {item['url']}")
            logger.info(f"     {get_emoji('article')} {item['title'][:60]}...")
        if len(duplicate_list) > 10:
            logger.info(f"  ... and {len(duplicate_list) - 10} more")
        logger.info("")

    # Log failures
    if failed_list:
        logger.info(f"{get_emoji('failed')} Failed Insertions ({len(failed_list)}):")
        for i, item in enumerate(failed_list[:10], 1):  # Show first 10
            logger.info(f"  {i}. {get_emoji('url')} {item['url']}")
            logger.info(f"     {get_emoji('article')} {item['title'][:60]}...")
            logger.info(f"     {get_emoji('warning')} Error: {item['reason']}")
        if len(failed_list) > 10:
            logger.info(f"  ... and {len(failed_list) - 10} more")
        logger.info("")

    log_separator(logger)

    return {
        'success': success_count,
        'duplicate': duplicate_count,
        'failed': failed_count,
        'success_urls': success_list,
        'duplicate_urls': duplicate_list,
        'failed_urls': failed_list
    }


def test_connection() -> bool:
    """
    Test database connection.

    Returns:
        True if connection successful, False otherwise
    """
    try:
        log_operation(logger, 'db_test_connection', status='starting')

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()

        cursor.close()
        release_db_connection(conn)

        log_operation(logger, 'db_test_connection', status='success', db_version=str(version[0])[:100])
        logger.info(f"Database connection test successful: {version[0][:100]}")

        return True

    except Exception as e:
        log_error(logger, 'db_test_connection', e, status='failed')
        return False


def close_connection_pool():
    """
    Close all connections in the pool.
    """
    global connection_pool

    if connection_pool:
        try:
            log_operation(logger, 'db_pool_close', status='starting')
            connection_pool.closeall()
            connection_pool = None
            log_operation(logger, 'db_pool_close', status='success')
            logger.info("Database connection pool closed successfully")
        except Exception as e:
            log_error(logger, 'db_pool_close', e, status='failed')
