import typer
from typing_extensions import Annotated
from gnews.utils.constants import AVAILABLE_COUNTRIES, AVAILABLE_LANGUAGES, SECTIONS, TOPICS, BASE_URL, USER_AGENT

app = typer.Typer()

@app.command()
def search(
    keyword: Annotated[str, typer.Argument()], 
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")],
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
    ):
    pass

@app.command()
def trending(
    country: Annotated[str, typer.Option(help="The country from which to get trending news from")] = "US"
    ):
    pass

@app.command()
def topic(
    topic: Annotated[str, typer.Argument(help="What topic to get news related to")],
    limit: Annotated[int, typer.Option(help="Limit the number of articles received")],
    ):
    # check if topic is in 
    pass

@app.command()
def location(
    location: Annotated[str, typer.Argument(help="Where news received will be related to.")],
    format: Annotated[str, typer.Option(help="Determine the format of output (json, csv, table)")] = "json"
    ):
    pass

if __name__ == "__main__":
    app()