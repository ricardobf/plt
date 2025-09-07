class ProjectError(Exception):
  pass

class Project:
  def __init__(self, session, base_url):
    self.session = session
    self.base_url = base_url

  def list(self, workspace: str):
    """List all projects in the specified workspace"""
    url = f"{self.base_url}/workspaces/{workspace}/projects/"
    r = self.session.get(url)
    if r.status_code != 200:
      raise ProjectError(f"Error listing projects: {r.status_code} {r.text}")
    return r.json()

  def create(self, workspace: str, key: str, name: str, is_private: bool = True):
    """Create a new project in the specified workspace"""
    url = f"{self.base_url}/workspaces/{workspace}/projects/"
    payload = {"key": key, "name": name, "is_private": is_private}
    r = self.session.post(url, json=payload)
    if r.status_code not in (200, 201):
      raise ProjectError(f"Error creating project: {r.status_code} {r.text}")
    return r.json()

  def delete(self, workspace: str, project_key: str):
    """Delete a project in the specified workspace"""
    url = f"{self.base_url}/workspaces/{workspace}/projects/{project_key}"
    r = self.session.delete(url)
    if r.status_code != 204:
      raise ProjectError(f"Error deleting project: {r.status_code} {r.text}")
    return f"Project {project_key} deleted successfully."

  def list_user_permissions(self, workspace: str, project_key: str):
    """List all user permissions for a project in the specified workspace"""
    url = f"{self.base_url}/workspaces/{workspace}/projects/{project_key}/permissions-config/users"
    r = self.session.get(url)
    if r.status_code != 200:
      raise ProjectError(f"Error listing user permissions: {r.status_code} {r.text}")
    return r.json()

  def grant_user_permission(self, workspace: str, project_key: str, user_uuid: str, permission: str):
    """Grant user permissions for a project in the specified workspace"""
    url = f"{self.base_url}/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{user_uuid}"
    payload = {"permission": permission}
    r = self.session.put(url, json=payload)
    if r.status_code != 200:
      raise ProjectError(f"Error granting user permissions: {r.status_code} {r.text}")
    return r.json()

  def revoke_user_permissions(self, workspace: str, project_key: str, user_uuid: str):
    """Revoke user permissions for a project in the specified workspace"""
    url = f"{self.base_url}/workspaces/{workspace}/projects/{project_key}/permissions-config/users/{user_uuid}"
    r = self.session.delete(url)
    if r.status_code != 204:
      raise ProjectError(f"Error revoking user permissions: {r.status_code} {r.text}")
    return f"User {user_uuid} permissions revoked successfully."
