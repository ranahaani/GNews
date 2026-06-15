# Getting Full Article Text

## Install

Full article extraction requires the `fulltext` extra:

```shell
pip install gnews[fulltext]
```

## Usage

```python
from gnews import GNews

g = GNews(max_results=5)
articles = g.get_news("OpenAI")

article = g.get_full_article(articles[0]["url"])
print(article["text"])   # full article text
print(article["url"])    # original URL
```

## Return value

```python
{
    "text": "Full article text...",
    "url": "https://example.com/article"
}
```

## Error handling

```python
from gnews.exceptions import NetworkError

try:
    article = g.get_full_article(url)
except NetworkError as e:
    print(f"Could not fetch article: {e}")
except ImportError:
    print("Run: pip install gnews[fulltext]")
```

## Limitations

- **Paywalls**: Articles behind paywalls cannot be extracted
- **JS-heavy sites**: Some modern sites block plain HTTP requests
- **Bot detection**: Sites using Cloudflare may block extraction

If `get_full_article()` fails consistently on a site, navigate to the URL directly in your browser.
