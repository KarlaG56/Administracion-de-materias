from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship,backref
from src.Admin.Infraestructura.Models.MateriaMySQLModels import Materia
from src.Database.MySQL import Base

class Tema(Base):
    __tablename__ = 'temas'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    materia_id = Column(String(36), ForeignKey('materias.uuid'))
    materia = relationship(Materia, backref=backref('temas', uselist=True))
