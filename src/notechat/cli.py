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
import re
import os

from notechat import __app_name__, __version__
from notechat.config import set_config, get_config, CONFIG_DIR_PATH
from notechat.chatbot import Chatbot

app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"{__app_name__} version {__version__}")
        raise typer.Exit()


def validate_open_ai_key(api_key):
    if api_key is None:
        return False
    pattern = r"sk-[A-Za-z0-9_-]{32}"
    return re.match(pattern, api_key) is not None


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
    Configure NoteChat settings.
    """

    # select a valid notes folder
    notes_folder = None
    while notes_folder is None:
        notes_folder = typer.prompt("Enter your notes folder")
        if not os.path.exists(notes_folder):
            typer.echo("Invalid notes folder. try again.")
            notes_folder = None

    set_config("note_path", notes_folder)

    # select a valid OpenAI API Key
    open_ai_key = None
    while not validate_open_ai_key(open_ai_key):
        if open_ai_key is not None:
            typer.echo("Invalid API Key. try again.")
        open_ai_key = typer.prompt("Enter your OpenAI API Key")

    set_config("open_ai_key", open_ai_key)

    # select a valid OpenAI LLM
    open_ai_model = None
    valid_open_ai_models = ["gpt-3.5-turbo", "gpt-4"]
    while open_ai_model not in valid_open_ai_models:
        if open_ai_model is not None:
            typer.echo(f"Invalid model: {open_ai_model}. try again.")
        open_ai_model = typer.prompt(
            f"Enter your OpenAI model ({', '.join(valid_open_ai_models)})"
        )

    set_config("open_ai_model", open_ai_model)

    typer.echo("config: done")
    typer.Exit()


@app.command()
def chat(question: str):
    """
    Chat with your notes.
    """
    typer.echo("loading...\n")
    bot = Chatbot(
        notes_folder=get_config("note_path"),
        db_path=CONFIG_DIR_PATH,
        open_ai_key=get_config("open_ai_key"),
        open_ai_model=get_config("open_ai_model"),
    )
    result = bot.query(question)
    typer.echo(result.get("answer"))
    typer.echo(result.get("sources", "no sources found with this information"))
    typer.Exit()
