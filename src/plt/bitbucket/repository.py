class RepositoryError(Exception):
    pass


class Repository:
    def __init__(self, session, base_url):
        self.session = session
        self.base_url = base_url

    def create(
        self,
        workspace: str,
        repo_slug: str,
        project_key: str | None = None,
        is_private: bool = True,
        scm: str = "git",
        description: str | None = None,
    ):
        """Create a new repository in the specified workspace"""
        url = f"{self.base_url}/repositories/{workspace}/{repo_slug}"
        payload = {"scm": scm, "is_private": is_private, "description": description}
        if project_key:
            payload["project"] = {"key": project_key}
        r = self.session.post(url, json=payload)
        if r.status_code not in (200, 201):
            raise RepositoryError(
                f"Error creating repository: {r.status_code} {r.text}"
            )
        return r.json()

    def delete(self, workspace: str, repo_slug: str):
        """Delete a repository in the specified workspace"""
        url = f"{self.base_url}/repositories/{workspace}/{repo_slug}"
        r = self.session.delete(url)
        if r.status_code != 204:
            raise RepositoryError(
                f"Error deleting repository: {r.status_code} {r.text}"
            )
        return f"Repository {repo_slug} deleted successfully."

    def list_user_permissions(self, workspace: str, repo_slug: str):
        """List all user permissions on a repository in the specified workspace"""
        url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/permissions-config/users"
        r = self.session.get(url)
        if r.status_code != 200:
            raise RepositoryError(
                f"Error listing user permissions: {r.status_code} {r.text}"
            )
        return r.json()

    def grant_user_permission(
        self, workspace: str, repo_slug: str, user_uuid: str, permission: str
    ):
        """Grant a user permission on a repository in the specified workspace"""
        url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/permissions-config/users/{user_uuid}"
        payload = {"permission": permission}
        r = self.session.put(url, json=payload)
        if r.status_code not in (200, 201):
            raise RepositoryError(
                f"Error granting user permission: {r.status_code} {r.text}"
            )
        return r.json()

    def revoke_user_permissions(self, workspace: str, repo_slug: str, user_uuid: str):
        """Revoke a user's permission on a repository in the specified workspace"""
        url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/permissions-config/users/{user_uuid}"
        r = self.session.delete(url)
        if r.status_code != 204:
            raise RepositoryError(
                f"Error revoking user permission: {r.status_code} {r.text}"
            )
        return f"User {user_uuid} permission revoked successfully."

    def list_branch_permissions(self, workspace: str, repo_slug: str):
        """List all branch permissions for a repository in the specified workspace"""
        url = (
            f"{self.base_url}/repositories/{workspace}/{repo_slug}/branch-restrictions"
        )
        r = self.session.get(url)
        if r.status_code != 200:
            raise RepositoryError(
                f"Error listing branch permissions: {r.status_code} {r.text}"
            )
        return r.json()

    def configure_branch_permissions(
        self,
        workspace: str,
        repo_slug: str,
        branch: str = "main",
        exempt_users: list[str] | None = None,
        exempt_groups: list[str] | None = None,
    ):
        """
        Configure branch permissions to exempt certain users from requiring PRs.
        """
        if exempt_users is None:
            exempt_users = []
        if exempt_groups is None:
            exempt_groups = []

        url = (
            f"{self.base_url}/repositories/{workspace}/{repo_slug}/branch-restrictions"
        )

        payload = {
            "kind": "push",
            "pattern": branch,
            "users": [{"type": "user", "uuid": u} for u in exempt_users],
            "groups": [{"type": "group", "slug": g} for g in exempt_groups],
        }

        r = self.session.post(url, json=payload)
        if r.status_code not in (200, 201):
            raise RepositoryError(
                f"Error configuring branch permissions: {r.status_code} {r.text}"
            )
        return r.json()
