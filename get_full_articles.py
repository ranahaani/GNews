#!/usr/bin/env python3
"""
Script to fetch news articles with full text content and save to Supabase PostgreSQL.
Includes comprehensive logging to Grafana Loki.
"""
import json
import sys
import re
import requests
from bs4 import BeautifulSoup
from gnews import GNews
from datetime import datetime, timedelta, timezone
import time

# Import logging and database utilities
from gnews.utils.logger import (
    setup_logger, log_operation, log_error, log_url_action,
    log_separator, log_overall_summary, get_emoji
)
from gnews.utils.db import insert_articles_batch, test_connection, close_connection_pool

# Setup logger
logger = setup_logger('get_full_articles')

# Try to import Google News URL decoder
try:
    from googlenewsdecoder import new_decoderv1
    HAS_DECODER = True
    logger.info("Google News decoder available")
except ImportError:
    HAS_DECODER = False
    logger.warning("Google News decoder not available")


def infer_category_from_content(title, description):
    """
    Infer article category based on title and description keywords.
    All articles must be categorized - no 'GENERAL' fallback.
    """
    # Combine title and description for analysis
    text = (title + " " + description).lower()

    # Define keyword patterns for major categories (order matters for tie-breaking)
    category_keywords = {
        'TECHNOLOGY': [
            'tech', 'ai', 'artificial intelligence', 'software', 'app', 'digital', 'cyber',
            'computer', 'internet', 'online', 'data', 'algorithm', 'robot', 'smartphone',
            'gadget', 'innovation', 'startup', 'silicon valley', 'coding', 'programming',
            'gaming', 'xbox', 'playstation', 'video game', 'apple', 'google', 'microsoft',
            'meta', 'twitter', 'social media', 'blockchain', 'cryptocurrency'
        ],
        'BUSINESS': [
            'business', 'economy', 'market', 'stock', 'finance', 'corporate', 'company',
            'trade', 'industry', 'commerce', 'investment', 'profit', 'revenue', 'ceo',
            'earnings', 'wall street', 'economic', 'financial', 'bankruptcy', 'merger',
            'acquisition', 'sales', 'consumer', 'retail', 'inflation', 'jobs report'
        ],
        'US': [
            'trump', 'biden', 'congress', 'senate', 'house', 'washington', 'federal',
            'supreme court', 'governor', 'mayor', 'state', 'legislature', 'shutdown',
            'white house', 'capitol', 'department', 'agency', 'american', 'u.s.', 'usa',
            'america', 'united states', 'immigration', 'border', 'law enforcement',
            'police', 'fbi', 'doj', 'domestic', 'national'
        ],
        'POLITICS': [
            'politics', 'election', 'vote', 'voting', 'ballot', 'campaign', 'democrat',
            'republican', 'policy', 'legislation', 'political', 'partisan', 'primary',
            'candidate', 'poll', 'debate'
        ],
        'HEALTH': [
            'health', 'medical', 'disease', 'hospital', 'doctor', 'patient', 'treatment',
            'vaccine', 'virus', 'covid', 'medicine', 'healthcare', 'diagnosis', 'study',
            'cancer', 'drug', 'fda', 'cdc', 'outbreak', 'pandemic', 'illness', 'mental health',
            'obesity', 'diabetes', 'heart', 'surgery', 'clinic'
        ],
        'SCIENCE': [
            'science', 'research', 'study', 'scientist', 'discovery', 'space', 'nasa',
            'climate', 'environment', 'planet', 'universe', 'physics', 'chemistry',
            'biology', 'experiment', 'laboratory', 'asteroid', 'galaxy', 'telescope',
            'quantum', 'renewable', 'fossil fuel', 'emissions', 'warming'
        ],
        'SPORTS': [
            'sports', 'football', 'basketball', 'baseball', 'soccer', 'nfl', 'nba',
            'mlb', 'nhl', 'game', 'team', 'player', 'coach', 'championship', 'league',
            'tournament', 'olympic', 'athlete', 'hockey', 'tennis', 'golf', 'match',
            'season', 'playoffs', 'super bowl', 'world series', 'finals'
        ],
        'ENTERTAINMENT': [
            'movie', 'film', 'actor', 'actress', 'celebrity', 'music', 'album', 'concert',
            'show', 'television', 'tv', 'netflix', 'streaming', 'hollywood', 'singer',
            'band', 'entertainment', 'award', 'grammy', 'oscar', 'emmy', 'premiere',
            'box office', 'billboard', 'broadway', 'theater', 'series', 'episode'
        ],
        'WORLD': [
            'international', 'global', 'foreign', 'world', 'europe', 'asia', 'africa',
            'middle east', 'latin america', 'war', 'conflict', 'peace', 'united nations',
            'diplomatic', 'uk', 'britain', 'france', 'germany', 'china', 'russia',
            'israel', 'palestine', 'iran', 'ukraine', 'korea', 'japan', 'india',
            'attack', 'terror', 'terrorism', 'military', 'invasion', 'sanctions',
            'treaty', 'ambassador', 'embassy', 'refugee', 'humanitarian'
        ],
    }

    # Score each category
    scores = {}
    for category, keywords in category_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text)
        if score > 0:
            scores[category] = score

    # Return category with highest score
    if scores:
        return max(scores, key=scores.get)

    # If no keywords match, use fallback logic based on common patterns
    # Check for US-related content first
    if any(word in text for word in ['trump', 'biden', 'washington', 'federal', 'state', 'american']):
        return 'US'

    # Default to US for political/governmental content
    if any(word in text for word in ['government', 'president', 'congress', 'senate', 'house']):
        return 'US'

    # Default to WORLD for international indicators
    if any(word in text for word in ['country', 'nation', 'international']):
        return 'WORLD'

    # Last resort: categorize as US (most common for US-based news)
    return 'US'


def filter_articles_by_date(articles, hours=24):
    """
    Filter articles to only include those published within the last N hours (UTC).

    Args:
        articles: List of article dictionaries
        hours: Number of hours to look back (default: 24)

    Returns:
        List of articles published within the time window
    """
    now_utc = datetime.now(timezone.utc)
    cutoff = now_utc - timedelta(hours=hours)

    logger.info("")
    logger.info(f"{get_emoji('clock')} Filtering articles by publish date (last {hours} hours UTC)...")
    logger.info(f"{get_emoji('date')} Current UTC Time: {now_utc.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info(f"{get_emoji('time')} Cutoff Time: {cutoff.strftime('%Y-%m-%d %H:%M:%S')}")
    logger.info("─────────────────────────────────────────")

    kept = []
    skipped = []

    for idx, article in enumerate(articles, 1):
        title = article.get('title', 'No title')
        url = article.get('url', '')
        published_date = article.get('published date', '')

        # Parse date
        pub_date_utc = None
        if published_date:
            try:
                # Try parsing common date formats
                for fmt in ['%a, %d %b %Y %H:%M:%S %Z', '%a, %d %b %Y %H:%M:%S GMT',
                           '%Y-%m-%d %H:%M:%S.%f%z', '%Y-%m-%d %H:%M:%S%z']:
                    try:
                        pub_date_utc = datetime.strptime(published_date, fmt)
                        # Ensure timezone-aware
                        if pub_date_utc.tzinfo is None:
                            pub_date_utc = pub_date_utc.replace(tzinfo=timezone.utc)
                        break
                    except ValueError:
                        continue
            except Exception as e:
                logger.debug(f"Date parse error for '{published_date}': {e}")

        # Check if within time window
        if pub_date_utc and pub_date_utc >= cutoff:
            age_hours = (now_utc - pub_date_utc).total_seconds() / 3600
            log_url_action(
                logger,
                'keep',
                url,
                title,
                published=pub_date_utc.strftime('%Y-%m-%d %H:%M UTC'),
                age_hours=f"{age_hours:.1f} hours ago"
            )
            kept.append(article)
        else:
            if pub_date_utc:
                age_hours = (now_utc - pub_date_utc).total_seconds() / 3600
                log_url_action(
                    logger,
                    'skip',
                    url,
                    title,
                    reason=f"Too old ({age_hours:.1f} hours ago)"
                )
            else:
                log_url_action(
                    logger,
                    'skip',
                    url,
                    title,
                    reason="Unparseable date"
                )
            skipped.append(article)

        if idx % 10 == 0 or idx == len(articles):
            logger.info("")  # Blank line every 10 articles

    # Log summary
    logger.info("")
    logger.info(f"{get_emoji('summary')} Date Filter Summary:")
    logger.info(f"   {get_emoji('success')} Kept: {len(kept)}/{len(articles)} ({len(kept)/len(articles)*100:.1f}%)" if articles else "   No articles")
    logger.info(f"   {get_emoji('failed')} Skipped: {len(skipped)}/{len(articles)} ({len(skipped)/len(articles)*100:.1f}%)" if articles else "   No articles")
    logger.info("")

    return kept


def get_articles_with_full_text(keyword=None, max_results=10, language='en', country='US',
                                  period=None, topic=None, location=None, site=None):
    """
    Fetch news articles with full text content.

    Args:
        keyword: Search keyword for news
        max_results: Number of articles to fetch (default: 10)
        language: Language code (default: 'en')
        country: Country code (default: 'US')
        period: Time period (e.g., '7d', '1m')
        topic: News topic (e.g., 'WORLD', 'BUSINESS', 'TECHNOLOGY')
        location: Geographic location
        site: Specific website to search (e.g., 'cnn.com')

    Returns:
        List of dictionaries with article data including full text
    """
    start_time = time.time()

    log_operation(
        logger,
        'fetch_articles_start',
        keyword=keyword,
        max_results=max_results,
        language=language,
        country=country,
        period=period,
        topic=topic,
        location=location,
        site=site
    )

    # Initialize GNews
    logger.info(f"Initializing GNews with language={language}, country={country}, max_results={max_results}")
    google_news = GNews(language=language, country=country, max_results=max_results, period=period)

    # Determine search method and category
    search_method = None
    category = None

    # Fetch news based on parameters
    if topic:
        logger.info(f"Fetching news by topic: {topic}")
        articles = google_news.get_news_by_topic(topic)
        search_method = 'topic'
        # Special handling: Map NATION to US
        if topic.upper() == 'NATION':
            category = 'US'
            logger.info(f"{get_emoji('us')} Converting NATION topic to US category")
        else:
            category = topic.upper()
    elif location:
        logger.info(f"Fetching news by location: {location}")
        articles = google_news.get_news_by_location(location)
        search_method = 'location'
        category = location
    elif site:
        logger.info(f"Fetching news by site: {site}")
        articles = google_news.get_news_by_site(site)
        search_method = 'site'
        category = site
    elif keyword:
        logger.info(f"Fetching news by keyword: {keyword}")
        articles = google_news.get_news(keyword)
        search_method = 'keyword'
        category = keyword
    else:
        logger.info("Fetching top news")
        articles = google_news.get_top_news()
        search_method = 'top_news'
        category = 'TOP_NEWS'

    log_operation(
        logger,
        'articles_fetched',
        search_method=search_method,
        category=category,
        count=len(articles)
    )
    logger.info(f"Fetched {len(articles)} articles using {search_method} method")

    # Enrich articles with full text content
    enriched_articles = []
    logger.info(f"Starting to enrich {len(articles)} articles with full text")

    for idx, article in enumerate(articles, 1):
        logger.info(f"Processing article {idx}/{len(articles)}")
        # Clean up title - remove publisher suffix if present
        title = article.get('title', '')
        publisher_name = article.get('publisher', {})
        if isinstance(publisher_name, dict):
            publisher_name = publisher_name.get('title', '')

        # Remove publisher from title if it's appended at the end
        if publisher_name and title.endswith(f" - {publisher_name}"):
            title = title[:-len(f" - {publisher_name}")].strip()
        elif publisher_name and title.endswith(f"  {publisher_name}"):
            title = title[:-len(f"  {publisher_name}")].strip()

        article['title'] = title
        logger.debug(f"Article title: {title[:100]}")

        # Add category and search method metadata
        # For top news, infer category from content
        if search_method == 'top_news':
            inferred_category = infer_category_from_content(title, article.get('description', ''))
            article['category'] = inferred_category
            article['category_source'] = 'inferred'
            logger.debug(f"Category inferred: {inferred_category}")
        else:
            article['category'] = category
            article['category_source'] = 'explicit'
            logger.debug(f"Category explicit: {category}")

        article['search_method'] = search_method

        try:
            # Resolve Google News redirect URL to actual article URL
            original_url = article.pop('url')  # Remove the original 'url' key
            actual_url = original_url
            logger.debug(f"Original URL: {original_url[:100]}")

            if 'news.google.com' in actual_url and HAS_DECODER:
                try:
                    logger.debug("Attempting to decode Google News URL")
                    # Use googlenewsdecoder to get the actual article URL
                    decoded_url = new_decoderv1(actual_url, interval=1)
                    if decoded_url and decoded_url.get('status') and decoded_url.get('decoded_url'):
                        actual_url = decoded_url['decoded_url']
                        article['decoded_successfully'] = True
                        log_operation(logger, 'url_decode', status='success', original=original_url[:100], decoded=actual_url[:100])
                        logger.info(f"URL decoded successfully: {actual_url[:100]}")
                    else:
                        article['decode_failed'] = True
                        log_operation(logger, 'url_decode', status='failed', url=original_url[:100])
                        logger.warning(f"URL decode failed: {original_url[:100]}")
                except Exception as decode_error:
                    article['decode_error'] = str(decode_error)
                    log_error(logger, 'url_decode', decode_error, url=original_url[:100])
            else:
                if not HAS_DECODER and 'news.google.com' in actual_url:
                    article['note'] = "Install googlenewsdecoder for better URL resolution: pip install googlenewsdecoder"
                    logger.debug("Decoder not available for Google News URL")

            # Set actual_url as the URL in the output
            article['url'] = actual_url

            # Get full article using newspaper3k
            try:
                logger.debug(f"Downloading article from: {actual_url[:100]}")
                import newspaper
                full_article = newspaper.Article(url=actual_url, language=language)
                full_article.download()
                full_article.parse()

                if full_article.text and len(full_article.text.strip()) > 0:
                    article['full_text'] = full_article.text.strip()
                    article['authors'] = full_article.authors if hasattr(full_article, 'authors') else []
                    # Note: We're removing publish_date from being stored, as per requirements
                    log_operation(
                        logger,
                        'article_text_extracted',
                        status='success',
                        url=actual_url[:100],
                        text_length=len(article['full_text']),
                        authors_count=len(article['authors'])
                    )
                    logger.info(f"Article text extracted: {len(article['full_text'])} chars, {len(article['authors'])} authors")
                else:
                    article['full_text'] = None
                    article['authors'] = []
                    article['note'] = "Could not extract article text - Google News redirect may have failed"
                    log_operation(logger, 'article_text_extraction', status='failed_empty', url=actual_url[:100])
                    logger.warning(f"No text extracted from article: {actual_url[:100]}")

            except ImportError:
                article['full_text'] = None
                article['error'] = "newspaper3k not installed. Install with: pip install newspaper3k"
                article['authors'] = []
                log_error(logger, 'article_download', ImportError("newspaper3k not installed"), url=actual_url[:100])

        except Exception as e:
            article['full_text'] = None
            article['error'] = str(e)
            article['authors'] = []
            log_error(logger, 'article_processing', e, url=article.get('url', 'unknown')[:100])

        enriched_articles.append(article)

    elapsed_time = time.time() - start_time
    log_operation(
        logger,
        'fetch_articles_complete',
        total_articles=len(enriched_articles),
        elapsed_seconds=f"{elapsed_time:.2f}",
        avg_time_per_article=f"{elapsed_time/len(enriched_articles):.2f}" if enriched_articles else "0"
    )
    logger.info(f"Article enrichment complete: {len(enriched_articles)} articles in {elapsed_time:.2f}s")

    return enriched_articles


def main():
    """
    Main function to demonstrate usage and handle command-line arguments.
    """
    import argparse

    parser = argparse.ArgumentParser(description='Fetch news articles with full text and save to database')
    parser.add_argument('--keyword', '-k', type=str, help='Search keyword')
    parser.add_argument('--topic', '-t', type=str, help='News topic (e.g., WORLD, BUSINESS, TECHNOLOGY)')
    parser.add_argument('--location', '-l', type=str, help='Geographic location')
    parser.add_argument('--site', '-s', type=str, help='Specific website (e.g., cnn.com)')
    parser.add_argument('--max-results', '-m', type=int, default=10, help='Maximum number of results (default: 10)')
    parser.add_argument('--language', type=str, default='en', help='Language code (default: en)')
    parser.add_argument('--country', type=str, default='US', help='Country code (default: US)')
    parser.add_argument('--period', '-p', type=str, help='Time period (e.g., 7d, 1m, 1y)')
    parser.add_argument('--output', '-o', type=str, help='Output JSON file (optional, for debugging)')
    parser.add_argument('--pretty', action='store_true', help='Pretty print JSON output (when using --output)')
    parser.add_argument('--no-db', action='store_true', help='Disable database insertion (for testing)')
    parser.add_argument('--table', type=str, default='sources', help='Database table name (default: sources)')
    parser.add_argument('--test-db', action='store_true', help='Test database connection and exit')

    args = parser.parse_args()

    # Test database connection if requested
    if args.test_db:
        log_operation(logger, 'script_start', mode='test_db')
        logger.info("Testing database connection...")
        if test_connection():
            logger.info("Database connection test successful!")
            print("✓ Database connection successful", file=sys.stderr)
            sys.exit(0)
        else:
            logger.error("Database connection test failed!")
            print("✗ Database connection failed", file=sys.stderr)
            sys.exit(1)

    # Log script start
    log_operation(
        logger,
        'script_start',
        mode='fetch_and_insert',
        keyword=args.keyword,
        topic=args.topic,
        location=args.location,
        site=args.site,
        max_results=args.max_results,
        use_db=not args.no_db
    )

    # Validate that at least one search parameter is provided
    if not any([args.keyword, args.topic, args.location, args.site]):
        logger.info("No search parameters provided. Fetching top news...")
        print("Note: No search parameters provided. Fetching top news...\n", file=sys.stderr)

    # Log fetching header
    topic_name = args.topic or args.keyword or args.location or args.site or 'TOP_NEWS'
    logger.info("")
    log_separator(logger)
    logger.info(f"{get_emoji('target')} FETCHING TOPIC: {topic_name}")
    log_separator(logger)
    logger.info(f"{get_emoji('count')} Max Results Requested: {args.max_results}")
    logger.info(f"{get_emoji('clock')} Time Filter: Last 24 hours (UTC)")
    log_separator(logger)

    # Fetch articles
    try:
        start_time = time.time()

        # Fetch initial batch
        raw_articles = get_articles_with_full_text(
            keyword=args.keyword,
            max_results=args.max_results * 3,  # Fetch more initially to account for filtering
            language=args.language,
            country=args.country,
            period=args.period,
            topic=args.topic,
            location=args.location,
            site=args.site
        )

        # Filter by date (last 24 hours)
        filtered_articles = filter_articles_by_date(raw_articles, hours=24)

        # Trim to requested max
        articles = filtered_articles[:args.max_results]

        logger.info(f"{get_emoji('summary')} Article Filtering Complete:")
        logger.info(f"   {get_emoji('fetch')} Initial fetch: {len(raw_articles)}")
        logger.info(f"   {get_emoji('success')} After date filter: {len(filtered_articles)}")
        logger.info(f"   {get_emoji('target')} Final count: {len(articles)}")
        logger.info("")

        # Track stats for overall summary
        total_fetched = len(raw_articles)
        total_filtered = len(filtered_articles)
        total_skipped_date = total_fetched - total_filtered

        # Save to database (unless disabled)
        if not args.no_db:
            result = insert_articles_batch(articles, table_name=args.table)

            elapsed_time = time.time() - start_time

            # Calculate text extraction stats
            text_success = sum(1 for a in articles if a.get('full_text'))
            text_failed = len(articles) - text_success

            # Log overall summary
            stats = {
                'fetch_attempts': 1,
                'total_fetched': total_fetched,
                'date_filter': {
                    'kept': total_filtered,
                    'kept_pct': (total_filtered / total_fetched * 100) if total_fetched > 0 else 0,
                    'skipped': total_skipped_date,
                    'skipped_pct': (total_skipped_date / total_fetched * 100) if total_fetched > 0 else 0,
                },
                'text_extraction': {
                    'success': text_success,
                    'success_pct': (text_success / len(articles) * 100) if articles else 0,
                    'failed': text_failed,
                    'failed_pct': (text_failed / len(articles) * 100) if articles else 0,
                },
                'database': {
                    'inserted': result['success'],
                    'inserted_pct': (result['success'] / len(articles) * 100) if articles else 0,
                    'duplicates': result['duplicate'],
                    'duplicates_pct': (result['duplicate'] / len(articles) * 100) if articles else 0,
                    'failed': result['failed'],
                    'failed_pct': (result['failed'] / len(articles) * 100) if articles else 0,
                },
                'unique_articles': result['success'],
                'elapsed_time': elapsed_time,
                'avg_time': elapsed_time / len(articles) if articles else 0,
            }

            log_overall_summary(logger, topic_name, stats)

            # Console output
            print(f"\n{get_emoji('success')} Successfully inserted {result['success']}/{len(articles)} articles into database", file=sys.stderr)
            print(f"{get_emoji('duplicate')} Duplicates skipped: {result['duplicate']}", file=sys.stderr)
            if result['failed'] > 0:
                print(f"{get_emoji('failed')} Failed to insert {result['failed']} articles", file=sys.stderr)

        # Optional: Save to JSON file for debugging
        if args.output:
            logger.info(f"Saving articles to JSON file: {args.output}")
            json_output = json.dumps(articles, indent=2 if args.pretty else None, ensure_ascii=False)
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"✓ Saved {len(articles)} articles to {args.output}", file=sys.stderr)
            log_operation(logger, 'json_export', status='success', file=args.output, count=len(articles))

        # Close database connections
        close_connection_pool()
        logger.info("Database connections closed")

    except Exception as e:
        log_error(logger, 'script_execution', e)
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
