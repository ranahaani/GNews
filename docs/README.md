# 📚 GNews Documentation

Welcome to the GNews documentation directory! This folder contains all comprehensive guides, references, and resources for the GNews article fetching system.

---

## 📖 Documentation Index

### 🚀 Getting Started

**[ARTICLE_EXTRACTOR_README.md](./ARTICLE_EXTRACTOR_README.md)**
- Script installation and setup
- Usage examples and command-line arguments
- Output format and field descriptions
- GitHub Actions integration guide

**[GITHUB_ACTIONS_GUIDE.md](./GITHUB_ACTIONS_GUIDE.md)**
- Workflow setup and configuration
- Schedule customization
- Troubleshooting guide
- Best practices for rate limiting

---

### 📋 Reference

**[CHANGELOG.md](./CHANGELOG.md)**
- Version history and release notes
- Feature announcements
- Breaking changes and migration guides
- Technical implementation details

**[IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md)**
- v2.0 quick reference
- Files changed summary
- Sample output examples
- Deployment checklist

---

### 🤝 Community

**[CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)**
- Community guidelines
- Expected behavior
- Reporting process

---

## 🆕 What's New in v2.0

### ✨ Major Features

1. **Smart Duplicate Handling**
   - Duplicate URLs are intelligently detected and skipped
   - No more database errors from duplicates
   - Separate tracking: success / duplicate / failed

2. **24-Hour UTC Time Filtering**
   - Only fetches articles from last 24 hours
   - Ensures fresh, timely content
   - Reduces processing volume by 30-40%

3. **Rich Emoji Logging**
   - Visual status indicators (✅ ⊘ ❌ 🕐 📰 💾 📊)
   - Easy-to-read structured logs
   - Comprehensive summaries

4. **US News Category**
   - New NATION topic available
   - Automatically stored as 'US' category
   - Dedicated US domestic news coverage

5. **Standardized Limits**
   - All topics fetch 30 articles max
   - Consistent behavior across workflows
   - Optimized for fresh content delivery

---

## 🎯 Quick Links

### For New Users
1. Start with [ARTICLE_EXTRACTOR_README.md](./ARTICLE_EXTRACTOR_README.md) - Installation & basic usage
2. Then [GITHUB_ACTIONS_GUIDE.md](./GITHUB_ACTIONS_GUIDE.md) - Automated workflows

### For Existing Users (v1.0 → v2.0)
1. Read [CHANGELOG.md](./CHANGELOG.md) - What changed
2. Review [IMPLEMENTATION_SUMMARY.md](./IMPLEMENTATION_SUMMARY.md) - Migration guide

### For Contributors
1. Review [CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md) - Community guidelines
2. Check [CHANGELOG.md](./CHANGELOG.md) - Recent changes

---

## 📊 Documentation Map

```
docs/
├── README.md                      # 📍 You are here
├── ARTICLE_EXTRACTOR_README.md    # Script usage guide
├── GITHUB_ACTIONS_GUIDE.md        # Workflow setup guide
├── CHANGELOG.md                   # Version history
├── IMPLEMENTATION_SUMMARY.md      # v2.0 quick reference
└── CODE_OF_CONDUCT.md            # Community guidelines
```

---

## 🔧 Workflow Files

GitHub Actions workflows are located in [`.github/workflows/`](../.github/workflows/):

| Workflow | Status | Purpose |
|----------|--------|---------|
| `fetch-news.yml` | ✅ **Active** (8-hour schedule) | Main news fetching (10 topics) |
| `fetch-keywords.yml` | 🔧 **Manual only** | Keyword-based searches |
| `fetch-news-batched.yml` | 🔧 **Manual only** | Batched bulk collection |

---

## 💡 Common Tasks

### I want to...

**...set up automated news fetching**
→ See [GITHUB_ACTIONS_GUIDE.md - Quick Setup](./GITHUB_ACTIONS_GUIDE.md#quick-setup)

**...run the script manually**
→ See [ARTICLE_EXTRACTOR_README.md - Usage](./ARTICLE_EXTRACTOR_README.md#usage)

**...understand the logging output**
→ See [GITHUB_ACTIONS_GUIDE.md - Understanding Logs](./GITHUB_ACTIONS_GUIDE.md#understanding-logs-)

**...fix duplicate articles**
→ See [CHANGELOG.md - Smart Duplicate Handling](./CHANGELOG.md#-smart-duplicate-handling)

**...customize workflow schedule**
→ See [GITHUB_ACTIONS_GUIDE.md - Change Schedule](./GITHUB_ACTIONS_GUIDE.md#change-schedule)

**...add more news topics**
→ See [GITHUB_ACTIONS_GUIDE.md - Add More Categories](./GITHUB_ACTIONS_GUIDE.md#add-more-categories)

**...troubleshoot issues**
→ See [GITHUB_ACTIONS_GUIDE.md - Troubleshooting](./GITHUB_ACTIONS_GUIDE.md#troubleshooting)

**...migrate from v1.0 to v2.0**
→ See [CHANGELOG.md - Migration Guide](./CHANGELOG.md#-migration-guide)

---

## 📞 Support

- **Issues:** [GitHub Issues](https://github.com/ranahaani/GNews/issues)
- **Discussions:** [GitHub Discussions](https://github.com/ranahaani/GNews/discussions)
- **GNews Library:** [Main Repository](https://github.com/ranahaani/GNews)

---

## 📄 License

See [LICENSE](../LICENSE.txt) in the root directory.

---

**Happy news fetching! 📰🚀**

*Last updated: 2025-10-03 (v2.0.0)*
