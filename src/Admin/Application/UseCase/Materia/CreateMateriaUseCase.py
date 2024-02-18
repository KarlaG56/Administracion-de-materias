from src.Admin.Domain.Port.PortMateria import PortMateria
from src.Admin.Domain.Entity.Materia import Materia
from typing import Any
from src.Admin.Application.DTOS.Responses.MateriaResponse import materia_response


class CreateMateriaUseCase:
    def __init__(self, repository: PortMateria):
        self.repository = repository

    def run(self, data) -> Any:
        try:
            materia = self.repository.create(Materia(data['name'], data['career'], data['status']))
            return {"data": materia_response(materia), "status": "success"}
        except Exception as e:
            print(e)
