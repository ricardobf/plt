from .vcs_provider import VCSProvider
from .github.github import GitHub


class GitHubProvider(VCSProvider):
    """Provider for GitHub VCS operations."""

    def __init__(self):
        self.github = GitHub()

    def list(self, resource, args):
        return self.github.repository.list()

    def create(self, resource, args):
        return self.github.repository.create(
            repo=args.repo, is_private=args.is_private, description=args.description
        )

    def delete(self, resource, args):
        return self.github.repository.delete(repo=args.repo)

    def grant(self, resource, args):
        return None

    def revoke(self, resource, args):
        return None

    def configure_branch_permissions(self, resource, args):
        return None
