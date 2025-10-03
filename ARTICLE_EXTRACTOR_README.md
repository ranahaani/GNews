# Full Article Extractor for GNews

This script extends the GNews library to fetch complete article text and output results in JSON format.

## Features

- ✅ Fetches news articles using GNews API
- ✅ Decodes Google News redirect URLs to actual article URLs
- ✅ Extracts full article text using newspaper3k
- ✅ Returns cleaned titles (removes publisher suffix)
- ✅ Includes category/topic field for organizing articles (auto-inferred for top news)
- ✅ Includes article metadata: authors, images, publish date
- ✅ Outputs to JSON file or stdout
- ✅ Supports all GNews search methods

## Installation

```bash
# Install required dependencies
pip install gnews newspaper3k googlenewsdecoder
```

## Usage

### Basic Examples

```bash
# Search by keyword and print to stdout
python get_full_articles.py --keyword "artificial intelligence" --max-results 5 --pretty

# Save to JSON file
python get_full_articles.py --keyword "Python" --max-results 10 --output articles.json

# Get top news
python get_full_articles.py --max-results 10 --pretty

# Search by topic
python get_full_articles.py --topic TECHNOLOGY --max-results 5

# Search by location
python get_full_articles.py --location "New York" --max-results 5

# Search by site
python get_full_articles.py --site cnn.com --max-results 5
```

### Advanced Options

```bash
# Specify language and country
python get_full_articles.py --keyword "news" --language en --country US --max-results 10

# Use time period
python get_full_articles.py --keyword "AI" --period 7d --max-results 10
```

## Command-Line Arguments

| Argument | Short | Description | Default |
|----------|-------|-------------|---------|
| `--keyword` | `-k` | Search keyword | None |
| `--topic` | `-t` | News topic (e.g., WORLD, BUSINESS, TECHNOLOGY) | None |
| `--location` | `-l` | Geographic location | None |
| `--site` | `-s` | Specific website (e.g., cnn.com) | None |
| `--max-results` | `-m` | Maximum number of results | 10 |
| `--language` | | Language code | en |
| `--country` | | Country code | US |
| `--period` | `-p` | Time period (e.g., 7d, 1m, 1y) | None |
| `--output` | `-o` | Output JSON file path | stdout |
| `--pretty` | | Pretty print JSON output | False |

## Output Format

The script returns an array of article objects with the following structure:

```json
[
  {
    "title": "Article Title",
    "description": "Article summary from Google News",
    "published date": "Thu, 02 Oct 2025 05:16:56 GMT",
    "url": "https://news.google.com/rss/articles/...",
    "publisher": {
      "href": "https://example.com",
      "title": "Publisher Name"
    },
    "category": "TECHNOLOGY",
    "category_source": "explicit",
    "search_method": "topic",
    "actual_url": "https://example.com/article",
    "decoded_successfully": true,
    "full_text": "Complete article text...",
    "authors": ["Author Name"],
    "images": ["https://example.com/image1.jpg", "..."],
    "top_image": "https://example.com/main-image.jpg",
    "publish_date": "2025-10-02 00:00:00"
  }
]
```

### Field Descriptions

- **title**: Clean article title (publisher suffix removed)
- **description**: Summary/description from Google News RSS feed
- **published date**: Publication date from Google News
- **url**: Original Google News RSS URL
- **publisher**: Publisher information (name and website)
- **category**: Category/topic of the article
  - For topic searches: the topic name (e.g., "TECHNOLOGY", "BUSINESS")
  - For keyword searches: the search keyword
  - For location searches: the location name
  - For site searches: the site domain
  - For top news: **automatically inferred** from article content using keyword analysis (e.g., "US", "WORLD", "TECHNOLOGY", "BUSINESS", "POLITICS", "HEALTH", "SCIENCE", "SPORTS", "ENTERTAINMENT")
- **category_source**: How the category was determined
  - "explicit" - provided by search method (topic/keyword/location/site)
  - "inferred" - automatically detected from article content (for top news)
- **search_method**: Method used to fetch articles ("topic", "keyword", "location", "site", "top_news")
- **actual_url**: Resolved article URL (after decoding Google News redirect)
- **decoded_successfully**: Boolean indicating if URL decoding succeeded
- **full_text**: Complete article text content
- **authors**: List of article authors
- **images**: List of all images found in the article
- **top_image**: Main/featured image URL
- **publish_date**: Publication date extracted from article (may differ from Google News date)

## Available Topics

WORLD, NATION, BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH, POLITICS, CELEBRITIES, TV, MUSIC, MOVIES, THEATER, SOCCER, CYCLING, MOTOR SPORTS, TENNIS, COMBAT SPORTS, BASKETBALL, BASEBALL, FOOTBALL, SPORTS BETTING, WATER SPORTS, HOCKEY, GOLF, CRICKET, RUGBY, ECONOMY, PERSONAL FINANCE, FINANCE, DIGITAL CURRENCIES, MOBILE, ENERGY, GAMING, INTERNET SECURITY, GADGETS, VIRTUAL REALITY, ROBOTICS, NUTRITION, PUBLIC HEALTH, MENTAL HEALTH, MEDICINE, SPACE, WILDLIFE, ENVIRONMENT, NEUROSCIENCE, PHYSICS, GEOLOGY, PALEONTOLOGY, SOCIAL SCIENCES, EDUCATION, JOBS, ONLINE EDUCATION, HIGHER EDUCATION, VEHICLES, ARTS-DESIGN, BEAUTY, FOOD, TRAVEL, SHOPPING, HOME, OUTDOORS, FASHION

## Automatic Category Inference for Top News

When fetching top news (without specifying a topic), the script **automatically categorizes every article** using keyword analysis. All articles are assigned to one of the following categories:

- **US** - Domestic US news, federal government, Trump, Biden, Congress, law enforcement
- **WORLD** - International news, foreign affairs, conflicts, diplomacy
- **TECHNOLOGY** - Tech companies, AI, software, gadgets, social media
- **BUSINESS** - Economy, markets, corporate news, finance
- **POLITICS** - Elections, campaigns, voting, political parties
- **HEALTH** - Medical news, healthcare, diseases, treatments
- **SCIENCE** - Research, discoveries, climate, space, environment
- **SPORTS** - All sports news and events
- **ENTERTAINMENT** - Movies, music, celebrities, TV shows

**Every article is guaranteed to be categorized** - there is no "uncategorized" or "general" fallback. The inference is based on keyword matching from the article's title and description. The `category_source` field will be `"inferred"` for auto-categorized articles and `"explicit"` for articles fetched via topic/keyword/location/site searches.

## GitHub Actions Integration

This script is optimized for running in GitHub Actions workflows for automated news collection.

### Recommended Setup

**Native Python (Recommended):**
- ✅ Faster execution (~2-3 minutes)
- ✅ Lower resource usage
- ✅ Built-in dependency caching
- ✅ Simpler maintenance

**Docker (Optional):**
- Use only if you need exact reproducibility across platforms
- Adds ~1-2 minutes overhead per run

### Parallel Job Limits

When running multiple variations in parallel:

- **Conservative (Recommended):** 8-10 parallel jobs
  - Respects rate limits for Google News and target sites
  - Stable and reliable execution

- **Moderate:** 12-15 parallel jobs
  - Good balance between speed and stability

- **Maximum:** 20 parallel jobs (GitHub Actions free tier limit)
  - May encounter rate limiting
  - Use with caution

### Pre-Built Workflow Files

Three production-ready GitHub Actions workflow files are included in `.github/workflows/`:

1. **`fetch-news.yml`** - Standard parallel execution
   - Fetches 8 major categories + top news
   - Runs every 6 hours
   - 10 parallel jobs
   - **Best for:** Regular automated collection

2. **`fetch-keywords.yml`** - Keyword-based searches
   - Fetches 10 popular keyword topics (AI, crypto, climate, etc.)
   - Runs daily at 6 AM UTC
   - 8 parallel jobs
   - **Best for:** Tracking specific topics

3. **`fetch-news-batched.yml`** - Sequential batched execution
   - Runs jobs in 3 sequential batches to avoid rate limiting
   - Batch 1: Major topics (5 parallel)
   - Batch 2: Secondary topics (5 parallel)
   - Batch 3: Specialized searches (4 parallel)
   - **Best for:** Large-scale collection (20+ variations)

Simply push these files to your repository to enable automated news collection!

📖 **See [GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md) for detailed setup instructions, troubleshooting, and customization examples.**

### Example Workflow

```yaml
name: Fetch News Articles

on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
  workflow_dispatch:

jobs:
  fetch-news:
    runs-on: ubuntu-latest
    strategy:
      max-parallel: 10
      fail-fast: false
      matrix:
        category:
          - { topic: 'TECHNOLOGY', max: 50 }
          - { topic: 'BUSINESS', max: 50 }
          - { topic: 'WORLD', max: 50 }
          - { topic: 'HEALTH', max: 50 }
          - { topic: 'SCIENCE', max: 30 }
          - { topic: 'SPORTS', max: 30 }
          - { topic: 'ENTERTAINMENT', max: 30 }
          - { topic: 'POLITICS', max: 30 }

    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'
          cache: 'pip'

      - name: Install dependencies
        run: pip install gnews newspaper3k googlenewsdecoder

      - name: Fetch ${{ matrix.category.topic }} News
        run: |
          python get_full_articles.py \
            --topic ${{ matrix.category.topic }} \
            --max-results ${{ matrix.category.max }} \
            --output ${{ matrix.category.topic }}_news.json \
            --pretty

      - name: Upload results
        uses: actions/upload-artifact@v3
        with:
          name: ${{ matrix.category.topic }}-news
          path: ${{ matrix.category.topic }}_news.json
```

### Batched Execution (For 20+ variations)

For larger workloads, use sequential batches to avoid rate limits:

```yaml
jobs:
  batch-1:
    strategy:
      max-parallel: 8
      matrix:
        topic: [TECHNOLOGY, BUSINESS, WORLD, HEALTH]
    # ... steps ...

  batch-2:
    needs: batch-1  # Wait for batch 1
    strategy:
      max-parallel: 8
      matrix:
        topic: [SCIENCE, SPORTS, ENTERTAINMENT, POLITICS]
    # ... steps ...
```

## Notes

- The `googlenewsdecoder` library is required to properly resolve Google News redirect URLs
- Article extraction quality depends on the source website's structure
- Some articles may fail to extract due to paywalls or anti-scraping measures
- Rate limiting may occur with high volume requests (recommended: 8-10 parallel jobs max)
- Category inference for top news is keyword-based; all articles are guaranteed to be categorized into one of the 9 categories
- When running in GitHub Actions, use pip caching to speed up dependency installation
