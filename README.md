{'content': '[![Contributors][contributors-shield]][contributors-url]\n[![Forks][forks-shield]][forks-url]\n[![Stargazers][stars-shield]][stars-url]\n[![Issues][issues-shield]][issues-url]\n[![MIT License][license-shield]][license-url]\n[![Download][download-sheild]][download-url]\n[![LinkedIn][linkedin-shield]][linkedin-url]\n[![Docs][docs-shield]][docs-url]\n\n<br />\n<br />\n\n<!-- SPONSOR -->\n<a href="https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews">\n  <img src="https://github.com/ranahaani/GNews/raw/master/imgs/searchapi-banner.png" alt="Sponsored by SearchApi — Google News API" width="100%">\n</a>\n<p align="center"><sub>Sponsored by <a href="https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews">SearchApi</a></sub></p>\n\n> **Related: [gnews-agent](https://github.com/ranahaani/gnews-agent)** — persistent, semantic news intelligence for AI agents, built on GNews. Fetch, dedupe, embed, and query articles from Python, a CLI, or an MCP server. `pip install gnews-agent` · [guide](#related-gnews-agent)\n\n<!-- PROJECT LOGO -->\n<br />\n<p align="center">\n  <a href="https://github.com/ranahaani/GNews">\n    <img src="https://github.com/ranahaani/GNews/raw/master/imgs/logo.png" alt="GNews">\n  </a>\n  \n<h3 align="center">GNews 📰</h3>\n\n  <p align="center">\n    A Happy and lightweight Python Package that Provides an API to search for articles on Google News and returns a usable JSON response! 🚀\n    <br />    \n    If you like ❤️ GNews or find it useful 🌟, support the project by buying me a coffee ☕.\n    <br />\n    <a href="https://www.buymeacoffee.com/ranahaani" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" ></a>\n    <br />\n    <br />\n    <a href="https://github.com/ranahaani/GNews/blob/master/README.md">🚀 View Demo</a>\n    ·\n    <a href="https://github.com/ranahaani/GNews/issues">🐞 Report Bug</a>\n    ·\n    <a href="https://github.com/ranahaani/GNews/issues">🚀 Request Feature</a>\n  </p>\n</p>\n\n<!-- TABLE OF CONTENTS -->\n<details open="open">\n   <summary>Table of Contents 📑</summary>\n   <ol>\n      <li>\n         <a href="#about-gnews">About 🚩</a>\n         <ul>\n            <li><a href="#demo">Demo 📺</a></li>\n         </ul>\n      </li>\n      <li>\n         <a href="#getting-started">Getting Started 🚀</a>\n         <ul>\n            <li><a href="#1-installing-the-gnews-package">Installing the GNews package 📦</a></li>\n         </ul>\n        <ul>\n            <li><a href="#2-setting-up-gnews-for-local-development">Setting Up GNews for Local Development 🧑\u200d💻</a></li>\n         </ul>\n      </li>\n      <li>\n         <a href="#example-usage">Usage 🧩</a>\n         <ul>\n            <li><a href="#Get-top-news">Top News 🌟</a></li>\n            <li><a href="#Get-news-by-keyword">News by Keywords 🔎</a></li>\n            <li><a href="#Get-news-by-major-topic">News by Major Topics 🚀</a></li>\n            <li><a href="#Get-news-by-geo-location">News by GEO Location 🌎</a></li>\n            <li><a href="#get-news-by-site">News by Site 📰</a></li>\n            <li><a href="#results-specification">Results 📊</a></li>\n            <li><a href="#supported-countries">Supported Countries 🌐</a></li>\n            <li><a href="#supported-languages">Supported Languages 🌍</a></li>\n            <li><a href="#article-properties">Article Properties 📝</a></li>\n            <li><a href="#getting-full-article">Getting Full Article 📰</a></li>\n            <li><a href="#export-results">Export Results 💾</a></li>\n            <li><a href="#cli-usage">CLI Usage 💻</a></li>\n            <li><a href="#async-support">Async Support ⚡</a></li>\n            <li><a href="#url-resolution">URL Resolution 🔗</a></li>\n         </ul>\n      </li>\n            <li>
         <a href="#real-world-examples">Real-World Examples 🌍</a>
         <ul>
            <li><a href="#1-building-a-news-bot">Building a News Bot 🤖</a></li>
            <li><a href="#2-market-sentiment-analysis">Market Sentiment Analysis 📈</a></li>
            <li><a href="#3-research-data-collection">Research Data Collection 📚</a></li>
            <li><a href="#4-news-monitoring-dashboard">News Monitoring Dashboard 📊</a></li>
            <li><a href="#5-multi-language-news-aggregation">Multi-language News Aggregation 🌐</a></li>
         </ul>
      </li>
<li><a href="#searchapi-integration">SearchApi Integration 🔍</a></li>\n      <li><a href="#using-gnews-behind-a-proxy">Using GNews Behind a Proxy 🛡️</a></li>\n      <li><a href="#related-gnews-agent">Related: gnews-agent</a></li>\n      <li><a href="#todo">To Do 📋</a></li>\n      <li><a href="#roadmap">Roadmap 🛣️</a></li>\n      <li><a href="#contributing">Contributing 🤝</a></li>\n      <li><a href="#license">License ⚖️</a></li>\n      <li><a href="#contact">Contact 📬</a></li>\n      <li><a href="#acknowledgements">Acknowledgements 🙏</a></li>\n   </ol>\n</details>\n<!-- ABOUT GNews -->\n\n## About GNews\n\n🚩 GNews is A Happy and lightweight Python Package that searches Google News RSS Feed and returns a usable JSON\nresponse \\\n🚩 As well as you can fetch full article (**No need to write scrappers for articles fetching anymore**) \\\n🚩 Scraping a lot of articles and your IP keeps getting blocked? Route GNews requests through [RapidProxy](https://www.rapidproxy.io/?ref=gnews&utm_source=github&utm_medium=readme&utm_campaign=gnews) residential proxies to keep pulling full articles without getting rate-limited. GNews users get 10% off with code `RAPID10`.\n\n<a href="https://www.rapidproxy.io/?ref=gnews&utm_source=github&utm_medium=readme&utm_campaign=gnews">\n  <img src="https://github.com/ranahaani/GNews/raw/master/imgs/rapidproxy-banner.png" alt="RapidProxy — Residential and ISP Proxies for Web Scraping" width="100%">\n</a>\n<p align="center"><sub><a href="https://www.rapidproxy.io/?ref=gnews&utm_source=github&utm_medium=readme&utm_campaign=gnews">Try RapidProxy</a> — 90M+ residential IPs with smart rotation, sticky sessions and non-expiring traffic, from $0.55/GB. Get 10% off with code <b>RAPID10</b>.</sub></p>\n\nGoogle News cover across **141+ countries** with **41+ languages**. On the bottom left side of the Google News page you\nmay find a `Language & region` section where you can find all of the supported combinations.\n\n### Demo\n\n[![GNews Demo][demo-gif]](https://github.com/ranahaani/GNews)\n\n\n\n<!-- GETTING STARTED -->\n\n## Getting Started\n\nThis section provides instructions for two different use cases:\n\n1. **Installing the GNews package** for immediate use.\n2. **Setting up the GNews project** for local development.\n\n### 1. Installing the GNews package\n\nTo install the package and start using it in your own projects, follow these steps:\n\n``` shell\npip install gnews\n```\n\nTo also enable full article text extraction:\n\n```shell\npip install gnews[fulltext]\n```\n\nTo enable real article URL resolution (resolves Google News redirect URLs):\n\n```shell\npip install gnews[playwright]\nplaywright install chromium\n```\n### 2. Setting Up GNews for Local Development\n\nIf you want to make modifications locally, follow these steps to set up the development environment.\n\n#### Option 1: Setup with Docker\n\n1. Install [docker and docker-compose](https://docs.docker.com/get-docker/).\n2. Configure the `.env` file by placing your MongoDB credentials.\n3. Run the following command to build and start the Docker containers:\n\n``` shell\ndocker-compose up --build\n```\n\n#### Option 2: Install Using Git Clone\n\n1. Clone this repository:\n``` shell\ngit clone https://github.com/ranahaani/GNews.git\n```\n\n2. Set up a virtual environment:\n```shell\nvirtualenv venv\nsource venv/bin/activate  # MacOS/Linux\n.\\venv\\Scripts\\activate  # Windows\n```\n\n3. Install the required dependencies:\n```shell\npip install -r requirements.txt\n```\n\n<!-- USAGE EXAMPLES -->\n\n### Example usage

```python
from gnews import GNews

google_news = GNews()
news = google_news.get_news('Pakistan')
print(news[0])
```

Output:

```json
{
  "publisher": "Aljazeera.com",
  "description": "Pakistan accuses India of stoking conflict in Indian Ocean",
  "published date": "Tue, 16 Feb 2021 11:50:43 GMT",
  "title": "Pakistan accuses India of stoking conflict in Indian Ocean",
  "url": "https://www.aljazeera.com/news/2021/2/16/pakistan-accuses-india-of-nuclearizing-indian-ocean"
}
```

> **Tip:** GNews returns up to `max_results` articles (default: 100). Adjust with `GNews(max_results=N)`.
### 📘 Interactive Tutorial \n\nWe have created a step-by-step **[ jupyter Notebook tutorial ]** that demonstrates:\n\n- Basic usage and setup  \n- Filtering news (by topic, location, domain, date range, etc.)\n- Exporting results (CSV, JSON)  \n- Real-world analysis: **Sentiment Analysis on news headlines**\n- Advanced usage & best practices  \n- Interactive examples you can run line-by-line\n\n👉 **Open the tutorial here:**  \n[examples/tutorial.ipynb](./examples/tutorial.ipynb)\n\nThis is the best way to learn GNews hands-on.\n\n
## Real-World Examples

The following examples demonstrate practical applications of GNews in real-world scenarios. Each example is self-contained and runnable.

### 1. Building a News Bot

Automatically fetch top headlines and format them for posting to a messaging platform or social media feed.

```python
from gnews import GNews

def fetch_daily_briefing(topic="TECHNOLOGY", max_articles=5):
    # Fetch top news for a topic and format a daily briefing
    google_news = GNews(language='en', country='US', max_results=max_articles)
    articles = google_news.get_news_by_topic(topic)

    briefing = f"📰 **Daily {topic.title()} Briefing**\n\n"
    for i, article in enumerate(articles, 1):
        briefing += f"{i}. **{article['title']}**\n"
        briefing += f"   _{article['publisher']} — {article['published date']}_\n"
        briefing += f"   {article['url']}\n\n"

    return briefing

if __name__ == "__main__":
    print(fetch_daily_briefing())
```

> **Use case:** Pair with a scheduler (e.g., `cron`, `APScheduler`) and a bot API (Slack, Telegram, Discord) to deliver automated news digests.

### 2. Market Sentiment Analysis

Collect financial news headlines and perform a basic sentiment analysis to gauge market mood.

```python
from gnews import GNews

def analyze_market_sentiment(keyword, max_articles=20):
    # Fetch news for a financial keyword and compute a simple sentiment score
    google_news = GNews(language='en', country='US', max_results=max_articles)
    articles = google_news.get_news(keyword)

    positive_words = {'surge', 'gain', 'profit', 'growth', 'rally', 'boom', 'rise', 'record', 'boost', 'strong'}
    negative_words = {'crash', 'loss', 'decline', 'fall', 'drop', 'recession', 'slump', 'panic', 'fear', 'weak'}

    scores = []
    for article in articles:
        title = article['title'].lower()
        description = article.get('description', '').lower()
        text = title + ' ' + description

        pos = sum(1 for w in positive_words if w in text)
        neg = sum(1 for w in negative_words if w in text)

        if pos > neg:
            scores.append(1)    # positive
        elif neg > pos:
            scores.append(-1)   # negative
        else:
            scores.append(0)    # neutral

    avg_score = sum(scores) / len(scores) if scores else 0
    sentiment = "Bullish" if avg_score > 0.1 else "Bearish" if avg_score < -0.1 else "Neutral"

    print(f"Keyword: {keyword}")
    print(f"Articles analyzed: {len(scores)}")
    print(f"Sentiment score: {avg_score:+.2f} ({sentiment})")
    return avg_score

if __name__ == "__main__":
    analyze_market_sentiment("Tesla stock")
```

> **Use case:** Integrate with `TextBlob` or `VADER` for more accurate NLP-based sentiment, or feed headlines into an LLM for deeper analysis.

### 3. Research Data Collection

Systematically collect news articles over a date range and export them for academic or data-science research.

```python
from gnews import GNews
from datetime import datetime

def collect_research_data(keyword, start_date, end_date, max_articles=100):
    # Collect and export news articles for research within a date range
    google_news = GNews(
        language='en',
        country='US',
        max_results=max_articles,
        start_date=start_date,
        end_date=end_date,
    )
    articles = google_news.get_news(keyword)

    # Export to JSON for further analysis
    filename = f"research_{keyword.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.json"
    google_news.save_to_json(articles, filename)

    print(f"Collected {len(articles)} articles for '"{keyword}'")
    print(f"Date range: {start_date} to {end_date}")
    print(f"Saved to: {filename}")

    # Preview first 3 articles
    for i, article in enumerate(articles[:3], 1):
        print(f"\n{i}. {article['title']}")
        print(f"   Publisher: {article['publisher']}")

    return articles

if __name__ == "__main__":
    collect_research_data(
        keyword="climate change policy",
        start_date=(2024, 1, 1),
        end_date=(2024, 3, 31),
        max_articles=50,
    )
```

> **Use case:** Combine with `pandas` for data cleaning and exploratory analysis, or use `gnews[fulltext]` to extract full article text for qualitative coding.

### 4. News Monitoring Dashboard

Build a reusable function that monitors specific topics and highlights trending publishers.

```python
from gnews import GNews
from collections import Counter

def monitor_topics(topics, max_per_topic=10):
    # Monitor multiple topics and report trending publishers
    google_news = GNews(language='en', country='US', max_results=max_per_topic)
    all_articles = {}

    for topic in topics:
        articles = google_news.get_news_by_topic(topic)
        all_articles[topic] = articles
        print(f"\n📡 {topic}: {len(articles)} articles")

    # Identify trending publishers across all topics
    publisher_counts = Counter()
    for articles in all_articles.values():
        for article in articles:
            publisher_counts[article['publisher']] += 1

    print("\n📰 Top Publishers Across All Topics:")
    for publisher, count in publisher_counts.most_common(10):
        print(f"  {publisher}: {count} articles")

    # Detect overlapping stories (same publisher across multiple topics)
    print("\n🔗 Publishers Covering Multiple Topics:")
    topic_sets = {}
    for topic, articles in all_articles.items():
        for article in articles:
            pub = article['publisher']
            if pub not in topic_sets:
                topic_sets[pub] = set()
            topic_sets[pub].add(topic)

    for pub, topics_covered in topic_sets.items():
        if len(topics_covered) > 1:
            print(f"  {pub}: {', '.join(topics_covered)}")

    return all_articles

if __name__ == "__main__":
    monitor_topics(["TECHNOLOGY", "BUSINESS", "SCIENCE"], max_per_topic=10)
```

> **Use case:** Wrap with a web framework (Flask, Streamlit, Dash) to build an interactive dashboard. Use `asyncio.gather` with the `*_async` methods for faster multi-topic fetching.

### 5. Multi-language News Aggregation

Aggregate news about the same topic from multiple languages and countries for a global perspective.

```python
from gnews import GNews

def aggregate_multilingual_news(keyword, language_country_pairs, max_results=5):
    # Fetch news for the same keyword across multiple language/region combinations
    results = {}

    for lang, country in language_country_pairs:
        google_news = GNews(language=lang, country=country, max_results=max_results)
        articles = google_news.get_news(keyword)
        results[f"{lang}-{country}"] = articles

        print(f"\n🌍 {lang.upper()} ({country}): {len(articles)} articles")
        for i, article in enumerate(articles[:2], 1):
            print(f"  {i}. {article['title']}")
            print(f"     {article['publisher']}")

    total = sum(len(a) for a in results.values())
    print(f"\n📊 Total articles collected: {total} across {len(language_country_pairs)} regions")

    return results

if __name__ == "__main__":
    pairs = [
        ("en", "US"),       # English - United States
        ("en", "GB"),       # English - United Kingdom
        ("fr", "FR"),       # French - France
        ("de", "DE"),       # German - Germany
        ("es-419", "AR"),   # Spanish - Argentina
    ]
    aggregate_multilingual_news("artificial intelligence", pairs)
```

> **Use case:** Useful for cross-cultural research, international journalism, or building multi-region news feeds. Translate headlines with an API (e.g., Google Translate) for side-by-side comparison.
### Get top news\n\n* `GNews.get_top_news()`\n\n### Get news by keyword\n\n* `GNews.get_news(keyword)`\n\n### Get news by major topic\n\n* `GNews.get_news_by_topic(topic)`\n* Available topics:` WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH, POLITICS, CELEBRITIES, TV, MUSIC, MOVIES, THEATER, SOCCER, CYCLING, MOTOR SPORTS, TENNIS, COMBAT SPORTS, BASKETBALL, BASEBALL, FOOTBALL, SPORTS BETTING, WATER SPORTS, HOCKEY, GOLF, \nCRICKET, RUGBY, ECONOMY, PERSONAL FINANCE, FINANCE, DIGITAL CURRENCIES, MOBILE, ENERGY, GAMING, INTERNET SECURITY, GADGETS, VIRTUAL REALITY, ROBOTICS, NUTRITION, PUBLIC HEALTH, MENTAL HEALTH, MEDICINE, SPACE, WILDLIFE, ENVIRONMENT, NEUROSCIENCE, PHYSICS, GEOLOGY, PALEONTOLOGY, SOCIAL SCIENCES, EDUCATION, JOBS, ONLINE EDUCATION, HIGHER EDUCATION, VEHICLES, ARTS-DESIGN, BEAUTY, FOOD, TRAVEL, SHOPPING, HOME, OUTDOORS, FASHION.`\n\n### Get news by geo location\n\n* `GNews.get_news_by_location(location)`\n* location can be name of city/state/country\n\n### Get news by site\n\n* `GNews.get_news_by_site(site)`\n* site should be in the format of: `"cnn.com"`\n\n### Results specification\nAll parameters are optional and can be passed during initialization. Here’s a list of the available parameters:\n\n- **language**: The language in which to return results (default: \'en\').\n- **country**: The country code for the headlines (default: \'US\').\n- **period**: The time period for which you want news.\n- **start_date**: Date after which results must have been published.\n- **end_date**: Date before which results must have been published.\n- **max_results**: The maximum number of results to return (default: 100).\n- **exclude_websites**: A list of websites to exclude from results.\n- **max_retries**: Retry attempts on HTTP 429 from Google News (default: `3`). Set to `0` to disable retries.\n- **retry_backoff_base**: Base seconds for exponential backoff between retries (default: `1.0`). Effective delay is `min(retry_backoff_max, retry_backoff_base * 2 ** attempt)` plus uniform jitter in `[0, retry_backoff_base)`.\n- **retry_backoff_max**: Cap (in seconds) for any single backoff delay (default: `60.0`).\n- **proxy**: A dictionary specifying the proxy settings used to route requests. The dictionary should contain a single key-value pair where the key is the protocol (`http` or `https`) and the value is the proxy address. Example:\n```python\n# Example with only HTTP proxy\n  proxy = {\n      \'http\': \'http://your_proxy_address\',\n  }\n  \n# Example with only HTTPS proxy\n  proxy = {\n      \'https\': \'http://your_proxy_address\',\n  }\n```\n  \n#### Example Initialization\n```python\nfrom gnews import GNews\n\n# Initialize GNews with various parameters, including proxy\ngoogle_news = GNews(\n    language=\'en\',\n    country=\'US\',\n    period=\'7d\',\n    start_date=None,\n    end_date=None,\n    max_results=10,\n    exclude_websites=[\'yahoo.com\', \'cnn.com\'],\n    proxy={\n        \'https\': \'https://your_proxy_address\'\n    }\n)\n```\n\n* Or change it to an existing object\n\n```python\ngoogle_news.period = \'7d\'  # News from last 7 days\ngoogle_news.max_results = 10  # number of responses across a keyword\ngoogle_news.country = \'United States\'  # News from a specific country \ngoogle_news.language = \'english\'  # News in a specific language\ngoogle_news.exclude_websites = [\'yahoo.com\', \'cnn.com\']  # Exclude news from specific website i.e Yahoo.com and CNN.com\ngoogle_news.start_date = (2020, 1, 1) # Search from 1st Jan 2020\ngoogle_news.end_date = (2020, 3, 1) # Search until 1st March 2020\n```\n\nThe format of the timeframe is a string comprised of a number, followed by a letter representing the time operator. For\nexample 1y would signify 1 year. Full list of operators below:\n\n```\n - h = hours (eg: 12h)\n - d = days (eg: 7d)\n - m = months (eg: 6m)\n - y = years (eg: 1y)\n ```\n \nSetting the start and end dates can be done by passing in either a datetime or a tuple in the form (YYYY, MM, DD).\n\n### Supported Countries\n\n```python\nprint(google_news.AVAILABLE_COUNTRIES)\n\n{\'Australia\': \'AU\', \'Botswana\': \'BW\', \'Canada \': \'CA\', \'Ethiopia\': \'ET\', \'Ghana\': \'GH\', \'India \': \'IN\',\n \'Indonesia\': \'ID\', \'Ireland\': \'IE\', \'Israel \': \'IL\', \'Kenya\': \'KE\', \'Latvia\': \'LV\', \'Malaysia\': \'MY\', \'Namibia\': \'NA\',\n \'New Zealand\': \'NZ\', \'Nigeria\': \'NG\', \'Pakistan\': \'PK\', \'Philippines\': \'PH\', \'Singapore\': \'SG\', \'South Africa\': \'ZA\',\n \'Tanzania\': \'TZ\', \'Uganda\': \'UG\', \'United Kingdom\': \'GB\', \'United States\': \'US\', \'Zimbabwe\': \'ZW\',\n \'Czech Republic\': \'CZ\', \'Germany\': \'DE\', \'Austria\': \'AT\', \'Switzerland\': \'CH\', \'Argentina\': \'AR\', \'Chile\': \'CL\',\n \'Colombia\': \'CO\', \'Cuba\': \'CU\', \'Mexico\': \'MX\', \'Peru\': \'PE\', \'Venezuela\': \'VE\', \'Belgium \': \'BE\', \'France\': \'FR\',\n \'Morocco\': \'MA\', \'Senegal\': \'SN\', \'Italy\': \'IT\', \'Lithuania\': \'LT\', \'Hungary\': \'HU\', \'Netherlands\': \'NL\',\n \'Norway\': \'NO\', \'Poland\': \'PL\', \'Brazil\': \'BR\', \'Portugal\': \'PT\', \'Romania\': \'RO\', \'Slovakia\': \'SK\', \'Slovenia\': \'SI\',\n \'Sweden\': \'SE\', \'Vietnam\': \'VN\', \'Turkey\': \'TR\', \'Greece\': \'GR\', \'Bulgaria\': \'BG\', \'Russia\': \'RU\', \'Ukraine \': \'UA\',\n \'Serbia\': \'RS\', \'United Arab Emirates\': \'AE\', \'Saudi Arabia\': \'SA\', \'Lebanon\': \'LB\', \'Egypt\': \'EG\',\n \'Bangladesh\': \'BD\', \'Thailand\': \'TH\', \'China\': \'CN\', \'Taiwan\': \'TW\', \'Hong Kong\': \'HK\', \'Japan\': \'JP\',\n \'Republic of Korea\': \'KR\'}\n```\n\n### Supported Languages\n\n```python\nprint(google_news.AVAILABLE_LANGUAGES)\n\n{\'english\': \'en\', \'indonesian\': \'id\', \'czech\': \'cs\', \'german\': \'de\', \'spanish\': \'es-419\', \'french\': \'fr\',\n \'italian\': \'it\', \'latvian\': \'lv\', \'lithuanian\': \'lt\', \'hungarian\': \'hu\', \'dutch\': \'nl\', \'norwegian\': \'no\',\n \'polish\': \'pl\', \'portuguese brasil\': \'pt-419\', \'portuguese portugal\': \'pt-150\', \'romanian\': \'ro\', \'slovak\': \'sk\',\n \'slovenian\': \'sl\', \'swedish\': \'sv\', \'vietnamese\': \'vi\', \'turkish\': \'tr\', \'greek\': \'el\', \'bulgarian\': \'bg\',\n \'russian\': \'ru\', \'serbian\': \'sr\', \'ukrainian\': \'uk\', \'hebrew\': \'he\', \'arabic\': \'ar\', \'marathi\': \'mr\', \'hindi\': \'hi\',\n \'bengali\': \'bn\', \'tamil\': \'ta\', \'telugu\': \'te\', \'malyalam\': \'ml\', \'thai\': \'th\', \'chinese simplified\': \'zh-Hans\',\n \'chinese traditional\': \'zh-Hant\', \'japanese\': \'ja\', \'korean\': \'ko\'}\n```\n\n### Article Properties\n\n- Get news returns a list of articles with the following keys:\n\n**RSS backend (default):**\n\n| Field | Description | Example |\n|-------|-------------|---------|\n| `title` | Article title | `"Pakistan PM calls for ceasefire"` |\n| `description` | Short summary | `"Pakistan\'s prime minister said..."` |\n| `published date` | Published date (RFC 2822) | `"Wed, 07 Jun 2026 07:01:30 GMT"` |\n| `url` | Direct article URL | `"https://bbc.com/news/..."` |\n| `publisher` | Publisher name | `"BBC News"` |\n\n**SearchApi backend (additional fields):**\n\n| Field | Description | Example |\n|-------|-------------|---------|\n| `iso_date` | ISO 8601 publish date | `"2026-06-07T07:01:30Z"` |\n| `thumbnail` | Article image (base64) | `"data:image/jpeg;base64,..."` |\n| `favicon` | Publisher logo (base64) | `"data:image/png;base64,..."` |\n| `rank` | Position in search results | `1` |\n\n## Getting full article\n\nFirst install the optional dependency:\n\n```shell\npip install gnews[fulltext]\n```\n\nThen use `get_full_article()`:\n\n```python\nfrom gnews import GNews\n\ngoogle_news = GNews()\narticles = google_news.get_news(‘Pakistan’)\narticle = google_news.get_full_article(articles[0][‘url’])\n\nprint(article[‘text’])   # full article text\nprint(article[‘url’])    # original URL\n```\n\n> **Note:** Some sites block automated requests (paywalls, Cloudflare). `get_full_article()` will raise a `NetworkError` in those cases.\n\n## Export Results\n\nSave articles directly to JSON or CSV:\n\n```python\nfrom gnews import GNews\n\ng = GNews(max_results=10)\narticles = g.get_news("artificial intelligence")\n\n# Save to JSON\ng.save_to_json(articles, "news.json")\n\n# Save to CSV\ng.save_to_csv(articles, "news.csv")\n```\n\nBoth methods return the output file path. No extra dependencies required.\n\n## CLI Usage\n\nGNews includes a command-line interface out of the box:\n\n```shell\n# Search news\ngnews search "artificial intelligence"\ngnews search "Pakistan" --lang ur --country PK --max 5\n\n# Top headlines\ngnews top\ngnews top --max 10\n\n# By topic\ngnews topic TECHNOLOGY\ngnews topic BUSINESS --max 5\n\n# By site\ngnews site bbc.com\ngnews site cnn.com --max 3\n\n# By location\ngnews location Pakistan\ngnews location India --max 5\n\n# JSON output (pipe-friendly)\ngnews search "OpenAI" --json\ngnews top --json | python3 -m json.tool\n```\n\n**Options available on all commands:**\n\n| Option | Default | Description |\n|--------|---------|-------------|\n| `--lang` | `en` | Language code |\n| `--country` | `US` | Country code |\n| `--max` | `10` | Max results |\n| `--json` | off | Output as JSON |\n\n## Using GNews Behind a Proxy\n\nGoogle News rate-limits aggressively. If you are pulling more than a few hundred articles, or calling `get_full_article()` across many domains, you will eventually see HTTP 429s and blocked requests from a single IP.\n\nThe fix is to route requests through rotating residential proxies. GNews accepts a standard `requests`-style proxy dict, so any provider works:\n\n```python\nfrom gnews import GNews\n\ngoogle_news = GNews(\n    proxy={\n        \'http\': \'http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_PROXY_HOST:YOUR_PORT\',\n        \'https\': \'http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_PROXY_HOST:YOUR_PORT\',\n    }\n)\n\narticles = google_news.get_news(\'artificial intelligence\')\n```\n\n### Recommended provider\n\nGNews is sponsored by [RapidProxy](https://www.rapidproxy.io/?ref=gnews&utm_source=github&utm_medium=docs&utm_campaign=gnews), which is what the maintainer uses for high-volume runs. It offers 90M+ residential IPs, smart rotation, sticky sessions and native static ISP IPs, with traffic that does not expire. Pricing starts at $0.55/GB, and the code `RAPID10` gives GNews users 10% off.\n\n```python\nfrom gnews import GNews\n\nRAPIDPROXY = \'http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_PROXY_HOST:YOUR_PORT\'\n\ngoogle_news = GNews(\n    proxy={\'http\': RAPIDPROXY, \'https\': RAPIDPROXY},\n    max_retries=3,\n)\n\narticles = google_news.get_news(\'artificial intelligence\')\nfull = google_news.get_full_article(articles[0][\'url\'])\n```\n\nReplace `YOUR_USERNAME`, `YOUR_PASSWORD`, `YOUR_PROXY_HOST` and `YOUR_PORT` with the values generated in your RapidProxy dashboard. Sticky sessions are useful when you want consecutive requests to keep the same exit IP; rotating sessions are better for spreading a large crawl across many IPs.\n\n### Tips\n\n- Keep `max_retries` at 3 or higher so transient 429s are retried on a fresh IP.\n- Use sticky sessions when fetching an article body, since some sites tie the session to the IP that loaded the page.\n- Residential IPs are slower than datacenter IPs. Increase concurrency rather than expecting each request to be fast.\n- If you would rather skip proxies entirely, the [SearchApi backend](#searchapi-integration) handles blocking on their side.\n\n## SearchApi Integration\n\nGNews supports [SearchApi](https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews) as an optional backend. When a `searchapi_key` is provided, GNews uses SearchApi instead of the default Google News RSS feed.\n\n**Benefits over RSS:**\n- Resolved article URLs (fixes broken redirect links, see [#62](https://github.com/ranahaani/GNews/issues/62))\n- Pagination beyond the ~100-result RSS cap\n- Richer article data: `thumbnail`, `favicon`, `iso_date`, `rank`, `snippet`\n- No IP blocks or rate limits from Google\n\n### Setup\n\n```shell\npip install gnews\n```\n\nGet a free API key at [searchapi.io](https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews).\n\n### Usage\n\n```python\nfrom gnews import GNews\n\n# Pass your SearchApi key to enable the SearchApi backend\ngoogle_news = GNews(searchapi_key="YOUR_SEARCHAPI_KEY")\n\n# All existing methods work as before\narticles = google_news.get_news("artificial intelligence")\nprint(articles[0])\n```\n\n```\n{\n  \'title\': \'OpenAI announces new model\',\n  \'description\': \'Article snippet from SearchApi...\',\n  \'published date\': \'2 hours ago\',\n  \'iso_date\': \'2026-06-11T10:00:00Z\',\n  \'url\': \'https://techcrunch.com/2026/06/11/openai-new-model\',\n  \'publisher\': \'TechCrunch\',\n  \'thumbnail\': \'data:image/jpeg;base64,...\',\n  \'favicon\': \'data:image/png;base64,...\',\n  \'rank\': 1\n}\n```\n\n### Pagination\n\n```python\ngoogle_news = GNews(searchapi_key="YOUR_KEY", max_results=50)\n\n# Get page 2 results (breaks past the ~100 RSS cap)\narticles = google_news.get_news("Python", page=2)\n```\n\n### Additional article fields (SearchApi backend only)\n\n| Field | Description |\n|---|---|\n| `iso_date` | Absolute ISO 8601 publish date |\n| `thumbnail` | Article image (base64) |\n| `favicon` | Publisher logo (base64) |\n| `rank` | Position in search results |\n\n> The RSS backend (default, no API key required) continues to work exactly as before. The SearchApi backend is fully opt-in.\n\n<!-- ToDo -->\n\n## Async Support\n\nAll search methods have async equivalents — no new dependencies required:\n\n```python\nimport asyncio\nfrom gnews import GNews\n\ng = GNews(max_results=10)\n\n# Single async query\narticles = asyncio.run(g.get_news_async("AI"))\n\n# Fetch multiple topics concurrently\nasync def main():\n    ai, python, pakistan = await asyncio.gather(\n        g.get_news_async("AI"),\n        g.get_news_async("Python"),\n        g.get_news_async("Pakistan"),\n    )\n    return ai, python, pakistan\n\nasyncio.run(main())\n```\n\n| Async method | Sync equivalent |\n|---|---|\n| `get_news_async(key, page=1)` | `get_news()` |\n| `get_top_news_async()` | `get_top_news()` |\n| `get_news_by_topic_async(topic)` | `get_news_by_topic()` |\n| `get_news_by_location_async(location)` | `get_news_by_location()` |\n| `get_news_by_site_async(site)` | `get_news_by_site()` |\n\n## URL Resolution\n\nBy default, Google News RSS returns redirect URLs (`news.google.com/rss/articles/...`) instead of real article URLs. Google requires JavaScript execution to resolve them — plain HTTP requests cannot follow these redirects.\n\nInstall the optional Playwright extra to get real article URLs automatically:\n\n```shell\npip install gnews[playwright]\nplaywright install chromium  # one-time setup\n```\n\nOnce installed, URL resolution is automatic — no code changes needed:\n\n```python\nfrom gnews import GNews\n\ng = GNews(max_results=5)\narticles = g.get_news("AI")\n\n# With gnews[playwright] installed:\nprint(articles[0][\'url\'])  # https://www.politico.com/news/...\n\n# Without gnews[playwright]:\nprint(articles[0][\'url\'])  # https://news.google.com/rss/articles/...\n```\n\nIf resolution fails for a specific article (paywall, timeout, consent gate), GNews falls back to the Google URL silently — it never crashes.\n\n> **Note:** For production use without Playwright, the [SearchApi backend](#searchapi-integration) always returns real article URLs with zero setup beyond an API key.\n\n## Related: gnews-agent\n\n[gnews-agent](https://github.com/ranahaani/gnews-agent) ([PyPI: `gnews-agent`](https://pypi.org/project/gnews-agent/)) is the sibling package for agents. GNews returns articles. gnews-agent keeps them: it fetches through GNews, deduplicates by title and publisher, embeds the text, and stores it (SQLite + Chroma by default) so later queries are semantic rather than another live search. The same operations — ingest, search, timeline, brief, sentiment, and stats — are available as a Python library, a CLI, and an MCP server for Claude, Cursor, and other clients.\n\nIt depends on GNews (`gnews>=0.8.2`) and installs it for you. `ingest`, `search`, `timeline`, and `stats` need no API key. `brief` and `sentiment` call an LLM.\n\n```shell\npip install gnews-agent\n```\n\n```python\nfrom gnews_agent import NewsMemory\n\nmemory = NewsMemory()\nmemory.ingest("OpenAI", method="get_news")\nresults = memory.search("GPT-5 safety", days=7)\nprint(results)\n```\n\nOptional extras cover an OpenAI embedding backend (`gnews-agent[openai]`), full-article text (`gnews-agent[fulltext]`), and alternate vector stores. The [gnews-agent README](https://github.com/ranahaani/gnews-agent#readme) documents the CLI, the MCP server, and the Claude Code skill. A shorter guide is in these docs: [gnews-agent](https://gnews.readthedocs.io/en/latest/gnews-agent.html).\n\n## Todo\n\n- Save to MongoDB\n- Save to SQLite\n- ~~Save to JSON~~ ✅\n- ~~Save to .CSV file~~ ✅\n- ~~More than 100 articles~~ ✅\n- ~~Async support~~ ✅\n- ~~Real article URL resolution~~ ✅\n- FastAPI wrapper\n\n<!-- ROADMAP -->\n\n## Roadmap\n\nSee the [open issues](https://github.com/ranahaani/GNews/issues) for a list of proposed features (and known issues).\n\n\n\n<!-- CONTRIBUTING -->\n\n## Contributing\n\nContributions are what make the open source community such an amazing place to be learn, inspire, and create. Any\ncontributions you make are **greatly appreciated**.\n\n1. Fork the Project\n2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)\n3. Commit your Changes (`git commit -m \'Add some AmazingFeature\'`)\n4. Push to the Branch (`git push origin feature/AmazingFeature`)\n5. Open a Pull Request\n\n<!-- LICENSE -->\n\n## License\n\nDistributed under the MIT License. See `LICENSE` for more information.\n\n\n\n<!-- CONTACT -->\n\n## Contact\n\nMuhammad Abdullah - [@ranahaani](https://twitter.com/ranahaani) - ranahaani@gmail.com\n\nProject Link: [https://github.com/ranahaani/GNews](https://github.com/ranahaani/GNews)\n\n[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/ranahaani)\n\n[contributors-shield]: https://img.shields.io/github/contributors/ranahaani/GNews.svg?style=for-the-badge\n\n[contributors-url]: https://github.com/ranahaani/GNews/graphs/contributors\n\n[forks-shield]: https://img.shields.io/github/forks/ranahaani/GNews.svg?style=for-the-badge\n\n[forks-url]: https://github.com/ranahaani/GNews/network/members\n\n[stars-shield]: https://img.shields.io/github/stars/ranahaani/GNews.svg?style=for-the-badge\n\n[stars-url]: https://github.com/ranahaani/GNews/stargazers\n\n[issues-shield]: https://img.shields.io/github/issues/ranahaani/GNews.svg?style=for-the-badge\n\n[issues-url]: https://github.com/ranahaani/GNews/issues\n\n[license-shield]: https://img.shields.io/github/license/ranahaani/GNews.svg?style=for-the-badge\n\n[license-url]: https://github.com/ranahaani/GNews/blob/master/LICENSE.txt\n\n[download-sheild]: https://img.shields.io/pypi/dm/GNews.svg?style=for-the-badge\n\n[download-url]: https://pypistats.org/packages/gnews\n\n[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555\n\n[linkedin-url]: https://linkedin.com/in/ranahaani\n\n[docs-shield]: https://img.shields.io/readthedocs/gnews?style=for-the-badge\n\n[docs-url]: https://gnews.readthedocs.io/en/latest/\n\n[demo-gif]: https://github.com/ranahaani/GNews/raw/master/imgs/gnews.gif\n', 'download_url': 'https://raw.githubusercontent.com/ranahaani/GNews/master/README.md', 'encoding': 'text', 'git_url': 'https://api.github.com/repos/ranahaani/GNews/git/blobs/4eb922abb1e47c9737ffd7120d1fa0629f8b98b4', 'html_url': 'https://github.com/ranahaani/GNews/blob/master/README.md', 'name': 'README.md', 'path': 'README.md', 'sha': '4eb922abb1e47c9737ffd7120d1fa0629f8b98b4', 'size': 27288, 'type': 'file', 'url': 'https://api.github.com/repos/ranahaani/GNews/contents/README.md?ref=master'}