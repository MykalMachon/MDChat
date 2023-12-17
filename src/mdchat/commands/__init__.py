# Generic utilities and values for the mdchat bot

import re
from mdchat.config import set_config, get_config
from typer import Typer


def validate_open_ai_key(api_key):
    if api_key is None:
        return False
    pattern = r"sk-[A-Za-z0-9_-]{32}"
    return re.match(pattern, api_key) is not None


def config_prompt(
    key: str,
    curr_prompt: str,
    new_prompt: str,
    error_msg: str,
    validate_func=None,
    typer: Typer = None,
):
    """
    Prompt the user to change a config value.
    """
    curr_value = get_config(key)
    if curr_value is not None:
        typer.echo(f"{curr_prompt}: {curr_value}")
        should_change = typer.prompt("Would you like to change it? (y/n)", default="n")
        if should_change == "n":
            return curr_value
    new_value = None
    while new_value is None:
        new_value = typer.prompt(f"{new_prompt}")
        if not validate_func(new_value):
            typer.echo(error_msg)
            new_value = None
        else:
            set_config(key, new_value)
    return new_value