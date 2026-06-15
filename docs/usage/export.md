# Exporting Results

## Save to JSON

```python
from gnews import GNews

g = GNews(max_results=20)
articles = g.get_news("artificial intelligence")

path = g.save_to_json(articles, "news.json")
print(f"Saved to {path}")
```

Output format:

```json
[
  {
    "title": "AI Breakthrough",
    "description": "Researchers have...",
    "published date": "Mon, 15 Jun 2026 10:00:00 GMT",
    "url": "https://example.com/ai",
    "publisher": "TechNews"
  }
]
```

## Save to CSV

```python
path = g.save_to_csv(articles, "news.csv")
```

The CSV header is auto-detected from the article fields. Compatible with Excel, pandas, and any CSV reader.

```python
import pandas as pd

df = pd.read_csv("news.csv")
print(df.head())
```

## Both methods return the path

```python
json_path = g.save_to_json(articles, "/tmp/news.json")
csv_path = g.save_to_csv(articles, "/tmp/news.csv")
```

No extra dependencies required — uses Python stdlib `json` and `csv`.
