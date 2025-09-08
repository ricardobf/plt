from .vcs_provider import VCSProvider
from .github.github import GitHub

class GitHubProvider(VCSProvider):
    """Provider for GitHub VCS operations."""
    def __init__(self):
        self.github = GitHub()

    # def list_repos(self, project_key=None):
    #     return self.github.repository.list(project_key)

    # def create_repo(self, name, project_key=None, is_private=True, description=None):
    #     return self.github.repository.create(name=name, project_key=project_key, is_private=is_private, description=description)

    # def delete_repo(self, repo_slug):
    #     return self.github.repository.delete(repo_slug)
