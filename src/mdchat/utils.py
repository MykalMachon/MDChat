import re
from pathlib import Path


# validators
def validate_openai_api_key(api_key):
    """
    validate the general format of an openai api key.
    does not garuntee that the key is valid.
    """
    if api_key is None:
        return False
    pattern = r"sk-[A-Za-z0-9_-]{32}"
    if re.match(pattern, api_key) is None:
        return False
    return True


def validate_markdown_file(file_path):
    """
    validate that a file path is a markdown file.
    """
    if file_path is None:
        return False
    if not Path(file_path).is_file():
        return False
    if Path(file_path).suffix != ".md":
        return False
    return True
