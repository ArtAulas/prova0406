from sqlalchemy import Column, String, SmallInteger, Date
from pydantic import BaseModel
from db_config import Base

class Tarefas(Base):
    __tablename__='tarefas'
    id=Column('id',SmallInteger, primary_key=True, autoincrement=True)
    title=Column('title',String(50))
    description=Column('description',String(50))
    completion_date=Column('completion_date',Date)
    priority=Column('priority',String(50))

class TarefasRequest(BaseModel):
    title:str
    description:str
    completion_date:str
    priority:str