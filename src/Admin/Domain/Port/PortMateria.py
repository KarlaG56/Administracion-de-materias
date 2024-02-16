from typing import Any
from abc import ABC, abstractmethod
from src.Admin.Domain.Entity.Materia import Materia


class PortMateria(ABC):

    @abstractmethod
    def list(self) -> Any: pass

    @abstractmethod
    def find(self, id: str) -> Any: pass

    @abstractmethod
    def create(self, materia: Materia) -> Any: pass

    @abstractmethod
    def update(self, name: str, status: bool, career: str) -> Any: pass

    @abstractmethod
    def delete(self, id: str) -> Any: pass
