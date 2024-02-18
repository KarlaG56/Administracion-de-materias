from src.Admin.Application.UseCase.Tema.FindTemaUseCase import FindTemaUseCase
from src.Admin.Domain.Port.PortTema import PortTema
from typing import Any
from flask import jsonify


class FindTemaController:
    def __init__(self, repository: PortTema):
        self.useCase = FindTemaUseCase(repository)

    def run(self, id):
        try:
            return jsonify(self.useCase.run(id)), 200
        except Exception as e:
            return jsonify({"Message": "Tema was not found", "error": e}), 500
