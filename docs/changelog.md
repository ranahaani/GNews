# Changelog

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
