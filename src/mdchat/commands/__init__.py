# Generic utilities and values for the mdchat bot

import re

from mdchat.config import set_config, get_config

from typer import Typer
from rich import print


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
        print(f":gear: {curr_prompt}: [green]{curr_value}[/green]")
        should_change = typer.confirm("Would you like to change it?", default="n")
        if not should_change:
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
