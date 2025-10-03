#!/usr/bin/env python3
"""
Comprehensive logging utility with Grafana Loki integration.
Works in both dev and GitHub Actions environments.
"""
import logging
import os
import sys
from datetime import datetime
from typing import Optional
import socket

try:
    from logging_loki import LokiHandler
    HAS_LOKI = True
except ImportError:
    HAS_LOKI = False

from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def setup_logger(name: str = "gnews", level: Optional[str] = None) -> logging.Logger:
    """
    Setup logger with Loki handler and console fallback.

    Args:
        name: Logger name
        level: Log level (DEBUG, INFO, WARNING, ERROR). Auto-detects if None.

    Returns:
        Configured logger instance
    """
    # Detect environment
    is_github_actions = os.getenv('GITHUB_ACTIONS') == 'true'
    is_dev = not is_github_actions

    # Determine log level
    if level is None:
        level = 'DEBUG' if is_dev else 'INFO'

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, level.upper()))

    # Clear existing handlers
    logger.handlers = []

    # Console handler (always active)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, level.upper()))
    console_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    # Loki handler (if configured)
    loki_url = os.getenv('LOKI_URL')
    grafana_user = os.getenv('GRAFANA_CLOUD_USER')
    grafana_api_key = os.getenv('GRAFANA_CLOUD_API_KEY')

    if HAS_LOKI and loki_url and grafana_user and grafana_api_key:
        try:
            # Prepare labels
            environment = 'github-actions' if is_github_actions else 'dev'
            hostname = socket.gethostname()

            labels = {
                'application': 'gnews',
                'environment': environment,
                'hostname': hostname,
                'script': name,
            }

            # Add GitHub-specific labels if in Actions
            if is_github_actions:
                labels.update({
                    'github_workflow': os.getenv('GITHUB_WORKFLOW', 'unknown'),
                    'github_run_id': os.getenv('GITHUB_RUN_ID', 'unknown'),
                    'github_repository': os.getenv('GITHUB_REPOSITORY', 'unknown'),
                })

            # Create Loki handler with authentication
            loki_handler = LokiHandler(
                url=loki_url,
                tags=labels,
                auth=(grafana_user, grafana_api_key),
                version="1",
            )
            loki_handler.setLevel(getattr(logging, level.upper()))
            logger.addHandler(loki_handler)

            logger.info(f"Loki logging initialized successfully for environment: {environment}")

        except Exception as e:
            logger.warning(f"Failed to initialize Loki handler: {e}. Using console logging only.")
    else:
        if not HAS_LOKI:
            logger.warning("python-logging-loki not installed. Using console logging only.")
        elif not all([loki_url, grafana_user, grafana_api_key]):
            logger.warning("Loki credentials not configured. Using console logging only.")

    return logger


def log_operation(logger: logging.Logger, operation: str, **kwargs):
    """
    Log an operation with structured data.

    Args:
        logger: Logger instance
        operation: Operation name (e.g., 'fetch_articles', 'db_insert')
        **kwargs: Additional key-value pairs to log
    """
    log_data = {
        'operation': operation,
        'timestamp': datetime.utcnow().isoformat(),
        **kwargs
    }

    # Format as key=value pairs
    log_message = ' | '.join([f"{k}={v}" for k, v in log_data.items()])
    logger.info(log_message)


def log_error(logger: logging.Logger, operation: str, error: Exception, **kwargs):
    """
    Log an error with structured data and exception details.

    Args:
        logger: Logger instance
        operation: Operation name
        error: Exception that occurred
        **kwargs: Additional context
    """
    log_data = {
        'operation': operation,
        'timestamp': datetime.utcnow().isoformat(),
        'error_type': type(error).__name__,
        'error_message': str(error),
        **kwargs
    }

    log_message = ' | '.join([f"{k}={v}" for k, v in log_data.items()])
    logger.error(log_message, exc_info=True)


# Emoji mapping for visual logging
EMOJI_MAP = {
    # Status
    'success': '✅',
    'duplicate': '⊘',
    'failed': '❌',
    'warning': '⚠️',
    'info': 'ℹ️',
    'check': '✓',

    # Actions
    'fetch': '📥',
    'insert': '💾',
    'skip': '🚫',
    'keep': '✓',
    'processing': '⚙️',
    'attempt': '🔄',

    # Content
    'article': '📰',
    'url': '🔗',
    'text': '📝',
    'author': '✍️',
    'date': '📅',
    'time': '⏱️',
    'clock': '🕐',
    'length': '📏',

    # Progress
    'summary': '📊',
    'topic': '🎯',
    'trophy': '🏆',
    'target': '🎯',
    'chart': '📈',
    'count': '🔢',

    # Categories
    'us': '🇺🇸',
    'world': '🌍',
    'tech': '💻',
    'business': '💼',
    'health': '🏥',
    'science': '🔬',
    'sports': '⚽',
    'entertainment': '🎬',
    'politics': '🏛️',

    # Misc
    'decode': '🔓',
    'lock': '🔒',
    'package': '📦',
}


def get_emoji(key: str, default: str = '') -> str:
    """
    Get emoji by key from EMOJI_MAP.

    Args:
        key: Emoji key
        default: Default value if key not found

    Returns:
        Emoji string or default
    """
    return EMOJI_MAP.get(key.lower(), default)


def log_separator(logger: logging.Logger, char: str = '═', length: int = 43):
    """
    Log a visual separator line.

    Args:
        logger: Logger instance
        char: Character to use for separator
        length: Length of separator
    """
    logger.info(char * length)


def log_url_action(logger: logging.Logger, action: str, url: str, title: str, **kwargs):
    """
    Log an action on a specific URL with emoji indicators.

    Args:
        logger: Logger instance
        action: Action type (success, duplicate, failed, keep, skip, etc.)
        url: Article URL
        title: Article title (will be truncated to 60 chars)
        **kwargs: Additional info to log (e.g., reason, age_hours, error)
    """
    # Get emoji for action
    emoji = get_emoji(action, '•')

    # Truncate title
    title_short = title[:60] + '...' if len(title) > 60 else title

    # Log action with emoji
    logger.info(f"{emoji} [{action.upper()}] {title_short}")
    logger.info(f"   {get_emoji('url')} {url}")

    # Log additional context
    for key, value in kwargs.items():
        if key == 'error' or key == 'reason':
            logger.info(f"   {get_emoji('warning')} {key.capitalize()}: {value}")
        elif key == 'age_hours':
            logger.info(f"   {get_emoji('time')} Age: {value}")
        elif key == 'published':
            logger.info(f"   {get_emoji('date')} Published: {value}")
        elif key == 'text_length':
            logger.info(f"   {get_emoji('length')} Length: {value:,} characters")
        elif key == 'category':
            logger.info(f"   {get_emoji('topic')} Category: {value}")
        else:
            logger.info(f"   • {key}: {value}")


def log_summary_section(logger: logging.Logger, title: str, data: dict, emoji: str = '📊'):
    """
    Log a formatted summary section.

    Args:
        logger: Logger instance
        title: Section title
        data: Dictionary of summary data
        emoji: Emoji for section header
    """
    logger.info("")
    logger.info(f"{emoji} {title}")

    for key, value in data.items():
        if isinstance(value, dict):
            # Nested data
            logger.info(f"   {key}:")
            for sub_key, sub_value in value.items():
                logger.info(f"      {sub_key}: {sub_value}")
        else:
            logger.info(f"   {key}: {value}")


def log_overall_summary(logger: logging.Logger, topic: str, stats: dict):
    """
    Log comprehensive overall summary for a topic.

    Args:
        logger: Logger instance
        topic: Topic/category name
        stats: Dictionary with summary statistics
    """
    logger.info("")
    log_separator(logger)
    logger.info(f"{get_emoji('trophy')} TOPIC SUMMARY: {topic}")
    log_separator(logger)

    # Fetch stats
    if 'fetch_attempts' in stats:
        logger.info(f"{get_emoji('attempt')} Total Fetch Attempts: {stats['fetch_attempts']}")
    if 'total_fetched' in stats:
        logger.info(f"{get_emoji('fetch')} Total Articles Fetched: {stats['total_fetched']}")

    logger.info("")

    # Date filtering
    if 'date_filter' in stats:
        df = stats['date_filter']
        logger.info(f"{get_emoji('clock')} Date Filtering Results:")
        logger.info(f"   {get_emoji('success')} Kept: {df.get('kept', 0)} ({df.get('kept_pct', 0):.1f}%)")
        logger.info(f"   {get_emoji('failed')} Skipped: {df.get('skipped', 0)} ({df.get('skipped_pct', 0):.1f}%)")
        logger.info("")

    # Text extraction
    if 'text_extraction' in stats:
        te = stats['text_extraction']
        logger.info(f"{get_emoji('text')} Text Extraction Results:")
        logger.info(f"   {get_emoji('success')} Success: {te.get('success', 0)} ({te.get('success_pct', 0):.1f}%)")
        logger.info(f"   {get_emoji('failed')} Failed: {te.get('failed', 0)} ({te.get('failed_pct', 0):.1f}%)")
        logger.info("")

    # Database results
    if 'database' in stats:
        db = stats['database']
        logger.info(f"{get_emoji('insert')} Database Insert Results:")
        logger.info(f"   {get_emoji('success')} Inserted: {db.get('inserted', 0)} ({db.get('inserted_pct', 0):.1f}%)")
        logger.info(f"   {get_emoji('duplicate')} Duplicates: {db.get('duplicates', 0)} ({db.get('duplicates_pct', 0):.1f}%)")
        logger.info(f"   {get_emoji('failed')} Failed: {db.get('failed', 0)} ({db.get('failed_pct', 0):.1f}%)")
        logger.info("")

    # Final results
    if 'unique_articles' in stats:
        logger.info(f"{get_emoji('target')} Final Unique Articles: {stats['unique_articles']} {get_emoji('check')}")
    if 'elapsed_time' in stats:
        logger.info(f"{get_emoji('time')} Total Elapsed Time: {stats['elapsed_time']:.1f} seconds")
    if 'avg_time' in stats:
        logger.info(f"{get_emoji('chart')} Average per Article: {stats['avg_time']:.1f} seconds")

    log_separator(logger)


# Create default logger instance
default_logger = setup_logger()
