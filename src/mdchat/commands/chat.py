from typer import Typer
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich import print

from mdchat.config import get_config, CONFIG_DIR_PATH
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


def cli_chat(typer: Typer):
    """
    This initiates a continious chat with mdchat.
    It will create a new index from your notes and then allow
    you to chat back and forth in a continious chain.
    """
    # load initial model
    bot = cli_show_progress(
        "Indexing your notes...",
        lambda: Chatbot(
            notes_folder=get_config("note_path"),
            db_path=CONFIG_DIR_PATH,
            open_ai_key=get_config("open_ai_key"),
            open_ai_model=get_config("open_ai_model"),
            force_new=True,
        ),
    )

    query = None
    while query != "exit":
        query = typer.prompt("you")
        result = cli_show_progress("Generating a response...", lambda: bot.query(query))
        print(f"[bold blue]mdchat[/bold blue]: {result.get('answer', 'no response found')}")
        print(f"[bold blue]sources[/bold blue]: {result.get('sources', 'no sources found')}")
