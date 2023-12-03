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
from rptodo import __app_name__, __version__

import typer

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.command()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Print the version and exit",
    ),
):
    """This is the main entrypoint into the app"""
    if note_dir:
        typer.echo(f"Setting note dir to {note_dir}")
    if version:
        typer.echo(f"{__app_name__} version {__version__}")
