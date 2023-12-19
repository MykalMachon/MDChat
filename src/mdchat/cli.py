"""
cli.py is the primary entrypoint into this app.
it uses the typer library to create a CLI interface

the CLI interface will allow you to:
- set your note directory 
- set the active large language model used for generating responses
- query your notes and get a response with sources 

docs: https://typer.tiangolo.com/
"""
import typer

from mdchat import __app_name__, __version__
from mdchat.config import set_config, get_config, CONFIG_DIR_PATH
from mdchat.chatbot import Chatbot

from mdchat.commands.config import cli_config
from mdchat.commands.chat import cli_chat

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
    cli_config(typer)


@app.command()
def chat():
    cli_chat(typer)
