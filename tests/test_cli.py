from typer.testing import CliRunner
from notechat import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert __app_name__ in result.stdout
    assert __version__ in result.stdout