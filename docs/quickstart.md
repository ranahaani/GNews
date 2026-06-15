# Quickstart

## Search news

```python
from gnews import GNews

g = GNews()
articles = g.get_news("artificial intelligence")

for article in articles:
    print(article["title"])
    print(article["url"])
```

## Top headlines

```python
g = GNews(max_results=10)
articles = g.get_top_news()
```

## Filter by language and country

```python
g = GNews(language="de", country="DE", max_results=5)
articles = g.get_news("Bundesliga")
```

## What you get back

Each article is a dict:

```python
{
    "title": "OpenAI announces GPT-5",
    "description": "OpenAI has released...",
    "published date": "Mon, 15 Jun 2026 10:00:00 GMT",
    "url": "https://techcrunch.com/...",
    "publisher": "TechCrunch"
}
```

See [Article Properties](reference/api.md) for the full field reference.
