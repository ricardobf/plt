from .vcs_provider import VCSProvider
from .bitbucket.bitbucket import Bitbucket

class BitbucketProvider(VCSProvider):
    """Provider for Bitbucket VCS operations."""
    def __init__(self):
        self.bitbucket = Bitbucket()

    def list(self):
        if 
        if self.resource == "project":
            return self.bitbucket.project.list(self.workspace)
        else:
            return []

    # def create(self, resource, key, name, is_private=True):
    #     if resource == "project":
    #         return self.bitbucket.project.create(key=key, name=name, is_private=is_private)
    #     elif resource == "repository":
    #         return self.bitbucket.repository.create(key=key, name=name, is_private=is_private)
    #     elif resource == "workspace":
    #         return self.bitbucket.workspace.create(key=key, name=name, is_private=is_private)
    #     else:
    #         return None

    # def delete(self, resource, key):
    #     if resource == "project":
    #         return self.bitbucket.project.delete(key)
    #     elif resource == "repository":
    #         return self.bitbucket.repository.delete(key)
    #     elif resource == "workspace":
    #         return self.bitbucket.workspace.delete(key)
    #     else:
    #         return None

    # def list_repos(self, project_key=None):
    #     return self.bitbucket.repository.list(project_key)

    # def create_repo(self, name, project_key=None, is_private=True, description=None):
    #     return self.bitbucket.repository.create(name=name, project_key=project_key, is_private=is_private, description=description)

    # def delete_repo(self, repo_slug):
    #     return self.bitbucket.repository.delete(repo_slug)

    # def list_user_permissions(self, resource, key=None):
    #     if resource == "project":
    #         return self.bitbucket.project.list_user_permissions(key)
    #     elif resource == "repository":
    #         return self.bitbucket.repository.list_user_permissions(key)
    #     elif resource == "workspace":
    #         return self.bitbucket.workspace.list_user_permissions(key)
    #     else:
    #         return []

    # def grant_user_permission(self, resource, key, user_uuid, permission):
    #     if resource == "project":
    #         return self.bitbucket.project.grant_user_permission(key, user_uuid, permission)
    #     elif resource == "repository":
    #         return self.bitbucket.repository.grant_user_permission(key, user_uuid, permission)

    # def revoke_user_permission(self, resource, key, user_uuid):
    #     if resource == "project":
    #         return self.bitbucket.project.revoke_user_permissions(key, user_uuid)
    #     elif resource == "repository":
    #         return self.bitbucket.repository.revoke_user_permissions(key, user_uuid)

    # def configure_branch_permissions(self, workspace: str, repo_slug: str, branch: str, exempt_users: list[str], exempt_groups: list[str]):
    #     return self.bitbucket.repository.configure_branch_permissions(workspace, repo_slug, branch, exempt_users, exempt_groups)