import os

from mdchat.commands import config_prompt
from mdchat.utils import validate_openai_api_key


def cli_config(typer):
    """
    Configure NoteChat settings.
    """
    config_prompt(
        "note_path",
        "Your current notes folder is",
        "Enter the path of your notes folder",
        "Invalid notes folder. try again.",
        lambda x: os.path.exists(x),
        typer,
    )
    config_prompt(
        "open_ai_key",
        "Your current OpenAI API Key is",
        "Enter your OpenAI API Key",
        "Invalid API Key. Try again.",
        validate_openai_api_key,
        typer,
    )
    config_prompt(
        "open_ai_model",
        "Your current OpenAI model is",
        "Enter a valid OpenAI model (gpt-3.5-turbo, gpt-4)",
        "Invalid model. Try again.",
        lambda x: x in ["gpt-3.5-turbo", "gpt-4"],
        typer,
    )

    typer.echo("config: done")
    typer.Exit()
