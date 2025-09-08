from .vcs_provider import VCSProvider
from .bitbucket.bitbucket import Bitbucket


class BitbucketProvider(VCSProvider):
    """Provider for Bitbucket VCS operations."""

    def __init__(self):
        self.bitbucket = Bitbucket()

    def list(self, resource, args):
        if resource == "repository":
            if args.user_permissions:
                return self.bitbucket.repository.list_user_permissions(
                    args.workspace, args.repo
                )
        elif resource == "project":
            if args.user_permissions:
                return self.bitbucket.project.list_user_permissions(
                    args.workspace, args.project
                )
            return self.bitbucket.project.list(args.workspace)
        elif resource == "workspace":
            return self.bitbucket.workspace.list_user_permissions(args.workspace)
        else:
            return None

    def create(self, resource, args):
        if resource == "repository":
            return self.bitbucket.repository.create(
                workspace=args.workspace,
                repo=args.repo,
                project=args.project,
                is_private=args.is_private,
                description=args.description,
            )
        elif resource == "project":
            return self.bitbucket.project.create(
                workspace=args.workspace, project=args.project
            )
        else:
            return None

    def delete(self, resource, args):
        if resource == "repository":
            return self.bitbucket.repository.delete(
                workspace=args.workspace, repo=args.repo
            )
        elif resource == "project":
            return self.bitbucket.project.delete(
                workspace=args.workspace, project=args.project
            )
        else:
            return None

    def grant(self, resource, args):
        if resource == "repository":
            return self.bitbucket.repository.grant_user_permission(
                workspace=args.workspace,
                repo=args.repo,
                user_uuid=args.user_uuid,
                permission=args.permission,
            )
        elif resource == "project":
            return self.bitbucket.project.grant_user_permission(
                workspace=args.workspace,
                project=args.project,
                user_uuid=args.user_uuid,
                permission=args.permission,
            )
        else:
            return None

    def revoke(self, resource, args):
        if resource == "repository":
            return self.bitbucket.repository.revoke_user_permissions(
                workspace=args.workspace, repo=args.repo, user_uuid=args.user_uuid
            )
        elif resource == "project":
            return self.bitbucket.project.revoke_user_permissions(
                workspace=args.workspace, project=args.project, user_uuid=args.user_uuid
            )
        else:
            return None

    def configure_branch_permissions(self, resource, args):
        if resource == "repository":
            return self.bitbucket.repository.configure_branch_permissions(
                workspace=args.workspace,
                repo=args.repo,
                branch=args.branch,
                exempt_users=args.exempt_users,
                exempt_groups=args.exempt_groups,
            )
        else:
            return None
