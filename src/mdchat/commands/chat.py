from typer import Typer
from rich import print
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

from mdchat.config import get_config, CONFIG_DIR_PATH, check_if_config_is_valid
from mdchat.chatbot import Chatbot


def cli_show_progress(task_description: str, task_func: callable):
    """Show progress for a task"""
    with Progress(
        SpinnerColumn(),
        TextColumn("[bold green]{task.description}[/bold green]"),
        transient=True,
    ) as progress:
        task = progress.add_task(task_description, total=1)
        ret_val = task_func()
        progress.update(task, advance=1, completed=1)
        return ret_val


def cli_chat_single_file(typer: Typer, file: str):
    """
    This initiates a continious chat with mdchat.
    This is for a single file; not your default notes directory.
    """
    config_valid = check_if_config_is_valid()
    if not config_valid:
        print(f"Config is invalid.\nPlease run [bold blue]mdchat config[/bold blue]")
        typer.Exit()
        return

    bot = cli_show_progress(
        "Indexing your notes...",
        lambda: Chatbot(
            notes_folder=file,
            db_path=CONFIG_DIR_PATH,
            open_ai_key=get_config("open_ai_key"),
            open_ai_model=get_config("open_ai_model"),
        ),
    )

    query = None
    while query != "exit":
        query = typer.prompt("you")
        result = cli_show_progress("Generating a response...", lambda: bot.query(query))
        print(
            Panel.fit(
                f"[bold blue]mdchat[/bold blue]: {result.get('answer', 'no response found')}\n[bold blue]sources[/bold blue]: {result.get('sources', 'no sources found')}",
                title=f"Chatting with \"{file.split('/')[-1]}\"",
            )
        )


def cli_chat(typer: Typer):
    """
    This initiates a continious chat with mdchat.
    It will create a new index from your notes and then allow
    you to chat back and forth in a continious chain.
    """
    # validate that config is valid
    config_valid = check_if_config_is_valid()
    if not config_valid:
        print(f"Config is invalid.\nPlease run [bold blue]mdchat config[/bold blue]")
        typer.Exit()
        return

    # load initial model
    bot = cli_show_progress(
        "Indexing your notes...",
        lambda: Chatbot(
            notes_folder=get_config("note_path"),
            db_path=CONFIG_DIR_PATH,
            open_ai_key=get_config("open_ai_key"),
            open_ai_model=get_config("open_ai_model"),
        ),
    )

    query = None
    while query != "exit":
        query = typer.prompt("you")
        result = cli_show_progress("Generating a response...", lambda: bot.query(query))
        print(
            Panel.fit(
                f"[bold blue]mdchat[/bold blue]: {result.get('answer', 'no response found')}\n[bold blue]sources[/bold blue]: {result.get('sources', 'no sources found')}"
            )
        )
