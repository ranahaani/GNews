# Exceptions

All exceptions are in `gnews.exceptions`.

```python
from gnews.exceptions import NetworkError, InvalidConfigError, RateLimitError
```

## NetworkError

Raised when an article or feed cannot be fetched.

```python
from gnews.exceptions import NetworkError

try:
    articles = g.get_news("Python")
except NetworkError as e:
    print(f"Network error: {e}")
```

## InvalidConfigError

Raised when invalid parameters are passed.

```python
g = GNews(max_results=0)  # raises InvalidConfigError
g.exclude_websites = "yahoo.com"  # raises InvalidConfigError (must be list)
```

## RateLimitError

Raised when Google News rate-limits the RSS feed (HTTP 429).

```python
from gnews.exceptions import RateLimitError

try:
    articles = g.get_news("Python")
except RateLimitError:
    print("Rate limited — try again later or use SearchApi backend")
```

## GNewsException

Base class for all GNews exceptions.

```python
from gnews.exceptions import GNewsException

try:
    articles = g.get_news("Python")
except GNewsException as e:
    print(f"GNews error: {e}")
```
