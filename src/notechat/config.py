"""
Contains the configuration for NoteChat.
All settings should be stored in the user's home directory
at the location ~/.notechat/config.json. 

idea: store chat history + config in this location via a sqlite db.
"""

import os 

NOTE_PATH = os.getenv('NOTECHAT_NOTE_PATH', '~/notes')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', None)

def init_app():
    """ Initialize the app"""
    # TODO: create the config file if it doesn't exist
    # TODO: store the notepath in a config location
    pass

def _init_config_file():
    """ Initialize the config file """
    # TODO: create a config file
    pass

