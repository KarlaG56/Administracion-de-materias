from flask import Blueprint, request
from src.Admin.Infraestructura.Controller.Tema.CreateTemaController import CreateTemaController
from src.Admin.Infraestructura.Controller.Tema.FindTemaController import FindTemaController
from src.Admin.Infraestructura.Controller.Tema.ListTemasController import ListTemasController
from src.Admin.Infraestructura.Controller.Tema.UpdateTemaController import UpdateTemaController
from src.Admin.Infraestructura.Controller.Tema.DeleteTemaController import DeleteTemaController
from src.Admin.Infraestructura.Repository.TemaMySQLRepository import TemaMySQLRepository

tema_blueprint = Blueprint("temas", __name__)
repository = TemaMySQLRepository()
create_controller = CreateTemaController(repository)
find_controller = FindTemaController(repository)
list_controller = ListTemasController(repository)
update_controller = UpdateTemaController(repository)
delete_controller = DeleteTemaController(repository)

@tema_blueprint.route("/<string:id>", methods=["GET"])
def find(id):
    return find_controller.run(id)

@tema_blueprint.route("/", methods=["GET"])
def list():
    return list_controller.run()

@tema_blueprint.route("/<string:materia_id>", methods=["POST"])
def create(materia_id):
    return create_controller.run(materia_id, request)

@tema_blueprint.route("/<string:id>", methods=["PUT"])
def update(id):
    return update_controller.run(id, request)

@tema_blueprint.route("/<string:id>", methods=["DELETE"])
def delete(id):
    return delete_controller.run(id)

