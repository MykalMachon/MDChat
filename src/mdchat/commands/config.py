import os

from mdchat.commands import config_prompt
from mdchat.utils import validate_openai_api_key, validate_openai_model, valid_openai_models


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
        f"Enter a valid OpenAI model {', '.join(valid_openai_models)}",
        "Invalid model. Try again.",
        validate_openai_model,
        typer,
    )

    typer.echo("config: done")
    typer.Exit()
