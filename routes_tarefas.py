#CRUD- CREATE READ UPDATE DELETE
from fastapi import APIRouter, Depends, Response
from db_tarefas import TarefasRequest, Tarefas
from sqlalchemy.orm import Session

from db_config import Base, engine, get_db
Base.metadata.create_all(bind=engine)

router=APIRouter(prefix='/tarefas')

@router.post("/inserir")#Create
def inserir(request:TarefasRequest, db:Session=Depends(get_db)):
    rDici=request.model_dump()
    db.add(Tarefas(**rDici))
    db.commit()
    return rDici

@router.get("/buscar")#Read
def buscar(db:Session=Depends(get_db)):
    tarefasdb=db.query(Tarefas).all()
    return tarefasdb