from src.Admin.Application.UseCase.Materia.DeleteMateriaUseCase import DeleteMateriaUseCase
from src.Admin.Domain.Port.PortMateria import PortMateria
from typing import Any
from flask import jsonify


class DeleteMateriaController:
    def __init__(self, repository: PortMateria):
        self.useCase = DeleteMateriaUseCase(repository)

    def run(self, id):
        try:
            return jsonify(self.useCase.run(id))
        except Exception as e:
            return jsonify({"message": "Not posible delete", "error": e}), 500
