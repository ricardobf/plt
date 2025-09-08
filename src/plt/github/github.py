import requests
from requests.auth import HTTPBasicAuth
from plt.config import Settings
from .repository import Repository


class GitHubError(Exception):
    pass


class GitHub:
    def __init__(self):
        self.base_url = "https://api.github.com"
        self.username = Settings.GITHUB_USERNAME
        self.token = Settings.GITHUB_TOKEN

        if not self.username or not self.token:
            raise GitHubError("GITHUB_USERNAME or GITHUB_TOKEN not set")
        self.auth = (self.username, self.token)
        self.session = requests.Session()
        self.session.auth = self.auth

        # self.project = Project(self.session, self.base_url)
        self.repository = Repository(self.session, self.base_url, self.username)
        # self.workspace = Workspace(self.session, self.base_url)
