from src.Admin.Domain.Port.PortMateria import PortMateria
from src.Admin.Application.UseCase.Materia.ListMateriasUseCase import ListMateriaUseCase
from flask import jsonify
from typing import Any


class ListMateriasController:
    def __init__(self, repository: PortMateria):
        self.useCase = ListMateriaUseCase(repository)

    def run(self) -> Any:
        try:
            return jsonify(self.useCase.run()), 200
        except Exception as e:
            return jsonify({"message": "Materias not found", "error": e}), 500
