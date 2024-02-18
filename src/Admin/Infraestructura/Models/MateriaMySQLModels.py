from sqlalchemy import Column, String, Boolean
from src.Database.MySQL import Base

class Materia(Base):
    __tablename__ = 'materias'
    uuid = Column(String(36), primary_key=True)
    name = Column(String(255), nullable=False)
    status = Column(Boolean, nullable=False)
    career = Column(String(255), nullable=False)
