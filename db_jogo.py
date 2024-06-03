from sqlalchemy import Column, SmallInteger, String
from pydantic import BaseModel
from db_config import Base

#ORM-definir a tabela no banco de dados
#class Cartas(Base):
#    __tablename__='cartas'
#    id=Column('id',SmallInteger, primary_key=True,autoincrement=True)
#    nome=Column('nome',String(50))
#    vida=Column('vida',SmallInteger)
#    ataque=Column('ataque',SmallInteger)
#    defesa=Column('defesa',SmallInteger)
#    desc=Column('descricao',String(50))

#class CartasResponse(BaseModel):
#    nome:str
#    vida:int
#    ataque:int
#    defesa:int
#    desc:str