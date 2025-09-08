class RepositoryError(Exception):
    pass


class Repository:
    def __init__(self, session, base_url, username):
        self.session = session
        self.base_url = base_url
        self.username = username

    def list(self):
        """List repositories for the authenticated user"""
        url = f"{self.base_url}/users/{self.username}/repos"
        response = self.session.get(url)
        if response.status_code != 200:
            raise RepositoryError(f"Failed to list repositories: {response.text}")
        return response.json()

    def create(self, repo, is_private=True, description=None):
        """Create a new repository for the authenticated user"""
        url = f"{self.base_url}/user/repos"
        data = {"name": repo, "private": is_private, "description": description}
        response = self.session.post(url, json=data)
        if response.status_code != 201:
            raise RepositoryError(f"Failed to create repository: {response.text}")
        return response.json()

    def delete(self, repo):
        """Delete a repository for the authenticated user"""
        url = f"{self.base_url}/repos/{self.username}/{repo}"
        response = self.session.delete(url)
        if response.status_code != 204:
            raise RepositoryError(f"Failed to delete repository: {response.text}")
        return {"message": "Repository deleted successfully"}
