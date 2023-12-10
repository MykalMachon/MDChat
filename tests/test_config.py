import os
from mdchat import config

def test_init_app():
  config.init_app()
  assert os.path.exists(config.CONFIG_DIR_PATH)
  assert os.path.exists(config.CONFIG_FILE_PATH)

def test_set_config():
  key = "TEST_KEY"
  value = "TEST_VALUE"
  config.set_config(key, value)
  assert config.get_config(key) == value

def test_get_config():
  key = "TEST_KEY"
  value = "TEST_VALUE"
  config.set_config(key, value)
  assert config.get_config(key) == value

def test_check_if_config_exists():
  assert config._check_if_config_exists() == True

def test_init_config_files():
  config._init_config_files()
  assert os.path.exists(config.CONFIG_DIR_PATH)
  assert os.path.exists(config.CONFIG_FILE_PATH)

