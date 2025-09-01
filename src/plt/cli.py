import typer
from dotenv import load_dotenv

from plt.bitbucket import BitbucketOAuthClient, BitbucketError
# from plt.github_api import GitHubClient, GitHubError

load_dotenv()

app = typer.Typer(help="plt: Bitbucket & GitHub helper")
bitbucket_app = typer.Typer(help="Bitbucket commands")
# github_app = typer.Typer(help="GitHub commands")
app.add_typer(bitbucket_app, name="bitbucket")
# app.add_typer(github_app, name="github")

# Bitbucket - Create Project
@bitbucket_app.command("create-project")
def create_project(
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace"),
  key: str = typer.Option(..., "--key", help="Project key"),
  name: str = typer.Option(..., "--name", help="Project name"),
  is_private: bool = typer.Option(True, "--is-private", help="Make project private"),
):
  client = BitbucketOAuthClient()
  try:
    result = client.create_project(workspace, key, name, is_private)
    typer.echo(result)
  except BitbucketError as e:
    typer.echo(str(e))

# Bitbucket - Create Repository
@bitbucket_app.command("create-repo")
def create_repo(
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace"),
  repo: str = typer.Option(..., "--repo", help="Repository slug"),
  project_key: str = typer.Option(None, "--project-key", help="Project key"),
  description: str = typer.Option(None, "--description", help="Repository description"),
  is_private: bool = typer.Option(True, "--is-private", help="Make repository private"),
):
  client = BitbucketOAuthClient()
  try:
    result = client.create_repository(workspace, repo, project_key, is_private, description=description)
    typer.echo(result)
  except BitbucketError as e:
    typer.echo(str(e))

# Bitbucket - Grant User Permission
@bitbucket_app.command("grant-user")
def grant_user(
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace"),
  repo: str = typer.Option(..., "--repo", help="Repository slug"),
  user_uuid: str = typer.Option(..., "--user-uuid", help="User UUID"),
  permission: str = typer.Option("write", "--permission", help="Repository permission"),
):
  client = BitbucketOAuthClient()
  try:
    result = client.add_repo_user_permission(workspace, repo, user_uuid, permission)
    typer.echo(result)
  except BitbucketError as e:
    typer.echo(str(e))

# Bitbucket - Revoke User Permission
@bitbucket_app.command("revoke-user")
def revoke_user(
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace"),
  repo: str = typer.Option(..., "--repo", help="Repository slug"),
  user_uuid: str = typer.Option(..., "--user-uuid", help="User UUID"),
):
  client = BitbucketOAuthClient()
  try:
    result = client.remove_repo_user_permission(workspace, repo, user_uuid)
    typer.echo(result)
  except BitbucketError as e:
    typer.echo(str(e))

# Bitbucket - Add Branch Restriction
@bitbucket_app.command("add-branch-restriction")
def add_branch_restriction(
  workspace: str = typer.Option(..., "--workspace", help="Bitbucket workspace"),
  repo: str = typer.Option(..., "--repo", help="Repository slug"),
  kind: str = typer.Option(..., "--kind", help="Restriction kind"),
  pattern: str = typer.Option(..., "--pattern", help="Branch pattern"),
  users: str = None
):
  client = BitbucketOAuthClient()
  users_list = users.split(",") if users else None
  try:
    result = client.create_branch_restriction(workspace, repo, kind, pattern, users_list)
    typer.echo(result)
  except BitbucketError as e:
    typer.echo(str(e))

if __name__ == "__main__":
  app()
