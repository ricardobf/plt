import pytest
from unittest.mock import Mock
from plt.bitbucket.repository import Repository, RepositoryError


@pytest.fixture
def mock_session():
    return Mock()


@pytest.fixture
def repository(mock_session):
    return Repository(session=mock_session, base_url="https://bitbucket.api.com")


class TestRepository:
    def test_create_success(self, repository, mock_session):
        mock_session.post.return_value.status_code = 201
        mock_session.post.return_value.json.return_value = {"name": "plt-repo"}

        result = repository.create("plt-workspace", "plt-repo")

        mock_session.post.assert_called_once_with(
            "https://bitbucket.api.com/repositories/plt-workspace/plt-repo",
            json={"scm": "git", "is_private": True, "description": None},
        )
        assert result["name"] == "plt-repo"

    def test_create_failure(self, repository, mock_session):
        mock_session.post.return_value.status_code = 400
        mock_session.post.return_value.text = "Bad Request"

        with pytest.raises(
            RepositoryError, match="Error creating repository: 400 Bad Request"
        ):
            repository.create("plt-workspace", "plt-repo")

    def test_delete_success(self, repository, mock_session):
        mock_session.delete.return_value.status_code = 204

        result = repository.delete("plt-workspace", "plt-repo")
        assert result == "Repository plt-repo deleted successfully."

    def test_delete_failure(self, repository, mock_session):
        mock_session.delete.return_value.status_code = 404
        mock_session.delete.return_value.text = "Not Found"

        with pytest.raises(
            RepositoryError, match="Error deleting repository: 404 Not Found"
        ):
            repository.delete("plt-workspace", "plt-repo")

    def test_list_user_permissions_success(self, repository, mock_session):
        mock_session.get.return_value.status_code = 200
        mock_session.get.return_value.json.return_value = {"permissions": []}

        result = repository.list_user_permissions("plt-workspace", "plt-repo")

        mock_session.get.assert_called_once_with(
            "https://bitbucket.api.com/repositories/plt-workspace/plt-repo/permissions-config/users"
        )
        assert result == {"permissions": []}

    def test_list_user_permissions_failure(self, repository, mock_session):
        mock_session.get.return_value.status_code = 500
        mock_session.get.return_value.text = "Internal Error"

        with pytest.raises(
            RepositoryError, match="Error listing user permissions: 500 Internal Error"
        ):
            repository.list_user_permissions("plt-workspace", "plt-repo")

    def test_grant_user_permission_success(self, repository, mock_session):
        mock_session.put.return_value.status_code = 200
        mock_session.put.return_value.json.return_value = {"permission": "admin"}

        result = repository.grant_user_permission(
            "plt-workspace", "plt-repo", "ricardobarbosa", "admin"
        )

        mock_session.put.assert_called_once_with(
            "https://bitbucket.api.com/repositories/plt-workspace/plt-repo/permissions-config/users/ricardobarbosa",
            json={"permission": "admin"},
        )
        assert result["permission"] == "admin"

    def test_grant_user_permission_failure(self, repository, mock_session):
        mock_session.put.return_value.status_code = 403
        mock_session.put.return_value.text = "Forbidden"

        with pytest.raises(
            RepositoryError, match="Error granting user permission: 403 Forbidden"
        ):
            repository.grant_user_permission(
                "plt-workspace", "plt-repo", "ricardobarbosa", "admin"
            )

    def test_revoke_user_permissions_success(self, repository, mock_session):
        mock_session.delete.return_value.status_code = 204

        result = repository.revoke_user_permissions(
            "plt-workspace", "plt-repo", "ricardobarbosa"
        )
        assert result == "User ricardobarbosa permission revoked successfully."

    def test_revoke_user_permissions_failure(self, repository, mock_session):
        mock_session.delete.return_value.status_code = 500
        mock_session.delete.return_value.text = "Server Error"

        with pytest.raises(
            RepositoryError, match="Error revoking user permission: 500 Server Error"
        ):
            repository.revoke_user_permissions(
                "plt-workspace", "plt-repo", "ricardobarbosa"
            )
