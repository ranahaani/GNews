# Retries & Backoff

## The problem

Google News RSS returns **HTTP 429 (Too Many Requests)** when callers fetch too aggressively. Prior to 0.8.2, a single 429 raised `RateLimitError` immediately — every downstream consumer had to wrap `get_news()` in its own retry loop.

Since 0.8.2, GNews retries 429 responses automatically with capped exponential backoff plus uniform jitter.

## Defaults (no code changes required)

```python
from gnews import GNews

g = GNews()  # max_retries=3, retry_backoff_base=1.0s, retry_backoff_max=60.0s
articles = g.get_news("OpenAI")
# Up to 4 total attempts (1 initial + 3 retries) with growing backoff between them.
```

## Tuning

```python
from gnews import GNews

g = GNews(
    max_retries=5,           # retry up to 5 times after the initial attempt
    retry_backoff_base=2.0,  # 2s, 4s, 8s, 16s, 32s growth
    retry_backoff_max=30.0,  # cap any single wait at 30s
)
```

## Disabling retries (previous behaviour)

```python
g = GNews(max_retries=0)
# Behaves exactly like 0.8.1 and earlier — first 429 raises RateLimitError.
```

## Backoff formula

Each retry waits:

```
delay = min(retry_backoff_max, retry_backoff_base * 2 ** attempt) + uniform(0, retry_backoff_base)
```

where `attempt` is the zero-indexed retry number. The jitter term avoids thundering-herd retries when many clients hit the same 429 at the same moment.

## When retries give up

After `max_retries + 1` total attempts, `RateLimitError` is raised. Catch it the same way you always have:

```python
from gnews import GNews
from gnews.exceptions import RateLimitError

try:
    articles = g.get_news("OpenAI")
except RateLimitError:
    # Google is still saying no — back off at the application level
    ...
```

## What is not retried

- `NetworkError` (DNS, TLS, parser failures) — these are usually not transient at the HTTP layer; raise immediately.
- Non-429 success/empty responses — returned as-is.
- 429s during `_get_news_more_than_100` pagination — each individual page fetch is retried independently, but a permanent 429 will still terminate the walk.
