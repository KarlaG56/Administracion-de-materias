import uuid


class Tema:
    def __init__(self, name, status, id_materia):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.status = status
        self.materia = id_materia
