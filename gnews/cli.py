import typer
import gnews
from typing_extensions import Annotated
import json
from tabulate import tabulate
import os

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
    keyword: Annotated[str, typer.Argument()],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")] = 10,
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
):
    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these: \"json\", \"csv\", or \"table\"")
        return

    google_news = gnews.GNews(max_results=limit)
    articles = google_news.get_news(keyword)

    if not articles:
        typer.echo(f"No articles found for the keyword \"{keyword}\".")
        return

    format_result(articles, format, f"search_{keyword}")

@app.command()
def topic(
    topic: Annotated[str, typer.Argument(help="What topic to get news related to")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")] = 10,
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
):
    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these: \"json\", \"csv\", or \"table\"")
        return

    google_news = gnews.GNews(max_results=limit)
    articles = google_news.get_news_by_topic(topic)

    if not articles:
        typer.echo(f"No articles found for the topic \"{topic}\".")
        return

    format_result(articles, format, f"topic_{topic}")

@app.command()
def location(
    location: Annotated[str, typer.Argument(help="Where news received will be related to.")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")] = 10,
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
):
    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these: \"json\", \"csv\", or \"table\"")
        return

    google_news = gnews.GNews(max_results=limit)
    articles = google_news.get_news_by_location(location)

    if not articles:
        typer.echo(f"No articles found for the location \"{location}\".")
        return

    format_result(articles, format, f"location_{location}")

if __name__ == "__main__":
    app()
