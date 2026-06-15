[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![Download][download-sheild]][download-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Docs][docs-shield]][docs-url]

<br />
<br />

<!-- SPONSOR -->
<a href="https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews">
  <img src="https://github.com/ranahaani/GNews/raw/master/imgs/searchapi-banner.png" alt="Sponsored by SearchApi — Google News API" width="100%">
</a>
<p align="center"><sub>Sponsored by <a href="https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews">SearchApi</a></sub></p>

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
            <li><a href="#export-results">Export Results 💾</a></li>
            <li><a href="#cli-usage">CLI Usage 💻</a></li>
         </ul>
      </li>
      <li><a href="#searchapi-integration">SearchApi Integration 🔍</a></li>
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

To also enable full article text extraction:

```shell
pip install gnews[fulltext]
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

- Get news returns a list of articles with the following keys:

**RSS backend (default):**

| Field | Description | Example |
|-------|-------------|---------|
| `title` | Article title | `"Pakistan PM calls for ceasefire"` |
| `description` | Short summary | `"Pakistan's prime minister said..."` |
| `published date` | Published date (RFC 2822) | `"Wed, 07 Jun 2026 07:01:30 GMT"` |
| `url` | Direct article URL | `"https://bbc.com/news/..."` |
| `publisher` | Publisher name | `"BBC News"` |

**SearchApi backend (additional fields):**

| Field | Description | Example |
|-------|-------------|---------|
| `iso_date` | ISO 8601 publish date | `"2026-06-07T07:01:30Z"` |
| `thumbnail` | Article image (base64) | `"data:image/jpeg;base64,..."` |
| `favicon` | Publisher logo (base64) | `"data:image/png;base64,..."` |
| `rank` | Position in search results | `1` |

## Getting full article

First install the optional dependency:

```shell
pip install gnews[fulltext]
```

Then use `get_full_article()`:

```python
from gnews import GNews

google_news = GNews()
articles = google_news.get_news(‘Pakistan’)
article = google_news.get_full_article(articles[0][‘url’])

print(article[‘text’])   # full article text
print(article[‘url’])    # original URL
```

> **Note:** Some sites block automated requests (paywalls, Cloudflare). `get_full_article()` will raise a `NetworkError` in those cases.

## Export Results

Save articles directly to JSON or CSV:

```python
from gnews import GNews

g = GNews(max_results=10)
articles = g.get_news("artificial intelligence")

# Save to JSON
g.save_to_json(articles, "news.json")

# Save to CSV
g.save_to_csv(articles, "news.csv")
```

Both methods return the output file path. No extra dependencies required.

## CLI Usage

GNews includes a command-line interface out of the box:

```shell
# Search news
gnews search "artificial intelligence"
gnews search "Pakistan" --lang ur --country PK --max 5

# Top headlines
gnews top
gnews top --max 10

# By topic
gnews topic TECHNOLOGY
gnews topic BUSINESS --max 5

# By site
gnews site bbc.com
gnews site cnn.com --max 3

# By location
gnews location Pakistan
gnews location India --max 5

# JSON output (pipe-friendly)
gnews search "OpenAI" --json
gnews top --json | python3 -m json.tool
```

**Options available on all commands:**

| Option | Default | Description |
|--------|---------|-------------|
| `--lang` | `en` | Language code |
| `--country` | `US` | Country code |
| `--max` | `10` | Max results |
| `--json` | off | Output as JSON |

## SearchApi Integration

GNews supports [SearchApi](https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews) as an optional backend. When a `searchapi_key` is provided, GNews uses SearchApi instead of the default Google News RSS feed.

**Benefits over RSS:**
- Resolved article URLs (fixes broken redirect links, see [#62](https://github.com/ranahaani/GNews/issues/62))
- Pagination beyond the ~100-result RSS cap
- Richer article data: `thumbnail`, `favicon`, `iso_date`, `rank`, `snippet`
- No IP blocks or rate limits from Google

### Setup

```shell
pip install gnews
```

Get a free API key at [searchapi.io](https://www.searchapi.io/google-news?utm_source=github&utm_medium=sponsorship&utm_campaign=google_news_api&utm_content=ranahaani_GNews).

### Usage

```python
from gnews import GNews

# Pass your SearchApi key to enable the SearchApi backend
google_news = GNews(searchapi_key="YOUR_SEARCHAPI_KEY")

# All existing methods work as before
articles = google_news.get_news("artificial intelligence")
print(articles[0])
```

```
{
  'title': 'OpenAI announces new model',
  'description': 'Article snippet from SearchApi...',
  'published date': '2 hours ago',
  'iso_date': '2026-06-11T10:00:00Z',
  'url': 'https://techcrunch.com/2026/06/11/openai-new-model',
  'publisher': 'TechCrunch',
  'thumbnail': 'data:image/jpeg;base64,...',
  'favicon': 'data:image/png;base64,...',
  'rank': 1
}
```

### Pagination

```python
google_news = GNews(searchapi_key="YOUR_KEY", max_results=50)

# Get page 2 results (breaks past the ~100 RSS cap)
articles = google_news.get_news("Python", page=2)
```

### Additional article fields (SearchApi backend only)

| Field | Description |
|---|---|
| `iso_date` | Absolute ISO 8601 publish date |
| `thumbnail` | Article image (base64) |
| `favicon` | Publisher logo (base64) |
| `rank` | Position in search results |

> The RSS backend (default, no API key required) continues to work exactly as before. The SearchApi backend is fully opt-in.

<!-- ToDo -->

## Todo

- Save to MongoDB
- Save to SQLite
- ~~Save to JSON~~ ✅
- ~~Save to .CSV file~~ ✅
- ~~More than 100 articles~~ ✅
- Async support
- FastAPI wrapper

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

[docs-shield]: https://img.shields.io/readthedocs/gnews?style=for-the-badge

[docs-url]: https://gnews.readthedocs.io/en/latest/

[demo-gif]: https://github.com/ranahaani/GNews/raw/master/imgs/gnews.gif
