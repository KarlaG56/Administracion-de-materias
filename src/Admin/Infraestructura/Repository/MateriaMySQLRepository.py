from src.Admin.Domain.Port.PortMateria import PortMateria
from src.Admin.Domain.Entity.Materia import Materia
from src.Admin.Infraestructura.Models.MateriaMySQLModels import Materia as Model
from src.Database.MySQL import MySQLConection


class MateriaMySQLRepository(PortMateria):
    def __init__(self):
        conection = MySQLConection()
        self.session = conection.session()
    def list(self) -> Model:
        return self.session.query(Model).all()

    def find(self, id: str) -> Model:
        return self.session.query(Model).filter(Model.uuid == id).first()

    def create(self, materia: Materia) -> Model:
        new = Model(uuid=materia.uuid, name=materia.name,
                    status=materia.status, career=materia.career)
        self.session.add(new)
        self.session.commit()
        return new

    def update(self, id: str, name: str, status: bool, career: str) -> Model:
        materia = self.find(id)
        materia.name = name
        materia.status = status
        materia.career = career
        self.session.commit()
        return materia

    def delete(self, id: str):
        self.session.delete(self.find(id))
        self.session.commit()

