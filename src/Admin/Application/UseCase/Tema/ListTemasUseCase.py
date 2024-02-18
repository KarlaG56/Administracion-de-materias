from typing import Any
from src.Admin.Application.DTOS.Responses.TemaResponse import tema_response
from src.Admin.Domain.Port.PortTema import PortTema


class ListTemasUseCase:
    def __init__(self, repository: PortTema):
        self.repository = repository

    def run(self) -> Any:
        try:
            return {"status": "success", "data":[tema_response(tema) for tema in self.repository.list()]}
        except Exception as e:
            print(e)
