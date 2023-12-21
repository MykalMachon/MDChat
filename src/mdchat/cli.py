"""
cli.py is the primary entrypoint into this app.
it uses the typer library to create a CLI interface

the CLI interface will allow you to:
- set your note directory 
- set the active large language model used for generating responses
- query your notes and get a response with sources 

docs: https://typer.tiangolo.com/
"""
from pathlib import Path

import typer
from typing_extensions import Annotated

from mdchat import __app_name__, __version__
from mdchat.commands.config import cli_config
from mdchat.commands.chat import cli_chat, cli_chat_single_file
from mdchat.utils import validate_markdown_file

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.callback()
def main(
    version: bool = typer.Option(
        None,
        "--version",
        "-v",
        is_eager=True,
        help="Print the version and exit",
        callback=version_callback,
    )
):
    """
    Main function to handle version flag.
    """
    if version:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


@app.command()
def config():
    """
    Configure mdchat settings.
    You can set your default note directory, llm, api keys, and more.
    """
    cli_config(typer)


@app.command()
def chat(
    file: Annotated[
        str, typer.Option("--file", "-f", help="Path to a single file to use as a note")
    ] = None,
):
    """
    Chat with your notes.
    You can pass in a single file to use as a note, or chat with your default note directory.
    """
    if file:
        if not validate_markdown_file(file):
            typer.echo(f"Invalid file, either can't read the file or it does not exist")
            raise typer.Exit()
        cli_chat_single_file(typer, file)
    else:
        cli_chat(typer)
