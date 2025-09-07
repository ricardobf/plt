import typer
from typing_extensions import Annotated

from plt.bitbucket.bitbucket import Bitbucket, BitbucketError
from plt.github.github import GitHub, GitHubError

app = typer.Typer(help="PLT Challenge: VCS management CLI")

bitbucket_app = typer.Typer(help="Bitbucket commands")
github_app = typer.Typer(help="GitHub commands")
app.add_typer(bitbucket_app, name="bitbucket")
app.add_typer(github_app, name="github")

# Bitbucket - Project
@bitbucket_app.command("project")
def project(
  action: str = typer.Option(..., "--action", help="Action to perform (create, delete)"),
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace"),
  key: Annotated[str, typer.Option(help="Project key")] = "",
  name: Annotated[str, typer.Option(help="Project name")] = "",
  is_private: Annotated[bool, typer.Option(help="Make project private")] = True,
  user_uuid: Annotated[str | None, typer.Option(help="User UUID")] = None,
  permission: Annotated[str | None, typer.Option(help="Project permission")] = None
):
  bitbucket = Bitbucket()
  try:
    if action == "list":
        result = bitbucket.project.list(workspace)
        typer.echo(result)
    elif action == "create":
        result = bitbucket.project.create(workspace, key, name, is_private)
        typer.echo(result)
    elif action == "delete":
        result = bitbucket.project.delete(workspace, key)
        typer.echo(result)
    elif action == "list-user-permissions":
        result = bitbucket.project.list_user_permissions(workspace, key)
        typer.echo(result)
    elif action == "grant-user-permission":
        result = bitbucket.project.grant_user_permission(workspace, key, user_uuid, permission)
        typer.echo(result)
    elif action == "revoke-user-permissions":
        result = bitbucket.project.revoke_user_permissions(workspace, key, user_uuid)
        typer.echo(result)
    else:
        typer.echo(f"Action '{action}' not supported.")
  except BitbucketError as e:
    typer.echo(str(e))

# Bitbucket - Repository
@bitbucket_app.command("repository")
def repository(
  action: str = typer.Option(..., "--action", help="Action to perform (create, delete)"),
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace"),
  key: Annotated[str, typer.Option(help="Repository slug")] = "",
  project_key: Annotated[str | None, typer.Option(help="Project key")] = None,
  description: Annotated[str | None, typer.Option(help="Repository description")] = None,
  is_private: Annotated[bool, typer.Option(help="Make repository private")] = True,
  user_uuid: Annotated[str | None, typer.Option(help="User UUID")] = None,
  permission: Annotated[str | None, typer.Option(help="Repository permission")] = None
):
  bitbucket = Bitbucket()
  try:
    if action == "create":
      result = bitbucket.repository.create(workspace, key, project_key, is_private, description)
      typer.echo(result)
    elif action == "delete":
      result = bitbucket.repository.delete(workspace, key)
      typer.echo(result)
    elif action == "list-user-permissions":
      result = bitbucket.repository.list_user_permissions(workspace, key)
      typer.echo(result)
    elif action == "grant-user-permission":
      result = bitbucket.repository.grant_user_permission(workspace, key, user_uuid, permission)
      typer.echo(result)
    elif action == "revoke-user-permissions":
      result = bitbucket.repository.revoke_user_permissions(workspace, key, user_uuid)
      typer.echo(result)
    else:
      typer.echo(f"Action '{action}' not supported.")
  except BitbucketError as e:
    typer.echo(str(e))

# Bitbucket - Workspace
@bitbucket_app.command("workspace")
def workspace(
  action: str = typer.Option(..., "--action", help="Action to perform (list-permissions)"),
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace")
):
  bitbucket = Bitbucket()
  try:
    if action == "list-user-permissions":
      result = bitbucket.workspace.list_user_permissions(workspace)
      typer.echo(result)
    else:
      typer.echo(f"Action '{action}' not supported.")
  except BitbucketError as e:
    typer.echo(str(e))

# GitHub - Repository
@github_app.command("repository")
def repository(
  action: str = typer.Option(..., "--action", help="Action to perform (create, delete)"),
  name: Annotated[str, typer.Option(help="Repository name")] = "",
  description: Annotated[str | None, typer.Option(help="Repository description")] = None,
  is_private: Annotated[bool, typer.Option(help="Make repository private")] = True
):
  client = GitHub()
  try:
    if action == "list":
      result = client.repository.list_repos(name)
      typer.echo(result)
    elif action == "create":
      result = client.repository.create_repo(name, description, is_private)
      typer.echo(result)
    elif action == "delete":
      result = client.repository.delete_repo(name)
      typer.echo(result)
    else:
      typer.echo(f"Action '{action}' not supported.")
  except GitHubError as e:
    typer.echo(str(e))
