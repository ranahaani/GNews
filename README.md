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
      <li>
         <a href="#real-world-examples">Real-World Examples 🌍</a>
         <ul>
            <li><a href="#1-building-a-news-bot">Building a News Bot 🤖</a></li>
            <li><a href="#2-market-sentiment-analysis">Market Sentiment Analysis 📈</a></li>
            <li><a href="#3-research-data-collection">Research Data Collection 🔬</a></li>
            <li><a href="#4-news-monitoring-dashboard">News Monitoring Dashboard 📊</a></li>
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
All parameters are optional and can be passed during initialization. Here's a list of the available parameters:

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

* Or change it on an existing object

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

> End-of-Mission press releases include statements of IMF staff teams that convey preliminary findings after a mission. The views expressed are those of the IMF staff and do not necessarily represent the views of the IMF's Executive Board.\n\nIMF staff and the Pakistani authorities have reached an agreement on a package of measures to complete second to fifth reviews of the authorities' reform program supported by the IMF Extended Fund Facility (EFF) ..... (full article)

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

The following examples demonstrate practical applications of the GNews library. Each example is self-contained and can be run directly.

### 1. Building a News Bot

Automate posting the latest headlines to a messaging platform or social media feed. This example fetches top news and formats it as a concise summary suitable for automated posting.

```python
from gnews import GNews

def fetch_top_headlines(country='US', max_results=5):
    """Fetch top news headlines and format them for a bot post."""
    google_news = GNews(language='en', country=country, max_results=max_results)
    news = google_news.get_top_news()
    
    messages = []
    for article in news:
        message = f"📰 {article['title']}\n🔗 {article['url']}\n📅 {article['published date']}"
        messages.append(message)
    
    return messages

# Usage
headlines = fetch_top_headlines(country='US', max_results=3)
for headline in headlines:
    print(headline)
    print('---')
    # Integrate with your bot framework here, e.g.:
    # slack_client.chat_postMessage(channel='#news', text=headline)
    # twitter_client.update_status(status=headline)
```

> **What this does:** Fetches the top 3 news headlines from the US, formats each with a title, link, and date, and returns them as ready-to-post messages. Uncomment the integration lines to connect with Slack, Twitter, or other platforms.

### 2. Market Sentiment Analysis

Analyze the sentiment of financial news headlines to gauge market mood. This is useful for traders and analysts who want a quick overview of market sentiment based on recent news coverage.

```python
from gnews import GNews

def analyze_market_sentiment(keyword, period='7d', max_results=20):
    """Fetch news for a financial keyword and perform basic sentiment analysis."""
    google_news = GNews(language='en', country='US', period=period, max_results=max_results)
    news = google_news.get_news(keyword)
    
    # Simple keyword-based sentiment scoring
    positive_words = {'surge', 'gain', 'growth', 'profit', 'rise', 'boost', 'rally', 'record', 'strong', 'upbeat'}
    negative_words = {'fall', 'drop', 'loss', 'decline', 'crash', 'recession', 'down', 'slump', 'weak', 'fear'}
    
    results = []
    for article in news:
        title = article['title'].lower()
        description = article['description'].lower() if article['description'] else ''
        text = title + ' ' + description
        
        pos_count = sum(1 for word in positive_words if word in text)
        neg_count = sum(1 for word in negative_words if word in text)
        
        if pos_count > neg_count:
            sentiment = 'Positive'
        elif neg_count > pos_count:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
        
        results.append({
            'title': article['title'],
            'sentiment': sentiment,
            'score': pos_count - neg_count
        })
    
    return results

# Usage
sentiments = analyze_market_sentiment('AAPL stock', period='7d', max_results=10)
for item in sentiments:
    print(f"[{item['sentiment']}] {item['title']} (score: {item['score']})")
```

> **What this does:** Fetches news articles about a financial keyword (e.g., "AAPL stock"), scores each article's sentiment using a keyword-matching approach, and labels it as Positive, Negative, or Neutral. For production use, consider integrating NLP libraries like `TextBlob` or `VADER` for more accurate sentiment analysis.

### 3. Research Data Collection

Collect and export news data for academic research or data analysis. This example demonstrates how to systematically gather articles on a research topic and save them to a CSV file for further analysis.

```python
import csv
from datetime import datetime
from gnews import GNews

def collect_research_data(keyword, start_date, end_date, max_results=50, filename='research_data.csv'):
    """Collect news articles for research and export to CSV."""
    google_news = GNews(
        language='en',
        country='US',
        max_results=max_results,
        start_date=start_date,
        end_date=end_date
    )
    news = google_news.get_news(keyword)
    
    with open(filename, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Title', 'Published Date', 'Publisher', 'Description', 'URL'])
        
        for article in news:
            writer.writerow([
                article['title'],
                article['published date'],
                article['publisher'],
                article.get('description', ''),
                article['url']
            ])
    
    print(f"Exported {len(news)} articles to {filename}")
    return filename

# Usage
collect_research_data(
    keyword='climate change',
    start_date=(2024, 1, 1),
    end_date=(2024, 12, 31),
    max_results=50,
    filename='climate_research.csv'
)
```

> **What this does:** Searches for articles about a research topic within a date range, collects up to 50 results, and writes them to a CSV file with columns for title, date, publisher, description, and URL. This output can be directly imported into tools like Excel, pandas, or SPSS for analysis.

### 4. News Monitoring Dashboard

Build a monitoring system that tracks specific topics and summarizes recent coverage. This is ideal for PR teams, brand managers, or anyone who needs to stay updated on specific subjects.

```python
from gnews import GNews
from collections import Counter

def monitor_topics(keywords, period='1d', max_results=10):
    """Monitor multiple keywords and generate a summary dashboard."""
    google_news = GNews(language='en', country='US', period=period, max_results=max_results)
    
    dashboard = {}
    all_publishers = []
    
    for keyword in keywords:
        news = google_news.get_news(keyword)
        publishers = [article['publisher'] for article in news if article['publisher']]
        all_publishers.extend(publishers)
        
        dashboard[keyword] = {
            'article_count': len(news),
            'top_publishers': Counter(publishers).most_common(3),
            'latest_headline': news[0]['title'] if news else 'No articles found',
            'latest_url': news[0]['url'] if news else None
        }
    
    # Overall summary
    print("=" * 60)
    print(f"📊 NEWS MONITORING DASHBOARD — Last {period}")
    print("=" * 60)
    
    for keyword, data in dashboard.items():
        print(f"\n🔍 {keyword.upper()}")
        print(f"   Articles: {data['article_count']}")
        print(f"   Latest:   {data['latest_headline']}")
        if data['top_publishers']:
            print(f"   Top sources: {', '.join(p[0] for p in data['top_publishers'])}")
    
    print(f"\n📰 Most Active Publishers Overall:")
    for publisher, count in Counter(all_publishers).most_common(5):
        print(f"   {publisher}: {count} articles")

# Usage
monitor_topics(
    keywords=['artificial intelligence', ' cybersecurity', 'cloud computing'],
    period='1d',
    max_results=10
)
```

> **What this does:** Monitors multiple keywords simultaneously, tracks article counts per topic, identifies the most active publishers, and prints a formatted dashboard summary. This can be extended to send alerts via email or integrate with dashboard tools like Grafana or Streamlit.

### 5. Multi-language News Aggregation

Aggregate and compare news coverage across different languages and regions. This is valuable for multilingual analysis, international journalism, or understanding how different regions report on the same topic.

```python
from gnews import GNews

def aggregate_multilingual_news(keyword, language_country_pairs, max_results=5):
    """Fetch news for the same keyword across multiple languages and regions."""
    all_results = {}
    
    for language, country in language_country_pairs:
        google_news = GNews(
            language=language,
            country=country,
            max_results=max_results
        )
        news = google_news.get_news(keyword)
        
        all_results[f"{language}-{country}"] = [
            {
                'title': article['title'],
                'publisher': article['publisher'],
                'url': article['url'],
                'published_date': article['published date']
            }
            for article in news
        ]
    
    # Print comparison summary
    print(f"🌍 Multi-language News Report for: '{keyword}'")
    print("=" * 60)
    
    for region, articles in all_results.items():
        print(f"\n🏷️ Region: {region}")
        print(f"   Articles found: {len(articles)}")
        for article in articles[:2]:  # Show top 2 per region
            print(f"   • {article['title'][:80]}...")
    
    return all_results

# Usage
aggregate_multilingual_news(
    keyword='technology',
    language_country_pairs=[
        ('en', 'US'),    # English - United States
        ('en', 'GB'),    # English - United Kingdom
        ('fr', 'FR'),    # French - France
        ('de', 'DE'),    # German - Germany
        ('es-419', 'AR'), # Spanish - Argentina
    ],
    max_results=5
)
```

> **What this does:** Searches for the same keyword across five different language/region combinations, collects the top 5 articles from each, and prints a comparative summary. This enables cross-cultural news analysis and helps identify regional perspectives on global topics.

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