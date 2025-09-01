import pytest
from typer.testing import CliRunner
from plt.cli import app

runner = CliRunner()

def test_create_project_cli_success(mocker):
  mock_client = mocker.patch("plt.cli.BitbucketOAuthClient")
  instance = mock_client.return_value
  instance.create_project.return_value = {"key": "PLT", "name": "PLT Project"}

  result = runner.invoke(app, [
    "bitbucket", "create-project",
    "--workspace", "plt-workspace",
    "--key", "PLT",
    "--name", "PLT Project",
    "--is-private"
  ])
  assert result.exit_code == 0
  assert "PLT Project" in result.stdout

def test_create_project_cli_error(mocker):
  mock_client = mocker.patch("plt.cli.BitbucketOAuthClient")
  instance = mock_client.return_value
  instance.create_project.side_effect = Exception("Something went wrong")

  result = runner.invoke(app, [
    "bitbucket", "create-project",
    "--workspace", "plt-workspace",
    "--key", "PLT",
    "--name", "PLT Project"
  ])
  assert result.exit_code == 1
