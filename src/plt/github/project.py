class ProjectError(Exception):
  pass

class Project:
  def __init__(self):
    self.base_url = "https://api.github.com"
    self.auth = ("username", "token")

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
