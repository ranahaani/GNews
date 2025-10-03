# Changelog

All notable changes to this project will be documented in this file.

## [2.0.0] - 2025-10-03

### 🎉 Major Release: Smart Duplicate Handling & Enhanced Logging

This release introduces intelligent article deduplication, 24-hour time filtering, and comprehensive emoji-based logging for better monitoring and debugging.

---

### ✨ New Features

#### 🔄 Smart Duplicate Handling
- **Zero-error duplicate detection** - Duplicate URLs are now intelligently detected and skipped without counting as failures
- **Database-level conflict resolution** - Uses PostgreSQL `ON CONFLICT (url) DO NOTHING` for efficient duplicate handling
- **Detailed tracking** - Separate counts for: successful inserts, duplicates skipped, and actual failures
- **URL-level reporting** - Logs show exactly which articles were inserted, which were duplicates, and which failed

#### 🕐 24-Hour UTC Time Filtering
- **Fresh news only** - All articles are filtered to include only those published within the last 24 hours (UTC)
- **Timezone-aware** - Proper UTC timezone handling for accurate date comparisons
- **Age tracking** - Shows article age in hours for transparency
- **Fallback handling** - Articles with unparseable dates are gracefully skipped and logged

#### 📊 Rich Emoji-Based Logging
- **30+ emojis** for quick visual scanning of logs
- **Per-URL action logs** - Every article URL is logged with its processing status
- **Comprehensive summaries** - Per-topic and overall summaries with statistics
- **Hierarchical logging** - Easy-to-read structured output with sections and separators

Status emojis:
- ✅ Success
- ⊘ Duplicate (skipped)
- ❌ Failed
- 🕐 Time filtering
- 📰 Article processing
- 💾 Database operations
- 📊 Summaries

#### 🇺🇸 US News Category
- **New NATION topic support** - Fetches US domestic news headlines
- **Automatic renaming** - NATION topic is automatically stored as 'US' category in database
- **Consistent labeling** - All US news appears under unified 'US' category

---

### 🔧 Changes

#### Workflow Schedules
- **Updated to 8-hour intervals** - All workflows now run at 4AM, 12PM, and 8PM EST (9AM, 5PM, 1AM UTC)
- **Reduced frequency** - Changed from every 6 hours to every 8 hours for better rate limiting

#### Article Limits
- **Standardized to 30 articles** - All topics now fetch maximum of 30 articles (previously 25-100)
- **Smarter fetching** - Fetches 3x the target initially (90 articles) to account for date filtering
- **Target guarantee** - Ensures 30 unique, fresh articles per topic after filtering

#### Workflows Updated
1. **fetch-news.yml** - Main news workflow
   - Added NATION/US topic
   - Updated schedule to 8-hour intervals
   - All topics capped at 30 articles
   - Enhanced with duplicate tracking

2. **fetch-keywords.yml** - Keyword-based workflow
   - Updated schedule to 8-hour intervals
   - Standardized all keywords to 30 articles

3. **fetch-news-batched.yml** - Batched workflow
   - **NOW MANUAL-ONLY** - Schedule removed (use fetch-news.yml instead)
   - Can still be triggered manually via workflow_dispatch
   - Updated to 30 articles per topic
   - Added NATION to batch-1 topics

---

### 📝 Technical Details

#### Database Module (`gnews/utils/db.py`)
```python
# New return format
{
    'status': 'success',  # or 'duplicate', 'failed'
    'url': 'https://...',
    'title': 'Article title',
    'reason': 'Error details (if failed)'
}

# Batch insert now returns
{
    'success': 30,           # Inserted articles
    'duplicate': 15,         # Skipped duplicates
    'failed': 3,             # Actual failures
    'success_urls': [...],   # List of inserted URLs
    'duplicate_urls': [...], # List of duplicate URLs
    'failed_urls': [...]     # List of failed URLs with reasons
}
```

#### Main Script (`get_full_articles.py`)
- **New function**: `filter_articles_by_date(articles, hours=24)`
- **Enhanced**: `get_articles_with_full_text()` with NATION→US mapping
- **Improved**: `main()` with comprehensive summary statistics
- **Metrics tracked**:
  - Total articles fetched
  - Articles after date filter
  - Articles after text extraction
  - Database insert results (success/duplicate/failed)
  - Elapsed time and averages

#### Logger Module (`gnews/utils/logger.py`)
- **New**: `EMOJI_MAP` - 30+ status and action emojis
- **New**: `get_emoji(key)` - Emoji lookup helper
- **New**: `log_separator()` - Visual separator lines
- **New**: `log_url_action()` - Standardized URL logging
- **New**: `log_summary_section()` - Formatted summary blocks
- **New**: `log_overall_summary()` - Comprehensive topic summaries

---

### 📊 Sample Log Output

```
═══════════════════════════════════════════
🎯 FETCHING TOPIC: US (from NATION)
═══════════════════════════════════════════
🔢 Max Results Requested: 30
🕐 Time Filter: Last 24 hours (UTC)
═══════════════════════════════════════════

🔄 [Fetch Attempt 1/1] Requesting 90 articles...
📥 Received 90 articles

🕐 Filtering by date (last 24 hours)...
✅ KEEP "Biden announces new policy..." (2.5h ago)
❌ SKIP "Old news story..." (48h ago - too old)

📊 Date Filter Summary:
   ✅ Kept: 62/90 (68.9%)
   ❌ Skipped: 28/90 (31.1%)

💾 Inserting 30 articles into database...
✅ [1/30] SUCCESS - "Biden announces..."
⊘ [2/30] DUPLICATE - "Trump rally..." (already exists)
❌ [3/30] FAILED - "Tech story..." (connection error)

═══════════════════════════════════════════
📊 BATCH INSERT SUMMARY
═══════════════════════════════════════════
📦 Total Processed: 30
✅ Successfully Inserted: 25 (83.3%)
⊘ Duplicates Skipped: 4 (13.3%)
❌ Failed: 1 (3.3%)
═══════════════════════════════════════════

═══════════════════════════════════════════
🏆 TOPIC SUMMARY: US
═══════════════════════════════════════════
🔄 Total Fetch Attempts: 1
📥 Total Articles Fetched: 90

🕐 Date Filtering Results:
   ✅ Kept: 62 (68.9%)
   ❌ Skipped: 28 (31.1%)

📝 Text Extraction Results:
   ✅ Success: 30 (100.0%)
   ❌ Failed: 0 (0.0%)

💾 Database Insert Results:
   ✅ Inserted: 25 (83.3%)
   ⊘ Duplicates: 4 (13.3%)
   ❌ Failed: 1 (3.3%)

🎯 Final Unique Articles: 25 ✓
⏱️ Total Elapsed Time: 156.3 seconds
📈 Average per Article: 5.2 seconds
═══════════════════════════════════════════
```

---

### 🔄 Migration Guide

#### For Existing Users

1. **Database Schema** - No changes required! The `url` column should already be your primary key.

2. **Script Updates** - Update your code to handle new return format:
   ```python
   # OLD
   result = insert_articles_batch(articles)
   print(f"Success: {result['success']}, Failed: {result['failed']}")

   # NEW
   result = insert_articles_batch(articles)
   print(f"Success: {result['success']}, "
         f"Duplicates: {result['duplicate']}, "
         f"Failed: {result['failed']}")
   ```

3. **Workflow Changes** - If using custom workflows:
   - Update schedule if you want 8-hour intervals
   - Update max values to 30 for consistency
   - Consider using fetch-news.yml instead of fetch-news-batched.yml

4. **US News** - NATION topic is now available and maps to 'US' category

---

### 💡 Benefits

1. **Cleaner Data** - No duplicate articles in database
2. **Fresh Content** - Only articles from last 24 hours
3. **Better Monitoring** - Rich logs make debugging easier
4. **Accurate Metrics** - Distinguish between duplicates and failures
5. **Consistent Categories** - All topics standardized to 30 articles
6. **US News** - Dedicated category for US domestic news

---

### 🐛 Bug Fixes

- Fixed duplicate articles causing database errors (now handled gracefully)
- Fixed old articles being included (now filtered to 24 hours)
- Fixed misleading "failed" counts (duplicates no longer counted as failures)
- Fixed NATION topic not being available

---

### ⚠️ Breaking Changes

1. **`insert_article()` return type changed**
   - Old: Returns `bool` (True/False)
   - New: Returns `dict` with status, url, title, reason

2. **`insert_articles_batch()` return type changed**
   - Old: `{'success': int, 'failed': int}`
   - New: `{'success': int, 'duplicate': int, 'failed': int, ...}`

3. **`fetch-news-batched.yml` schedule removed**
   - No longer runs automatically
   - Manual trigger only
   - Use `fetch-news.yml` for scheduled runs

---

### 📚 Documentation Updates

- Updated [GITHUB_ACTIONS_GUIDE.md](GITHUB_ACTIONS_GUIDE.md) with new schedules and limits
- Updated [ARTICLE_EXTRACTOR_README.md](ARTICLE_EXTRACTOR_README.md) with US topic and new features
- Added this [CHANGELOG.md](CHANGELOG.md)

---

### 🙏 Credits

This release focuses on production reliability and operational excellence, making the news fetching system more robust and easier to monitor.

---

## [1.0.0] - 2024-XX-XX

### Initial Release
- Basic news fetching functionality
- GitHub Actions workflows
- Article text extraction
- Category inference for top news
