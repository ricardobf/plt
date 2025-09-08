import typer
from typing_extensions import Annotated
from .bitbucket_provider import BitbucketProvider
from .github_provider import GitHubProvider

app = typer.Typer(help="PLT Challenge: VCS management CLI")

providers = ["bitbucket", "github"]


def get_provider(name: str):
    if name == "bitbucket":
        return BitbucketProvider()
    elif name == "github":
        return GitHubProvider()
    else:
        raise ValueError(f"Unknown provider: {name}")

@app.command()
def project(
    provider: Annotated[str, typer.Option(..., "--provider", help=f"VCS provider ({', '.join(providers)})")],
    resource: Annotated[str | None, typer.Option(help="Resource type (project, repository, workspace)")],
    action: str = typer.Option(..., "--action", help="Action to perform (list, create, delete, list-user-permissions, grant-user-permission, revoke-user-permission, configure-branch-permissions)"),
    workspace: Annotated[str | None, typer.Option(help="Workspace name")] = None,
    project: Annotated[str | None, typer.Option(help="Project name")] = None,
    repo: Annotated[str | None, typer.Option(help="Repository name")] = None,
    uuid: Annotated[str | None, typer.Option(help="User UUID")] = None,
    exempt_users: Annotated[list[str], typer.Option(help="Exempt users")] = [],
    exempt_groups: Annotated[list[str], typer.Option(help="Exempt groups")] = [],
    is_private: Annotated[bool, typer.Option(help="Is private")] = True
):
    vcs = get_provider(provider)
    if action == "list":
        typer.echo(vcs.list(resource, workspace))
    # elif action == "create":
    #     typer.echo(vcs.create_project(key=key, name=name, is_private=is_private))
    # elif action == "delete":
    #     typer.echo(vcs.delete_project(key))
    else:
        typer.echo(f"Action '{action}' not supported.")