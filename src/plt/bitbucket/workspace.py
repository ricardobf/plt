class WorkspaceError(Exception):
  pass

class Workspace:
  def __init__(self, session, base_url):
    self.session = session
    self.base_url = base_url

  def list_user_permissions(self, workspace: str):
    """List all user permissions on a workspace"""
    url = f"{self.base_url}/workspaces/{workspace}/permissions"
    r = self.session.get(url)
    if r.status_code != 200:
      raise WorkspaceError(f"Error fetching workspace permissions: {r.status_code} {r.text}")
    return r.json()
