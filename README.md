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
      <li><a href="#real-world-examples">Real-World Examples 🌟</a></li>
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

🚩 GNews is A Happy and lightweight Python Package that searches Google News RSS Feed and returns a usable JSON
response \
🚩 As well as you can fetch full article (**No need to write scrappers for articles fetching anymore**)

Google News cover across **141+ countries** with **41+ languages**. On the bottom left side of the Google News page you
may find a `Language & region` section where you can find all of the supported combinations.

### Demo

[![GNews Demo][demo-gif]](https://github.com/ranahaani/GNews)



<!-- GETTING STARTED -->

## Getting Started

This section provides instructions for two different use cases:

1. **Installing the GNews package** for immediate use.
2. **Setting up the GNews project** for local development.

### 1. Installing the GNews package

To install the package and start using it in your own projects, follow these steps:

``` shell
pip install gnews
```
### 2. Setting Up GNews for Local Development

If you want to make modifications locally, follow these steps to set up the development environment.

#### Option 1: Setup with Docker

1. Install [docker and docker-compose](https://docs.docker.com/get-docker/).
2. Configure the `.env` file by placing your MongoDB credentials.
3. Run the following command to build and start the Docker containers:

``` shell
docker-compose up --build
```

#### Option 2: Install Using Git Clone

1. Clone this repository:
``` shell
git clone https://github.com/ranahaani/GNews.git
```

2. Set up a virtual environment:
```shell
virtualenv venv
source venv/bin/activate  # MacOS/Linux
.\venv\Scripts\activate  # Windows
```

3. Install the required dependencies:
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

We have created a step-by-step **[ jupyter Notebook tutorial ]** that demonstrates:

- Basic usage and setup  
- Filtering news (by topic, location, domain, date range, etc.)
- Exporting results (CSV, JSON)  
- Real-world analysis: **Sentiment Analysis on news headlines**
- Advanced usage & best practices  
- Interactive examples you can run line-by-line

👉 **Open the tutorial here:**  
[examples/tutorial.ipynb](./examples/tutorial.ipynb)

This is the best way to learn GNews hands-on.

### Get top news

* `GNews.get_top_news()`

### Get news by keyword

* `GNews.get_news(keyword)`

### Get news by major topic

* `GNews.get_news_by_topic(topic)`
* Available topics:` WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH, POLITICS, CELEBRITIES, TV, MUSIC, MOVIES, THEATER, SOCCER, CYCLING, MOTOR SPORTS, TENNIS, COMBAT SPORTS, BASKETBALL, BASEBALL, FOOTBALL, SPORTS BETTING, WATER SPORTS, HOCKEY, GOLF, 
CRICKET, RUGBY, ECONOMY, PERSONAL FINANCE, FINANCE, DIGITAL CURRENCIES, MOBILE, ENERGY, GAMING, INTERNET SECURITY, GADGETS, VIRTUAL REALITY, ROBOTICS, NUTRITION, PUBLIC HEALTH, MENTAL HEALTH, MEDICINE, SPACE, WILDLIFE, ENVIRONMENT, NEUROSCIENCE, PHYSICS, GEOLOGY, PALEONTOLOGY, SOCIAL SCIENCES, EDUCATION, JOBS, ONLINE EDUCATION, HIGHER EDUCATION, VEHICLES, ARTS-DESIGN, BEAUTY, FOOD, TRAVEL, SHOPPING, HOME, OUTDOORS, FASHION.`

### Get news by geo location

* `GNews.get_news_by_location(location)`
* location can be name of city/state/country

### Get news by site

* `GNews.get_news_by_site(site)`
* site should be in the format of: `"cnn.com"`

### Results specification
All parameters are optional and can be passed during initialization. Here’s a list of the available parameters:

- **language**: The language in which to return results (default: 'en').
- **country**: The country code for the headlines (default: 'US').
- **period**: The time period for which you want news.
- **start_date**: Date after which results must have been published.
- **end_date**: Date before which results must have been published.
- **max_results**: The maximum number of results to return (default: 100).
- **exclude_websites**: A list of websites to exclude from results.
- **proxy**: A dictionary specifying the proxy settings used to route requests. The dictionary should contain a single key-value pair where the key is the protocol (`http` or `https`) and the value is the proxy address. Example:
```python
# Example with only HTTP proxy
  proxy = {
      'http': 'http://your_proxy_address',
  }
  
# Example with only HTTPS proxy
  proxy = {
      'https': 'http://your_proxy_address',
  }
```
  
#### Example Initialization
```python
from gnews import GNews

# Initialize GNews with various parameters, including proxy
google_news = GNews(
    language='en',
    country='US',
    period='7d',
    start_date=None,
    end_date=None,
    max_results=10,
    exclude_websites=['yahoo.com', 'cnn.com'],
    proxy={
        'https': 'https://your_proxy_address'
    }
)
```

* Or change it to an existing object

```python
google_news.period = '7d'  # News from last 7 days
google_news.max_results = 10  # number of responses across a keyword
google_news.country = 'United States'  # News from a specific country 
google_news.language = 'english'  # News in a specific language
google_news.exclude_websites = ['yahoo.com', 'cnn.com']  # Exclude news from specific website i.e Yahoo.com and CNN.com
google_news.start_date = (2020, 1, 1) # Search from 1st Jan 2020
google_news.end_date = (2020, 3, 1) # Search until 1st March 2020
```

The format of the timeframe is a string comprised of a number, followed by a letter representing the time operator. For
example 1y would signify 1 year. Full list of operators below:

```
 - h = hours (eg: 12h)
 - d = days (eg: 7d)
 - m = months (eg: 6m)
 - y = years (eg: 1y)
 ```
 
Setting the start and end dates can be done by passing in either a datetime or a tuple in the form (YYYY, MM, DD).

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

- Get news returns the list with following keys: `title`, `published_date`, `description`, `url`, `publisher`.

| Properties   | Description                                    | Example                                                                                                                                                                                                                                                                             |
|--------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| title        | Title of the article                           | IMF Staff and Pakistan Reach Staff-Level Agreement on the Pending Reviews Under the Extended Fund Facility                                                                                                                                                                                                   |
| url         | Google news link to article                    | [Article Link](http://news.google.com/news/url?sa=t&fd=R&ct2=us&usg=AFQjCNGNR4Qg8LGbjszT1yt2s2lMXvvufQ&clid=c3a7d30bb8a4878e06b80cf16b898331&cid=52779522121279&ei=VQU7WYjiFoLEhQHIs4HQCQ&url=https://www.theguardian.com/commentisfree/2017/jun/07/why-dont-unicorns-exist-google) |
| published date      | Published date                                 | Wed, 07 Jun 2017 07:01:30 GMT                                                                                                                                                                                                                                                       |
| description  | Short description of article                   | IMF Staff and Pakistan Reach Staff-Level Agreement on the Pending Reviews Under the Extended Fund Facility ...                                                                                                                                                                                                                  |
| publisher    | Publisher of article                           | The Guardian                                                                                                                                                                                                                                                                        |                                                                                                                                                        |

## Getting full article

* To read a full article you can either:
    * Navigate to the url directly in your browser, or
    * Use `newspaper3k` library to scrape the article
* The article url, needed for both methods, is accessed as `article['url']`.

#### Using newspaper3k

1. Install the library - `pip3 install newspaper3k`.
2. Use `get_full_article` method from `GNews`, that creates an `newspaper.article.Article` object from the url.

```python
from gnews import GNews

google_news = GNews()
json_resp = google_news.get_news('Pakistan')
article = google_news.get_full_article(
    json_resp[0]['url'])  # newspaper3k instance, you can access newspaper3k all attributes in article
```

This new object contains `title`, `text` (full article) or `images` attributes. Examples:

```python
article.title 
```

> IMF Staff and Pakistan Reach Staff-Level Agreement on the Pending Reviews Under the Extended Fund Facility'

```python
article.text 
```

> End-of-Mission press releases include statements of IMF staff teams that convey preliminary findings after a mission. The views expressed are those of the IMF staff and do not necessarily represent the views of the IMF’s Executive Board.\n\nIMF staff and the Pakistani authorities have reached an agreement on a package of measures to complete second to fifth reviews of the authorities’ reform program supported by the IMF Extended Fund Facility (EFF) ..... (full article)

```python
article.images
```

> `{'https://www.imf.org/~/media/Images/IMF/Live-Page/imf-live-rgb-h.ashx?la=en', 'https://www.imf.org/-/media/Images/IMF/Data/imf-logo-eng-sep2019-update.ashx', 'https://www.imf.org/-/media/Images/IMF/Data/imf-seal-shadow-sep2019-update.ashx', 'https://www.imf.org/-/media/Images/IMF/Social/TW-Thumb/twitter-seal.ashx', 'https://www.imf.org/assets/imf/images/footer/IMF_seal.png'}
`

```python
article.authors
```

> `[]`

Read full documentation for `newspaper3k`
[newspaper3k](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#parsing-an-article)

<!-- REAL-WORLD EXAMPLES -->

## Real-World Examples

The following examples demonstrate practical applications of GNews in real-world scenarios. Each example includes complete, runnable code that you can adapt for your own projects.

### 1. Building a News Bot for Social Media

Automatically fetch and post news updates to social media or messaging platforms. This example shows how to create a simple bot that collects tech news and formats it for posting.

```python
from gnews import GNews
import time
from datetime import datetime

class NewsBot:
    def __init__(self, topics, interval_hours=6):
        """
        Initialize a news bot that fetches news periodically
        
        :param topics: List of topics to monitor
        :param interval_hours: Hours between updates
        """
        self.google_news = GNews(
            language='en',
            country='US',
            period='6h',  # Only fetch recent news
            max_results=5
        )
        self.topics = topics
        self.interval = interval_hours * 3600
        self.seen_urls = set()
    
    def format_post(self, article):
        """Format article for social media post"""
        post = f"""
🔥 {article['title']}

📰 {article['publisher']}
🔗 {article['url']}

#{self.current_topic.replace(' ', '')} #News
        """
        return post.strip()
    
    def fetch_and_post(self):
        """Fetch news and generate posts"""
        posts = []
        
        for topic in self.topics:
            self.current_topic = topic
            articles = self.google_news.get_news(topic)
            
            for article in articles:
                # Skip if already posted
                if article['url'] in self.seen_urls:
                    continue
                
                self.seen_urls.add(article['url'])
                post = self.format_post(article)
                posts.append(post)
        
        return posts
    
    def run_once(self):
        """Run the bot once and return formatted posts"""
        print(f"[{datetime.now()}] Fetching news...")
        posts = self.fetch_and_post()
        print(f"Generated {len(posts)} new posts")
        return posts

# Usage Example
if __name__ == "__main__":
    bot = NewsBot(topics=['Artificial Intelligence', 'Cybersecurity', 'Startups'])
    
    # Fetch news once
    new_posts = bot.run_once()
    
    # Display posts (in production, you'd send these to your social media API)
    for i, post in enumerate(new_posts[:3], 1):
        print(f"\n--- Post {i} ---")
        print(post)
    
    # To run continuously (uncomment in production):
    # while True:
    #     posts = bot.run_once()
    #     # Send posts to your social media platform here
    #     time.sleep(bot.interval)
```

**Best Practices:**
- Store `seen_urls` in a database for persistence across restarts
- Implement error handling and retry logic
- Use environment variables for API keys and configuration
- Add rate limiting to avoid overwhelming your social media APIs

---

### 2. Market Sentiment Analysis for Financial Markets

Analyze news sentiment for stocks, cryptocurrencies, or financial markets to gauge market mood and inform trading decisions.

```python
from gnews import GNews
import pandas as pd
from collections import Counter
from datetime import datetime

try:
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    VADER_AVAILABLE = True
except ImportError:
    print("Install vaderSentiment: pip install vaderSentiment")
    VADER_AVAILABLE = False

class MarketSentimentAnalyzer:
    def __init__(self):
        self.google_news = GNews(
            language='en',
            country='US',
            period='24h',  # Last 24 hours for recent market sentiment
            max_results=50
        )
        if VADER_AVAILABLE:
            self.sentiment_analyzer = SentimentIntensityAnalyzer()
    
    def analyze_stock(self, stock_symbol, company_name):
        """
        Analyze sentiment for a specific stock
        
        :param stock_symbol: Stock ticker symbol (e.g., 'AAPL')
        :param company_name: Company name for search
        :return: Dictionary with sentiment analysis results
        """
        # Fetch news about the company
        search_query = f"{company_name} stock {stock_symbol}"
        articles = self.google_news.get_news(search_query)
        
        if not articles:
            return {"error": f"No news found for {company_name}"}
        
        sentiments = []
        analyzed_articles = []
        
        for article in articles:
            text = f"{article['title']} {article['description']}"
            
            if VADER_AVAILABLE:
                scores = self.sentiment_analyzer.polarity_scores(text)
                compound = scores['compound']
                
                # Classify sentiment
                if compound >= 0.05:
                    sentiment = 'Positive'
                elif compound <= -0.05:
                    sentiment = 'Negative'
                else:
                    sentiment = 'Neutral'
                
                sentiments.append(sentiment)
                analyzed_articles.append({
                    'title': article['title'],
                    'publisher': article['publisher'],
                    'sentiment': sentiment,
                    'score': compound,
                    'url': article['url']
                })
        
        # Calculate overall sentiment
        sentiment_counts = Counter(sentiments)
        total = len(sentiments)
        
        return {
            'stock': stock_symbol,
            'company': company_name,
            'total_articles': total,
            'sentiment_distribution': {
                'positive': sentiment_counts.get('Positive', 0),
                'neutral': sentiment_counts.get('Neutral', 0),
                'negative': sentiment_counts.get('Negative', 0)
            },
            'sentiment_percentages': {
                'positive': round(sentiment_counts.get('Positive', 0) / total * 100, 2),
                'neutral': round(sentiment_counts.get('Neutral', 0) / total * 100, 2),
                'negative': round(sentiment_counts.get('Negative', 0) / total * 100, 2)
            },
            'articles': analyzed_articles,
            'timestamp': datetime.now().isoformat()
        }
    
    def generate_report(self, analysis):
        """Generate a readable sentiment report"""
        print(f"\n{'='*60}")
        print(f"Market Sentiment Report: {analysis['company']} ({analysis['stock']})")
        print(f"{'='*60}")
        print(f"Analysis Time: {analysis['timestamp']}")
        print(f"Total Articles Analyzed: {analysis['total_articles']}\n")
        
        print("Sentiment Distribution:")
        print(f"  ✅ Positive: {analysis['sentiment_percentages']['positive']}% "
              f"({analysis['sentiment_distribution']['positive']} articles)")
        print(f"  ⚪ Neutral:  {analysis['sentiment_percentages']['neutral']}% "
              f"({analysis['sentiment_distribution']['neutral']} articles)")
        print(f"  ❌ Negative: {analysis['sentiment_percentages']['negative']}% "
              f"({analysis['sentiment_distribution']['negative']} articles)")
        
        # Overall market sentiment
        pos_pct = analysis['sentiment_percentages']['positive']
        neg_pct = analysis['sentiment_percentages']['negative']
        
        if pos_pct > neg_pct + 10:
            overall = "🔥 BULLISH - Predominantly positive sentiment"
        elif neg_pct > pos_pct + 10:
            overall = "🐻 BEARISH - Predominantly negative sentiment"
        else:
            overall = "↔️  NEUTRAL - Mixed or balanced sentiment"
        
        print(f"\nOverall Market Sentiment: {overall}\n")
        
        # Top headlines
        print("Top 5 Headlines:")
        for i, article in enumerate(analysis['articles'][:5], 1):
            emoji = {'Positive': '✅', 'Neutral': '⚪', 'Negative': '❌'}
            print(f"{i}. {emoji[article['sentiment']]} {article['title'][:80]}...")
        
        print(f"{'='*60}\n")

# Usage Example
if __name__ == "__main__":
    analyzer = MarketSentimentAnalyzer()
    
    # Analyze multiple stocks
    stocks = [
        ('AAPL', 'Apple'),
        ('TSLA', 'Tesla'),
        ('NVDA', 'NVIDIA')
    ]
    
    results = []
    for symbol, name in stocks:
        analysis = analyzer.analyze_stock(symbol, name)
        if 'error' not in analysis:
            analyzer.generate_report(analysis)
            results.append(analysis)
    
    # Save to CSV for further analysis
    if results:
        df = pd.DataFrame([{
            'Stock': r['stock'],
            'Company': r['company'],
            'Total Articles': r['total_articles'],
            'Positive %': r['sentiment_percentages']['positive'],
            'Neutral %': r['sentiment_percentages']['neutral'],
            'Negative %': r['sentiment_percentages']['negative']
        } for r in results])
        
        df.to_csv('market_sentiment_analysis.csv', index=False)
        print("Analysis saved to: market_sentiment_analysis.csv")
```

**Use Cases:**
- Pre-market sentiment analysis for day traders
- Long-term investment research
- Risk assessment for portfolio management
- Automated trading signal generation (combined with other indicators)

---

### 3. Research Data Collection for Academic Studies

Collect and organize news data for academic research, content analysis, or journalism studies.

```python
from gnews import GNews
import pandas as pd
import json
from datetime import datetime, timedelta
import os

class NewsDataCollector:
    def __init__(self, output_dir='research_data'):
        """
        Initialize research data collector
        
        :param output_dir: Directory to save collected data
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        self.google_news = GNews(
            language='en',
            country='US',
            max_results=100
        )
    
    def collect_by_date_range(self, keyword, start_date, end_date, 
                               country='US', language='en'):
        """
        Collect news articles for a specific date range
        
        :param keyword: Search keyword
        :param start_date: Tuple (YYYY, MM, DD)
        :param end_date: Tuple (YYYY, MM, DD)
        :param country: Country code
        :param language: Language code
        :return: List of articles
        """
        self.google_news.country = country
        self.google_news.language = language
        self.google_news.start_date = start_date
        self.google_news.end_date = end_date
        
        print(f"Collecting news for '{keyword}' from {start_date} to {end_date}...")
        articles = self.google_news.get_news(keyword)
        print(f"Found {len(articles)} articles")
        
        return articles
    
    def collect_comparative_study(self, keywords, date_range, countries):
        """
        Collect data for comparative analysis across keywords and countries
        
        :param keywords: List of keywords to compare
        :param date_range: Tuple of (start_date, end_date)
        :param countries: List of country codes
        :return: Structured dataset
        """
        dataset = []
        start_date, end_date = date_range
        
        for country in countries:
            for keyword in keywords:
                articles = self.collect_by_date_range(
                    keyword, start_date, end_date, country=country
                )
                
                for article in articles:
                    article['keyword'] = keyword
                    article['country'] = country
                    article['collection_date'] = datetime.now().isoformat()
                
                dataset.extend(articles)
        
        return dataset
    
    def export_dataset(self, data, filename_prefix):
        """
        Export collected data in multiple formats
        
        :param data: List of articles
        :param filename_prefix: Prefix for output files
        """
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # Export as JSON
        json_file = os.path.join(
            self.output_dir, 
            f"{filename_prefix}_{timestamp}.json"
        )
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✅ Saved JSON: {json_file}")
        
        # Export as CSV
        csv_file = os.path.join(
            self.output_dir, 
            f"{filename_prefix}_{timestamp}.csv"
        )
        df = pd.DataFrame(data)
        df.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"✅ Saved CSV: {csv_file}")
        
        # Generate summary statistics
        self.generate_summary(df, filename_prefix, timestamp)
        
        return json_file, csv_file
    
    def generate_summary(self, df, filename_prefix, timestamp):
        """Generate summary statistics for the dataset"""
        summary_file = os.path.join(
            self.output_dir, 
            f"{filename_prefix}_{timestamp}_summary.txt"
        )
        
        with open(summary_file, 'w') as f:
            f.write("="*60 + "\n")
            f.write("Research Dataset Summary\n")
            f.write("="*60 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Total Articles: {len(df)}\n\n")
            
            if 'keyword' in df.columns:
                f.write("Articles by Keyword:\n")
                f.write(df['keyword'].value_counts().to_string())
                f.write("\n\n")
            
            if 'country' in df.columns:
                f.write("Articles by Country:\n")
                f.write(df['country'].value_counts().to_string())
                f.write("\n\n")
            
            if 'publisher' in df.columns:
                f.write("Top 10 Publishers:\n")
                f.write(df['publisher'].value_counts().head(10).to_string())
                f.write("\n\n")
        
        print(f"✅ Saved Summary: {summary_file}")

# Usage Example
if __name__ == "__main__":
    collector = NewsDataCollector(output_dir='climate_research_data')
    
    # Example 1: Single keyword, date range study
    print("\n--- Example 1: Climate Change Coverage Analysis ---")
    articles = collector.collect_by_date_range(
        keyword='climate change',
        start_date=(2024, 1, 1),
        end_date=(2024, 12, 31),
        country='US'
    )
    collector.export_dataset(articles, 'climate_change_2024')
    
    # Example 2: Comparative study across topics and countries
    print("\n--- Example 2: Comparative Environmental News Study ---")
    comparative_data = collector.collect_comparative_study(
        keywords=['climate change', 'renewable energy', 'pollution'],
        date_range=((2024, 6, 1), (2024, 12, 31)),
        countries=['US', 'GB', 'IN', 'AU']
    )
    collector.export_dataset(comparative_data, 'environmental_comparative_study')
    
    print("\n✅ Data collection complete! Check the 'climate_research_data' directory.")
```

**Research Applications:**
- Media framing analysis
- Cross-cultural news comparison
- Topic evolution over time
- Publisher bias studies
- Discourse analysis

**Data Management Tips:**
- Use consistent naming conventions
- Document your collection methodology
- Store raw data separately from processed data
- Include metadata (collection date, search parameters)
- Version your datasets

---

### 4. News Monitoring Dashboard for Brand/Topic Tracking

Monitor mentions of your brand, competitors, or specific topics in real-time and generate alerts.

```python
from gnews import GNews
from datetime import datetime
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class NewsMonitor:
    def __init__(self, alert_email=None):
        """
        Initialize news monitoring system
        
        :param alert_email: Email address for alerts (optional)
        """
        self.google_news = GNews(
            language='en',
            country='US',
            period='1h',  # Check last hour
            max_results=10
        )
        self.alert_email = alert_email
        self.monitored_topics = {}
        self.alert_log = []
    
    def add_topic(self, topic_name, keywords, alert_keywords=None):
        """
        Add a topic to monitor
        
        :param topic_name: Name for this monitoring topic
        :param keywords: Search keywords
        :param alert_keywords: Keywords that trigger alerts (optional)
        """
        self.monitored_topics[topic_name] = {
            'keywords': keywords,
            'alert_keywords': alert_keywords or [],
            'last_checked': None,
            'seen_urls': set()
        }
        print(f"✅ Now monitoring: {topic_name}")
    
    def check_topic(self, topic_name):
        """Check for new articles on a monitored topic"""
        topic = self.monitored_topics[topic_name]
        articles = self.google_news.get_news(topic['keywords'])
        
        new_articles = []
        alerts = []
        
        for article in articles:
            if article['url'] not in topic['seen_urls']:
                topic['seen_urls'].add(article['url'])
                new_articles.append(article)
                
                # Check if article contains alert keywords
                text = f"{article['title']} {article['description']}".lower()
                triggered_keywords = [
                    kw for kw in topic['alert_keywords'] 
                    if kw.lower() in text
                ]
                
                if triggered_keywords:
                    alerts.append({
                        'article': article,
                        'triggered_keywords': triggered_keywords
                    })
        
        topic['last_checked'] = datetime.now()
        
        return new_articles, alerts
    
    def send_alert_email(self, topic_name, alerts):
        """Send email alert (requires SMTP configuration)"""
        if not self.alert_email:
            return
        
        # Note: Configure your SMTP settings here
        print(f"📧 Alert: {len(alerts)} urgent articles found for '{topic_name}'")
        # Email sending code would go here
        # This is a placeholder - configure with your SMTP server
    
    def generate_dashboard_report(self):
        """Generate a text-based dashboard summary"""
        print("\n" + "="*80)
        print(f"📊 NEWS MONITORING DASHBOARD - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80 + "\n")
        
        for topic_name, topic_data in self.monitored_topics.items():
            print(f"📌 {topic_name}")
            print(f"   Keywords: {topic_data['keywords']}")
            print(f"   Last Checked: {topic_data['last_checked']}")
            print(f"   Articles Tracked: {len(topic_data['seen_urls'])}")
            
            if topic_data['alert_keywords']:
                print(f"   🚨 Alert Keywords: {', '.join(topic_data['alert_keywords'])}")
            print()
    
    def monitor_once(self):
        """Run one monitoring cycle for all topics"""
        print(f"\n🔍 Monitoring cycle started: {datetime.now()}")
        
        all_new_articles = {}
        all_alerts = {}
        
        for topic_name in self.monitored_topics:
            new_articles, alerts = self.check_topic(topic_name)
            
            all_new_articles[topic_name] = new_articles
            all_alerts[topic_name] = alerts
            
            print(f"  • {topic_name}: {len(new_articles)} new articles, "
                  f"{len(alerts)} alerts")
            
            # Send alerts if any
            if alerts:
                self.send_alert_email(topic_name, alerts)
                for alert in alerts:
                    print(f"    🚨 ALERT: {alert['article']['title'][:70]}...")
                    print(f"       Triggered by: {', '.join(alert['triggered_keywords'])}")
        
        return all_new_articles, all_alerts
    
    def run_continuous(self, check_interval_minutes=60):
        """
        Run continuous monitoring
        
        :param check_interval_minutes: Minutes between checks
        """
        print(f"\n🚀 Starting continuous monitoring (checking every {check_interval_minutes} min)")
        print("Press Ctrl+C to stop\n")
        
        try:
            while True:
                self.monitor_once()
                self.generate_dashboard_report()
                
                print(f"⏳ Waiting {check_interval_minutes} minutes until next check...\n")
                time.sleep(check_interval_minutes * 60)
        
        except KeyboardInterrupt:
            print("\n\n🛑 Monitoring stopped by user")
            self.generate_dashboard_report()

# Usage Example
if __name__ == "__main__":
    # Initialize monitor
    monitor = NewsMonitor(alert_email="your-email@example.com")
    
    # Add topics to monitor
    monitor.add_topic(
        topic_name="Company Brand Mentions",
        keywords="YourCompany OR YourProduct",
        alert_keywords=["lawsuit", "scandal", "breach", "crisis", "controversy"]
    )
    
    monitor.add_topic(
        topic_name="Competitor Analysis",
        keywords="CompetitorName",
        alert_keywords=["new product", "acquisition", "partnership", "funding"]
    )
    
    monitor.add_topic(
        topic_name="Industry Trends",
        keywords="artificial intelligence industry trends",
        alert_keywords=["regulation", "breakthrough", "investment"]
    )
    
    # Run once for testing
    print("--- Running Single Monitoring Cycle ---")
    new_articles, alerts = monitor.monitor_once()
    monitor.generate_dashboard_report()
    
    # For continuous monitoring, uncomment:
    # monitor.run_continuous(check_interval_minutes=60)
```

**Use Cases:**
- Brand reputation monitoring
- Competitor intelligence gathering
- Crisis detection and management
- Industry trend tracking
- Product launch monitoring

**Deployment Options:**
- Run as a cron job on a server
- Deploy as a cloud function (AWS Lambda, Google Cloud Functions)
- Use with task schedulers (Celery, APScheduler)
- Integrate with Slack/Discord webhooks for instant notifications

---

### 5. Multi-language News Aggregation

Aggregate and compare news coverage across different languages and regions to get a global perspective.

```python
from gnews import GNews
import pandas as pd
from datetime import datetime

class MultiLanguageNewsAggregator:
    def __init__(self):
        """Initialize multi-language news aggregator"""
        self.supported_languages = {
            'english': 'en',
            'spanish': 'es-419',
            'french': 'fr',
            'german': 'de',
            'chinese simplified': 'zh-Hans',
            'japanese': 'ja',
            'arabic': 'ar',
            'hindi': 'hi',
            'portuguese brasil': 'pt-419'
        }
        
        self.supported_countries = {
            'United States': 'US',
            'United Kingdom': 'GB',
            'France': 'FR',
            'Germany': 'DE',
            'Japan': 'JP',
            'China': 'CN',
            'Brazil': 'BR',
            'India': 'IN',
            'Mexico': 'MX'
        }
    
    def fetch_multilingual_news(self, keyword, languages=None, max_per_language=10):
        """
        Fetch news in multiple languages
        
        :param keyword: Search keyword (can be translated for each language)
        :param languages: List of language codes (uses all if None)
        :param max_per_language: Maximum articles per language
        :return: DataFrame with multilingual news
        """
        if languages is None:
            languages = list(self.supported_languages.values())[:5]  # Top 5
        
        all_articles = []
        
        for lang_code in languages:
            lang_name = [k for k, v in self.supported_languages.items() 
                        if v == lang_code][0]
            
            print(f"Fetching {lang_name} news...")
            
            google_news = GNews(
                language=lang_code,
                period='24h',
                max_results=max_per_language
            )
            
            articles = google_news.get_news(keyword)
            
            for article in articles:
                article['language'] = lang_name
                article['language_code'] = lang_code
                article['search_keyword'] = keyword
            
            all_articles.extend(articles)
            print(f"  ✓ Found {len(articles)} {lang_name} articles")
        
        return pd.DataFrame(all_articles)
    
    def fetch_regional_perspectives(self, keyword, regions=None):
        """
        Fetch news from different regions/countries
        
        :param keyword: Search keyword
        :param regions: List of tuples (country_name, country_code, language_code)
        :return: DataFrame with regional news
        """
        if regions is None:
            # Default: Major global regions
            regions = [
                ('United States', 'US', 'en'),
                ('United Kingdom', 'GB', 'en'),
                ('France', 'FR', 'fr'),
                ('Germany', 'DE', 'de'),
                ('Japan', 'JP', 'ja'),
                ('Brazil', 'BR', 'pt-419'),
                ('India', 'IN', 'en')
            ]
        
        all_articles = []
        
        for country_name, country_code, lang_code in regions:
            print(f"Fetching news from {country_name}...")
            
            google_news = GNews(
                language=lang_code,
                country=country_code,
                period='24h',
                max_results=15
            )
            
            articles = google_news.get_news(keyword)
            
            for article in articles:
                article['region'] = country_name
                article['country_code'] = country_code
                article['language_code'] = lang_code
            
            all_articles.extend(articles)
            print(f"  ✓ Found {len(articles)} articles from {country_name}")
        
        return pd.DataFrame(all_articles)
    
    def analyze_coverage_differences(self, df):
        """
        Analyze how coverage differs across languages/regions
        
        :param df: DataFrame with multilingual news
        """
        print("\n" + "="*70)
        print("📊 MULTI-LANGUAGE NEWS COVERAGE ANALYSIS")
        print("="*70 + "\n")
        
        if 'language' in df.columns:
            print("📰 Articles by Language:")
            print(df['language'].value_counts().to_string())
            print()
        
        if 'region' in df.columns:
            print("🌍 Articles by Region:")
            print(df['region'].value_counts().to_string())
            print()
        
        if 'publisher' in df.columns:
            print("🏢 Top Publishers:")
            print(df['publisher'].value_counts().head(10).to_string())
            print()
        
        print(f"📅 Date Range: {df['published date'].min()} to {df['published date'].max()}")
        print(f"📊 Total Unique Articles: {len(df)}")
        print("="*70 + "\n")
    
    def export_comparison_report(self, df, keyword, output_file='multilingual_news'):
        """Export comprehensive comparison report"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        # CSV export
        csv_file = f"{output_file}_{timestamp}.csv"
        df.to_csv(csv_file, index=False, encoding='utf-8')
        print(f"✅ Exported to: {csv_file}")
        
        # HTML export for easy viewing
        html_file = f"{output_file}_{timestamp}.html"
        html_content = f"""
        <html>
        <head>
            <title>Multi-language News Report: {keyword}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 20px; }}
                h1 {{ color: #333; }}
                .article {{ border: 1px solid #ddd; padding: 15px; margin: 10px 0; }}
                .meta {{ color: #666; font-size: 0.9em; }}
            </style>
        </head>
        <body>
            <h1>Multi-language News Report: {keyword}</h1>
            <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            <p>Total Articles: {len(df)}</p>
        """
        
        # Group by language or region
        group_by = 'language' if 'language' in df.columns else 'region'
        
        for group_name, group_df in df.groupby(group_by):
            html_content += f"<h2>{group_name} ({len(group_df)} articles)</h2>"
            
            for _, article in group_df.iterrows():
                html_content += f"""
                <div class="article">
                    <h3>{article['title']}</h3>
                    <p class="meta">
                        Publisher: {article['publisher']} | 
                        Published: {article['published date']}
                    </p>
                    <p>{article['description']}</p>
                    <a href="{article['url']}" target="_blank">Read more →</a>
                </div>
                """
        
        html_content += "</body></html>"
        
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"✅ HTML report: {html_file}")

# Usage Example
if __name__ == "__main__":
    aggregator = MultiLanguageNewsAggregator()
    
    # Example 1: Compare same topic across languages
    print("\n--- Example 1: Multi-language Coverage ---")
    keyword = "climate change"
    df_multilang = aggregator.fetch_multilingual_news(
        keyword=keyword,
        languages=['en', 'es-419', 'fr', 'de', 'ja'],
        max_per_language=10
    )
    aggregator.analyze_coverage_differences(df_multilang)
    aggregator.export_comparison_report(df_multilang, keyword, 'climate_multilang')
    
    # Example 2: Regional perspectives on global events
    print("\n--- Example 2: Regional Perspectives ---")
    df_regional = aggregator.fetch_regional_perspectives(
        keyword="artificial intelligence regulation"
    )
    aggregator.analyze_coverage_differences(df_regional)
    aggregator.export_comparison_report(df_regional, "AI regulation", 'ai_regional')
    
    print("\n✅ Analysis complete! Check the generated CSV and HTML files.")
```

**Applications:**
- International news monitoring
- Cross-cultural media studies
- Global event coverage comparison
- Translation and localization research
- International brand monitoring

**Best Practices:**
- Be aware of keyword translation nuances
- Consider time zones when comparing regional news
- Note that some topics may have different names in different languages
- Use language-specific sentiment analysis tools for accuracy
- Respect cultural context when interpreting results

---

## Summary of Real-World Examples

These five examples demonstrate GNews's versatility:

| Example | Complexity | Use Case | Key Features |
|---------|-----------|----------|--------------|
| News Bot | Medium | Automation | Periodic fetching, deduplication, formatting |
| Market Sentiment | Advanced | Finance | Sentiment analysis, multi-stock tracking |
| Research Collection | Medium | Academia | Date ranges, multi-format export, statistics |
| News Monitoring | Advanced | Business | Real-time alerts, continuous monitoring |
| Multi-language Aggregation | Advanced | Global | Cross-cultural comparison, regional analysis |

Each example can be customized and extended based on your specific needs. For more basic usage, refer to the [Interactive Tutorial](./examples/tutorial.ipynb).

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

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any
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
