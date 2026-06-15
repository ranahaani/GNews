# API Reference

## GNews

```python
class GNews(
    language: str = "en",
    country: str = "US",
    max_results: int = 100,
    period: str | None = None,
    start_date: tuple | datetime | None = None,
    end_date: tuple | datetime | None = None,
    exclude_websites: list[str] | None = None,
    proxy: dict | None = None,
    searchapi_key: str | None = None,
)
```

### Methods

#### get_news(key, page=1)

Search news by keyword.

```python
articles = g.get_news("OpenAI")
articles = g.get_news("Python", page=2)  # pagination (SearchApi only)
```

**Returns:** `list[dict]`

---

#### get_top_news()

Get current top headlines.

```python
articles = g.get_top_news()
```

**Returns:** `list[dict]`

---

#### get_news_by_topic(topic)

Get news for a major topic.

```python
articles = g.get_news_by_topic("TECHNOLOGY")
```

**Returns:** `list[dict]`

---

#### get_news_by_location(location)

Get news for a city, state, or country.

```python
articles = g.get_news_by_location("Pakistan")
```

**Returns:** `list[dict]`

---

#### get_news_by_site(site)

Get news from a specific domain.

```python
articles = g.get_news_by_site("bbc.com")
```

**Returns:** `list[dict]`

---

#### get_full_article(url)

Extract full article text. Requires `pip install gnews[fulltext]`.

```python
article = g.get_full_article("https://example.com/article")
# {"text": "...", "url": "..."}
```

**Returns:** `dict` with keys `text`, `url`

**Raises:** `ImportError` if trafilatura not installed, `NetworkError` on failure

---

#### save_to_json(articles, path)

Save articles to a JSON file.

```python
g.save_to_json(articles, "news.json")
```

**Returns:** `str` — the output path

---

#### save_to_csv(articles, path)

Save articles to a CSV file.

```python
g.save_to_csv(articles, "news.csv")
```

**Returns:** `str` — the output path

---

## Article Properties

### RSS backend fields

| Field | Type | Description |
|-------|------|-------------|
| `title` | str | Article title |
| `description` | str | Short summary |
| `published date` | str | RFC 2822 date |
| `url` | str | Article URL |
| `publisher` | str/dict | Publisher info |

### SearchApi extra fields

| Field | Type | Description |
|-------|------|-------------|
| `iso_date` | str | ISO 8601 date |
| `thumbnail` | str | Article image (base64) |
| `favicon` | str | Publisher logo (base64) |
| `rank` | int | Position in results |
