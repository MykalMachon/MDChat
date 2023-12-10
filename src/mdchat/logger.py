import os
import logging

from mdchat.config import CONFIG_DIR_PATH

# Get the user's home directory
home_dir = CONFIG_DIR_PATH

# Create a logger
logger = logging.getLogger("my_logger")
logger.setLevel(logging.DEBUG)

# Create a file handler
log_file = os.path.join(home_dir, "notepath.log")
file_handler = logging.FileHandler(log_file)

# Create a formatter and add it to the file handler
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger
logger.addHandler(file_handler)
