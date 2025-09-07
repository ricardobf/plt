# import pytest
# from unittest.mock import MagicMock
# from plt.bitbucket.bitbucket import Bitbucket, BitbucketError


# # ----------------- Fixtures -----------------

# @pytest.fixture
# def mock_session():
#     return MagicMock()


# @pytest.fixture
# def repo(mock_session):
#     return Repository(mock_session, "https://api.bitbucket.org/2.0")


# @pytest.fixture
# def project(mock_session):
#     return Project(mock_session, "https://api.bitbucket.org/2.0")


# @pytest.fixture
# def workspace(mock_session):
#     return Workspace(mock_session, "https://api.bitbucket.org/2.0")


# # ----------------- Repository Tests -----------------

# def test_repository_create_success(repo, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 201
#     mock_response.json.return_value = {"slug": "test-repo"}
#     mock_session.post.return_value = mock_response

#     result = repo.create("workspace1", "test-repo", project_key="PRJ")
#     assert result["slug"] == "test-repo"
#     mock_session.post.assert_called_once()


# def test_repository_create_failure(repo, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 400
#     mock_response.text = "Bad Request"
#     mock_session.post.return_value = mock_response

#     with pytest.raises(RepositoryError):
#         repo.create("workspace1", "fail-repo")


# def test_repository_delete_success(repo, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 204
#     mock_session.delete.return_value = mock_response

#     result = repo.delete("workspace1", "test-repo")
#     assert "deleted successfully" in result


# def test_repository_delete_failure(repo, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 404
#     mock_response.text = "Not Found"
#     mock_session.delete.return_value = mock_response

#     with pytest.raises(RepositoryError):
#         repo.delete("workspace1", "fail-repo")


# def test_repository_list_user_permissions_success(repo, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {"values": [{"user": "user1", "permission": "admin"}]}
#     mock_session.get.return_value = mock_response

#     result = repo.list_user_permissions("workspace1", "test-repo")
#     assert result["values"][0]["user"] == "user1"


# def test_repository_grant_user_permission_success(repo, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 201
#     mock_response.json.return_value = {"user": "user1", "permission": "write"}
#     mock_session.put.return_value = mock_response

#     result = repo.grant_user_permission("workspace1", "test-repo", "user1-uuid", "write")
#     assert result["permission"] == "write"


# def test_repository_revoke_user_permissions_success(repo, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 204
#     mock_session.delete.return_value = mock_response

#     result = repo.revoke_user_permissions("workspace1", "test-repo", "user1-uuid")
#     assert "revoked successfully" in result


# # ----------------- Project Tests -----------------

# def test_project_create_success(project, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 201
#     mock_response.json.return_value = {"key": "PRJ"}
#     mock_session.post.return_value = mock_response

#     result = project.create("workspace1", "New Project")
#     assert result["key"] == "PRJ"


# def test_project_create_failure(project, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 400
#     mock_response.text = "Bad Request"
#     mock_session.post.return_value = mock_response

#     with pytest.raises(ProjectError):
#         project.create("workspace1", "Fail Project")


# def test_project_list_success(project, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {"values": [{"key": "PRJ1"}, {"key": "PRJ2"}]}
#     mock_session.get.return_value = mock_response

#     result = project.list("workspace1")
#     assert len(result["values"]) == 2


# # ----------------- Workspace Tests -----------------

# def test_workspace_get_success(workspace, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 200
#     mock_response.json.return_value = {"name": "My Workspace"}
#     mock_session.get.return_value = mock_response

#     result = workspace.get("workspace1")
#     assert result["name"] == "My Workspace"


# def test_workspace_get_failure(workspace, mock_session):
#     mock_response = MagicMock()
#     mock_response.status_code = 404
#     mock_response.text = "Not Found"
#     mock_session.get.return_value = mock_response

#     with pytest.raises(WorkspaceError):
#         workspace.get("unknown-workspace")

