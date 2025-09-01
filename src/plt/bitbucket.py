import os
import requests
from requests.auth import HTTPBasicAuth

class BitbucketError(Exception):
    pass

class BitbucketOAuthClient:
  def __init__(self, client_id: str | None = None, client_secret: str | None = None, base_url: str | None = None):
    self.client_id = client_id or os.environ.get("BITBUCKET_CLIENT_ID")
    self.client_secret = client_secret or os.environ.get("BITBUCKET_CLIENT_SECRET")
    self.base_url = base_url or "https://api.bitbucket.org/2.0"

    if not self.client_id or not self.client_secret:
      raise BitbucketError("BITBUCKET_CLIENT_ID or BITBUCKET_CLIENT_SECRET not set")

    self.session = requests.Session()
    self.session.headers.update({"Accept": "application/json", "Content-Type": "application/json"})
    self._authenticate()

  # Authentication using OAuth2 to retrieve access token
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

  # Create Project
  def create_project(self, workspace: str, key: str, name: str, is_private: bool = True):
    url = f"{self.base_url}/workspaces/{workspace}/projects/"
    payload = {"key": key, "name": name, "is_private": is_private}
    r = self.session.post(url, json=payload)
    if r.status_code not in (200, 201):
      raise BitbucketError(f"Error creating project: {r.status_code} {r.text}")
    return r.json()

  # Create Repository
  def create_repository(self, workspace: str, repo_slug: str, project_key: str | None = None, is_private: bool = True, scm: str = "git", description: str | None = None):
    url = f"{self.base_url}/repositories/{workspace}/{repo_slug}"
    payload = {"scm": scm, "is_private": is_private}
    if project_key:
      payload["project"] = {"key": project_key}
    if description:
      payload["description"] = description
    r = self.session.post(url, json=payload)
    if r.status_code not in (200, 201):
      raise BitbucketError(f"Error creating repository: {r.status_code} {r.text}")
    return r.json()

  # Grant User Permission
  def add_repo_user_permission(self, workspace: str, repo_slug: str, user_uuid: str, permission: str):
    url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/permissions/users/{user_uuid}"
    payload = {"permission": permission}
    r = self.session.put(url, json=payload)
    if r.status_code not in (200, 201):
      raise BitbucketError(f"Error granting user permission: {r.status_code} {r.text}")
    return r.json()

  # Revoke User Permission
  def remove_repo_user_permission(self, workspace: str, repo_slug: str, user_uuid: str):
    url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/permissions/users/{user_uuid}"
    r = self.session.delete(url)
    if r.status_code not in (204, 200):
      raise BitbucketError(f"Error revoking user permission: {r.status_code} {r.text}")
    return r.json()

  # Create Branch Restriction
  def create_branch_restriction(self, workspace: str, repo_slug: str, kind: str, pattern: str, users: list[str] | None = None):
    url = f"{self.base_url}/repositories/{workspace}/{repo_slug}/branch-restrictions"
    payload = {"kind": kind, "pattern": pattern}
    if users:
      payload["users"] = users
    r = self.session.post(url, json=payload)
    if r.status_code not in (200, 201):
      raise BitbucketError(f"Error creating branch restriction: {r.status_code} {r.text}")
    return r.json()
