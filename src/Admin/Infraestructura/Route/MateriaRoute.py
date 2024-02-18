from flask import Blueprint, request
from src.Admin.Infraestructura.Repository.MateriaMySQLRepository import MateriaMySQLRepository
from src.Admin.Infraestructura.Controller.Materia.CreateMateriaController import CreateMateriaController
from src.Admin.Infraestructura.Controller.Materia.FindMateriaController import FindMateriaController
from src.Admin.Infraestructura.Controller.Materia.ListMateriasController import ListMateriasController
from src.Admin.Infraestructura.Controller.Materia.UpdateMateriaController import UpdateMateriaController
from src.Admin.Infraestructura.Controller.Materia.DeleteMateriaController import DeleteMateriaController

materia_blueprint = Blueprint("materia", __name__)
repository = MateriaMySQLRepository()
list_controller = ListMateriasController(repository)
create_cotroller = CreateMateriaController(repository)
find_controller = FindMateriaController(repository)
update_controller = UpdateMateriaController(repository)
delete_controller = DeleteMateriaController(repository)

@materia_blueprint.route("/<string:id>", methods=["GET"])
def find_materia(id):
    return find_controller.run(id)

@materia_blueprint.route("/", methods=["GET"])
def list():
    return list_controller.run()
@materia_blueprint.route("/", methods=['POST'])
def create_materia():
    return create_cotroller.run(request)

@materia_blueprint.route("/<string:id>", methods=["PUT"])
def update_materia(id):
    return update_controller.run(id, request)

@materia_blueprint.route("/<string:id>", methods=["DELETE"])
def delete_materia(id):
    return delete_controller.run(id)

