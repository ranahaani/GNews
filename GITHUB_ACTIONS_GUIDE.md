# GitHub Actions Quick Start Guide

## Overview

This repository includes 3 pre-configured GitHub Actions workflows for automated news collection.

## Workflow Comparison

| Workflow | Schedule | Parallel Jobs | Total Variations | Best For |
|----------|----------|---------------|------------------|----------|
| `fetch-news.yml` | Every 6 hours | 10 | 9 categories | Daily automation |
| `fetch-keywords.yml` | Daily 6 AM | 8 | 10 keywords | Topic tracking |
| `fetch-news-batched.yml` | Daily midnight | 5 per batch | 16+ sources | Large-scale |

## Quick Setup

1. **Push workflows to your repository:**
   ```bash
   git add .github/workflows/
   git commit -m "Add news fetching workflows"
   git push
   ```

2. **Workflows will run automatically** based on their schedules

3. **Manual trigger:**
   - Go to Actions tab in GitHub
   - Select a workflow
   - Click "Run workflow"

## Customization Guide

### Change Schedule

Edit the `cron` expression:

```yaml
schedule:
  - cron: '0 */6 * * *'  # Every 6 hours
  # Pattern: minute hour day month weekday
```

Common schedules:
- Every hour: `'0 * * * *'`
- Every 4 hours: `'0 */4 * * *'`
- Daily at 9 AM: `'0 9 * * *'`
- Twice daily: `'0 6,18 * * *'`

### Adjust Parallel Jobs

Modify `max-parallel` value:

```yaml
strategy:
  max-parallel: 10  # Change this number
```

**Recommendations:**
- Conservative: 8-10
- Moderate: 12-15
- Maximum: 20

### Add More Categories

Edit the matrix in any workflow:

```yaml
matrix:
  category:
    - { topic: 'TECHNOLOGY', max: 50 }
    - { topic: 'YOUR_NEW_TOPIC', max: 30 }  # Add here
```

### Change Results Per Category

Modify the `max` value:

```yaml
- { topic: 'TECHNOLOGY', max: 100 }  # Fetch 100 articles
```

## Output & Artifacts

### Where to Find Results

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

## Rate Limiting Best Practices

### Symptoms of Rate Limiting
- HTTP 429 errors
- Empty article text
- Frequent download failures

### Solutions

1. **Reduce parallel jobs:**
   ```yaml
   max-parallel: 8  # Lower this value
   ```

2. **Add delays between batches:**
   ```yaml
   - name: Wait before next batch
     run: sleep 60  # Wait 60 seconds
   ```

3. **Use batched workflow:**
   - Switch to `fetch-news-batched.yml`
   - Batches run sequentially with natural delays

4. **Reduce max_results:**
   ```yaml
   max: 25  # Lower from 50
   ```

## Cost Estimation (Free Tier)

### GitHub Actions Free Tier
- 2,000 minutes/month (private repos)
- Unlimited minutes (public repos)
- 20 concurrent jobs

### Estimated Usage

**Standard workflow (`fetch-news.yml`):**
- Runtime per execution: ~5-8 minutes
- 4 runs per day: ~30 minutes/day
- Monthly usage: ~900 minutes
- **✅ Well within free tier**

**All 3 workflows running:**
- Combined: ~15 minutes per cycle
- Monthly: ~2,700 minutes
- **⚠️ May need paid plan for private repos**

## Troubleshooting

### Workflow Not Running

**Check:**
1. Workflow file is in `.github/workflows/` directory
2. File has `.yml` or `.yaml` extension
3. YAML syntax is valid (use YAML validator)
4. Repository has Actions enabled (Settings > Actions)

### Jobs Failing

**Common causes:**
1. **Rate limiting** → Reduce parallel jobs
2. **Network timeout** → Add retry logic
3. **Invalid topic name** → Check available topics list
4. **Missing dependencies** → Verify pip install step

### Empty Article Text

**Likely causes:**
1. Google News redirect not resolved → Install `googlenewsdecoder`
2. Paywall blocking content → Expected behavior
3. Anti-scraping measures → Some sites block automated access

## Advanced Examples

### Custom Workflow with Retry Logic

```yaml
- name: Fetch with retries
  uses: nick-fields/retry@v2
  with:
    timeout_minutes: 10
    max_attempts: 3
    command: |
      python get_full_articles.py \
        --topic TECHNOLOGY \
        --max-results 50 \
        --output tech_news.json
```

### Notification on Failure

```yaml
- name: Notify on failure
  if: failure()
  run: |
    curl -X POST https://api.slack.com/... \
      -d "Workflow failed: ${{ github.workflow }}"
```

### Upload to Cloud Storage

```yaml
- name: Upload to S3
  uses: aws-actions/configure-aws-credentials@v1
  # ... configure AWS

- run: aws s3 cp *.json s3://my-bucket/news/
```

## Support

- **Issues:** Report at [repository issues](https://github.com/ranahaani/GNews/issues)
- **Documentation:** See [ARTICLE_EXTRACTOR_README.md](ARTICLE_EXTRACTOR_README.md)
- **GNews Library:** https://github.com/ranahaani/GNews
