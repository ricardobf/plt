# import pytest
# from typer.testing import CliRunner
# from unittest.mock import patch, MagicMock

# from plt.cli import app

# runner = CliRunner()


# @pytest.fixture
# def mock_bitbucket_provider():
#     with patch("plt.cli.BitbucketProvider") as MockProvider:
#         instance = MockProvider.return_value
#         instance.list.return_value = ["project1", "project2"]
#         instance.create.return_value = "created"
#         instance.delete.return_value = "deleted"
#         instance.grant.return_value = "granted"
#         instance.revoke.return_value = "revoked"
#         instance.configure_branch_permissions.return_value = "configured"
#         yield instance


# @pytest.fixture
# def mock_github_provider():
#     with patch("plt.cli.GitHubProvider") as MockProvider:
#         instance = MockProvider.return_value
#         instance.list.return_value = ["repo1", "repo2"]
#         instance.create.return_value = "created"
#         instance.delete.return_value = "deleted"
#         instance.grant.return_value = "granted"
#         instance.revoke.return_value = "revoked"
#         instance.configure_branch_permissions.return_value = "configured"
#         yield instance


# def test_bitbucket_list(mock_bitbucket_provider):
#     result = runner.invoke(
#         app,
#         [
#             "plt",
#             "--provider",
#             "bitbucket",
#             "--resource",
#             "project",
#             "--action",
#             "list",
#         ],
#     )
#     assert result.exit_code == 0
#     assert "project1" in result.output
#     assert "project2" in result.output


# def test_github_list(mock_github_provider):
#     result = runner.invoke(
#         app,
#         [
#             "plt",
#             "--provider",
#             "github",
#             "--resource",
#             "repository",
#             "--action",
#             "list",
#         ],
#     )
#     assert result.exit_code == 0
#     assert "repo1" in result.output
#     assert "repo2" in result.output


# def test_create_action(mock_bitbucket_provider):
#     result = runner.invoke(
#         app,
#         [
#             "plt",
#             "--provider",
#             "bitbucket",
#             "--resource",
#             "project",
#             "--action",
#             "create",
#             "--project",
#             "new_project",
#         ],
#     )
#     assert result.exit_code == 0
#     assert "created" in result.output


# def test_invalid_provider():
#     result = runner.invoke(
#         app,
#         [
#             "plt",
#             "--provider",
#             "unknown",
#             "--resource",
#             "project",
#             "--action",
#             "list",
#         ],
#     )
#     assert result.exit_code != 0
#     assert "Unknown provider: unknown" in result.output
