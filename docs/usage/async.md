# Async Support

All search methods have async equivalents. No extra dependencies — uses Python's built-in `asyncio`.

## Basic usage

```python
import asyncio
from gnews import GNews

g = GNews(max_results=10)

articles = asyncio.run(g.get_news_async("artificial intelligence"))
```

## Concurrent queries

The real power of async is fetching multiple queries simultaneously:

```python
import asyncio
from gnews import GNews

g = GNews(max_results=10)

async def main():
    ai, python, pakistan = await asyncio.gather(
        g.get_news_async("AI"),
        g.get_news_async("Python"),
        g.get_news_async("Pakistan"),
    )
    print(f"AI: {len(ai)} articles")
    print(f"Python: {len(python)} articles")
    print(f"Pakistan: {len(pakistan)} articles")

asyncio.run(main())
```

## Available async methods

| Async method | Sync equivalent |
|---|---|
| `get_news_async(key, page=1)` | `get_news()` |
| `get_top_news_async()` | `get_top_news()` |
| `get_news_by_topic_async(topic)` | `get_news_by_topic()` |
| `get_news_by_location_async(location)` | `get_news_by_location()` |
| `get_news_by_site_async(site)` | `get_news_by_site()` |

## With SearchApi backend

Works the same with the SearchApi backend:

```python
g = GNews(searchapi_key="YOUR_KEY", max_results=10)

async def main():
    results = await asyncio.gather(
        g.get_news_async("OpenAI"),
        g.get_news_async("Anthropic"),
        g.get_news_async("Google AI"),
    )
    return results

asyncio.run(main())
```

## FastAPI integration

```python
from fastapi import FastAPI
from gnews import GNews

app = FastAPI()
g = GNews(max_results=10)

@app.get("/news/{query}")
async def get_news(query: str):
    return await g.get_news_async(query)

@app.get("/top")
async def get_top():
    return await g.get_top_news_async()
```

## Notes

- Sync methods (`get_news()`, etc.) continue to work exactly as before
- Async methods run the sync implementation in a thread pool — safe for I/O-bound work
- All parameters and return values are identical to their sync counterparts
