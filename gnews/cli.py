import typer
import gnews
from typing_extensions import Annotated
import json
from tabulate import tabulate

app = typer.Typer()

def format_result(results: list | list[dict[str, any]], format: str):
    if format == "json":
        print(json.dumps(results))
    elif format == "csv":
        header = "title,description,published_date,url,publisher,publisher_href\n"
        csv = header + ""
        for article in results:
            csv += article["title"] + "," + article["description"] + "," + f"\"{article['published date']}\""
            csv += "," + article["url"] + "," + article["publisher"]["title"] + "," + article["publisher"]["href"]
            csv += "\n"
        print(csv)
    else:
        #table format
        headers = ["Title", "Description", "Published Date", "Url", "Publisher", "Publisher Href"]
        data = []
        for article in results:
            new_data = []
            new_data.append(article["title"])
            new_data.append(article["description"])
            new_data.append(article["published date"])
            new_data.append(article["url"])
            new_data.append(article["publisher"]["title"])
            new_data.append(article["publisher"]["href"])
            data.append(new_data)
        
        print(tabulate(data, headers=headers, tablefmt="grid", missingval="?"))


@app.command()
def search(
    keyword: Annotated[str, typer.Argument()], 
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")] = 100,
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
    ):
    if format not in ["json", "csv", "table"]:
        typer.echo("Format should be one of these three options: \"json\", \"csv\", or \"table\"") 
        return

    google_news = gnews.GNews(max_results=limit)
    articles = google_news.get_news(keyword)

    if len(articles) == 0:
        typer.echo(f"No articles were found for the keyword \"{keyword}\".")
        return
    
    return format_result(articles, format)

@app.command()
def trending(
    country: Annotated[str, typer.Option(help="The country from which to get trending news from")] = "US",
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")] = 100,
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
    ):
    pass

@app.command()
def topic(
    topic: Annotated[str, typer.Argument(help="What topic to get news related to")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")] = 100,
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
    ):
    # check if topic is in 
    pass

@app.command()
def location(
    location: Annotated[str, typer.Argument(help="Where news received will be related to.")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")] = 100,
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
    ):
    pass

if __name__ == "__main__":
    app()