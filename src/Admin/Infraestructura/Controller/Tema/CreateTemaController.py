from src.Admin.Application.UseCase.Tema.CreateTemaUseCase import CreateTemaUseCase
from src.Admin.Domain.Port.PortTema import PortTema
from typing import Any
from flask import jsonify


class CreateTemaController:
    def __init__(self, repository: PortTema):
        self.useCase = CreateTemaUseCase(repository)

    def run(self, id, request) -> Any:
        try:
            return jsonify(self.useCase.run(id, request.get_json())), 200
        except Exception as e:
            return jsonify({"Message": "Was not possible create tema", "error": e}), 500
