import pytest
from unittest.mock import Mock
from plt.bitbucket.project import Project, ProjectError


@pytest.fixture
def mock_session():
    return Mock()


@pytest.fixture
def project(mock_session):
    return Project(session=mock_session, base_url="https://bitbucket.api.com")


class TestProject:
    def test_list_success(self, project, mock_session):
        mock_session.get.return_value.status_code = 200
        mock_session.get.return_value.json.return_value = {"projects": []}

        result = project.list("plt-workspace")

        mock_session.get.assert_called_once_with(
            "https://bitbucket.api.com/workspaces/plt-workspace/projects/"
        )
        assert result == {"projects": []}

    def test_list_failure(self, project, mock_session):
        mock_session.get.return_value.status_code = 500
        mock_session.get.return_value.text = "Internal Server Error"

        with pytest.raises(ProjectError, match="Error listing projects: 500"):
            project.list("plt-workspace")

    def test_create_success(self, project, mock_session):
        mock_session.post.return_value.status_code = 201
        mock_session.post.return_value.json.return_value = {"key": "PLT", "name": "PLT"}

        result = project.create("plt-workspace", "PLT")

        mock_session.post.assert_called_once_with(
            "https://bitbucket.api.com/workspaces/plt-workspace/projects/",
            json={"key": "PLT", "name": "PLT", "is_private": True},
        )
        assert result["key"] == "PLT"

    def test_create_failure(self, project, mock_session):
        mock_session.post.return_value.status_code = 400
        mock_session.post.return_value.text = "Bad Request"

        with pytest.raises(ProjectError, match="Error creating project: 400"):
            project.create("plt-workspace", "PLT", "PLT Project")

    def test_delete_success(self, project, mock_session):
        mock_session.delete.return_value.status_code = 204

        result = project.delete("plt-workspace", "PLT")

        mock_session.delete.assert_called_once_with(
            "https://bitbucket.api.com/workspaces/plt-workspace/projects/PLT"
        )
        assert result == "Project PLT deleted successfully."

    def test_delete_failure(self, project, mock_session):
        mock_session.delete.return_value.status_code = 404
        mock_session.delete.return_value.text = "Not Found"

        with pytest.raises(ProjectError, match="Error deleting project: 404"):
            project.delete("plt-workspace", "PLT")

    def test_list_user_permissions_success(self, project, mock_session):
        mock_session.get.return_value.status_code = 200
        mock_session.get.return_value.json.return_value = {"permissions": []}

        result = project.list_user_permissions("plt-workspace", "PLT")

        mock_session.get.assert_called_once_with(
            "https://bitbucket.api.com/workspaces/plt-workspace/projects/PLT/permissions-config/users"
        )
        assert result == {"permissions": []}

    def test_grant_user_permission_success(self, project, mock_session):
        mock_session.put.return_value.status_code = 200
        mock_session.put.return_value.json.return_value = {"permission": "admin"}

        result = project.grant_user_permission(
            "plt-workspace", "PLT", "ricardobarbosa", "admin"
        )

        mock_session.put.assert_called_once_with(
            "https://bitbucket.api.com/workspaces/plt-workspace/projects/PLT/permissions-config/users/ricardobarbosa",
            json={"permission": "admin"},
        )
        assert result["permission"] == "admin"

    def test_grant_user_permission_failure(self, project, mock_session):
        mock_session.put.return_value.status_code = 400
        mock_session.put.return_value.text = "Bad Request"

        with pytest.raises(
            ProjectError, match="Error granting user permissions: 400 Bad Request"
        ):
            project.grant_user_permission(
                "plt-workspace", "PLT", "ricardobarbosa", "admin"
            )

    def test_revoke_user_permissions_success(self, project, mock_session):
        mock_session.delete.return_value.status_code = 204

        result = project.revoke_user_permissions(
            "plt-workspace", "PLT", "ricardobarbosa"
        )

        mock_session.delete.assert_called_once_with(
            "https://bitbucket.api.com/workspaces/plt-workspace/projects/PLT/permissions-config/users/ricardobarbosa"
        )
        assert result == "User ricardobarbosa permissions revoked successfully."

    def test_revoke_user_permissions_failure(self, project, mock_session):
        mock_session.delete.return_value.status_code = 404
        mock_session.delete.return_value.text = "Not Found"

        with pytest.raises(ProjectError, match="Error revoking user permissions: 404"):
            project.revoke_user_permissions("plt-workspace", "PLT", "ricardobarbosa")
