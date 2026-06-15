# Installation

## Basic Install

```shell
pip install gnews
```

Requires Python 3.10+.

## With Full Article Support

To use `get_full_article()`, install the `fulltext` extra:

```shell
pip install gnews[fulltext]
```

This adds [trafilatura](https://trafilatura.readthedocs.io/) for article text extraction.

## With Real URL Resolution

To resolve Google News redirect URLs to real article URLs:

```shell
pip install gnews[playwright]
playwright install chromium  # one-time, downloads ~150MB Chromium
```

This adds [Playwright](https://playwright.dev/python/) for headless browser URL resolution. See [URL Resolution](usage/url-resolution.md) for details.

## Install all extras

```shell
pip install "gnews[fulltext,playwright]"
playwright install chromium
```

## Development Install

```shell
git clone https://github.com/ranahaani/GNews.git
cd GNews
pip install -r requirements.txt
```
