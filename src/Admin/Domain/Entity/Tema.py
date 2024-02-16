import uuid
from src.Admin.Domain.Entity.Materia import Materia

class Tema:
    def __int__(self, name, status, materia:Materia):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.status = status
        self.materia = materia
