from src.Admin.Infraestructura.Models.TemaMySQLModels import Tema

def tema_response(tema: Tema):
    return {"id": tema.uuid, "name": tema.name,
            "status": tema.status, "materia": tema.materia.name}
