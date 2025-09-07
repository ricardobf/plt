class RepositoryError(Exception):
  pass

class Repository:
  def __init__(self, session, base_url, username):
    self.session = session
    self.base_url = base_url
    self.username = username

  def list_repos(self, name, type=None):
    """List repositories for the authenticated user, optionally filtering by name and type"""
    url = f"{self.base_url}/users/{self.username}/repos"
    params = {}
    if name:
      params["name"] = name
    if type:
      params["type"] = type
    response = self.session.get(url, params=params)
    if response.status_code != 200:
      raise RepositoryError(f"Failed to list repositories: {response.text}")
    return response.json()

  def create_repo(self, name, private=True, description=None):
    """Create a new repository for the authenticated user"""
    url = f"{self.base_url}/user/repos"
    data = {
      "name": name,
      "private": private,
      "description": description
    }
    response = self.session.post(url, json=data)
    if response.status_code != 201:
      raise RepositoryError(f"Failed to create repository: {response.text}")
    return response.json()

  def delete_repo(self, name):
    """Delete a repository for the authenticated user"""
    url = f"{self.base_url}/repos/{self.username}/{name}"
    response = self.session.delete(url)
    if response.status_code != 204:
      raise RepositoryError(f"Failed to delete repository: {response.text}")
    return {"message": "Repository deleted successfully"}