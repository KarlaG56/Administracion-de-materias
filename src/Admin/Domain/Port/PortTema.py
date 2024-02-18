from typing import Any
from abc import ABC, abstractmethod
from src.Admin.Domain.Entity.Tema import Tema


class PortTema(ABC):

    @abstractmethod
    def list(self) -> Any: pass

    @abstractmethod
    def find(self, id: str) -> Any: pass

    @abstractmethod
    def create(self, tema: Tema) -> Any: pass

    @abstractmethod
    def update(self, id: str, name: str, status: bool, materia: str) -> Any: pass

    @abstractmethod
    def delete(self, id: str) -> Any: pass
