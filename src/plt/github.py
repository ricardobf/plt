import os
import requests
from github import Auth, Github

class GitHubError(Exception):
  pass

class GitHubOAuthClient:
  def __init__(self):
    self.username = os.environ.get("GITHUB_USERNAME")
    self.token = os.environ.get("GITHUB_TOKEN")
    if not self.username or not self.token:
      raise GitHubError("GITHUB_USERNAME or GITHUB_TOKEN not set")
    self.auth = Auth.Token(self.token)
    self.client = Github(auth=self.auth)
    self.base_url = os.environ.get("GITHUB_API_URL", "https://api.github.com")

  # Create a new project
  def create_project(self, name, body=None, private=True):
    url = f"{self.base_url}/user/projects"
    data = {
      "name": name,
      "body": body,
      "private": private
    }
    response = requests.post(url, json=data, auth=self.auth)
    if response.status_code != 201:
      raise GitHubError(f"Failed to create project: {response.text}")
    return response.json()

  # Create a new repository
  def create_repo(self, name, private=True, description=None):
    url = f"{self.base_url}/user/repos"
    data = {
      "name": name,
      "private": private,
      "description": description
    }
    response = requests.post(url, json=data, auth=self.auth)
    if response.status_code != 201:
      raise GitHubError(f"Failed to create repository: {response.text}")
    return response.json()
