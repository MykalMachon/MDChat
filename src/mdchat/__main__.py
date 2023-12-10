from mdchat import cli, __app_name__
from mdchat.config import init_app


def main():
    """This is the main entrypoint into the app"""
    init_app()
    cli.app(prog_name=__app_name__)
    pass


if __name__ == "__main__":
    main()
