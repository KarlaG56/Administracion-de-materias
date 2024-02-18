from src.Admin.Application.UseCase.Tema.ListTemasUseCase import ListTemasUseCase
from src.Admin.Domain.Port.PortTema import PortTema
from typing import Any
from flask import jsonify


class ListTemasController:
    def __init__(self, repository: PortTema):
        self.useCase = ListTemasUseCase(repository)

    def run(self):
        try:
            return jsonify(self.useCase.run()), 200
        except Exception as e:
            return jsonify({"Message": "Temas were not found", "error": e}), 500
