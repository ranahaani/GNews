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

## Development Install

```shell
git clone https://github.com/ranahaani/GNews.git
cd GNews
pip install -r requirements.txt
```
