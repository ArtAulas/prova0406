from sqlalchemy import create_engine
#jdbc:mysql://localhost:3306/banco-de-dados?allowPublicKeyRetrieval=true&useSSL=false
#^MUITO provavelmente essa

MYSQL_URL='jdbc:mysql://localhost:3306/banco-de-dados?allowPublicKeyRetrieval=true&useSSL=false'

#Base=declarative_base()
engine=create_engine(MYSQL_URL)

#with engine.connect() as con 
#^primeira maneira de rodar comandos, mais simples

#get_db_session
#^segunda maneira, mais complicada