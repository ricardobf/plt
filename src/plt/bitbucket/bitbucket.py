import requests
from requests.auth import HTTPBasicAuth
from plt.config import Settings
from .project import Project
from .repository import Repository
from .workspace import Workspace


class BitbucketError(Exception):
    pass

class Bitbucket:
    def __init__(self):
        self.base_url = "https://api.bitbucket.org/2.0"
        self.username = Settings.BITBUCKET_USERNAME
        self.api_token = Settings.BITBUCKET_API_TOKEN

        if not self.username or not self.api_token:
            raise BitbucketError(
                "BITBUCKET_USERNAME or BITBUCKET_API_TOKEN not set"
            )

        self.session = requests.Session()
        self.session.headers.update(
            {"Accept": "application/json", "Content-Type": "application/json"}
        )
        self._authenticate()
        self.project = Project(self.session, self.base_url)
        self.repository = Repository(self.session, self.base_url)
        self.workspace = Workspace(self.session, self.base_url)

    def _authenticate(self):
        """Authenticate using Bitbucket App Password"""
        self.session.auth = HTTPBasicAuth(self.username, self.api_token)

