from src.Admin.Domain.Port.PortTema import PortTema
from src.Admin.Infraestructura.Models.TemaMySQLModels import Tema as Model
from src.Admin.Domain.Entity.Tema import Tema
from src.Database.MySQL import MySQLConection


class TemaMySQLRepository(PortTema):

    def __init__(self):
        conection = MySQLConection()
        self.session = conection.session()

    def list(self) -> Model:
        return self.session.query(Model).all()

    def find(self, id: str) -> Model:
        return self.session.query(Model).filter(Model.uuid == id).first()

    def create(self, tema: Tema) -> Model:
        new = Model(uuid=tema.uuid, name=tema.name,
                     status=tema.status, materia_id=tema.materia)
        self.session.add(new)
        self.session.commit()
        return new

    def update(self, id: str, name: str, status: bool, materia: str) -> Model:
        tema = self.find(id)
        tema.materia_id = materia
        tema.name = name
        tema.status = status
        self.session.commit()
        return tema

    def delete(self, id: str):
        self.session.delete(self.find(id))
        self.session.commit()
