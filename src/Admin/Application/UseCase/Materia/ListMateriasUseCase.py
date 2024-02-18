from src.Admin.Domain.Port.PortMateria import PortMateria
from typing import Any
from src.Admin.Application.DTOS.Responses.MateriaResponse import materia_response


class ListMateriaUseCase:
    def __init__(self, repository: PortMateria):
        self.repository = repository

    def run(self) -> Any:
        try:
            return {"status": "success",
                    "data": [materia_response(materia) for materia in self.repository.list()]}
        except Exception as e:
            print(e)

