from mdchat import utils

def test_openai_api_validator():
  bad_openai_key__too_short = "sk-1234567890"
  bad_openai_key__no_sk = "12345678901234567890123456789012"
  assert utils.validate_openai_api_key(bad_openai_key__too_short) == False
  assert utils.validate_openai_api_key(bad_openai_key__no_sk) == False

  good_openai_key = "sk-12345678901234567890123412312312312"
  assert utils.validate_openai_api_key(good_openai_key) == True

def test_markdown_validator():
  bad_markdown_file = "tests/files/bad_markdown.txt"
  assert utils.validate_markdown_file(bad_markdown_file) == False

  good_markdown_file = "tests/files/good_markdown.md"
  assert utils.validate_markdown_file(good_markdown_file) == True