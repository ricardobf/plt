from dataclasses import dataclass


@dataclass
class PLTArgs:
    workspace: str | None = None
    project: str | None = None
    repo: str | None = None
    description: str | None = None
    user_uuid: str | None = None
    exempt_users: list[str] = None
    exempt_groups: list[str] = None
    is_private: bool = True
    user_permissions: bool = False
    permission: str | None = None
    branch: str | None = None
