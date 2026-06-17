# Changelog

## 0.8.1 (2026-06-18)

### Fixed
- Proxy now correctly forwarded to Playwright during URL resolution — previously Playwright launched Chromium without any proxy, bypassing the user's configured proxy entirely
- `resolve_url()` and `_resolve_with_playwright()` now accept a `proxies` parameter
- `process_url()` now passes `proxies` through to `resolve_url()`
- urllib-style proxy dict (`{"https": "http://host:port"}`) is automatically converted to Playwright's format (`{"server": "http://host:port"}`)

## 0.8.0 (2026-06-15)

### Added
- Real article URL resolution via Playwright (`pip install gnews[playwright]`)
- `resolve_url()` utility function for manual URL resolution
- Automatic fallback to Google URL when Playwright not installed or resolution fails
- `playwright>=1.40` optional extra

### Fixed
- Google News redirect URLs no longer returned as-is when Playwright is available

## 0.7.0 (2026-06-15)

### Added
- Async methods: `get_news_async()`, `get_top_news_async()`, `get_news_by_topic_async()`, `get_news_by_location_async()`, `get_news_by_site_async()`
- Works with both RSS and SearchApi backends
- No new dependencies — uses stdlib `asyncio`

## 0.6.0 (2026-06-15)

### Added
- `save_to_json()` and `save_to_csv()` export methods
- `gnews` CLI with `search`, `top`, `topic`, `site`, `location` commands
- [SearchApi](https://www.searchapi.io) backend — opt-in via `searchapi_key` parameter
- `get_full_article()` now uses `trafilatura` via `pip install gnews[fulltext]`
- Full type hints on all public methods
- Python 3.12, 3.13, 3.14 support
- CI matrix across Python 3.10–3.13

### Fixed
- Removed `logging.basicConfig` from module level — no longer pollutes user logging config
- Removed dynamic `pip install` anti-pattern from `get_full_article()`

### Changed
- `get_full_article()` returns `dict` with `text` and `url` keys instead of `newspaper.Article` object
- Dropped Python 3.8 and 3.9 support (both EOL)

## 0.5.1 (2026-06-15)

- Fix Python 3.8 type hint compatibility (`from __future__ import annotations`)

## 0.5.0 (2026-06-11)

- Initial SearchApi backend integration

## 0.4.3 and earlier

See [GitHub releases](https://github.com/ranahaani/GNews/releases).
