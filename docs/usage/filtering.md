# Filtering Results

## Initialization parameters

```python
from gnews import GNews

g = GNews(
    language="en",       # Language code (default: "en")
    country="US",        # Country code (default: "US")
    max_results=10,      # Max articles to return (default: 100)
    period="7d",         # Time period: 1h, 7d, 6m, 1y
    start_date=(2026, 1, 1),   # Or datetime object
    end_date=(2026, 6, 1),
    exclude_websites=["yahoo.com", "cnn.com"],
    proxy={"https": "https://your_proxy_address"},
)
```

## Update after creation

```python
g.language = "fr"
g.country = "FR"
g.max_results = 5
g.period = "1d"
g.start_date = (2026, 1, 1)
g.end_date = (2026, 6, 1)
g.exclude_websites = ["yahoo.com"]
```

## Period format

| Value | Meaning |
|-------|---------|
| `12h` | Last 12 hours |
| `7d` | Last 7 days |
| `6m` | Last 6 months |
| `1y` | Last 1 year |

## Date range

```python
from datetime import datetime

g = GNews(
    start_date=(2026, 1, 1),
    end_date=(2026, 6, 1),
)
# Or using datetime objects
g.start_date = datetime(2026, 1, 1)
g.end_date = datetime(2026, 6, 1)
```

> **Note:** Date ranges only work with `get_news()`. Other methods ignore start/end dates.
