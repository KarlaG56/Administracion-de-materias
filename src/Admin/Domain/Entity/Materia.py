import uuid


class Materia:
    def __init__(self, name, career, status):
        self.uuid = str(uuid.uuid4())
        self.name = name
        self.career = career
        self.status = status
