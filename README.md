# GNews [![Travis branch](https://img.shields.io/travis/brh55/google-news-rss/master.svg?style=flat-square)](https://travis-ci.org/brh55/google-news-rss) [![Coveralls branch](https://img.shields.io/coveralls/brh55/google-news-rss/master.svg?style=flat-square)](https://coveralls.io/github/brh55/google-news-rss) 

🚩 A Python Package (with CLI support) that searches Google News RSS Feed and returns a usable JSON response \
🚩 As well as you can fetch full article

![Usage](https://github.com/ranahaani/GNews/raw/main/imgs/img.png)

<p align="center">Coverts ⬇️</p>

```
{'publisher': 'Aljazeera.com',
 'description': 'Pakistan accuses India of stoking conflict in Indian Ocean  '
                'Aljazeera.com',
 'published date': 'Tue, 16 Feb 2021 11:50:43 GMT',
 'title': 'Pakistan accuses India of stoking conflict in Indian Ocean - '
          'Aljazeera.com',
 'url': 'https://www.aljazeera.com/news/2021/2/16/pakistan-accuses-india-of-nuclearizing-indian-ocean'}
```


## Install

``` 
pip install gnews
```

## Usage

```python
from GNews import GNews
google_news = GNews()
news = google_news.get_news('Pakistan')

```
**We can set country, language, period and size during initialization**

```python
google_news = GNews(language='en', country='US', period='7d', size=10)
```
On the bottom left side of the Google News page you may find a `Language & region` section where you can find all of the supported combinations.

### Getting full article
##### you can use newspaper3k to scrap full article, you can also get full article using `get_full_article` by passing url i.e
```python

from GNews import GNews
google_news = GNews()
news = google_news.get_news('Pakistan')
article = google_news.get_full_article(news[0]['url'])

```
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

>`[]`

Read full documentation for `newspaper3k`
[newspaper3k](https://newspaper.readthedocs.io/en/latest/user_guide/quickstart.html#parsing-an-article)

## Article Properties
| Properties   | Description                                    | Example                                                                                                                                                                                                                                                                             |
|--------------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| title        | Title of the article                           | IMF Staff and Pakistan Reach Staff-Level Agreement on the Pending Reviews Under the Extended Fund Facility                                                                                                                                                                                                   |
| url         | Google news link to article                    | [Article Link](http://news.google.com/news/url?sa=t&fd=R&ct2=us&usg=AFQjCNGNR4Qg8LGbjszT1yt2s2lMXvvufQ&clid=c3a7d30bb8a4878e06b80cf16b898331&cid=52779522121279&ei=VQU7WYjiFoLEhQHIs4HQCQ&url=https://www.theguardian.com/commentisfree/2017/jun/07/why-dont-unicorns-exist-google) |
| published date      | Published date                                 | Wed, 07 Jun 2017 07:01:30 GMT                                                                                                                                                                                                                                                       |
| description  | Short description of article                   | IMF Staff and Pakistan Reach Staff-Level Agreement on the Pending Reviews Under the Extended Fund Facility ...                                                                                                                                                                                                                  |
| publisher    | Publisher of article                           | The Guardian                                                                                                                                                                                                                                                                        |                                                                                                                                                        |

## License

MIT © 
