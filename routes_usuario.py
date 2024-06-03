#CRUD- CREATE READ UPDATE DELETE
from fastapi import APIRouter, Depends, Response
from db_user import UsuarioRequest, UsuarioResponse, Usuario
from sqlalchemy.orm import Session

from db_config import Base, engine, get_db
Base.metadata.create_all(bind=engine)

router=APIRouter(prefix='/usuarios')

@router.get("/buscar")#Read
def buscar(db:Session=Depends(get_db)):
    usuarios_on_db=db.query(Usuario).all()
    lista=[]
    for usuario_unico in usuarios_on_db:
        lista.append(UsuarioResponse.model_validate(usuario_unico))
    return lista

@router.get("/buscar/{id}")#Read
def buscarId(id:int, db:Session=Depends(get_db)):
    usuario_on_db=db.query(Usuario).filter(Usuario.id==id).first()
    if usuario_on_db is None:
        return Response(content='Usuário não encontrado',status_code=404)
    return UsuarioResponse.model_validate(usuario_on_db)

@router.get("/buscar/nome/{username}")#Read
def buscarNome(username:str, db:Session=Depends(get_db)):
    usuarios_on_db=db.query(Usuario).filter(Usuario.nome==username).all()
    lista=[]
    for usuario_unico in usuarios_on_db:
        lista.append(UsuarioResponse.model_validate(usuario_unico))
    return lista

@router.delete("/apagar/{id}")#Delete
def apagarId(id, db:Session=Depends(get_db)):
    usuario_on_db=db.query(Usuario).filter(Usuario.id==id).first()
    if usuario_on_db is None:
        return Response(content='Usuário não encontrado',status_code=404)
    db.delete(usuario_on_db)
    db.commit()

@router.post("/inserir")#Create
def inserir(request:UsuarioRequest, db:Session=Depends(get_db)):
    rDici=request.model_dump()
    db.add(Usuario(**rDici))
    db.commit()
    return rDici

@router.put("/atualizar/{id}")#Update
def atualizarId(id, request:UsuarioRequest, db:Session=Depends(get_db)):
    usuario_antigo=db.query(Usuario).filter(Usuario.id==id).first()
    if usuario_antigo is None:
        return Response(content='Usuário não encontrado',status_code=404)
    db.merge(Usuario(id=id, **request.model_dump()))
    db.commit()
    usuario_novo=db.query(Usuario).filter(Usuario.id==id).first()
    return usuario_novo
