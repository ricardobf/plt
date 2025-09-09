from typer.testing import CliRunner
from plt.cli import app

runner = CliRunner()


class TestBitbucketIntegration:
    def test_list_repository_user_permissions_integration(self):
        result = runner.invoke(
            app,
            [
                "--provider",
                "bitbucket",
                "--resource",
                "repository",
                "--action",
                "list",
                "--workspace",
                "plt-workspace",
                "--repo",
                "plt-repo",
                "--user-permissions",
            ],
            env={
                "BITBUCKET_USERNAME": os.getenv("BITBUCKET_USERNAME", ""),
                "BITBUCKET_API_TOKEN": os.getenv("BITBUCKET_API_TOKEN", ""),
            },
        )
        assert result.exit_code == 0
        assert "admin" in result.stdout

    def test_list_projects_integration(self):
        result = runner.invoke(
            app,
            [
                "--provider",
                "bitbucket",
                "--resource",
                "project",
                "--action",
                "list",
                "--workspace",
                "plt-workspace",
            ],
            env={
                "BITBUCKET_USERNAME": os.getenv("BITBUCKET_USERNAME", ""),
                "BITBUCKET_API_TOKEN": os.getenv("BITBUCKET_API_TOKEN", ""),
            },
        )
        assert result.exit_code == 0
        assert "PLT" in result.stdout

    def test_list_project_user_permissions_integration(self):
        result = runner.invoke(
            app,
            [
                "--provider",
                "bitbucket",
                "--resource",
                "project",
                "--action",
                "list",
                "--workspace",
                "plt-workspace",
                "--project",
                "PLT",
                "--user-permissions",
            ],
            env={
                "BITBUCKET_USERNAME": os.getenv("BITBUCKET_USERNAME", ""),
                "BITBUCKET_API_TOKEN": os.getenv("BITBUCKET_API_TOKEN", ""),
            },
        )
        assert result.exit_code == 0

    def test_list_workspace_user_permissions_integration(self):
        result = runner.invoke(
            app,
            [
                "--provider",
                "bitbucket",
                "--resource",
                "workspace",
                "--action",
                "list",
                "--workspace",
                "plt-workspace",
                "--user-permissions",
            ],
            env={
                "BITBUCKET_USERNAME": os.getenv("BITBUCKET_USERNAME", ""),
                "BITBUCKET_API_TOKEN": os.getenv("BITBUCKET_API_TOKEN", ""),
            },
        )
        assert result.exit_code == 0
        assert "Ricardo Barbosa" in result.stdout
        assert "owner" in result.stdout
