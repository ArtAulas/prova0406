from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, SmallInteger, String

from pydantic import BaseModel

#string de conexão para o banco
MYSQL_URL="mysql://usuario:senha@localhost:3306/banco-de-dados"
engine=create_engine(MYSQL_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#get_db função para acessar o banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#ORM-definir a tabela no banco de dados
class Usuario(Base):
    __tablename__='usuarios'
    id=Column('id',SmallInteger, primary_key=True)
    nome=Column('nome',String(16))

#schemas-utilizar para response e request
class UsuarioResponse(BaseModel):
    id: int
    nome: str

    class Config:
        from_attributes=True

class UsuarioRequest(BaseModel):
    id:int
    nome:str