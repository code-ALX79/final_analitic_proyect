# Final Project - Tripleteen

En este repositorio pongo a prueba mis habilidades como analista de datos, adquiridas a lo largo de mi formación, mediante el desarrollo de un caso real de **analítica de datos aplicada**.  

A través de varios proyectos prácticos, evaluaré diferentes **KPI** de manera individual, brindando soporte analítico de alto valor a las empresas y startups que me confiaron sus datos.

---

## 1. Conexión a base de datos (SQL + Pandas)

En este primer proyecto, nos conectaremos a una base de datos para realizar consultas mediante **SQL**, de forma independiente al proyecto principal.  

La empresa colaboradora es una **startup** que aprovechó la pandemia de **COVID-19** para desarrollar una aplicación orientada a los amantes de la lectura. Durante la cuarentena, muchas personas recurrieron a soluciones digitales que les permitieran aprovechar el tiempo libre desde casa, y esta startup fue una de ellas.  

Nos brindaron una base de datos real para analizar el comportamiento de sus usuarios y competidores.  
Mediante **pandas** y **SQL**, generaremos resultados precisos y de alto valor para apoyar su crecimiento.

---

## 2. Preprocesamiento de datos (Callmemaby)

El segundo proyecto se enfoca en la empresa **Callmemaby**, que busca desarrollar una nueva función para brindar soporte a los supervisores, permitiéndoles acceder fácilmente a la información de los **operadores menos eficaces**.  

El objetivo es optimizar la toma de decisiones mediante el análisis de métricas de desempeño operativo.

---

## 3. Proyecto internacional de analítica (Test A/B)

En este tercer proyecto retomamos un trabajo de alcance internacional que quedó inconcluso.  
El equipo anterior lanzó una **prueba A/B** y posteriormente abandonó el proyecto.  

Mediante la documentación técnica y los resultados existentes, implementaremos un **nuevo sistema de recomendaciones mejorado**, con el fin de evaluar:

- Si este cambio está generando comportamientos distintos entre los usuarios.  
- O si, por el contrario, los resultados eran previsibles y el abandono del proyecto estaba justificado.

---

## 4. Proyecto principal (Evaluación de desempeño - Callmemaby)

Este es el proyecto principal confiado por **Callmemaby**, donde se define que un operador es ineficaz si:

- Tiene una gran cantidad de llamadas entrantes perdidas (internas o externas).  
- Presenta un tiempo de espera prolongado en llamadas entrantes.  
- Realiza pocas llamadas salientes, pese a tener esa responsabilidad.

Mediante **visualizaciones temporales**, categorización de operadores y **pruebas de hipótesis estadísticas**, evaluaremos el comportamiento del equipo para identificar a los menos eficientes y proponer estrategias de mejora.

---

## Descripción general

Cada una de estas tareas independientes representa un reto estimulante que pondrá a prueba mis habilidades como analista de datos.  

Estos proyectos requieren **pensamiento crítico**, **precisión técnica** y **capacidad de aplicar los datos en beneficio de la empresa**.  
Con ellos, demuestro mi capacidad para abordar tareas reales que enfrenta un analista y destacar en cada una, ofreciendo información que respalde decisiones estratégicas.

---

## 🔧 Requisitos y configuración del entorno

> Es importante ejecutar los siguientes comandos desde el mismo directorio donde se ha clonado este repositorio.

Para desplazarse al directorio del proyecto:
```sh
cd nombre_del_directorio

1.1 Crear un entorno virtual

Se recomienda crear un entorno virtual .venv para garantizar un espacio de ejecución aislado, libre de errores de dependencia.

``` sh 
 python -m venv .venv
```
Creacion de el ambiente VIRTUAL 

```sh 
 source .venv/Scripts/activate
```
Activar el entorno virtual:

``` sh 
pip freeze > requirements.txt
```
 Exportar los paquetes instalados:
 
``` sh 
pip install -r requirements.txt
``` 
Instalar dependencias desde el archivo:


Luego se instalara el  archivo de requerimientos para trabajar con las mismas dependecnias  utilizadas al ejecutar el codigo.

Deberemos primero mostar el contenido de nuestrois archivos, y  ejecutar cada uno de los estos desde el directorio de nuestro repositorio.
  DEBIDO A QUE LOS ARCHIVOS DE DATOS ESTAN EN EL MISMO DIRECTOTIO DE LOS ARCHIVOS DE EJECUSION, ESTOS DEBERIAN LEERSE AL EJECURARLOS SIN NINGUN INCONVENIENTE.

**1.2 Archivos y ejecución**

Dado que los archivos de datos se encuentran en el mismo directorio que los de ejecución, podrán leerse sin inconvenientes al ejecutar los scripts.

🔹 Archivo conection-t.py

Visualizar:
``` sh
code conection-t.py
```

Ejecutar:
```sh
python conection-t.py
```
Antes de ejecutarlo, crea un archivo .env con las variables necesarias para la conexión a la base de datos:

``` Python 
tripleten_sql_user=""
tripleten_sql_pwd=""
tripleten_sql_host=""
tripleten_sql_port=""
tripleten_sql_db=""
```

Usaremos las librerías dotenv y sqlalchemy para establecer la conexión:

``` Python 
from sqlalchemy import create_engine
```

``` Python 
from dotenv import load_dotenv()
```

Este script incluye una consulta de prueba que muestra las primeras cinco filas de la base de datos:

 ``` txt 
tripleten_sql_user=""
tripleten_sql_pwd=""
tripleten_sql_host=""
tripleten_sql_port=""
tripleten_sql_db=""
```
El archivo conection_t.py, cuenta con una consulta de prueba que traera las 5 primeras filas de la base de datos al ser ejecutada. Esto fue implementado en este archivo,
para comprobar su correcto funsionamiento.

```Python
query = pd.read_sql("SELECT * FROM public.books LIMIT 5", con=engine)
print(query)
```
Si el resultado muestra las cinco primeras filas correctamente, la conexión es funcional.

🔹 Archivo queries.py

Visualizar:

``` sh 
code queries.py
```
Ejecutar:

``` sh
python queries.py
```

Este archivo contiene las consultas SQL necesarias para responder los siguientes requerimientos:

- Número de libros publicados después del 1 de enero del 2000.

- Número de reseñas de usuarios y calificación promedio por libro.

- Editorial con mayor número de libros con más de 50 páginas.

- Autor con la calificación promedio más alta.

- Número promedio de reseñas de texto entre usuarios que calificaron más de 50 libros.

En este apartado se ponen a prueba las habilidades en SQL adquiridas durante mi formación, aplicadas a un caso real de negocio.

🔹 Archivo project_test_A-B.py

Visualizar:

``` sh 
code project_test_A-B.py
```
Ejecutarlo:

``` sh
python project_test_A-B.py
```
Este script retoma una prueba A/B previa, con el objetivo de detectar diferencias de comportamiento entre el grupo de control y el grupo experimental.

Pasos principales:

- Estudiar la conversión en las diferentes etapas del embudo.

- Evaluar los resultados del test A/B.

- Describir conclusiones basadas en el análisis exploratorio y los resultados experimentales.

Cada análisis está documentado en Markdown dentro del propio script, explicando paso a paso las conclusiones obtenidas.
🔹 Archivo project_telecom.py

Visualizar:

``` sh
code project_telecom.py
```
Ejecutar
:
``` sh
python project_telecom.py
```

Este proyecto realiza un análisis completo del rendimiento de los operadores de Callmemaby, incluyendo:

- Análisis exploratorio de datos (EDA).

- Identificación de operadores ineficaces.

- Pruebas de hipótesis estadísticas.

Las visualizaciones utilizadas son interactivas para facilitar la interpretación de los resultados.
El archivo está estructurado de manera secuencial y clara para seguir el desarrollo analítico paso a paso.

🧠 Conclusión

Este conjunto de proyectos demuestra mi capacidad para desarrollar análisis de datos aplicados, desde la conexión y procesamiento de información hasta la interpretación y comunicación de resultados.

Cada módulo del repositorio representa un ejemplo práctico de cómo la analítica puede generar valor tangible para una organización.

En el siguiente enlace se podrá observar una explicación detallada del desarrollo y resolución del proyecto, especificando los resultados obtenidos en el mismo:
https://1drv.ms/b/c/75c608b03a43bf35/EZuSE_xWAuZLoCc2VUamYGEBYXiPYyLEe9MVovMmdWxwOA?e=NHceOs

En el siguiente enlace se podrá observar un dashboard sobre la duración de llamadas, con varios gráficos explicativos que permiten filtrar y obtener una visión más precisa sobre este aspecto importante:
https://public.tableau.com/views/DashboraddeduracinytipodellamadasCallmemaby/Dashboard1?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
