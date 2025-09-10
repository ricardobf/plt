import logging
from .vcs_provider import VCSProvider
from .bitbucket.bitbucket import Bitbucket


class BitbucketProvider(VCSProvider):
    """Provider for Bitbucket VCS operations."""

    def __init__(self):
        self.bitbucket = Bitbucket()

    def list(self, resource, args):
        if resource == "repository":
            if args.user_permissions:
                logging.debug(f"Listing user permissions for repository: {args.repo}")
                return self.bitbucket.repository.list_user_permissions(
                    args.workspace, args.repo
                )
        elif resource == "project":
            if args.user_permissions:
                logging.debug(f"Listing user permissions for project: {args.project}")
                return self.bitbucket.project.list_user_permissions(
                    args.workspace, args.project
                )
            logging.debug(f"Listing projects for workspace: {args.workspace}")
            return self.bitbucket.project.list(args.workspace)
        elif resource == "workspace":
            logging.debug(f"Listing user permissions for workspace: {args.workspace}")
            return self.bitbucket.workspace.list_user_permissions(args.workspace)
        else:
            logging.error(f"Unknown resource: {resource}")
            return None

    def create(self, resource, args):
        if resource == "repository":
            logging.debug(f"Creating repository: {args.repo}")
            return self.bitbucket.repository.create(
                workspace=args.workspace,
                repo=args.repo,
                project=args.project,
                is_private=args.is_private,
                description=args.description,
            )
        elif resource == "project":
            logging.debug(f"Creating project: {args.project}")
            return self.bitbucket.project.create(
                workspace=args.workspace, project=args.project
            )
        else:
            logging.error(f"Unknown resource: {resource}")
            return None

    def delete(self, resource, args):
        if resource == "repository":
            logging.debug(f"Deleting repository: {args.repo}")
            return self.bitbucket.repository.delete(
                workspace=args.workspace, repo=args.repo
            )
        elif resource == "project":
            logging.debug(f"Deleting project: {args.project}")
            return self.bitbucket.project.delete(
                workspace=args.workspace, project=args.project
            )
        else:
            logging.error(f"Unknown resource: {resource}")
            return None

    def grant(self, resource, args):
        if resource == "repository":
            logging.debug(
                f"Granting permission for user {args.user_uuid} on repository: {args.repo}"
            )
            return self.bitbucket.repository.grant_user_permission(
                workspace=args.workspace,
                repo=args.repo,
                user_uuid=args.user_uuid,
                permission=args.permission,
            )
        elif resource == "project":
            logging.debug(
                f"Granting permission for user {args.user_uuid} on project: {args.project}"
            )
            return self.bitbucket.project.grant_user_permission(
                workspace=args.workspace,
                project=args.project,
                user_uuid=args.user_uuid,
                permission=args.permission,
            )
        else:
            logging.error(f"Unknown resource: {resource}")
            return None

    def revoke(self, resource, args):
        if resource == "repository":
            logging.debug(
                f"Revoking permission for user {args.user_uuid} on repository: {args.repo}"
            )
            return self.bitbucket.repository.revoke_user_permissions(
                workspace=args.workspace, repo=args.repo, user_uuid=args.user_uuid
            )
        elif resource == "project":
            logging.debug(
                f"Revoking permission for user {args.user_uuid} on project: {args.project}"
            )
            return self.bitbucket.project.revoke_user_permissions(
                workspace=args.workspace, project=args.project, user_uuid=args.user_uuid
            )
        else:
            logging.error(f"Unknown resource: {resource}")
            return None

    def configure_branch_permissions(self, resource, args):
        if resource == "repository":
            logging.debug(
                f"Configuring branch permissions for user(s) {args.exempt_users} on repository: {args.repo}"
            )
            return self.bitbucket.repository.configure_branch_permissions(
                workspace=args.workspace,
                repo=args.repo,
                branch=args.branch,
                exempt_users=args.exempt_users,
                exempt_groups=args.exempt_groups,
            )
        else:
            logging.error(f"Unknown resource: {resource}")
            return None
