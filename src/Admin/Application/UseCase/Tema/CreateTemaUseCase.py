from typing import Any
from src.Admin.Application.DTOS.Responses.TemaResponse import tema_response
from src.Admin.Domain.Port.PortTema import PortTema
from src.Admin.Domain.Entity.Tema import Tema



class CreateTemaUseCase:
    def __init__(self, repository: PortTema):
        self.repository= repository

    def run(self, id, data) -> Any:
        try:
            tema = self.repository.create(Tema(data["name"], data["status"], id))
            return {"status": "Success", "data": tema_response(tema)}
        except Exception as  e:
            print(e)
