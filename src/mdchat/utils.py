import re

# validators 
def validate_open_ai_key(api_key):
    """
    validate the general format of an openai api key.
    does not garuntee that the key is valid.
    """
    if api_key is None:
        return False
    pattern = r"sk-[A-Za-z0-9_-]{32}"
    return re.match(pattern, api_key) is not None