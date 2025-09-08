from abc import ABC, abstractmethod
from typing import Any


class VCSProvider(ABC):
    """Abstract base class for all VCS providers."""

    @abstractmethod
    def list(self) -> Any:
        pass

    @abstractmethod
    def create(self) -> Any:
        pass

    @abstractmethod
    def delete(self) -> Any:
        pass

    @abstractmethod
    def grant(self) -> Any:
        pass

    @abstractmethod
    def revoke(self) -> Any:
        pass

    @abstractmethod
    def configure_branch_permissions(self) -> Any:
        pass
