import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

# Coneccion a la BD ----------------------------------------
db_config = {'user': os.getenv('tripleten_sql_user'),
             'pwd': os.getenv('tripleten_sql_pwd'),
             'host': os.getenv('tripleten_sql_host'),
             # puerto de conexión
             'port': os.getenv('tripleten_sql_port'),
             # nombre de la base de datos
             'db': os.getenv('tripleten_sql_db')}

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
                                                         db_config['pwd'],
                                                         db_config['host'],
                                                         db_config['port'],
                                                         db_config['db'])

engine = create_engine(connection_string, connect_args={
                       'sslmode': 'require'}, pool_size=10, max_overflow=20)

# Query ----------------------------------------

query = pd.read_sql("SELECT * FROM public.books LIMIT 5", con=engine)
print(query)
