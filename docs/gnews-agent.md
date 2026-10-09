# gnews-agent

[gnews-agent](https://github.com/ranahaani/gnews-agent) is the sibling package to GNews: a persistent, semantic news intelligence layer for AI agents.

GNews returns articles from Google News. gnews-agent keeps them. It fetches through GNews (141+ countries, 41+ languages), deduplicates by title and publisher, embeds the text, and stores it in SQLite plus a local vector index. Later searches hit that store instead of issuing another live query.

The same six operations are available from Python, the `gnews-agent` CLI, and an MCP server:

| Operation | What it does | API key |
|-----------|----------------|---------|
| `ingest` | Fetch, dedupe, embed, and store | No |
| `search` | Semantic search, re-ranked by recency | No |
| `timeline` | Articles for a topic over a window | No |
| `stats` | Counts for the local store | No |
| `brief` | Cited LLM summary | Yes |
| `sentiment` | LLM sentiment over the stored articles | Yes |

Published on PyPI as [`gnews-agent`](https://pypi.org/project/gnews-agent/). Requires Python 3.10+ and depends on `gnews>=0.8.2`.

## Install

```shell
pip install gnews-agent
```

Confirm the console script is on your path:

```shell
gnews-agent --version
```

Optional extras, only if you need them:

```shell
pip install "gnews-agent[openai]"     # OpenAI embedding backend
pip install "gnews-agent[fulltext]"   # full-article extraction via trafilatura
```

`lance`, `qdrant`, and `evals` extras are documented in the [gnews-agent README](https://github.com/ranahaani/gnews-agent#installation).

## Minimal example

The default store is SQLite plus Chroma on disk. `ingest` and `search` do not need an API key:

```python
from gnews_agent import NewsMemory

memory = NewsMemory()
memory.ingest("OpenAI", method="get_news")
results = memory.search("GPT-5 safety", days=7)
print(results)
```

The same store answers the other keyless calls:

```python
print(memory.timeline("OpenAI", days=30))
print(memory.stats())
```

`brief` and `sentiment` call an LLM. Set one provider key (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GROQ_API_KEY`, or `GEMINI_API_KEY`), or point the package at a local Ollama server. Variable names and model settings are in the [gnews-agent configuration section](https://github.com/ranahaani/gnews-agent#configuration).

## CLI

Every command prints JSON:

```shell
gnews-agent ingest "OpenAI" --method get_news
gnews-agent search "GPT-5 safety" --days 7 --limit 5
gnews-agent stats
```

## MCP server

`gnews-agent serve` exposes search, brief, sentiment, timeline, and topic monitoring to Claude, Cursor, and any other MCP client:

```shell
gnews-agent serve --transport stdio
```

Client config, the Claude Code `/gnews` skill, and the Docker image are documented in the [gnews-agent README](https://github.com/ranahaani/gnews-agent#readme).
