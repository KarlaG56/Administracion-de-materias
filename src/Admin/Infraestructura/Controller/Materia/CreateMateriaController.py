from src.Admin.Application.UseCase.Materia.CreateMateriaUseCase import CreateMateriaUseCase
from src.Admin.Domain.Port.PortMateria import PortMateria
from typing import Any
from flask import jsonify


class CreateMateriaController:
    def __init__(self, repository: PortMateria):
        self.useCase = CreateMateriaUseCase(repository)

    def run(self, request) -> Any:
        try:
            return jsonify(self.useCase.run(request.get_json())), 200
        except Exception as e:
            return jsonify({"message": "User not created", "error": e}), 500
