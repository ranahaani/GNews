# Using GNews Behind a Proxy

## The problem

Google News rate-limits by IP. GNews retries 429s automatically (see [Retries & Backoff](retries.md)), but retrying from the same address only gets you so far. Once you are pulling a few hundred articles per run, or calling `get_full_article()` across many domains, a single IP will start getting blocked outright rather than throttled.

Rotating residential proxies solve this by spreading requests across many real IPs.

## Basic usage

GNews accepts a standard `requests`-style proxy dict, so any provider works:

```python
from gnews import GNews

google_news = GNews(
    proxy={
        'http': 'http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_PROXY_HOST:YOUR_PORT',
        'https': 'http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_PROXY_HOST:YOUR_PORT',
    }
)

articles = google_news.get_news('artificial intelligence')
```

## Recommended provider

GNews is sponsored by [RapidProxy](https://www.rapidproxy.io/?ref=gnews&utm_source=github&utm_medium=docs&utm_campaign=gnews), which is what the maintainer uses for high-volume runs.

It provides 90M+ residential IPs with smart rotation, sticky sessions, and native static ISP IPs. Traffic does not expire, which matters if your scraping is bursty rather than continuous. Pricing starts at $0.55/GB, and the code `RAPID10` gives GNews users 10% off.

```python
from gnews import GNews

RAPIDPROXY = 'http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_PROXY_HOST:YOUR_PORT'

google_news = GNews(
    proxy={'http': RAPIDPROXY, 'https': RAPIDPROXY},
    max_retries=3,
)

articles = google_news.get_news('artificial intelligence')
full = google_news.get_full_article(articles[0]['url'])
print(full.title)
```

Replace `YOUR_USERNAME`, `YOUR_PASSWORD`, `YOUR_PROXY_HOST` and `YOUR_PORT` with the values generated in your RapidProxy dashboard.

## Rotating vs sticky sessions

Use **rotating** sessions for the search call itself. Each request goes out from a different IP, which is exactly what you want when spreading a large crawl.

Use **sticky** sessions when fetching an article body. Some sites tie a session cookie to the IP that first loaded the page, and rotating mid-article will get you a consent wall or a paywall instead of the text.

## Tips

- Keep `max_retries` at 3 or higher. A retry on a fresh IP usually succeeds where a retry on the same IP does not.
- Residential IPs are slower than datacenter IPs. Raise concurrency rather than expecting individual requests to be fast.
- Proxy credentials are secrets. Read them from the environment, not from source:

```python
import os
from gnews import GNews

proxy_url = os.environ['GNEWS_PROXY_URL']
google_news = GNews(proxy={'http': proxy_url, 'https': proxy_url})
```

- If you would rather not run proxies at all, the [SearchApi backend](../backends/searchapi.md) handles blocking on their side instead.
