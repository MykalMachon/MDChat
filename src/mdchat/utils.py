import re
from pathlib import Path

valid_openai_models = [
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-16k",
    "gpt-4",
]


def validate_openai_model(model):
    """
    validate the general format of an openai model.
    does not garuntee that the model is valid.
    """
    if model is None:
        return False
    if model not in valid_openai_models:
        return False
    return True


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
