# CLI Usage

GNews includes a command-line interface available after `pip install gnews`.

## Commands

### search

```shell
gnews search "artificial intelligence"
gnews search "Pakistan" --lang ur --country PK --max 5
gnews search "OpenAI" --json
```

### top

```shell
gnews top
gnews top --max 20 --json
```

### topic

```shell
gnews topic TECHNOLOGY
gnews topic BUSINESS --max 10 --json
```

### site

```shell
gnews site bbc.com
gnews site cnn.com --max 5 --json
```

### location

```shell
gnews location Pakistan
gnews location "New York" --json
```

## Common options

| Option | Default | Description |
|--------|---------|-------------|
| `--lang` | `en` | Language code |
| `--country` | `US` | Country code |
| `--max` | `10` | Max results |
| `--json` | off | Output as JSON |

## JSON output

The `--json` flag outputs valid JSON to stdout, making it easy to pipe into other tools:

```shell
gnews search "AI" --json | python3 -m json.tool
gnews top --json | jq '.[0].title'
```
