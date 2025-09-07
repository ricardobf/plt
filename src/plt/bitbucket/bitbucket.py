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
    self.client_id = Settings.BITBUCKET_CLIENT_ID
    self.client_secret = Settings.BITBUCKET_CLIENT_SECRET

    if not self.client_id or not self.client_secret:
      raise BitbucketError("BITBUCKET_CLIENT_ID or BITBUCKET_CLIENT_SECRET not set")

    self.session = requests.Session()
    self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    self._authenticate()
    self.project = Project(self.session, self.base_url)
    self.repository = Repository(self.session, self.base_url)
    self.workspace = Workspace(self.session, self.base_url)

  # Authenticate with Bitbucket API
  def _authenticate(self):
    url = "https://bitbucket.org/site/oauth2/access_token"
    r = requests.post(
      url,
      auth=HTTPBasicAuth(self.client_id, self.client_secret),
      data={"grant_type": "client_credentials"}
    )
    if r.status_code != 200:
      raise BitbucketError(f"Error fetching token: {r.status_code} {r.text}")
    data = r.json()
    access_token = data["access_token"]
    self.session.headers.update({"Authorization": f"Bearer {access_token}"})
