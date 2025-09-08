from abc import ABC, abstractmethod
from typing import Any

class VCSProvider(ABC):
    """Abstract base class for all VCS providers."""

    @abstractmethod
    def list(self) -> Any:
        pass

    # @abstractmethod
    # def create(self, key: str, name: str, is_private: bool = True) -> Any:
    #     pass
    
    # @abstractmethod
    # def delete(self, key: str) -> Any:
    #     pass

    # @abstractmethod
    # def grant_user_permission(self, resource: str, key: str, user_uuid: str, permission: str) -> Any:
    #     pass

    # @abstractmethod
    # def revoke_user_permission(self, resource: str, key: str, user_uuid: str) -> Any:
    #     pass

    # @abstractmethod
    # def configure_branch_permissions(self, workspace: str, repo_slug: str, branch: str, exempt_users: list[str], exempt_groups: list[str]) -> Any:
    #     pass
