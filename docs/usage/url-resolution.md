# URL Resolution

## The problem

Google News RSS returns redirect URLs like:

```
https://news.google.com/rss/articles/CBMirwFBVV95cUx...
```

These are **not** real article URLs. Google requires JavaScript execution to resolve them — plain HTTP requests (`requests.get`, `requests.head`) cannot follow these redirects. This is a known Google behavior change since mid-2023.

## Solution: Playwright extra

Install the optional Playwright extra to resolve URLs automatically:

```shell
pip install gnews[playwright]
playwright install chromium  # one-time setup, downloads ~150MB
```

Once installed, URL resolution is **automatic** — no code changes required:

```python
from gnews import GNews

g = GNews(max_results=5)
articles = g.get_news("artificial intelligence")

print(articles[0]['url'])
# https://www.politico.com/news/2026/06/15/...  ← real URL
```

## Fallback behavior

If Playwright is not installed or resolution fails for a specific article, GNews silently returns the original Google URL — it never raises an error:

```python
# Without gnews[playwright]:
print(articles[0]['url'])
# https://news.google.com/rss/articles/CBMi...  ← Google URL
```

## Success rate

Based on community testing (~70-80% success rate):

| Site type | Result |
|-----------|--------|
| Standard news sites (BBC, Reuters, WSJ) | ✅ Resolved |
| Sites with cookie consent gates | ⚠️ May fail |
| Paywalled sites | ⚠️ May fail |

## Production alternative

For 100% reliable real URLs without Playwright, use the [SearchApi backend](../backends/searchapi.md):

```python
g = GNews(searchapi_key="YOUR_KEY")
articles = g.get_news("AI")
print(articles[0]['url'])  # always a real URL
```

## Proxy support

If your environment requires a proxy, pass it to `GNews` — it will be used for both RSS fetching **and** Playwright URL resolution:

```python
g = GNews(
    max_results=5,
    proxy={"https": "http://myproxy.example.com:8080"}
)
articles = g.get_news("artificial intelligence")
```

Prior to 0.9.0, the proxy was applied to RSS fetching but silently bypassed during Playwright URL resolution. This is now fixed.

## Manual resolution

You can also resolve individual URLs directly, with optional proxy:

```python
from gnews.utils.utils import resolve_url

google_url = "https://news.google.com/rss/articles/CBMi..."

# Without proxy
real_url = resolve_url(google_url)

# With proxy
real_url = resolve_url(google_url, proxies={"https": "http://myproxy:8080"})

print(real_url)
```
