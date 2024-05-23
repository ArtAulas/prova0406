from sqlalchemy import create_engine, text

MYSQL_URL="mysql://usuario:senha@localhost:3306/banco-de-dados"
engine=create_engine(MYSQL_URL)

def create_table():#não há mais a necessidade de ser Usuário
    with engine.connect() as con:
        query=text('''create table Users(
                   id tinyint,
                   name varchar(10)
                   )''')
        con.execute(query)

