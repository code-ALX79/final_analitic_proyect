import pandas as pd
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
load_dotenv()

# Coneccion a la BD ----------------------------------------
db_config = {'user': os.getenv('tripleten_sql_user'),         # nombre de usuario
             'pwd': os.getenv('tripleten_sql_pwd'),  # contraseña
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


query_1 = pd.read_sql("""
SELECT COUNT(*) AS libros_publicados_despues_2000
FROM books
WHERE publication_date > '2000-01-01';
""", con=engine)

print(query_1)


query_2 = pd.read_sql("""
SELECT
    b.book_id,
    b.title,
    COUNT(rv.review_id) AS total_reseñas,
    AVG(r.rating) AS calificacion_promedio
FROM
    books b
LEFT JOIN ratings r ON b.book_id = r.book_id
LEFT JOIN reviews rv ON b.book_id = rv.book_id
GROUP BY
    b.book_id, b.title;
""", con=engine)

print(query_2)


query_3 = pd.read_sql("""
SELECT 
    p.publisher, 
    COUNT(*) AS total_libros_mas_50_paginas
FROM 
    books b
JOIN 
    publishers p ON b.publisher_id = p.publisher_id
WHERE 
    b.num_pages > 50
GROUP BY 
    p.publisher
ORDER BY 
    total_libros_mas_50_paginas DESC
LIMIT 1;
""", con=engine)

print(query_3)


query_4 = pd.read_sql("""
WITH CalificacionesPorAutor AS (
  SELECT
    a.author_id,
    a.author,
    AVG(r.rating) AS promedio_calificacion,
    COUNT(r.rating) AS total_calificaciones
  FROM
    authors a
  JOIN books b ON a.author_id = b.author_id
  JOIN ratings r ON b.book_id = r.book_id
  GROUP BY a.author_id, a.author
)
SELECT
  author,
  promedio_calificacion
FROM
  CalificacionesPorAutor
WHERE
  total_calificaciones >= 50
ORDER BY
  promedio_calificacion DESC
LIMIT 1;
""", con=engine)

print(query_4)


query_5 = pd.read_sql("""
WITH UsuariosConMas50Calificaciones AS (
    SELECT username AS uc_username
    FROM ratings
    GROUP BY username
    HAVING COUNT(*) > 50
)
SELECT
    AVG(ur.review_count) AS promedio_reseñas
FROM
    UsuariosConMas50Calificaciones uc
JOIN (
    SELECT username AS ur_username, COUNT(*) AS review_count
    FROM reviews
    GROUP BY username
) AS ur ON uc.uc_username = ur.ur_username;
""", con=engine)

print(query_5)
