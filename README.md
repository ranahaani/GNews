[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![MIT License][license-shield]][license-url] [![Download][download-sheild]][download-url] [![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/ranahaani/GNews">
    <img src="https://github.com/ranahaani/GNews/raw/master/imgs/logo.png" alt="GNews">
  </a>
<h3 align="center">GNews 📰</h3>
  <p align="center">
    A lightweight Python package that searches Google News and returns a usable JSON response! 🚀
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
      <li><a href="#about-gnews">About 🚩</a><ul><li><a href="#demo">Demo 📺</a></li></ul></li>
      <li><a href="#getting-started">Getting Started 🚀</a><ul><li><a href="#1-installing-the-gnews-package">Installing the GNews package 📦</a></li><li><a href="#2-setting-up-gnews-for-local-development">Setting Up GNews for Local Development 🧑‍💻</a></li></ul></li>
      <li><a href="#example-usage">Usage 🧩</a><ul><li><a href="#Get-top-news">Top News 🌟</a></li><li><a href="#Get-news-by-keyword">News by Keywords 🔎</a></li><li><a href="#Get-news-by-major-topic">News by Major Topics 🚀</a></li><li><a href="#Get-news-by-geo-location">News by GEO Location 🌎</a></li><li><a href="#get-news-by-site">News by Site 📰</a></li><li><a href="#results-specification">Results 📊</a></li><li><a href="#supported-countries">Supported Countries 🌐</a></li><li><a href="#supported-languages">Supported Languages 🌍</a></li><li><a href="#article-properties">Article Properties 📝</a></li><li><a href="#getting-full-article">Getting Full Article 📰</a></li></ul></li>
      <li><a href="#real-world-examples">Real-World Examples 🌍</a><ul><li><a href="#1-building-a-news-bot">Building a News Bot</a></li><li><a href="#2-market-sentiment-analysis">Market Sentiment Analysis</a></li><li><a href="#3-research-data-collection">Research Data Collection</a></li><li><a href="#4-news-monitoring-dashboard">News Monitoring Dashboard</a></li><li><a href="#5-multi-language-news-aggregation">Multi-language News Aggregation</a></li></ul></li>
      <li><a href="#todo">To Do 📋</a></li>
      <li><a href="#roadmap">Roadmap 🛣️</a></li>
      <li><a href="#contributing">Contributing 🤝</a></li>
      <li><a href="#license">License ⚖️</a></li>
      <li><a href="#contact">Contact 📬</a></li>
      <li><a href="#acknowledgements">Acknowledgements 🙏</a></li>
   </ol>
</details>

## About GNews

GNews is a lightweight Python package that searches Google News RSS Feed and returns a usable JSON response. You can also fetch full articles — **no need to write scrapers for article fetching anymore!**

Google News covers **141+ countries** with **41+ languages**. On the bottom left side of the Google News page you can find a `Language & region` section with all supported combinations.

### Demo

[![GNews Demo][demo-gif]](https://github.com/ranahaani/GNews)

## Getting Started

This section covers two use cases:

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
.\venv\Scripts\activate   # Windows
```

3. Install dependencies:
```shell
pip install -r requirements.txt
```

## Example usage

```python
from gnews import GNews

google_news = GNews()
pakistan_news = google_news.get_news('Pakistan')
print(pakistan_news[0])
```

Output:
```
[{
'publisher': 'Aljazeera.com',
 'description': 'Pakistan accuses India of stoking conflict in Indian Ocean Aljazeera.com',
 'published date': 'Tue, 16 Feb 2021 11:50:43 GMT',
 'title': 'Pakistan accuses India of stoking conflict in Indian Ocean - Aljazeera.com',
 'url': 'https://www.aljazeera.com/news/2021/2/16/pakistan-accuses-india-of-nuclearizing-indian-ocean'
 }, ...]
```

### 📘 Interactive Tutorial

A step-by-step **[Jupyter Notebook tutorial]** demonstrates:

- Basic usage and setup
- Filtering news (by topic, location, domain, date range, etc.)
- Exporting results (CSV, JSON)
- Real-world analysis: **Sentiment Analysis on news headlines**
- Advanced usage & best practices

👉 **Open the tutorial:** [examples/tutorial.ipynb](./examples/tutorial.ipynb)

### Get top news

```python
google_news = GNews()
top_news = google_news.get_top_news()
```

### Get news by keyword

```python
google_news = GNews()
news = google_news.get_news('artificial intelligence')
```

### Get news by major topic

```python
google_news = GNews()
tech_news = google_news.get_news_by_topic('TECHNOLOGY')
```

Available topics: `WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH, POLITICS, CELEBRITIES, TV, MUSIC, MOVIES, THEATER, SOCCER, CYCLING, MOTOR SPORTS, TENNIS, COMBAT SPORTS, BASKETBALL, BASEBALL, FOOTBALL, SPORTS BETTING, WATER SPORTS, HOCKEY, GOLF, CRICKET, RUGBY, ECONOMY, PERSONAL FINANCE, FINANCE, DIGITAL CURRENCIES, MOBILE, ENERGY, GAMING, INTERNET SECURITY, GADGETS, VIRTUAL REALITY, ROBOTICS, NUTRITION, PUBLIC HEALTH, MENTAL HEALTH, MEDICINE, SPACE, WILDLIFE, ENVIRONMENT, NEUROSCIENCE, PHYSICS, GEOLOGY, PALEONTOLOGY, SOCIAL SCIENCES, EDUCATION, JOBS, ONLINE EDUCATION, HIGHER EDUCATION, VEHICLES, ARTS-DESIGN, BEAUTY, FOOD, TRAVEL, SHOPPING, HOME, OUTDOORS, FASHION.`

### Get news by geo location

```python
google_news = GNews()
news = google_news.get_news_by_location('New York')
```

> Location can be a city, state, or country name.

### Get news by site

```python
google_news = GNews()
cnn_news = google_news.get_news_by_site('cnn.com')
```

> Site should be in the format: `"cnn.com"`

### Results specification

All parameters are optional and can be passed during initialization:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `language` | Language for results | `'en'` |
| `country` | Country code for headlines | `'US'` |
| `period` | Time period for news (e.g., `'7d'`) | `None` |
| `start_date` | Publish date after which results appear | `None` |
| `end_date` | Publish date before which results appear | `None` |
| `max_results` | Maximum number of results | `100` |
| `exclude_websites` | List of websites to exclude | `None` |
| `proxy` | Proxy settings for requests | `None` |

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
google_news.period = '7d'                # News from last 7 days
google_news.max_results = 10             # Max responses across a keyword
google_news.country = 'United States'    # News from a specific country
google_news.language = 'english'         # News in a specific language
google_news.exclude_websites = ['yahoo.com', 'cnn.com']
google_news.start_date = (2020, 1, 1)    # Search from 1st Jan 2020
google_news.end_date = (2020, 3, 1)      # Search until 1st March 2020
```

**Period format:** A number followed by a time operator:

| Operator | Meaning | Example |
|----------|---------|---------|
| `h` | Hours | `12h` |
| `d` | Days | `7d` |
| `m` | Months | `6m` |
| `y` | Years | `1y` |

**Date format:** Pass a `datetime` object or a tuple in the form `(YYYY, MM, DD)`.

### Supported Countries

```python
print(google_news.AVAILABLE_COUNTRIES)

{'Australia': 'AU', 'Botswana': 'BW', 'Canada': 'CA', 'Ethiopia': 'ET', 'Ghana': 'GH', 'India': 'IN',
 'Indonesia': 'ID', 'Ireland': 'IE', 'Israel': 'IL', 'Kenya': 'KE', 'Latvia': 'LV', 'Malaysia': 'MY',
 'Namibia': 'NA', 'New Zealand': 'NZ', 'Nigeria': 'NG', 'Pakistan': 'PK', 'Philippines': 'PH',
 'Singapore': 'SG', 'South Africa': 'ZA', 'Tanzania': 'TZ', 'Uganda': 'UG', 'United Kingdom': 'GB',
 'United States': 'US', 'Zimbabwe': 'ZW', 'Czech Republic': 'CZ', 'Germany': 'DE', 'Austria': 'AT',
 'Switzerland': 'CH', 'Argentina': 'AR', 'Chile': 'CL', 'Colombia': 'CO', 'Cuba': 'CU', 'Mexico': 'MX',
 'Peru': 'PE', 'Venezuela': 'VE', 'Belgium': 'BE', 'France': 'FR', 'Morocco': 'MA', 'Senegal': 'SN',
 'Italy': 'IT', 'Lithuania': 'LT', 'Hungary': 'HU', 'Netherlands': 'NL', 'Norway': 'NO', 'Poland': 'PL',
 'Brazil': 'BR', 'Portugal': 'PT', 'Romania': 'RO', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Sweden': 'SE',
 'Vietnam': 'VN', 'Turkey': 'TR', 'Greece': 'GR', 'Bulgaria': 'BG', 'Russia': 'RU', 'Ukraine': 'UA',
 'Serbia': 'RS', 'United Arab Emirates': 'AE', 'Saudi Arabia': 'SA', 'Lebanon': 'LB', 'Egypt': 'EG',
 'Bangladesh': 'BD', 'Thailand': 'TH', 'China': 'CN', 'Taiwan': 'TW', 'Hong Kong': 'HK', 'Japan': 'JP',
 'Republic of Korea': 'KR'}
```

### Supported Languages

```python
print(google_news.AVAILABLE_LANGUAGES)

{'english': 'en', 'indonesian': 'id', 'czech': 'cs', 'german': 'de', 'spanish': 'es-419', 'french': 'fr',
 'italian': 'it', 'latvian': 'lv', 'lithuanian': 'lt', 'hungarian': 'hu', 'dutch': 'nl', 'norwegian': 'no',
 'polish': 'pl', 'portuguese brasil': 'pt-419', 'portuguese portugal': 'pt-150', 'romanian': 'ro',
 'slovak': 'sk', 'slovenian': 'sl', 'swedish': 'sv', 'vietnamese': 'vi', 'turkish': 'tr', 'greek': 'el',
 'bulgarian': 'bg', 'russian': 'ru', 'serbian': 'sr', 'ukrainian': 'uk', 'hebrew': 'he', 'arabic': 'ar',
 'marathi': 'mr', 'hindi': 'hi', 'bengali': 'bn', 'tamil': 'ta', 'telugu': 'te', 'malyalam': 'ml',
 'thai': 'th', 'chinese simplified': 'zh-Hans', 'chinese traditional': 'zh-Hant', 'japanese': 'ja',
 'korean': 'ko'}
```

### Article Properties

Each article in the results list contains the following keys:

| Property | Description | Example |
|----------|-------------|---------|
| `title` | Title of the article | `IMF Staff and Pakistan Reach Staff-Level Agreement...` |
| `url` | Link to the article | `https://www.theguardian.com/...` |
| `published date` | Published date | `Wed, 07 Jun 2017 07:01:30 GMT` |
| `description` | Short description | `IMF Staff and Pakistan Reach Staff-Level Agreement...` |
| `publisher` | Publisher name | `The Guardian` |

### Getting full article

You can read a full article by either navigating to the URL in your browser, or using `newspaper3k` to scrape the article.

#### Using newspaper3k

1. Install the library: `pip install newspaper3k`
2. Use `get_full_article` to create a `newspaper.article.Article` object:

```python
from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('Pakistan')
article = google_news.get_full_article(json_resp[0]['url'])
```

The returned object has the following attributes:

```python
article.title    # Article title
article.text     # Full article text
article.images   # Set of image URLs
article.authors  # List of author names
```

Read the full `newspaper3k` documentation [here](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#parsing-an-article).

## Real-World Examples

### 1. Building a News Bot

A simple bot that fetches the latest news on a topic and posts it to a channel or social media feed:

```python
import time
from gnews import GNews

def news_bot(topic, interval_seconds=3600):
    """Fetch and display the latest news on a topic at regular intervals."""
    google_news = GNews(language='en', country='US', max_results=5)
    
    while True:
        articles = google_news.get_news(topic)
        for article in articles:
            print(f"📰 {article['title']}")
            print(f"   🔗 {article['url']}")
            print(f"   📅 {article['published date']}")
            print(f"   📡 {article['publisher']}")
            print()
        
        print(f"--- Next update in {interval_seconds} seconds ---\n")
        time.sleep(interval_seconds)

# Run the bot, checking for AI news every hour
news_bot('artificial intelligence', interval_seconds=3600)
```

### 2. Market Sentiment Analysis

Analyze the sentiment of financial news headlines to gauge market mood:

```python
from gnews import GNews

def analyze_market_sentiment(ticker, topic='FINANCE'):
    """Fetch finance news and display a simple sentiment summary."""
    google_news = GNews(language='en', country='US', max_results=20)
    articles = google_news.get_news(ticker)
    
    # Simple keyword-based sentiment classification
    positive_keywords = ['surge', 'gain', 'profit', 'growth', 'rally', 'bull', 'rise', 'boost', 'record', 'upbeat']
    negative_keywords = ['fall', 'drop', 'loss', 'crash', 'decline', 'bear', 'slump', 'plunge', 'recession', 'downgrade']
    
    positive, negative, neutral = 0, 0, 0
    
    for article in articles:
        title = article['title'].lower()
        if any(kw in title for kw in positive_keywords):
            positive += 1
        elif any(kw in title for kw in negative_keywords):
            negative += 1
        else:
            neutral += 1
    
    total = len(articles)
    print(f"Market Sentiment for '{ticker}':")
    print(f"  📈 Positive: {positive}/{total} ({positive/total*100:.1f}%)")
    print(f"  📉 Negative: {negative}/{total} ({negative/total*100:.1f}%)")
    print(f"  ➖ Neutral:  {neutral}/{total} ({neutral/total*100:.1f}%)")
    
    if positive > negative:
        print("  Overall: 🟢 Bullish sentiment")
    elif negative > positive:
        print("  Overall: 🔴 Bearish sentiment")
    else:
        print("  Overall: 🟡 Neutral sentiment")

analyze_market_sentiment('Tesla stock')
```

### 3. Research Data Collection

Collect and save news data for academic research in a structured format:

```python
import csv
from datetime import datetime
from gnews import GNews

def collect_research_data(keywords, filename='research_data.csv', max_results=50):
    """Collect news articles and export them to a CSV file for research."""
    google_news = GNews(language='en', country='US', max_results=max_results)
    
    fieldnames = ['keyword', 'title', 'url', 'published_date', 'description', 'publisher']
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for keyword in keywords:
            articles = google_news.get_news(keyword)
            for article in articles:
                writer.writerow({
                    'keyword': keyword,
                    'title': article.get('title', ''),
                    'url': article.get('url', ''),
                    'published_date': article.get('published date', ''),
                    'description': article.get('description', ''),
                    'publisher': article.get('publisher', '')
                })
            print(f"✅ Collected {len(articles)} articles for '{keyword}'")
    
    print(f"\n📁 Data saved to '{filename}'")

# Collect articles on climate change and renewable energy
collect_research_data(
    keywords=['climate change', 'renewable energy', 'sustainability'],
    filename='climate_research.csv'
)
```

### 4. News Monitoring Dashboard

Monitor specific topics and get notified when new articles are published:

```python
from datetime import datetime
from gnews import GNews

class NewsMonitor:
    """Monitor specific topics and report new articles."""
    
    def __init__(self, topics, language='en', country='US'):
        self.google_news = GNews(language=language, country=country, max_results=10)
        self.topics = topics
        self.seen_urls = {topic: set() for topic in topics}
    
    def check_for_updates(self):
        """Check each topic for new articles since the last check."""
        for topic in self.topics:
            articles = self.google_news.get_news(topic)
            new_articles = [
                a for a in articles if a['url'] not in self.seen_urls[topic]
            ]
            
            if new_articles:
                print(f"\n🚨 {len(new_articles)} new article(s) for '{topic}':")
                for article in new_articles:
                    print(f"  📰 {article['title']}")
                    print(f"     🔗 {article['url']}")
                    self.seen_urls[topic].add(article['url'])
            else:
                print(f"ℹ️  No new articles for '{topic}'")
    
    def run(self, check_interval_msg="Check complete"):
        """Run a single monitoring check."""
        print(f"\n⏰ Monitoring update — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        self.check_for_updates()
        print(f"✅ {check_interval_msg}")

# Monitor technology and AI news
monitor = NewsMonitor(topics=['artificial intelligence', 'cybersecurity', 'space exploration'])
monitor.run()
```

### 5. Multi-language News Aggregation

Aggregate and compare news coverage of the same topic across different languages and countries:

```python
from gnews import GNews

def aggregate_multilingual_news(topic, lang_country_pairs):
    """Fetch news for a topic across multiple languages and countries."""
    all_results = {}
    
    for language, country in lang_country_pairs:
        google_news = GNews(language=language, country=country, max_results=5)
        articles = google_news.get_news(topic)
        
        all_results[f"{language}/{country}"] = [
            {
                'title': a['title'],
                'publisher': a['publisher'],
                'url': a['url']
            }
            for a in articles
        ]
    
    # Display the results
    print(f"🌍 Multi-language news for: '{topic}'\n")
    for region, articles in all_results.items():
        print(f"  📍 {region} ({len(articles)} articles):")
        for a in articles:
            print(f"     • {a['title'][:80]}...")
            print(f"       📡 {a['publisher']}")
        print()
    
    return all_results

# Compare how "climate change" is covered across different regions
results = aggregate_multilingual_news('climate change', [
    ('en', 'US'),       # English / United States
    ('fr', 'FR'),       # French / France
    ('de', 'DE'),       # German / Germany
    ('es-419', 'AR'),   # Spanish / Argentina
    ('ja', 'JP'),       # Japanese / Japan
])
```

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

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

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
