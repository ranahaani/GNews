[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Download][download-sheild]][download-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ranahaani/GNews">
    <img src="https://github.com/ranahaani/GNews/raw/master/imgs/logo.png" alt="GNews">
  </a>

<h3 align="center">GNews</h3>

  <p align="center">
    A lightweight Python package that searches Google News and returns articles as JSON.
    <br />
    <br />
    <a href="https://github.com/ranahaani/GNews/blob/master/README.md">View Demo</a>
    ·
    <a href="https://github.com/ranahaani/GNews/issues">Report Bug</a>
    ·
    <a href="https://github.com/ranahaani/GNews/issues">Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
   <summary>Table of Contents</summary>
   <ol>
      <li>
         <a href="#about-gnews">About</a>
         <ul>
            <li><a href="#demo">Demo</a></li>
         </ul>
      </li>
      <li>
         <a href="#getting-started">Getting Started</a>
         <ul>
            <li><a href="#installation">Installation</a></li>
            <li><a href="#quick-start">Quick Start</a></li>
         </ul>
      </li>
      <li>
         <a href="#usage">Usage</a>
         <ul>
            <li><a href="#top-news">Top News</a></li>
            <li><a href="#news-by-keyword">News by Keyword</a></li>
            <li><a href="#news-by-topic">News by Topic</a></li>
            <li><a href="#news-by-location">News by Location</a></li>
            <li><a href="#news-by-site">News by Site</a></li>
            <li><a href="#configuration">Configuration</a></li>
            <li><a href="#article-properties">Article Properties</a></li>
            <li><a href="#getting-full-article">Getting Full Article</a></li>
         </ul>
      </li>
      <li><a href="#roadmap">Roadmap</a></li>
      <li><a href="#contributing">Contributing</a></li>
      <li><a href="#license">License</a></li>
      <li><a href="#contact">Contact</a></li>
      <li><a href="#acknowledgements">Acknowledgements</a></li>
   </ol>
</details>

## About GNews

GNews is a lightweight Python package that searches Google News RSS feeds and returns articles as structured JSON. It also provides a convenient method to fetch full article content without writing custom scrapers.

Google News covers **141+ countries** and **41+ languages**. The package supports most of these combinations.

### Demo

[![GNews Demo][demo-gif]](https://github.com/ranahaani/GNews)

## Getting Started

### Installation

Install the package directly from PyPI:

```shell
pip install gnews
```

### Quick Start

```python
from gnews import GNews

google_news = GNews()
articles = google_news.get_news('Python')
print(articles[0])
```

## Usage

### Top News

Retrieve the top news headlines for the configured country and language:

```python
articles = google_news.get_top_news()
```

### News by Keyword

Search for news containing a specific keyword:

```python
articles = google_news.get_news('Python')
```

### News by Topic

Fetch news articles for a predefined topic. Available topics include `WORLD`, `NATION`, `BUSINESS`, `TECHNOLOGY`, `ENTERTAINMENT`, `SPORTS`, `SCIENCE`, `HEALTH`, and many more. See the source code for the complete list.

```python
articles = google_news.get_news_by_topic('TECHNOLOGY')
```

### News by Location

Get news for a specific city, state, or country:

```python
articles = google_news.get_news_by_location('New York')
```

### News by Site

Limit results to a specific domain:

```python
articles = google_news.get_news_by_site('cnn.com')
```

### Configuration

All parameters are optional and can be set during initialization or later on the object.

| Parameter | Description | Default |
|-----------|-------------|---------|
| `language` | Language of the results (e.g., 'en', 'es') | `'en'` |
| `country` | Country code for headlines (e.g., 'US', 'GB') | `'US'` |
| `period` | Time period for news (e.g., '7d', '1y') | `None` |
| `start_date` | Start date as `datetime` or `(YYYY, MM, DD)` tuple | `None` |
| `end_date` | End date as `datetime` or `(YYYY, MM, DD)` tuple | `None` |
| `max_results` | Maximum number of articles to return | `100` |
| `exclude_websites` | List of domains to exclude | `[]` |
| `proxy` | Proxy dictionary for requests | `None` |

Example initialization with custom parameters:

```python
from gnews import GNews

google_news = GNews(
    language='en',
    country='US',
    period='7d',
    max_results=10,
    exclude_websites=['yahoo.com', 'cnn.com']
)
```

You can also modify these properties after creation:

```python
google_news.period = '1y'
google_news.max_results = 50
```

### Article Properties

Each article in the returned list contains the following keys:

| Key | Description |
|-----|-------------|
| `title` | Article title |
| `published_date` | Publication date in RFC 822 format |
| `description` | Short article summary |
| `url` | Direct link to the article on Google News |
| `publisher` | Name of the publishing source |

### Getting Full Article

To obtain the full article text, you can either visit the `url` directly or use the built‑in integration with `newspaper3k`.

1. Install newspaper3k:

```shell
pip install newspaper3k
```

2. Use the `get_full_article` method:

```python
from gnews import GNews

google_news = GNews()
articles = google_news.get_news('Python')
full_article = google_news.get_full_article(articles[0]['url'])

print(full_article.title)
print(full_article.text)
```

The returned object is a `newspaper.Article` instance, providing access to `title`, `text`, `images`, `authors`, and other attributes. Refer to the [newspaper3k documentation](https://newspaper.readthedocs.io/en/latest/) for details.

## Roadmap

See the [open issues](https://github.com/ranahaani/GNews/issues) for a list of proposed features and known issues.

## Contributing

Contributions are welcome and greatly appreciated.

1. Fork the project.
2. Create your feature branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a pull request.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Muhammad Abdullah – [@ranahaani](https://twitter.com/ranahaani) – ranahaani@gmail.com

Project Link: [https://github.com/ranahaani/GNews](https://github.com/ranahaani/GNews)

## Acknowledgements

* [newspaper3k](https://github.com/codelucas/newspaper)
* [Contributors](https://github.com/ranahaani/GNews/graphs/contributors)

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/ranahaani/GNews.svg?style=for-the-badge
[contributors-url]: https://github.com/ranahaani/GNews/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ranahaani/GNews.svg?style=for-the-badge
[forks-url]: https://github.com/ranahaani/GNews/network/members
[stars-shield]: https://img.shields.io/github/stars/ranahaani/GNews.svg?style=for-the-badge
[stars-url]: https://github.com/ranahaani/GNews/stargazers
[issues-shield]: https://img.shields.io/github/issues/ranahaani/GNews.svg?style=for-the-badge
[issues-url]: https://github.com/ranahaani/GNews/issues
[license-shield]: https://img.shields.io/github/license/ranahaani/GNews.svg?style=for-the-badge
[license-url]: https://github.com/ranahaani/GNews/blob/master/LICENSE.txt
[download-sheild]: https://img.shields.io/pypi/dm/GNews.svg?style=for-the-badge
[download-url]: https://pypistats.org/packages/gnews
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/ranahaani
[demo-gif]: https://github.com/ranahaani/GNews/raw/master/imgs/gnews.gif