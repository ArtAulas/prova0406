from sqlalchemy import text
from config_db import engine as e
#e.connect()
#não há a necessidade de ser usuário
#implementar get_db e BaseModel

def get_all_user():
    with e.connect() as con:
        query=text('''
            select *
            from Users
            ''')
        resposta=con.execute(query)
        r2=resposta.fetchall()
        return r2

def get_user_by_id(id):
    with e.connect() as con:
        query=text('''
            select *
            from Users
            where id=:idQ
        ''')
        dados={'idQ':id}
        resposta=con.execute(query,dados)
        r2=resposta.fetchall()
        return r2[0]

def inserir_user():
    pass

def delete_user():
    pass

def update_user():
    pass
