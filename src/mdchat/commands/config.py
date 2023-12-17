import re
import os

from mdchat.config import set_config, get_config

def validate_open_ai_key(api_key):
    if api_key is None:
        return False
    pattern = r"sk-[A-Za-z0-9_-]{32}"
    return re.match(pattern, api_key) is not None

def cli_config(typer): 
    """
    Configure NoteChat settings.
    """

    # select a valid notes folder
    notes_folder = get_config("note_path") or None
    if notes_folder is not None:
        typer.echo(f"Current notes folder: {notes_folder}")
    while notes_folder is None:
        notes_folder = typer.prompt("Enter your notes folder")
        if not os.path.exists(notes_folder):
            typer.echo("Invalid notes folder. try again.")
            notes_folder = None

    set_config("note_path", notes_folder)

    # select a valid OpenAI API Key
    open_ai_key = get_config("open_ai_key") or None
    while not validate_open_ai_key(open_ai_key):
        if open_ai_key is not None:
            typer.echo("Invalid API Key. try again.")
        open_ai_key = typer.prompt("Enter your OpenAI API Key")

    set_config("open_ai_key", open_ai_key)

    # select a valid OpenAI LLM
    open_ai_model = get_config("open_ai_model") or None
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