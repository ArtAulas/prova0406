from sqlalchemy import Column, SmallInteger, String
from pydantic import BaseModel
from db_config import Base

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