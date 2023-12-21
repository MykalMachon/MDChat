"""
Contains the configuration for NoteChat.
All settings should be stored in the user's home directory
at the location ~/.mdchat/config.json. 

idea: store chat history + config in this location via a sqlite db.
"""

import os
import pathlib
import json
import platform

from mdchat.utils import validate_openai_api_key

# TODO: use ~ for home directory on linux/mac, use %USERPROFILE% on windows
NOTE_PATH_DEFAULT = None
if platform.system() == "Windows":
    NOTE_PATH_DEFAULT = os.path.expandvars(r"%USERPROFILE%\Documents")
else:
    NOTE_PATH_DEFAULT = os.path.expanduser("~/notes")

NOTE_PATH = os.getenv("NOTECHAT_NOTE_PATH", "~/notes")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)

CONFIG_DIR_PATH = pathlib.Path.home() / ".mdchat"
CONFIG_FILE_PATH = CONFIG_DIR_PATH / "config.json"


def init_app():
    """Initialize the app"""
    if not _check_if_config_exists():
        _init_config_files()


def set_config(key, value):
    """Set a config value in the json file"""
    with open(CONFIG_FILE_PATH, "r") as config_file:
        config = json.load(config_file)
        config[key] = value
        with open(CONFIG_FILE_PATH, "w") as config_file:
            json.dump(config, config_file)


def get_config(key):
    """Get a config value from the json file"""
    try:
        with open(CONFIG_FILE_PATH, "r") as config_file:
            config = json.load(config_file)
            return config[key]
    except KeyError:
        return None


def _check_if_config_exists():
    """Check if the config file exists"""
    return os.path.exists(CONFIG_FILE_PATH)


def check_if_config_is_valid():
    """Check if the config file is valid"""
    # TODO: generalize validators here and rework config in general
    # config should be more general and easier to extend.
    if not _check_if_config_exists():
        return False
    if get_config("note_path") is None or not os.path.exists(get_config("note_path")):
        return False
    if get_config("open_ai_key") is None or not validate_openai_api_key(
        get_config("open_ai_key")
    ):
        return False
    if get_config("open_ai_model") is None or get_config("open_ai_model") not in [
        "gpt-3.5-turbo",
        "gpt-4",
    ]:
        return False
    return True


def _init_config_files():
    """Initialize the config file"""
    try:
        os.mkdir(CONFIG_DIR_PATH)
    except FileExistsError:
        print("Config directory already exists...")
    try:
        with open(CONFIG_FILE_PATH, "x") as config_file:
            config_file.write("{}")
        set_config("note_path", NOTE_PATH)
        set_config("open_ai_key", OPENAI_API_KEY)
    except FileExistsError:
        print("Config file already exists... moving on...")
    return True
