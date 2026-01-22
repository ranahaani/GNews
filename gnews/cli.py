import typer
import gnews
from typing_extensions import Annotated
import json
from tabulate import tabulate
import os
from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, TOPICS, SECTIONS
import urllib.parse

app = typer.Typer()

def get_unique_filename(base_name: str) -> str:
    if not os.path.exists(base_name):
        return base_name
    name, ext = os.path.splitext(base_name)
    counter = 1
    new_name = f"{name}_{counter}{ext}"
    while os.path.exists(new_name):
        counter += 1
        new_name = f"{name}_{counter}{ext}"
    return new_name

def format_result(results: list | list[dict[str, any]], format: str, filename_prefix: str):
    if format == "json":
        filename = get_unique_filename(f"{filename_prefix}.json")
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=2)
        print(f"Results saved to {os.path.abspath(filename)}")

    elif format == "csv":
        filename = get_unique_filename(f"{filename_prefix}.csv")
        header = "title,description,published_date,url,publisher,publisher_href\n"
        csv_data = header
        for article in results:
            csv_data += (
                f"\"{article['title']}\","
                f"\"{article['description']}\","
                f"\"{article['published date']}\","
                f"\"{article['url']}\","
                f"\"{article['publisher']['title']}\","
                f"\"{article['publisher']['href']}\"\n"
            )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(csv_data)
        print(f"Results saved to {os.path.abspath(filename)}")

    else:
        headers = ["Title", "Description", "Published Date", "Url", "Publisher", "Publisher Href"]
        data = [
            [
                article["title"],
                article["description"],
                article["published date"],
                article["url"],
                article["publisher"]["title"],
                article["publisher"]["href"],
            ]
            for article in results
        ]
        print(tabulate(data, headers=headers, tablefmt="grid", missingval="?"))

    print("Total", len(results), "articles.")

@app.command()
def search(
    keyword: Annotated[str, typer.Argument(help="The keyword by which to search Google News.")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received. Default is 10.")] = 10,
    format: Annotated[str, typer.Option(help="Determine the format of output. Default is \"json\" for json file. Options: (json, csv, table)")] = "json",
    language: Annotated[str, typer.Option(help="The language in which to return results, in a two character abbreviation. Defaults to \"en\"")] = "en"
):
    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these: \"json\", \"csv\", or \"table\"")
        return

    if language not in AVAILABLE_LANGUAGES.values():
        typer.echo("Language should be in the list of available languages.")
        return

    google_news = gnews.GNews(max_results=limit, language=language)
    articles = google_news.get_news(keyword)

    if not articles:
        typer.echo(f"No articles found for the keyword \"{keyword}\".")
        return

    format_result(articles, format, f"search_{keyword}")

@app.command()
def trending(
    country: Annotated[str, typer.Option(help="What country to get news related to as two character abbreviation. Default is \"US\".")] = "US",
    limit: Annotated[int, typer.Option(help="Limit the number of articles received. Default is 10.")] = 10,
    format: Annotated[str, typer.Option(help="Determine the format of output. Default is \"json\" for json file. Options: (json, csv, table)")] = "json",
    language: Annotated[str, typer.Option(help="The language in which to return results, in a two character abbreviation. Defaults to \"en\"")] = "en"
):
    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these: \"json\", \"csv\", or \"table\"")
        return

    if country not in AVAILABLE_COUNTRIES.values():
        typer.echo("Country should be in list of available countries.")
        return

    if language not in AVAILABLE_LANGUAGES.values():
        typer.echo("Language should be in the list of available languages.")
        return

    google_news = gnews.GNews(max_results=limit, country=country, language=language)
    articles = google_news.get_top_news()

    if not articles:
        typer.echo(f"No trending articles found for the country \"{country}\".")
        return

    format_result(articles, format, f"trending_{country}")
    pass

@app.command()
def topic(
    topic: Annotated[str, typer.Argument(help="What topic to get news related to")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received. Default is 10.")] = 10,
    format: Annotated[str, typer.Option(help="Determine the format of output. Default is \"json\" for json file. Options: (json, csv, table)")] = "json",
    language: Annotated[str, typer.Option(help="The language in which to return results, in a two character abbreviation. Defaults to \"en\"")] = "en"
    ):

    topic = topic.upper()
    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these: \"json\", \"csv\", or \"table\"")
        return

    if language not in AVAILABLE_LANGUAGES.values():
        typer.echo("Language should be in the list of available languages.")
        return

    if topic not in TOPICS and topic not in SECTIONS.keys():
        typer.echo("Topic should be in the list of available topics.")
        return

    google_news = gnews.GNews(max_results=limit, language=language)
    articles = google_news.get_news_by_topic(topic)

    if not articles:
        typer.echo(f"No articles found for the topic \"{topic}\".")
        return

    format_result(articles, format, f"topic_{topic}")

@app.command()
def location(
    location: Annotated[str, typer.Argument(help="Where news received will be related to.")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received. Default is 10.")] = 10,
    format: Annotated[str, typer.Option(help="Determine the format of output. Default is \"json\" for json file. Options: (json, csv, table)")] = "json",
    language: Annotated[str, typer.Option(help="The language in which to return results, in a two character abbreviation. Defaults to \"en\"")] = "en"
    ):
    # encodes for URL
    locationUrlSafe = urllib.parse.quote(location)

    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these: \"json\", \"csv\", or \"table\"")
        return

    if language not in AVAILABLE_LANGUAGES.values():
        typer.echo("Language should be in the list of available languages.")
        return

    google_news = gnews.GNews(max_results=limit, language=language)
    articles = google_news.get_news_by_location(locationUrlSafe)

    if not articles:
        typer.echo(f"No articles found for the location \"{location}\".")
        return

    format_result(articles, format, f"location_{location}")

if __name__ == "__main__":
    app()
