iimport pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

# Coneccion a la BD ---------------------------------------- 
db_config = {'user':os.getenv('tripleten_sql_user'),         # nombre de usuario
             'pwd': os.getenv('tripleten_sql_pwd'), # contraseña
             'host': os.getenv('tripleten_sql_host'),
             'port': os.getenv('tripleten_sql_port'),              # puerto de conexión
             'db': os.getenv('tripleten_sql_db')}          # nombre de la base de datos

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                                     db_config['pwd'],
                                                                       db_config['host'],
                                                                       db_config['port'],
                                                                       db_config['db'])

engine = create_engine(connection_string, connect_args={'sslmode':'require'},pool_size=10, max_overflow=20)

# Query ---------------------------------------- 
query="SELECT * FROM public.books LIMIT 5"
pd.io.sql.read_sql(query, con = engine)