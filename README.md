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
            <li><a href="#2-setting-up-gnews-for-local-development">Setting Up GNews for Local Development 🧑‍💻</a></li>
         </ul>
      </li>
      <li>
         <a href="#example-usage">Usage 🧩</a>
         <ul>
            <li><a href="#Get-top-news">Top News 🌟</a></li>
            <li><a href="#Get-news-by-keyword">News by Keywords 🔎</a></li>
            <li><a href="#Get-news-by-major-topic">News by Major Topics 🚀</a></li>
            <li><a href="#Get-news-by-geo-location">News by GEO Location 🌎</a></li>
            <li><a href="#get-news-by-site">News by Site 📰</a></li>
            <li><a href="#results-specification">Results 📊</a></li>
            <li><a href="#supported-countries">Supported Countries 🌐</a></li>
            <li><a href="#supported-languages">Supported Languages 🌍</a></li>
            <li><a href="#article-properties">Article Properties 📝</a></li>
            <li><a href="#getting-full-article">Getting Full Article 📰</a></li>
         </ul>
      </li>
      <li><a href="#real-world-examples">Real-World Examples 🌍</a>
         <ul>
            <li><a href="#1-building-a-news-bot">Building a News Bot</a></li>
            <li><a href="#2-market-sentiment-analysis">Market Sentiment Analysis</a></li>
            <li><a href="#3-research-data-collection">Research Data Collection</a></li>
            <li><a href="#4-news-monitoring-dashboard">News Monitoring Dashboard</a></li>
            <li><a href="#5-multi-language-news-aggregation">Multi-language News Aggregation</a></li>
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

🚩 GNews is a lightweight Python Package that searches Google News RSS Feed and returns a usable JSON response.
🚩 You can also fetch full article content (**No need to write scrapers for article fetching anymore**).

Google News covers **141+ countries** with **41+ languages**. On the bottom left side of the Google News page you
may find a `Language & region` section where you can find all of the supported combinations.

### Demo

[![GNews Demo][demo-gif]](https://github.com/ranahaani/GNews)



<!-- GETTING STARTED -->

## Getting Started

### 1. Installing the GNews package

```shell
pip install gnews
```

### 2. Setting Up GNews for Local Development

#### Option A: Setup with Docker

1. Install [docker and docker-compose](https://docs.docker.com/get-docker/).
2. Configure the `.env` file with your MongoDB credentials.
3. Build and start the containers:

```shell
docker-compose up --build
```

#### Option B: Install Using Git Clone

1. Clone this repository:
```shell
git clone https://github.com/ranahaani/GNews.git
```

2. Set up a virtual environment:
```shell
virtualenv venv
source venv/bin/activate  # macOS/Linux
.\venv\Scripts\activate   # Windows
```

3. Install the dependencies:
```shell
pip install -r requirements.txt
```

<!-- USAGE EXAMPLES -->

### Example usage

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
 'description': 'Pakistan accuses India of stoking conflict in Indian Ocean  '
                'Aljazeera.com',
 'published date': 'Tue, 16 Feb 2021 11:50:43 GMT',
 'title': 'Pakistan accuses India of stoking conflict in Indian Ocean - '
          'Aljazeera.com',
 'url': 'https://www.aljazeera.com/news/2021/2/16/pakistan-accuses-india-of-nuclearizing-indian-ocean'
 },
 ...]
```

### 📘 Interactive Tutorial 

A step-by-step **[Jupyter Notebook tutorial]** that demonstrates:

- Basic usage and setup  
- Filtering news (by topic, location, domain, date range, etc.)
- Exporting results (CSV, JSON)  
- Real-world analysis: **Sentiment Analysis on news headlines**
- Advanced usage & best practices  

👉 **[Open the tutorial](./examples/tutorial.ipynb)** — the best way to learn GNews hands-on.

### Get top news

* `GNews.get_top_news()`

### Get news by keyword

* `GNews.get_news(keyword)`

### Get news by major topic

* `GNews.get_news_by_topic(topic)`
* Available topics: `WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH, POLITICS, CELEBRITIES, TV, MUSIC, MOVIES, THEATER, SOCCER, CYCLING, MOTOR SPORTS, TENNIS, COMBAT SPORTS, BASKETBALL, BASEBALL, FOOTBALL, SPORTS BETTING, WATER SPORTS, HOCKEY, GOLF, CRICKET, RUGBY, ECONOMY, PERSONAL FINANCE, FINANCE, DIGITAL CURRENCIES, MOBILE, ENERGY, GAMING, INTERNET SECURITY, GADGETS, VIRTUAL REALITY, ROBOTICS, NUTRITION, PUBLIC HEALTH, MENTAL HEALTH, MEDICINE, SPACE, WILDLIFE, ENVIRONMENT, NEUROSCIENCE, PHYSICS, GEOLOGY, PALEONTOLOGY, SOCIAL SCIENCES, EDUCATION, JOBS, ONLINE EDUCATION, HIGHER EDUCATION, VEHICLES, ARTS-DESIGN, BEAUTY, FOOD, TRAVEL, SHOPPING, HOME, OUTDOORS, FASHION.`

### Get news by geo location

* `GNews.get_news_by_location(location)`
* Location can be the name of a city, state, or country.

### Get news by site

* `GNews.get_news_by_site(site)`
* Site should be in the format: `"cnn.com"`

### Results specification

All parameters are optional and can be passed during initialization:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `language` | Language for results | `'en'` |
| `country` | Country code for headlines | `'US'` |
| `period` | Time period for news | `None` |
| `start_date` | Earliest publish date | `None` |
| `end_date` | Latest publish date | `None` |
| `max_results` | Maximum number of results | `100` |
| `exclude_websites` | Websites to exclude from results | `None` |
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
    proxy={
        'https': 'https://your_proxy_address'
    }
)
```

#### Modifying an Existing Instance

```python
google_news.period = '7d'              # News from last 7 days
google_news.max_results = 10           # Number of responses per keyword
google_news.country = 'United States'  # News from a specific country
google_news.language = 'english'       # News in a specific language
google_news.exclude_websites = ['yahoo.com', 'cnn.com']
google_news.start_date = (2020, 1, 1)  # Search from 1st Jan 2020
google_news.end_date = (2020, 3, 1)    # Search until 1st March 2020
```

#### Timeframe Format

The `period` parameter uses a number followed by a time operator:

| Operator | Meaning | Example |
|----------|---------|---------|
| `h` | hours | `12h` |
| `d` | days | `7d` |
| `m` | months | `6m` |
| `y` | years | `1y` |

Start and end dates accept a `datetime` object or a tuple `(YYYY, MM, DD)`.

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

| Property | Description | Example |
|----------|-------------|---------|
| `title` | Title of the article | `IMF Staff and Pakistan Reach Staff-Level Agreement...` |
| `url` | Google News link to article | [Article Link](http://news.google.com/news/url?sa=t&fd=R&ct2=us&usg=AFQjCNGNR4Qg8LGbjszT1yt2s2lMXvvufQ&clid=c3a7d30bb8a4878e06b80cf16b898331&cid=52779522121279&ei=VQU7WYjiFoLEhQHIs4HQCQ&url=https://www.theguardian.com/commentisfree/2017/jun/07/why-dont-unicorns-exist-google) |
| `published date` | Publication date | `Wed, 07 Jun 2017 07:01:30 GMT` |
| `description` | Short description of article | `IMF Staff and Pakistan Reach Staff-Level Agreement...` |
| `publisher` | Publisher of article | `The Guardian` |

## Getting full article

To read a full article, you can either:
- Navigate to the URL directly in your browser, or
- Use the `newspaper3k` library to scrape the article content.

The article URL is accessed as `article['url']`.

#### Using newspaper3k

1. Install the library: `pip3 install newspaper3k`
2. Use the `get_full_article` method, which returns a `newspaper.article.Article` object:

```python
from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('Pakistan')
article = google_news.get_full_article(json_resp[0]['url'])
```

The `Article` object provides these attributes:

```python
article.title    # 'IMF Staff and Pakistan Reach Staff-Level Agreement...'
article.text     # Full article text
article.images   # Set of image URLs found in the article
article.authors  # List of author names
```

For more details, see the [newspaper3k documentation](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#parsing-an-article).

<!-- REAL-WORLD EXAMPLES -->

## Real-World Examples

### 1. Building a News Bot

Create a simple bot that fetches top news and formats it for posting to Slack or other platforms.

```python
import json
from gnews import GNews

def fetch_top_headlines(country='US', max_results=5):
    """Fetch top news headlines and format them as a summary message."""
    google_news = GNews(country=country, max_results=max_results)
    news = google_news.get_top_news()

    messages = []
    for i, article in enumerate(news, start=1):
        messages.append(f"{i}. **{article['title']}**\n   {article['url']}")

    return "\n".join(messages)

if __name__ == '__main__':
    # Post daily headlines (integrate with Slack API, Discord webhook, etc.)
    headlines = fetch_top_headlines(country='US', max_results=5)
    print("📰 Today's Top Headlines:\n")
    print(headlines)
```

**What this does:** Fetches the top news for a given country and formats each headline with its URL as a numbered list — ready to post to Slack, Discord, or any messaging platform.

---

### 2. Market Sentiment Analysis

Analyze financial news sentiment to gauge market mood. This example uses a simple keyword-based sentiment approach.

```python
from gnews import GNews

# Define positive and negative financial keywords
POSITIVE_KEYWORDS = ['growth', 'profit', 'gain', 'surge', 'record high', 'boom', 'rally']
NEGATIVE_KEYWORDS = ['loss', 'decline', 'crash', 'recession', 'debt', 'inflation', 'layoff']

def analyze_sentiment(text):
    """Score text from -1 (negative) to +1 (positive) based on keyword matches."""
    text_lower = text.lower()
    pos_count = sum(1 for kw in POSITIVE_KEYWORDS if kw in text_lower)
    neg_count = sum(1 for kw in NEGATIVE_KEYWORDS if kw in text_lower)
    total = pos_count + neg_count
    if total == 0:
        return 0.0
    return (pos_count - neg_count) / total

def get_market_sentiment(ticker='AAPL'):
    """Fetch news for a stock ticker and compute overall sentiment."""
    google_news = GNews(language='en', max_results=10)
    news = google_news.get_news(ticker)

    sentiments = []
    for article in news:
        score = analyze_sentiment(article.get('description', '') + ' ' + article.get('title', ''))
        sentiments.append({
            'title': article['title'],
            'sentiment': score,
            'url': article['url']
        })

    avg_sentiment = sum(s['sentiment'] for s in sentiments) / len(sentiments) if sentiments else 0
    label = 'Positive' if avg_sentiment > 0.1 else 'Negative' if avg_sentiment < -0.1 else 'Neutral'
    print(f"Market Sentiment for {ticker}: {label} (score: {avg_sentiment:.2f})")
    for s in sentiments:
        print(f"  [{s['sentiment']:+.2f}] {s['title']}")
    return sentiments

if __name__ == '__main__':
    get_market_sentiment('AAPL')
```

**What this does:** Retrieves news articles for a stock ticker, scores each article's description/title against positive/negative financial keywords, and reports an aggregate sentiment. You can integrate this with a trading dashboard or alert system.

---

### 3. Research Data Collection

Collect news articles on a topic and export them as JSON for academic research or data analysis.

```python
import json
from datetime import datetime
from gnews import GNews

def collect_research_data(keyword, start_date=None, end_date=None, max_results=50):
    """Fetch news for a research topic and save results to a JSON file."""
    google_news = GNews(
        language='en',
        max_results=max_results,
        start_date=start_date,
        end_date=end_date,
        exclude_websites=['youtube.com']
    )
    news = google_news.get_news(keyword)

    # Clean and structure the data
    research_data = {
        'query': keyword,
        'collected_at': datetime.now().isoformat(),
        'total_articles': len(news),
        'articles': [
            {
                'title': article.get('title', ''),
                'description': article.get('description', ''),
                'url': article.get('url', ''),
                'publisher': article.get('publisher', ''),
                'published_date': article.get('published date', '')
            }
            for article in news
        ]
    }

    # Save to JSON file
    filename = f"research_{keyword.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(research_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Collected {len(news)} articles for '{keyword}'")
    print(f"📄 Saved to: {filename}")
    return research_data

if __name__ == '__main__':
    # Collect articles about climate change from 2024
    data = collect_research_data(
        keyword='climate change',
        start_date=(2024, 1, 1),
        end_date=(2024, 12, 31),
        max_results=50
    )
```

**What this does:** Fetches news articles matching a research keyword within a date range, structures the data with metadata (query, timestamp, article count), and saves it to a timestamped JSON file. This is ideal for literature reviews, media studies, or any research that requires systematic news data collection.

---

### 4. News Monitoring Dashboard

Build a monitoring system that tracks specific topics and alerts when new articles appear.

```python
from datetime import datetime
from gnews import GNews

class NewsMonitor:
    """Monitor specific topics and detect new articles over time."""

    def __init__(self, topics, check_interval_minutes=60):
        self.google_news = GNews(language='en', max_results=10)
        self.topics = topics
        self.check_interval = check_interval_minutes
        self.seen_urls = {topic: set() for topic in topics}

    def check_for_new_articles(self):
        """Check each topic for articles not seen in previous checks."""
        new_articles = {}
        for topic in self.topics:
            news = self.google_news.get_news(topic)
            current_urls = {article['url'] for article in news}
            fresh = current_urls - self.seen_urls[topic]
            new_articles[topic] = [
                article for article in news if article['url'] in fresh
            ]
            self.seen_urls[topic] = current_urls
        return new_articles

    def run_once(self):
        """Perform a single monitoring check and print results."""
        print(f"\n📡 News Monitor — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        results = self.check_for_new_articles()
        for topic, articles in results.items():
            count = len(articles)
            print(f"\n🔍 {topic}: {count} new article(s)")
            for article in articles[:3]:  # Show top 3
                print(f"   • {article['title']}")
                print(f"     {article['url']}")

if __name__ == '__main__':
    # Monitor multiple topics
    monitor = NewsMonitor(
        topics=['artificial intelligence', 'cybersecurity', 'open source'],
        check_interval_minutes=30
    )
    monitor.run_once()
```

**What this does:** Creates a `NewsMonitor` class that tracks multiple topics, remembers previously seen articles (by URL), and reports only new ones on each check. Use this with a scheduler (e.g., `schedule`, cron) to run periodic checks and integrate with alerting tools.

---

### 5. Multi-language News Aggregation

Aggregate news about the same topic from multiple languages and countries for a global perspective.

```python
from gnews import GNews

def aggregate_multilingual_news(keyword, language_country_pairs):
    """
    Fetch news for the same keyword across multiple language/country combinations.
    
    Args:
        keyword: Search term (use terms recognizable in target languages).
        language_country_pairs: List of (language, country) tuples, e.g.
            [('english', 'US'), ('french', 'FR'), ('german', 'DE')]
    
    Returns:
        Dict mapping language-country labels to lists of articles.
    """
    results = {}
    for language, country in language_country_pairs:
        try:
            google_news = GNews(
                language=language,
                country=country,
                max_results=5
            )
            news = google_news.get_news(keyword)
            label = f"{language.title()} ({country})"
            results[label] = news
            print(f"✅ {label}: {len(news)} articles found")
        except Exception as e:
            label = f"{language.title()} ({country})"
            results[label] = []
            print(f"❌ {label}: Error — {e}")
    return results

def print_summary(results):
    """Print a summary of multilingual news results."""
    print("\n" + "=" * 60)
    print("🌍 Multilingual News Summary")
    print("=" * 60)
    for label, articles in results.items():
        print(f"\n📰 {label}")
        for article in articles[:3]:
            print(f"   • {article['title']}")

if __name__ == '__main__':
    # Compare coverage of "climate" across regions
    data = aggregate_multilingual_news(
        keyword='climate',
        language_country_pairs=[
            ('english', 'US'),
            ('french', 'FR'),
            ('german', 'DE'),
            ('spanish', 'AR'),
        ]
    )
    print_summary(data)
```

**What this does:** Fetches news for the same keyword across multiple language and country combinations, providing a comparative view of how different regions cover the same topic. This is useful for cross-cultural research, international journalism, or building multi-region news aggregators.

<!-- ToDo -->

## Todo

- Save to MongoDB
- Save to SQLite
- Save to JSON
- Save to .CSV file
- More than 100 articles

<!-- ROADMAP -->

## Roadmap

See the [open issues](https://github.com/ranahaani/GNews/issues) for a list of proposed features and known issues.



<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

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
