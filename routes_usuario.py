from fastapi import APIRouter, Depends
from config_db import UsuarioResponse, Usuario
from sqlalchemy.orm import Session

from config_db import Base, engine, get_db
Base.metadata.create_all(bind=engine)

router=APIRouter(prefix='/usuarios')

@router.get("/listar", response_model=list[UsuarioResponse])
def listar(db:Session=Depends(get_db)):
    usuarios_on_db=db.query(Usuario).all()
    lista=[]
    for usuario_unico in usuarios_on_db:
        lista.append(UsuarioResponse.from_orm(usuario_unico))
    return lista

@router.get("/listar/{id}")
def listar(id, db:Session=Depends(get_db)):
    usuario_on_db=db.query(Usuario).filter(Usuario.id==id).first()
    try:
        return UsuarioResponse.from_orm(usuario_on_db)
    except:
        return {'erro':'Usuário não encontrado'}