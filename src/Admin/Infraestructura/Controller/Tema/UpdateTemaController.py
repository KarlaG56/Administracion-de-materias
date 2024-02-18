from src.Admin.Application.UseCase.Tema.UpdateTemaUseCase import UpdateTemaUseCase
from src.Admin.Domain.Port.PortTema import PortTema
from typing import Any
from flask import jsonify


class UpdateTemaController:
    def __init__(self, repository: PortTema):
        self.useCase = UpdateTemaUseCase(repository)

    def run(self, id, request):
        try:
            return jsonify(self.useCase.run(id, request.get_json())), 200
        except Exception as e:
            return jsonify({"Message": "Was not possible update tema", "error": e}), 500
