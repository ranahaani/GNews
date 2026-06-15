# SearchApi Backend

[SearchApi](https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews) is an optional backend that replaces RSS with a reliable Google News API.

## Setup

Get a free API key at [searchapi.io](https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews), then pass it to `GNews`:

```python
from gnews import GNews

g = GNews(searchapi_key="YOUR_SEARCHAPI_KEY", max_results=10)
articles = g.get_news("artificial intelligence")
```

## Benefits over RSS

| Feature | RSS | SearchApi |
|---------|-----|-----------|
| Direct article URLs | ✅ (resolved) | ✅ |
| Absolute ISO dates | ❌ | ✅ |
| Thumbnails | ❌ | ✅ |
| Favicons | ❌ | ✅ |
| Result ranking | ❌ | ✅ |
| Pagination | ❌ | ✅ |
| No rate limits | ❌ | ✅ |

## Extra article fields

```python
{
    "title": "OpenAI announces new model",
    "description": "Article snippet...",
    "published date": "2 hours ago",
    "iso_date": "2026-06-15T10:00:00Z",   # ← absolute date
    "url": "https://techcrunch.com/...",
    "publisher": "TechCrunch",
    "thumbnail": "data:image/jpeg;base64,...",  # ← article image
    "favicon": "data:image/png;base64,...",     # ← publisher logo
    "rank": 1                                   # ← position in results
}
```

## Pagination

```python
g = GNews(searchapi_key="YOUR_KEY", max_results=50)

page1 = g.get_news("Python", page=1)
page2 = g.get_news("Python", page=2)
```

## Notes

- `get_top_news()` always uses RSS (SearchApi requires a search query)
- All other methods (`get_news`, `get_news_by_topic`, `get_news_by_location`, `get_news_by_site`) use SearchApi when a key is provided
