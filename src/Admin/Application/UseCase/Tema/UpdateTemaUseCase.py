from typing import Any
from src.Admin.Application.DTOS.Responses.TemaResponse import tema_response
from src.Admin.Domain.Port.PortTema import PortTema


class UpdateTemaUseCase:
    def __init__(self, repository: PortTema):
        self.repository = repository

    def run(self, id, data) -> Any:
        try:
            return {"status": "success",
                    "data": tema_response(self.repository.update(id, data["name"], data["status"], data["materia"]))}
        except Exception as e:
            print(e)
