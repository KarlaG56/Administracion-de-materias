from src.Admin.Domain.Port.PortMateria import PortMateria
from typing import Any

class DeleteMateriaUseCase:
    def __init__(self, repository: PortMateria):
        self.repository = repository

    def run(self, id):
        try:
            self.repository.delete(id)
            return {"message": "Delete success", "status": "success"}
        except Exception as e:
            print(e)
