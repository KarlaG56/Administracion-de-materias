from typing import Any
from src.Admin.Domain.Port.PortTema import PortTema


class DeleteTemaUseCase:
    def __init__(self, repository: PortTema):
        self.repository = repository

    def run(self, id) -> Any:
        try:
            self.repository.delete(id)
            return {"status": "success", "message": "Tema deleted"}
        except Exception as e:
            print(e)
