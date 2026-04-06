# GNews

A lightweight Python library for fetching news articles from Google News.

## Installation

```bash
pip install gnews
```

## Quick start

```python
from gnews import GNews

# Initialise GNews with a language and a max result count
gnews = GNews(language='english', max_results=10)

# Retrieve the latest headlines
for article in gnews.get_latest_news():
    print(article['title'])
```

## Detailed usage

- **Language** – Choose from the supported languages (e.g., `english`, `hindi`, `spanish`).
- **Region** – Optionally specify a region code (e.g., `US`, `IN`) using the `region` argument.
- **Search** – Use `gnews.get_news('keyword')` to search for articles containing a specific keyword.
- **Date range** – Filter results with `start_date` and `end_date` parameters.

## Contributing

Contributions are welcome!  Look for issues labelled **good‑first‑issue** if you’d like to start.  Feel free to open an issue or submit a pull request.

## License

MIT License
