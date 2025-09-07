import os
import requests

class GitHubError(Exception):
  pass

class GitHub:
  def __init__(self):
    self.username = os.environ.get("GITHUB_USERNAME")
    self.token = os.environ.get("GITHUB_TOKEN")
    if not self.username or not self.token:
      raise GitHubError("GITHUB_USERNAME or GITHUB_TOKEN not set")
    self.auth = (self.username, self.token)
    self.base_url = os.environ.get("GITHUB_API_URL", "https://api.github.com")
    self.session = requests.Session()
    self.session.auth = self.auth
