from src.Admin.Infraestructura.Models.MateriaMySQLModels import Materia

def materia_response(materia: Materia):
    return {"id": materia.uuid, "name": materia.name,
            "status": materia.status, "career": materia.career}
