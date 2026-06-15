from __future__ import annotations

import logging
import re

import requests
from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, GOOGLE_NEWS_REGEX

logger = logging.getLogger(__name__)


def lang_mapping(lang):
    return AVAILABLE_LANGUAGES.get(lang)


def country_mapping(country):
    return AVAILABLE_COUNTRIES.get(country)


def _resolve_with_playwright(url: str) -> str | None:
    try:
        from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout
    except ImportError:
        return None

    try:
        # Convert RSS URL to article URL for Playwright to follow JS redirect
        navigate_url = url.replace('/rss/articles/', '/articles/').split('?')[0]
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-dev-shm-usage"])
            context = browser.new_context(
                user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
            )
            page = context.new_page()
            page.goto(navigate_url, wait_until="domcontentloaded", timeout=15000)
            try:
                page.wait_for_url(
                    lambda u: "news.google.com" not in u,
                    timeout=10000,
                )
            except PWTimeout:
                pass
            real_url = page.url
            browser.close()
            return real_url if "news.google.com" not in real_url else None
    except Exception as e:
        logger.debug(f"Playwright URL resolution failed: {e}")
        return None


def resolve_url(url: str) -> str:
    if "news.google.com" not in url:
        return url
    try:
        from playwright.sync_api import sync_playwright  # noqa: F401
        resolved = _resolve_with_playwright(url)
        return resolved if resolved else url
    except ImportError:
        return url


def process_url(item, exclude_websites, proxies=None):
    source = item.get('source').get('href')
    if not all([not re.match(website, source) for website in
                [f'^http(s)?://(www.)?{website.lower()}.*' for website in exclude_websites]]):
        return
    url = item.get('link')
    if re.match(GOOGLE_NEWS_REGEX, url):
        resolved = resolve_url(url)
        if resolved != url:
            return resolved
        # fallback: try HEAD redirect (may still work in some environments)
        try:
            if proxies:
                url = requests.head(url, proxies=proxies, timeout=5, allow_redirects=True).url
            else:
                url = requests.head(url, timeout=5, allow_redirects=True).url
        except Exception:
            pass
    return url
