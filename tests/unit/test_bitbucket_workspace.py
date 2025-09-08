import pytest
from unittest.mock import Mock
from plt.bitbucket.workspace import Workspace, WorkspaceError


@pytest.fixture
def mock_session():
    return Mock()


@pytest.fixture
def workspace(mock_session):
    return Workspace(session=mock_session, base_url="https://bitbucket.api.com")


class TestWorkspace:
    def test_list_user_permissions_success(self, workspace, mock_session):
        mock_session.get.return_value.status_code = 200
        mock_session.get.return_value.json.return_value = {
            "permissions": ["admin", "write"]
        }

        result = workspace.list_user_permissions("plt-workspace")

        mock_session.get.assert_called_once_with(
            "https://bitbucket.api.com/workspaces/plt-workspace/permissions"
        )
        assert result == {"permissions": ["admin", "write"]}

    def test_list_user_permissions_failure(self, workspace, mock_session):
        mock_session.get.return_value.status_code = 500
        mock_session.get.return_value.text = "Internal Server Error"

        with pytest.raises(
            WorkspaceError,
            match="Error fetching workspace permissions: 500 Internal Server Error",
        ):
            workspace.list_user_permissions("plt-workspace")
