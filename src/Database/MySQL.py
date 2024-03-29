from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MySQLConection:
    def __init__(self):
        DATABASE_URI = 'mysql+mysqlconnector://root:My_SQL123@127.0.0.1:3306/administracion'
        engine = create_engine(DATABASE_URI)
        Base.metadata.create_all(bind=engine)
        self.session = sessionmaker(bind=engine)
