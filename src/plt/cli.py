import typer
from typing_extensions import Annotated
from .bitbucket_provider import BitbucketProvider
from .github_provider import GitHubProvider
from .args import PLTArgs

app = typer.Typer(help="PLT Challenge: VCS management CLI")


def get_provider(name: str):
    if name == "bitbucket":
        return BitbucketProvider()
    elif name == "github":
        return GitHubProvider()
    else:
        raise ValueError(f"Unknown provider: {name}")


@app.command()
def plt(
    provider: Annotated[
        str, typer.Option(..., "--provider", help="VCS provider (bitbucket, github)")
    ],
    resource: Annotated[
        str,
        typer.Option(
            ..., "--resource", help="Resource type (project, repository, workspace)"
        ),
    ],
    action: Annotated[
        str,
        typer.Option(
            ...,
            "--action",
            help="Action to perform (list, create, delete, grant, revoke, configure-branch-permissions)",
        ),
    ],
    workspace: Annotated[str | None, typer.Option(help="Workspace name")] = None,
    project: Annotated[str | None, typer.Option(help="Project name")] = None,
    repo: Annotated[str | None, typer.Option(help="Repository name")] = None,
    description: Annotated[str | None, typer.Option(help="Description")] = None,
    user_uuid: Annotated[str | None, typer.Option(help="User UUID")] = None,
    exempt_users: Annotated[list[str], typer.Option(help="Exempt users")] = [],
    exempt_groups: Annotated[list[str], typer.Option(help="Exempt groups")] = [],
    is_private: Annotated[bool, typer.Option(help="Is private")] = True,
    user_permissions: Annotated[bool, typer.Option(help="User permissions")] = False,
    permission: Annotated[str | None, typer.Option(help="Permission level")] = None,
    branch: Annotated[str | None, typer.Option(help="Branch name")] = None,
):
    """Main entry point for the PLT CLI."""
    vcs = get_provider(provider)

    args = PLTArgs(
        workspace=workspace,
        project=project,
        repo=repo,
        user_uuid=user_uuid,
        exempt_users=exempt_users,
        exempt_groups=exempt_groups,
        is_private=is_private,
        user_permissions=user_permissions,
        permission=permission,
        branch=branch,
    )

    if action == "list":
        typer.echo(vcs.list(resource, args))
    elif action == "create":
        typer.echo(vcs.create(resource, args))
    elif action == "delete":
        typer.echo(vcs.delete(resource, args))
    elif action == "grant":
        typer.echo(vcs.grant(resource, args))
    elif action == "revoke":
        typer.echo(vcs.revoke(resource, args))
    elif action == "configure-branch-permissions":
        typer.echo(vcs.configure_branch_permissions(resource, args))
    else:
        typer.echo(f"Action '{action}' not supported.")
