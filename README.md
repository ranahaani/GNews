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
  
<h3 align="center">GNews 📰</h3>

  <p align="center">
    A Happy and lightweight Python Package that Provides an API to search for articles on Google News and returns a usable JSON response! 🚀
    <br />    
    If you like ❤️ GNews or find it useful 🌟, support the project by buying me a coffee ☕.
    <br />
    <a href="https://www.buymeacoffee.com/ranahaani" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" ></a>
    <br />
    <br />
    <a href="https://github.com/ranahaani/GNews/blob/master/README.md">🚀 View Demo</a>
    ·
    <a href="https://github.com/ranahaani/GNews/issues">🐞 Report Bug</a>
    ·
    <a href="https://github.com/ranahaani/GNews/issues">🚀 Request Feature</a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
   <summary>Table of Contents 📑</summary>
   <ol>
      <li>
         <a href="#about-gnews">About 🚩</a>
         <ul>
            <li><a href="#demo">Demo 📺</a></li>
         </ul>
      </li>
      <li>
         <a href="#getting-started">Getting Started 🚀</a>
         <ul>
            <li><a href="#1-installing-the-gnews-package">Installing the GNews package 📦</a></li>
         </ul>
        <ul>
            <li><a href="#2-setting-up-gnews-for-local-development">Setting Up GNews for Local Development 🧑‍💻</a></li>
         </ul>
      </li>
      <li>
         <a href="#example-usage">Usage 🧩</a>
         <ul>
            <li><a href="#get-top-news">Top News 🌟</a></li>
            <li><a href="#get-news-by-keyword">News by Keywords 🔎</a></li>
            <li><a href="#get-news-by-major-topic">News by Major Topics 🚀</a></li>
            <li><a href="#get-news-by-geo-location">News by GEO Location 🌎</a></li>
            <li><a href="#get-news-by-site">News by Site 📰</a></li>
            <li><a href="#results-specification">Results 📊</a></li>
            <li><a href="#supported-countries">Supported Countries 🌐</a></li>
            <li><a href="#supported-languages">Supported Languages 🌍</a></li>
            <li><a href="#article-properties">Article Properties 📝</a></li>
            <li><a href="#getting-full-article">Getting Full Article 📰</a></li>
         </ul>
      </li>
      <li>
         <a href="#real-world-examples">Real-World Examples 🌍</a>
         <ul>
            <li><a href="#1-building-a-news-bot">Building a News Bot 🤖</a></li>
            <li><a href="#2-market-sentiment-analysis">Market Sentiment Analysis 📈</a></li>
            <li><a href="#3-research-data-collection">Research Data Collection 🔬</a></li>
            <li><a href="#4-news-monitoring-dashboard">News Monitoring Dashboard 📡</a></li>
            <li><a href="#5-multi-language-news-aggregation">Multi-language News Aggregation 🌐</a></li>
         </ul>
      </li>
      <li><a href="#todo">To Do 📋</a></li>
      <li><a href="#roadmap">Roadmap 🛣️</a></li>
      <li><a href="#contributing">Contributing 🤝</a></li>
      <li><a href="#license">License ⚖️</a></li>
      <li><a href="#contact">Contact 📬</a></li>
      <li><a href="#acknowledgements">Acknowledgements 🙏</a></li>
   </ol>
</details>
<!-- ABOUT GNews -->

## About GNews

🚩 GNews is a lightweight Python Package that searches Google News RSS Feed and returns a usable JSON response. \
🚩 You can also fetch full articles (**no need to write scrapers for article fetching anymore**).

Google News covers **141+ countries** with **41+ languages**. On the bottom left side of the Google News page you can find a `Language & region` section with all supported combinations.

### Demo

[![GNews Demo][demo-gif]](https://github.com/ranahaani/GNews)



<!-- GETTING STARTED -->

## Getting Started

This section provides instructions for two different use cases:

1. **Installing the GNews package** for immediate use.
2. **Setting up the GNews project** for local development.

### 1. Installing the GNews package

```shell
pip install gnews
```

### 2. Setting Up GNews for Local Development

#### Option 1: Setup with Docker

1. Install [docker and docker-compose](https://docs.docker.com/get-docker/).
2. Configure the `.env` file with your MongoDB credentials.
3. Run:

```shell
docker-compose up --build
```

#### Option 2: Install Using Git Clone

1. Clone the repository:
```shell
git clone https://github.com/ranahaani/GNews.git
```

2. Set up a virtual environment:
```shell
virtualenv venv
source venv/bin/activate  # MacOS/Linux
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```shell
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->

## Example usage

```python
from gnews import GNews

google_news = GNews()
pakistan_news = google_news.get_news('Pakistan')
print(pakistan_news[0])
```

Output:
```
{
  'publisher': 'Aljazeera.com',
  'description': 'Pakistan accuses India of stoking conflict in Indian Ocean - Aljazeera.com',
  'published date': 'Tue, 16 Feb 2021 11:50:43 GMT',
  'title': 'Pakistan accuses India of stoking conflict in Indian Ocean - Aljazeera.com',
  'url': 'https://www.aljazeera.com/news/2021/2/16/pakistan-accuses-india-of-nuclearizing-indian-ocean'
}
```

### 📘 Interactive Tutorial

We have created a step-by-step **[Jupyter Notebook tutorial]** that demonstrates:

- Basic usage and setup  
- Filtering news (by topic, location, domain, date range, etc.)
- Exporting results (CSV, JSON)  
- Real-world analysis: **Sentiment Analysis on news headlines**
- Advanced usage & best practices  
- Interactive examples you can run line-by-line

👉 **Open the tutorial here:** [examples/tutorial.ipynb](./examples/tutorial.ipynb)

---

### Get top news

```python
google_news.get_top_news()
```

### Get news by keyword

```python
google_news.get_news('Artificial Intelligence')
```

### Get news by major topic

```python
google_news.get_news_by_topic('BUSINESS')
```

Available topics: `WORLD`, `NATION`, `BUSINESS`, `TECHNOLOGY`, `ENTERTAINMENT`, `SPORTS`, `SCIENCE`, `HEALTH`, `POLITICS`, `CELEBRITIES`, `TV`, `MUSIC`, `MOVIES`, `THEATER`, `SOCCER`, `CYCLING`, `MOTOR SPORTS`, `TENNIS`, `COMBAT SPORTS`, `BASKETBALL`, `BASEBALL`, `FOOTBALL`, `SPORTS BETTING`, `WATER SPORTS`, `HOCKEY`, `GOLF`, `CRICKET`, `RUGBY`, `ECONOMY`, `PERSONAL FINANCE`, `FINANCE`, `DIGITAL CURRENCIES`, `MOBILE`, `ENERGY`, `GAMING`, `INTERNET SECURITY`, `GADGETS`, `VIRTUAL REALITY`, `ROBOTICS`, `NUTRITION`, `PUBLIC HEALTH`, `MENTAL HEALTH`, `MEDICINE`, `SPACE`, `WILDLIFE`, `ENVIRONMENT`, `NEUROSCIENCE`, `PHYSICS`, `GEOLOGY`, `PALEONTOLOGY`, `SOCIAL SCIENCES`, `EDUCATION`, `JOBS`, `ONLINE EDUCATION`, `HIGHER EDUCATION`, `VEHICLES`, `ARTS-DESIGN`, `BEAUTY`, `FOOD`, `TRAVEL`, `SHOPPING`, `HOME`, `OUTDOORS`, `FASHION`.

### Get news by geo location

```python
google_news.get_news_by_location('New York')
```

Location can be the name of a city, state, or country.

### Get news by site

```python
google_news.get_news_by_site('cnn.com')
```

Site should be in the format `"domain.com"`.

### Results specification

All parameters are optional and can be passed during initialization:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `language` | Language in which to return results | `'en'` |
| `country` | Country code for headlines | `'US'` |
| `period` | Time period for news (e.g., `'7d'`) | `None` |
| `start_date` | Date after which results must have been published | `None` |
| `end_date` | Date before which results must have been published | `None` |
| `max_results` | Maximum number of results to return | `100` |
| `exclude_websites` | List of websites to exclude from results | `[]` |
| `proxy` | Proxy settings for routing requests | `None` |

#### Example Initialization

```python
from gnews import GNews

google_news = GNews(
    language='en',
    country='US',
    period='7d',
    max_results=10,
    exclude_websites=['yahoo.com', 'cnn.com'],
    proxy={'https': 'https://your_proxy_address'}
)
```

You can also update parameters on an existing object:

```python
google_news.period = '7d'            # News from last 7 days
google_news.max_results = 10         # Limit number of responses
google_news.country = 'United States'  # News from a specific country
google_news.language = 'english'     # News in a specific language
google_news.exclude_websites = ['yahoo.com', 'cnn.com']
google_news.start_date = (2020, 1, 1)  # Search from 1st Jan 2020
google_news.end_date = (2020, 3, 1)    # Search until 1st March 2020
```

**Time period format:** A number followed by a letter: `h` (hours), `d` (days), `m` (months), `y` (years). Examples: `12h`, `7d`, `6m`, `1y`.

**Date format:** `start_date` and `end_date` accept either a `datetime` object or a tuple `(YYYY, MM, DD)`.

**Proxy format:** A dictionary with protocol as key and proxy address as value:
```python
proxy = {'http': 'http://your_proxy_address'}
proxy = {'https': 'https://your_proxy_address'}
```
### Supported Countries

```python
print(google_news.AVAILABLE_COUNTRIES)

{'Australia': 'AU', 'Botswana': 'BW', 'Canada ': 'CA', 'Ethiopia': 'ET', 'Ghana': 'GH', 'India ': 'IN',
 'Indonesia': 'ID', 'Ireland': 'IE', 'Israel ': 'IL', 'Kenya': 'KE', 'Latvia': 'LV', 'Malaysia': 'MY', 'Namibia': 'NA',
 'New Zealand': 'NZ', 'Nigeria': 'NG', 'Pakistan': 'PK', 'Philippines': 'PH', 'Singapore': 'SG', 'South Africa': 'ZA',
 'Tanzania': 'TZ', 'Uganda': 'UG', 'United Kingdom': 'GB', 'United States': 'US', 'Zimbabwe': 'ZW',
 'Czech Republic': 'CZ', 'Germany': 'DE', 'Austria': 'AT', 'Switzerland': 'CH', 'Argentina': 'AR', 'Chile': 'CL',
 'Colombia': 'CO', 'Cuba': 'CU', 'Mexico': 'MX', 'Peru': 'PE', 'Venezuela': 'VE', 'Belgium ': 'BE', 'France': 'FR',
 'Morocco': 'MA', 'Senegal': 'SN', 'Italy': 'IT', 'Lithuania': 'LT', 'Hungary': 'HU', 'Netherlands': 'NL',
 'Norway': 'NO', 'Poland': 'PL', 'Brazil': 'BR', 'Portugal': 'PT', 'Romania': 'RO', 'Slovakia': 'SK', 'Slovenia': 'SI',
 'Sweden': 'SE', 'Vietnam': 'VN', 'Turkey': 'TR', 'Greece': 'GR', 'Bulgaria': 'BG', 'Russia': 'RU', 'Ukraine ': 'UA',
 'Serbia': 'RS', 'United Arab Emirates': 'AE', 'Saudi Arabia': 'SA', 'Lebanon': 'LB', 'Egypt': 'EG',
 'Bangladesh': 'BD', 'Thailand': 'TH', 'China': 'CN', 'Taiwan': 'TW', 'Hong Kong': 'HK', 'Japan': 'JP',
 'Republic of Korea': 'KR'}
```

### Supported Languages

```python
print(google_news.AVAILABLE_LANGUAGES)

{'english': 'en', 'indonesian': 'id', 'czech': 'cs', 'german': 'de', 'spanish': 'es-419', 'french': 'fr',
 'italian': 'it', 'latvian': 'lv', 'lithuanian': 'lt', 'hungarian': 'hu', 'dutch': 'nl', 'norwegian': 'no',
 'polish': 'pl', 'portuguese brasil': 'pt-419', 'portuguese portugal': 'pt-150', 'romanian': 'ro', 'slovak': 'sk',
 'slovenian': 'sl', 'swedish': 'sv', 'vietnamese': 'vi', 'turkish': 'tr', 'greek': 'el', 'bulgarian': 'bg',
 'russian': 'ru', 'serbian': 'sr', 'ukrainian': 'uk', 'hebrew': 'he', 'arabic': 'ar', 'marathi': 'mr', 'hindi': 'hi',
 'bengali': 'bn', 'tamil': 'ta', 'telugu': 'te', 'malyalam': 'ml', 'thai': 'th', 'chinese simplified': 'zh-Hans',
 'chinese traditional': 'zh-Hant', 'japanese': 'ja', 'korean': 'ko'}
```

### Article Properties

Each news result contains the following fields:

| Property | Description |
|----------|-------------|
| `title` | Title of the article |
| `url` | Google news link to the article |
| `published date` | Publication date |
| `description` | Short description of the article |
| `publisher` | Publisher of the article |

## Getting full article

Use the `newspaper3k` library to scrape the full article content:

1. Install: `pip3 install newspaper3k`
2. Fetch the article:

```python
from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('Pakistan')
article = google_news.get_full_article(json_resp[0]['url'])

# Access article properties
article.title    # Article title
article.text     # Full article text
article.images   # Set of image URLs
article.authors  # List of authors
```

See full `newspaper3k` documentation [here](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#parsing-an-article).

---

## Real-World Examples

### 1. Building a News Bot

Create a simple bot that fetches top news and formats summaries for posting to Slack, Discord, or other platforms.

```python
from gnews import GNews

def fetch_and_format_news(topic, max_results=5):
    '''Fetch top news for a topic and format as a message.'''
    google_news = GNews(language='en', max_results=max_results)
    articles = google_news.get_news(topic)

    messages = []
    for i, article in enumerate(articles, 1):
        msg = f\"{i}. {article['title']}\n   {article['url']}\"
        messages.append(msg)

    return '\n\n'.join(messages)

if __name__ == '__main__':
    news_digest = fetch_and_format_news('Python Programming')
    print(news_digest)
```

### 2. Market Sentiment Analysis

Analyze financial news headlines to gauge market sentiment using a keyword-based approach.

```python
from gnews import GNews

def analyze_market_sentiment(ticker, max_results=20):
    '''Fetch news for a stock ticker and perform basic sentiment analysis.'''
    google_news = GNews(language='en', country='US', max_results=max_results)
    articles = google_news.get_news(ticker)

    positive_keywords = ['surge', 'growth', 'profit', 'gain', 'rise', 'bullish', 'record high']
    negative_keywords = ['fall', 'loss', 'decline', 'drop', 'crash', 'bearish', 'recession']

    positive_count = 0
    negative_count = 0

    for article in articles:
        title = article['title'].lower()
        if any(kw in title for kw in positive_keywords):
            positive_count += 1
        elif any(kw in title for kw in negative_keywords):
            negative_count += 1

    total = positive_count + negative_count or 1
    sentiment_score = (positive_count - negative_count) / total

    print(fNews Sentiment for {ticker}:)
    print(f  Positive: {positive_count} | Negative: {negative_count})
    print(f  Sentiment Score: {sentiment_score:+.2f})
    return sentiment_score

if __name__ == '__main__':
    analyze_market_sentiment('Apple Inc')
```

### 3. Research Data Collection

Collect and save news articles as JSON for academic research or data analysis pipelines.

```python
from gnews import GNews
import json
from datetime import datetime

def collect_research_data(keywords, output_file='research_data.json'):
    '''Collect news articles for research and save to a JSON file.'''
    google_news = GNews(language='en', max_results=50)
    all_articles = []

    for keyword in keywords:
        articles = google_news.get_news(keyword)
        for article in articles:
            all_articles.append({
                'keyword': keyword,
                'title': article['title'],
                'url': article['url'],
                'published_date': article['published date'],
                'publisher': article['publisher'],
                'description': article['description'],
                'collected_at': datetime.now().isoformat()
            })

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_articles, f, indent=2, ensure_ascii=False)

    print(fCollected {len(all_articles)} articles -> {output_file})
    return all_articles

if __name__ == '__main__':
    keywords = ['climate change', 'renewable energy', 'carbon emissions']
    collect_research_data(keywords)
```

### 4. News Monitoring Dashboard

Build a monitoring system that tracks specific topics and flags new articles as they appear.

```python
from gnews import GNews
import time

class NewsMonitor:
    '''Monitor news for specific topics and flag new articles.'''

    def __init__(self, topics, interval=300):
        self.google_news = GNews(language='en', max_results=10)
        self.topics = topics
        self.interval = interval  # seconds between checks
        self.seen_urls = {topic: set() for topic in topics}

    def check_for_new_articles(self):
        '''Check each topic for new articles since the last check.'''
        for topic in self.topics:
            articles = self.google_news.get_news(topic)
            new_articles = [
                a for a in articles if a['url'] not in self.seen_urls[topic]
            ]

            if new_articles:
                print(f
🔔 {len(new_articles)} new article(s) for '{topic}':)
                for article in new_articles:
                    print(f  - {article['title']})
                    self.seen_urls[topic].add(article['url'])
            else:
                print(f  No new articles for '{topic}')

    def run(self, iterations=5):
        '''Run the monitor for a given number of iterations.'''
        print(fStarting News Monitor (topics: {self.topics}))
        for i in range(iterations):
            print(f
--- Check {i + 1}/{iterations} ---)
            self.check_for_new_articles()
            if i < iterations - 1:
                time.sleep(self.interval)

if __name__ == '__main__':
    monitor = NewsMonitor(topics=['Artificial Intelligence', 'Space Exploration'])
    monitor.run(iterations=3)
```

### 5. Multi-language News Aggregation

Aggregate news about the same topic from multiple languages and countries for a global perspective.

```python
from gnews import GNews

def aggregate_multilingual_news(keyword, language_country_pairs):
    '''Fetch news for a keyword across multiple languages and countries.'''
    all_results = {}

    for language, country in language_country_pairs:
        try:
            google_news = GNews(language=language, country=country, max_results=5)
            articles = google_news.get_news(keyword)
            all_results[f{language}_{country}] = [
                {
                    'title': a['title'],
                    'url': a['url'],
                    'publisher': a['publisher']
                }
                for a in articles
            ]
            print(f  {language}/{country}: {len(articles)} articles found)
        except Exception as e:
            print(f  {language}/{country}: Error - {e})

    return all_results

if __name__ == '__main__':
    keyword = 'Climate Change'
    pairs = [
        ('en', 'US'),      # English / United States
        ('fr', 'FR'),      # French / France
        ('de', 'DE'),      # German / Germany
        ('es-419', 'AR'),  # Spanish / Argentina
        ('ja', 'JP'),      # Japanese / Japan
    ]

    print(fAggregating news for: '{keyword}')
    results = aggregate_multilingual_news(keyword, pairs)

    for region, articles in results.items():
        print(f
--- {region} ---)
        for a in articles[:3]:
            print(f  {a['title']})
```

---

<!-- ToDo -->

## Todo

- Save to MongoDB
- Save to SQLite
- Save to JSON
- Save to .CSV file
- More than 100 articles

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/ranahaani/GNews/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## Contact

Muhammad Abdullah - [@ranahaani](https://twitter.com/ranahaani) - ranahaani@gmail.com

Project Link: [https://github.com/ranahaani/GNews](https://github.com/ranahaani/GNews)

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ranahaani)

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
