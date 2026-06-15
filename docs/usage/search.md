# Searching News

## By keyword

```python
from gnews import GNews

g = GNews(max_results=10)
articles = g.get_news("Pakistan")
```

## Top headlines

```python
articles = g.get_top_news()
```

## By topic

```python
articles = g.get_news_by_topic("TECHNOLOGY")
```

Available topics: `WORLD`, `NATION`, `BUSINESS`, `TECHNOLOGY`, `ENTERTAINMENT`, `SPORTS`, `SCIENCE`, `HEALTH`, `POLITICS`, `CELEBRITIES`, `TV`, `MUSIC`, `MOVIES`, `THEATER`, `SOCCER`, `CYCLING`, `MOTOR SPORTS`, `TENNIS`, `COMBAT SPORTS`, `BASKETBALL`, `BASEBALL`, `FOOTBALL`, `SPORTS BETTING`, `WATER SPORTS`, `HOCKEY`, `GOLF`, `CRICKET`, `RUGBY`, `ECONOMY`, `PERSONAL FINANCE`, `FINANCE`, `DIGITAL CURRENCIES`, `MOBILE`, `ENERGY`, `GAMING`, `INTERNET SECURITY`, `GADGETS`, `VIRTUAL REALITY`, `ROBOTICS`, `NUTRITION`, `PUBLIC HEALTH`, `MENTAL HEALTH`, `MEDICINE`, `SPACE`, `WILDLIFE`, `ENVIRONMENT`, `NEUROSCIENCE`, `PHYSICS`, `GEOLOGY`, `PALEONTOLOGY`, `SOCIAL SCIENCES`, `EDUCATION`, `JOBS`, `ONLINE EDUCATION`, `HIGHER EDUCATION`, `VEHICLES`, `ARTS-DESIGN`, `BEAUTY`, `FOOD`, `TRAVEL`, `SHOPPING`, `HOME`, `OUTDOORS`, `FASHION`

## By location

```python
articles = g.get_news_by_location("Pakistan")
articles = g.get_news_by_location("Karachi")
```

## By site

```python
articles = g.get_news_by_site("bbc.com")
```
