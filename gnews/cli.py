from __future__ import annotations

import argparse
import json
import sys

from gnews import GNews


def _print_articles(articles: list[dict], as_json: bool) -> None:
    if as_json:
        print(json.dumps(articles, indent=2, ensure_ascii=False))
    else:
        for i, article in enumerate(articles, 1):
            print(f"{i}. {article.get('title', '')}")
            print(f"   {article.get('url', '')}")
            print(f"   {article.get('published date', '')} — {article.get('publisher', '')}")
            print()


def _build_client(args: argparse.Namespace) -> GNews:
    return GNews(
        language=args.lang,
        country=args.country,
        max_results=args.max,
    )


def _add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--lang", default="en", metavar="LANG", help="Language code (default: en)")
    parser.add_argument("--country", default="US", metavar="COUNTRY", help="Country code (default: US)")
    parser.add_argument("--max", type=int, default=10, metavar="N", help="Max results (default: 10)")
    parser.add_argument("--json", action="store_true", dest="as_json", help="Output as JSON")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="gnews",
        description="GNews — Search Google News from the terminal",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # search
    p_search = sub.add_parser("search", help="Search news by keyword")
    p_search.add_argument("query", help="Search query")
    _add_common_args(p_search)

    # top
    p_top = sub.add_parser("top", help="Get top headlines")
    _add_common_args(p_top)

    # topic
    p_topic = sub.add_parser("topic", help="Get news by topic")
    p_topic.add_argument("topic", help="Topic (e.g. TECHNOLOGY, BUSINESS, SPORTS)")
    _add_common_args(p_topic)

    # site
    p_site = sub.add_parser("site", help="Get news from a specific site")
    p_site.add_argument("site", help="Domain (e.g. bbc.com)")
    _add_common_args(p_site)

    # location
    p_loc = sub.add_parser("location", help="Get news by location")
    p_loc.add_argument("location", help="Location (e.g. Pakistan, India)")
    _add_common_args(p_loc)

    args = parser.parse_args()
    g = _build_client(args)

    if args.command == "search":
        articles = g.get_news(args.query)
    elif args.command == "top":
        articles = g.get_top_news()
    elif args.command == "topic":
        articles = g.get_news_by_topic(args.topic)
    elif args.command == "site":
        articles = g.get_news_by_site(args.site)
    elif args.command == "location":
        articles = g.get_news_by_location(args.location)

    _print_articles(articles, args.as_json)


if __name__ == "__main__":
    main()
