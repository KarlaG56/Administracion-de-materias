from src.Admin.Application.UseCase.Tema.DeleteTemaUseCase import DeleteTemaUseCase
from src.Admin.Domain.Port.PortTema import PortTema
from typing import Any
from flask import jsonify


class DeleteTemaController:
    def __init__(self, repository: PortTema):
        self.useCase = DeleteTemaUseCase(repository)

    def run(self, id):
        try:
            return jsonify(self.useCase.run(id)), 200
        except Exception as e:
            return jsonify({"Message": "Was not possible delete tema", "error": e}), 500
