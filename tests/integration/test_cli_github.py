from typer.testing import CliRunner
from plt.cli import app

runner = CliRunner()


class TestGitHubIntegration:
    def test_list_repositories_integration(self):
        result = runner.invoke(
            app,
            ["--provider", "github", "--resource", "repository", "--action", "list"],
        )
        assert result.exit_code == 0
        assert "chat-app" in result.stdout
