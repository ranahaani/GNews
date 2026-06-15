# RSS Backend (Default)

The RSS backend is the default. No API key required.

## How it works

GNews fetches Google News RSS feeds and parses them using `feedparser`. Article URLs are resolved from Google's redirect links to the actual article URLs.

## Article fields

| Field | Description |
|-------|-------------|
| `title` | Article title |
| `description` | Short summary |
| `published date` | RFC 2822 date string |
| `url` | Direct article URL |
| `publisher` | Publisher name/dict |

## Limitations

- Max ~100 results per query
- No absolute ISO dates (relative strings like "2 hours ago")
- No thumbnails or favicons
- Occasionally affected by Google RSS changes

## Usage

```python
from gnews import GNews

# Default — uses RSS
g = GNews(max_results=10)
articles = g.get_news("Python")
```
