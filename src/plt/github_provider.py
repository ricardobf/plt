import logging
from .vcs_provider import VCSProvider
from .github.github import GitHub


class GitHubProvider(VCSProvider):
    """Provider for GitHub VCS operations."""

    def __init__(self):
        self.github = GitHub()

    def list(self, resource, args):
        logging.debug(f"Listing {resource}")
        return self.github.repository.list()

    def create(self, resource, args):
        logging.debug(f"Creating repository: {args.repo}")
        return self.github.repository.create(
            repo=args.repo, is_private=args.is_private, description=args.description
        )

    def delete(self, resource, args):
        logging.debug(f"Deleting repository: {args.repo}")
        return self.github.repository.delete(repo=args.repo)

    def grant(self, resource, args):
        logging.error("Grant not implemented for this provider.")
        raise NotImplementedError("grant not implemented for this provider")

    def revoke(self, resource, args):
        logging.error("Revoke not implemented for this provider.")
        raise NotImplementedError("revoke not implemented for this provider")

    def configure_branch_permissions(self, resource, args):
        logging.error("Configure branch permissions not implemented for this provider.")
        raise NotImplementedError(
            "configure_branch_permissions not implemented for this provider"
        )
