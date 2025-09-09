from typer.testing import CliRunner
from plt.cli import app

runner = CliRunner()


class TestGitHubIntegration:
    def test_list_repositories_integration(self):
        result = runner.invoke(
            app,
            ["--provider", "github", "--resource", "repository", "--action", "list"],
            env={
                "GITHUB_USERNAME": os.getenv("GITHUB_USERNAME", ""),
                "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN", ""),
            },
        )
        assert result.exit_code == 0
        assert "chat-app" in result.stdout
