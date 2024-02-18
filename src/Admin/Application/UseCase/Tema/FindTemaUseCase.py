from typing import Any
from src.Admin.Application.DTOS.Responses.TemaResponse import tema_response
from src.Admin.Domain.Port.PortTema import PortTema


class FindTemaUseCase:
    def __init__(self, repository: PortTema):
        self.repository = repository

    def run(self, id) -> Any:
        try:
            return {"status": "Success", "data": tema_response(self.repository.find(id))}
        except Exception as e:
            print(e)
