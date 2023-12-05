"""
cli.py is the primary entrypoint into this app.
it uses the typer library to create a CLI interface

the CLI interface will allow you to:
- set your note directory 
- set the active large language model used for generating responses
- query your notes and get a response with sources 

docs: https://typer.tiangolo.com/
"""
from typing import Optional
from notechat import __app_name__, __version__

import typer

app = typer.Typer()

def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.callback()
def main(version: bool = typer.Option(None, "--version", "-v", is_eager=True, help="Print the version and exit", callback=version_callback)):
    """
    Main function to handle version flag.
    """
    if version:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.command()
def config(): 
    """
    Configure NoteChat settings.
    """
    typer.echo("config: todo")
    typer.Exit()

@app.command()
def chat():
    """
    Chat with your notes.
    """
    typer.echo("query: todo")
    typer.Exit()