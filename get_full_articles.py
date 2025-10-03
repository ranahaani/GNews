#!/usr/bin/env python3
"""
Script to fetch news articles with full text content and output as JSON.
"""
import json
import sys
import re
import requests
from bs4 import BeautifulSoup
from gnews import GNews

# Try to import Google News URL decoder
try:
    from googlenewsdecoder import new_decoderv1
    HAS_DECODER = True
except ImportError:
    HAS_DECODER = False


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
    # Initialize GNews
    google_news = GNews(language=language, country=country, max_results=max_results, period=period)

    # Determine search method and category
    search_method = None
    category = None

    # Fetch news based on parameters
    if topic:
        articles = google_news.get_news_by_topic(topic)
        search_method = 'topic'
        category = topic.upper()
    elif location:
        articles = google_news.get_news_by_location(location)
        search_method = 'location'
        category = location
    elif site:
        articles = google_news.get_news_by_site(site)
        search_method = 'site'
        category = site
    elif keyword:
        articles = google_news.get_news(keyword)
        search_method = 'keyword'
        category = keyword
    else:
        articles = google_news.get_top_news()
        search_method = 'top_news'
        category = 'TOP_NEWS'

    # Enrich articles with full text content
    enriched_articles = []
    for article in articles:
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

        # Add category and search method metadata
        # For top news, infer category from content
        if search_method == 'top_news':
            inferred_category = infer_category_from_content(title, article.get('description', ''))
            article['category'] = inferred_category
            article['category_source'] = 'inferred'
        else:
            article['category'] = category
            article['category_source'] = 'explicit'

        article['search_method'] = search_method

        try:
            # Resolve Google News redirect URL to actual article URL
            actual_url = article['url']

            if 'news.google.com' in actual_url and HAS_DECODER:
                try:
                    # Use googlenewsdecoder to get the actual article URL
                    decoded_url = new_decoderv1(actual_url, interval=1)
                    if decoded_url and decoded_url.get('status') and decoded_url.get('decoded_url'):
                        actual_url = decoded_url['decoded_url']
                        article['actual_url'] = actual_url
                        article['decoded_successfully'] = True
                    else:
                        article['actual_url'] = actual_url
                        article['decode_failed'] = True
                except Exception as decode_error:
                    article['actual_url'] = actual_url
                    article['decode_error'] = str(decode_error)
            else:
                article['actual_url'] = actual_url
                if not HAS_DECODER and 'news.google.com' in actual_url:
                    article['note'] = "Install googlenewsdecoder for better URL resolution: pip install googlenewsdecoder"

            # Get full article using newspaper3k
            try:
                import newspaper
                full_article = newspaper.Article(url=actual_url, language=language)
                full_article.download()
                full_article.parse()

                if full_article.text and len(full_article.text.strip()) > 0:
                    article['full_text'] = full_article.text.strip()
                    article['authors'] = full_article.authors if hasattr(full_article, 'authors') else []
                    article['images'] = list(full_article.images) if hasattr(full_article, 'images') else []
                    article['top_image'] = full_article.top_image if hasattr(full_article, 'top_image') else None
                    article['publish_date'] = str(full_article.publish_date) if hasattr(full_article, 'publish_date') and full_article.publish_date else None
                else:
                    article['full_text'] = None
                    article['authors'] = []
                    article['images'] = []
                    article['top_image'] = None
                    article['publish_date'] = None
                    article['note'] = "Could not extract article text - Google News redirect may have failed"

            except ImportError:
                article['full_text'] = None
                article['error'] = "newspaper3k not installed. Install with: pip install newspaper3k"
                article['authors'] = []
                article['images'] = []
                article['top_image'] = None
                article['publish_date'] = None

        except Exception as e:
            article['full_text'] = None
            article['error'] = str(e)
            article['authors'] = []
            article['images'] = []
            article['top_image'] = None
            article['publish_date'] = None

        enriched_articles.append(article)

    return enriched_articles


def main():
    """
    Main function to demonstrate usage and handle command-line arguments.
    """
    import argparse

    parser = argparse.ArgumentParser(description='Fetch news articles with full text as JSON')
    parser.add_argument('--keyword', '-k', type=str, help='Search keyword')
    parser.add_argument('--topic', '-t', type=str, help='News topic (e.g., WORLD, BUSINESS, TECHNOLOGY)')
    parser.add_argument('--location', '-l', type=str, help='Geographic location')
    parser.add_argument('--site', '-s', type=str, help='Specific website (e.g., cnn.com)')
    parser.add_argument('--max-results', '-m', type=int, default=10, help='Maximum number of results (default: 10)')
    parser.add_argument('--language', type=str, default='en', help='Language code (default: en)')
    parser.add_argument('--country', type=str, default='US', help='Country code (default: US)')
    parser.add_argument('--period', '-p', type=str, help='Time period (e.g., 7d, 1m, 1y)')
    parser.add_argument('--output', '-o', type=str, help='Output JSON file (default: stdout)')
    parser.add_argument('--pretty', action='store_true', help='Pretty print JSON output')

    args = parser.parse_args()

    # Validate that at least one search parameter is provided
    if not any([args.keyword, args.topic, args.location, args.site]):
        print("Note: No search parameters provided. Fetching top news...\n", file=sys.stderr)

    # Fetch articles
    try:
        articles = get_articles_with_full_text(
            keyword=args.keyword,
            max_results=args.max_results,
            language=args.language,
            country=args.country,
            period=args.period,
            topic=args.topic,
            location=args.location,
            site=args.site
        )

        # Prepare JSON output
        json_output = json.dumps(articles, indent=2 if args.pretty else None, ensure_ascii=False)

        # Write to file or stdout
        if args.output:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(json_output)
            print(f"Successfully saved {len(articles)} articles to {args.output}", file=sys.stderr)
        else:
            print(json_output)

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
