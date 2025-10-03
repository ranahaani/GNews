# GitHub Actions Quick Start Guide

## Overview

This repository includes 3 pre-configured GitHub Actions workflows for automated news collection with **smart duplicate handling**, **24-hour time filtering**, and **rich emoji logging**.

## 🆕 What's New in v2.0

- ✅ **Smart duplicate detection** - Skips duplicate URLs without errors
- 🕐 **24-hour time filter** - Only fetches articles from last 24 hours (UTC)
- 📊 **Rich emoji logging** - Easy-to-read logs with visual indicators
- 🇺🇸 **US news category** - New NATION topic (stored as 'US')
- ⏰ **8-hour schedule** - Runs at 4AM, 12PM, 8PM EST (was every 6 hours)
- 🎯 **Standardized limits** - All topics fetch 30 articles (was 25-100)

## Workflow Comparison

| Workflow | Schedule | Parallel Jobs | Articles/Topic | Total Categories | Best For |
|----------|----------|---------------|----------------|------------------|----------|
| `fetch-news.yml` | Every 8 hours (4AM, 12PM, 8PM EST) | 10 | 30 | 10 topics (inc. US) | **✅ Recommended** - Daily automation |
| `fetch-keywords.yml` | Every 8 hours | 8 | 30 | 10 keywords | Topic tracking |
| `fetch-news-batched.yml` | **🔧 Manual only** | 5 per batch | 30 | 16+ sources | Manual bulk collection |

**🎯 Recommended:** Use `fetch-news.yml` for automated scheduled runs. The batched workflow is now manual-only.

## Quick Setup

1. **Configure Supabase credentials** (required for database storage):
   - Go to repository **Settings → Secrets and variables → Actions**
   - Add the following secrets:
     ```
     SUPABASE_HOST=your-project.supabase.co
     SUPABASE_PORT=5432
     SUPABASE_DATABASE=postgres
     SUPABASE_USER=postgres
     SUPABASE_PASSWORD=your-password
     ```

2. **Push workflows to your repository:**
   ```bash
   git add .github/workflows/
   git commit -m "Add news fetching workflows with v2.0 features"
   git push
   ```

3. **Workflows will run automatically** based on their schedules:
   - Main news: 4AM, 12PM, 8PM EST daily
   - Keywords: 4AM, 12PM, 8PM EST daily

4. **Manual trigger:**
   - Go to Actions tab in GitHub
   - Select a workflow
   - Click "Run workflow"

## Understanding Logs 📊

### New Emoji-Based Logging

Workflows now feature rich emoji logging for easy monitoring:

```
═══════════════════════════════════════════
🎯 FETCHING TOPIC: US (from NATION)
═══════════════════════════════════════════
🔢 Max Results Requested: 30
🕐 Time Filter: Last 24 hours (UTC)
═══════════════════════════════════════════

🔄 Requesting 90 articles...
📥 Received 90 articles

🕐 Filtering by date...
✅ KEEP "Biden policy..." (2.5h ago)
❌ SKIP "Old story..." (48h ago)

📊 Date Filter Summary:
   ✅ Kept: 62/90 (68.9%)
   ❌ Skipped: 28/90 (31.1%)

💾 Inserting into database...
✅ SUCCESS - "Article 1..."
⊘ DUPLICATE - "Article 2..." (already exists)
❌ FAILED - "Article 3..." (connection error)

═══════════════════════════════════════════
🏆 TOPIC SUMMARY: US
═══════════════════════════════════════════
📥 Fetched: 90 articles
🕐 After 24h filter: 62 kept, 28 skipped
💾 Database: 25 inserted, 4 duplicates, 1 failed
🎯 Target: 25 unique articles ✓
⏱️ Time: 156s (6.2s/article)
═══════════════════════════════════════════
```

### Emoji Legend

| Emoji | Meaning |
|-------|---------|
| ✅ | Success / Kept |
| ⊘ | Duplicate (skipped, not an error) |
| ❌ | Failed / Skipped (too old) |
| 🕐 | Time filtering |
| 📰 | Article processing |
| 🔗 | URL |
| 💾 | Database operation |
| 📊 | Summary |
| 🎯 | Target/Goal |
| 🏆 | Final summary |
| 📥 | Fetched |
| 🔄 | Processing |

## Customization Guide

### Change Schedule

Edit the `cron` expression:

```yaml
schedule:
  - cron: '0 9,17 * * *'  # 4AM and 12PM EST (9AM, 5PM UTC)
  - cron: '0 1 * * *'     # 8PM EST (1AM UTC next day)
```

**EST to UTC Conversion:**
- 4AM EST = 9AM UTC
- 12PM EST = 5PM UTC
- 8PM EST = 1AM UTC (next day)

Common schedules:
- Every hour: `'0 * * * *'`
- Every 4 hours: `'0 */4 * * *'`
- Daily at 9 AM UTC: `'0 9 * * *'`
- Twice daily: `'0 6,18 * * *'`

### Adjust Parallel Jobs

Modify `max-parallel` value:

```yaml
strategy:
  max-parallel: 10  # Change this number
```

**Recommendations:**
- Conservative: 8-10 (recommended for stability)
- Moderate: 12-15
- Maximum: 20 (GitHub Actions limit)

⚠️ Higher parallelism may trigger rate limiting from news sources.

### Add More Categories

Edit the matrix in any workflow:

```yaml
matrix:
  category:
    - { topic: 'TECHNOLOGY', max: 30 }
    - { topic: 'YOUR_NEW_TOPIC', max: 30 }  # Add here
```

**Available topics:** WORLD, NATION (stored as US), BUSINESS, TECHNOLOGY, ENTERTAINMENT, SPORTS, SCIENCE, HEALTH, POLITICS

### Change Articles Per Category

All topics are standardized to 30 articles for consistency, but you can adjust:

```yaml
- { topic: 'TECHNOLOGY', max: 50 }  # Fetch up to 50 articles
```

**Note:** The system fetches 3x the max initially (e.g., 150 for max:50) to account for:
- 24-hour time filtering (typically removes 30-40%)
- Duplicate detection (varies by topic)
- Failed extractions (typically <5%)

This ensures you get close to your target after filtering.

## Output & Artifacts

### Where to Find Results

**Supabase Database (Primary):**
- All articles are automatically stored in your Supabase `sources` table
- Duplicates are intelligently skipped
- Only fresh articles (last 24 hours) are inserted

**JSON Artifacts (Backup):**
1. Go to **Actions** tab in GitHub
2. Click on a completed workflow run
3. Scroll to **Artifacts** section
4. Download individual category files or combined archive

### Artifact Retention

- Individual files: 30 days
- Combined archives: 90 days

Change retention in workflow:

```yaml
- uses: actions/upload-artifact@v4
  with:
    retention-days: 60  # Change this
```

## Troubleshooting

### Understanding "Duplicates"

⊘ **Duplicates are NOT errors!**

In v2.0, duplicate URLs are intelligently detected and skipped. This is **normal and expected**:

- Articles re-published by Google News
- Stories updated with new timestamps
- Previously fetched articles still in 24-hour window

**Example:**
```
💾 Database Insert Results:
   ✅ Inserted: 18 (60%)
   ⊘ Duplicates: 10 (33%)
   ❌ Failed: 2 (7%)
```

This shows:
- 18 new articles added
- 10 already in database (skipped safely)
- 2 actual failures (connection issues, etc.)

### Common Issues

**Jobs Failing:**
1. **Missing database credentials** → Add SUPABASE_* secrets
2. **Rate limiting** → Reduce `max-parallel` to 8
3. **Invalid topic name** → Check available topics list

**Empty Article Text:**
- Paywall blocking (expected for some sites)
- Anti-scraping measures
- Check logs for "Text Extract: FAILED"

## Support

- **Issues:** Report at [repository issues](https://github.com/ranahaani/GNews/issues)
- **Changelog:** See [CHANGELOG.md](CHANGELOG.md) for version history
- **Documentation:** See [ARTICLE_EXTRACTOR_README.md](ARTICLE_EXTRACTOR_README.md)
- **GNews Library:** https://github.com/ranahaani/GNews

## Version

Current version: **2.0.0**

See [CHANGELOG.md](CHANGELOG.md) for full release notes.
