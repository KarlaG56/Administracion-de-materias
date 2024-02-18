from src.Admin.Application.UseCase.Materia.FindMateriaUseCase import FindMateriaUseCase
from src.Admin.Domain.Port.PortMateria import PortMateria
from typing import Any
from flask import jsonify


class FindMateriaController:
    def __init__(self, repository: PortMateria):
        self.useCase = FindMateriaUseCase(repository)

    def run(self, id) -> Any:
        try:
            return jsonify(self.useCase.run(id)), 200
        except Exception as e:
            return jsonify({"message": "Materia not found", "error": e}), 500
