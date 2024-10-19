import pandas as pd
from sqlalchemy import create_engine

query_1 = """
SELECT COUNT(*) AS libros_publicados_despues_2000
FROM books
WHERE publication_date > '2000-01-01';
"""
pd.io.sql.read_sql(query_1, con = engine)


query_2 = """
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
"""
pd.io.sql.read_sql(query_2, con = engine)


query_3 = """
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
"""
pd.io.sql.read_sql(query_3, con = engine)


query_4 = """
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
"""
pd.io.sql.read_sql(query_4, con = engine)


uery_5 = """
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
"""
pd.io.sql.read_sql(query_5, con = engine)


