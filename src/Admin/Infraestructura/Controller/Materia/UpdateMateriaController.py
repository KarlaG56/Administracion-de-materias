from src.Admin.Application.UseCase.Materia.UpdateMateriaUseCase import UpdateMateriaUseCase
from src.Admin.Domain.Port.PortMateria import PortMateria
from typing import Any
from flask import jsonify


class UpdateMateriaController:
    def __init__(self, repository: PortMateria):
        self.useCase = UpdateMateriaUseCase(repository)

    def run(self, id, request) -> Any:
        try:
            data = request.get_json()
            return jsonify(self.useCase.run(id, data["name"], data["status"], data["career"]))
        except Exception as e:
            return jsonify({"message": "Was not posible update", "error": e}), 500
