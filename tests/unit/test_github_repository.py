import pytest
from unittest.mock import Mock
from plt.github.repository import Repository, RepositoryError


@pytest.fixture
def mock_session():
    return Mock()


@pytest.fixture
def github_repo(mock_session):
    return Repository(
        session=mock_session,
        base_url="https://github.api.com",
        username="ricardobarbosa",
    )


class TestGitHubRepository:
    def test_list_repos_success(self, github_repo, mock_session):
        mock_session.get.return_value.status_code = 200
        mock_session.get.return_value.json.return_value = [
            {"name": "plt-repo-1"},
            {"name": "plt-repo-2"},
        ]

        result = github_repo.list_repos(name="plt-repo-1")

        mock_session.get.assert_called_once_with(
            "https://github.api.com/users/ricardobarbosa/repos",
            params={"name": "plt-repo-1"},
        )
        assert result == [{"name": "plt-repo-1"}, {"name": "plt-repo-2"}]

    def test_list_repos_failure(self, github_repo, mock_session):
        mock_session.get.return_value.status_code = 500
        mock_session.get.return_value.text = "Internal Server Error"

        with pytest.raises(
            RepositoryError, match="Failed to list repositories: Internal Server Error"
        ):
            github_repo.list_repos(name="plt-repo-1")

    def test_create_repo_success(self, github_repo, mock_session):
        mock_session.post.return_value.status_code = 201
        mock_session.post.return_value.json.return_value = {"name": "plt-repo"}

        result = github_repo.create_repo(
            name="plt-repo", private=True, description="PLT Repo"
        )

        mock_session.post.assert_called_once_with(
            "https://github.api.com/user/repos",
            json={"name": "plt-repo", "private": True, "description": "PLT Repo"},
        )
        assert result["name"] == "plt-repo"

    def test_create_repo_failure(self, github_repo, mock_session):
        mock_session.post.return_value.status_code = 400
        mock_session.post.return_value.text = "Bad Request"

        with pytest.raises(
            RepositoryError, match="Failed to create repository: Bad Request"
        ):
            github_repo.create_repo(name="plt-repo")

    def test_delete_repo_success(self, github_repo, mock_session):
        mock_session.delete.return_value.status_code = 204

        result = github_repo.delete_repo("plt-repo")

        mock_session.delete.assert_called_once_with(
            "https://github.api.com/repos/ricardobarbosa/plt-repo"
        )
        assert result == {"message": "Repository deleted successfully"}

    def test_delete_repo_failure(self, github_repo, mock_session):
        mock_session.delete.return_value.status_code = 403
        mock_session.delete.return_value.text = "Forbidden"

        with pytest.raises(
            RepositoryError, match="Failed to delete repository: Forbidden"
        ):
            github_repo.delete_repo("plt-repo")
