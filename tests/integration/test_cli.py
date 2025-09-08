import pytest
from typer.testing import CliRunner
from unittest.mock import patch, MagicMock
from plt.cli import app

runner = CliRunner()


@patch("plt.cli.Bitbucket")
def test_bitbucket_project_list(mock_bitbucket_class):
    mock_bitbucket = MagicMock()
    mock_bitbucket.project.list.return_value = [{"key": "PLT"}]
    mock_bitbucket_class.return_value = mock_bitbucket

    result = runner.invoke(
        app,
        ["bitbucket", "project", "--action", "list", "--workspace", "plt-workspace"],
    )

    assert result.exit_code == 0
    mock_bitbucket.project.list.assert_called_once_with("plt-workspace")
    assert "PLT" in result.output


@patch("plt.cli.GitHub")
def test_github_repository_list(mock_github_class):
    mock_github = MagicMock()
    mock_github.repository.list_repos.return_value = [{"name": "plt-repo"}]
    mock_github_class.return_value = mock_github

    result = runner.invoke(
        app, ["github", "repository", "--action", "list", "--name", "plt-repo"]
    )

    assert result.exit_code == 0
    mock_github.repository.list_repos.assert_called_once_with("plt-repo")
    assert "plt-repo" in result.output
