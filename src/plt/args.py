from dataclasses import dataclass
from typing import Optional


@dataclass
class PLTArgs:
    workspace: Optional[str] = None
    project: Optional[str] = None
    repo: Optional[str] = None
    description: Optional[str] = None
    user_uuid: Optional[str] = None
    exempt_users: list[str] = None
    exempt_groups: list[str] = None
    is_private: bool = True
    user_permissions: bool = False
    permission: Optional[str] = None
    branch: Optional[str] = None
