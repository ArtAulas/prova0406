from sqlalchemy import create_engine
#jdbc:mysql://localhost:3306/banco-de-dados?allowPublicKeyRetrieval=true&useSSL=false
#^MUITO provavelmente essa

MYSQL_URL="jdbc:mysql://root:example@localhost:3306/banco-de-dados?allowPublicKeyRetrieval=true"
#ArgumentError: Could not parse SQLAlchemy URL from string
#Base=declarative_base()
engine=create_engine(MYSQL_URL)

#with engine.connect() as con 
#^primeira maneira de rodar comandos, mais simples

#get_db_session
#^segunda maneira, mais complicada

def criar_user():
    with engine.connect() as con:
        query='''
                create table User(
                    id tinyint,
                    name varchar(10)
                )'''
        con.execute(query)


criar_user()