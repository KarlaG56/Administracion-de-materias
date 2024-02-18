from src.Admin.Domain.Port.PortMateria import PortMateria
from typing import Any
from src.Admin.Application.DTOS.Responses.MateriaResponse import materia_response


class FindMateriaUseCase:
    def __init__(self, repository: PortMateria):
        self.repository = repository

    def run(self, id) -> Any:
        try:
            return {"status": "success", "data": materia_response(self.repository.find(id))}
        except Exception as e:
            print(e)
