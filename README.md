# final_proyect_tripleteen.

En este repositorio voy a poner a prueba mis habilidades como analista aprendidas en todo mi trayecto como estudiante, en un caso real de analítica de datos. Mediante varios proyectos  practicos, que evaluarán cada una de mis KPI por separado, brindando una excelente soporte a la corporación que solicitó mis servicios. 

1. Primero realizaremos un preprocesamiento de datos para una empresa que intenta desarrollar una nueva función que brindará a los supervisores y las supervisoras información sobre los operadores menos eficaces, para que puedan tomar decisiones importantes sobre aquellos operadores menos eficientes.

2. Luego nos vamos a conectar a una base de datos para realizarle  consultas mediante SQL de forma idependiente al proyecto principal ya que en esta ocasion una startup, que aprevecho el coronavirus 
para desarrollar una aplicación para los amantes de los libros, debido a que las personas en este tiempo recurrieron a soluciones saludables para quedarse en casa. Nos han brindado una base de datos de uno de los servicios que compiten en este mercado.  medinete pandas y SQL,llegaremos a resultados precisos y de alto valor para la startup que solicito nuestos servicios.


3. Tambien vamos a retomar un proyecto de analitica de linea internacional, que no se logro completar y que además culminarlos también lo  mejoraremos. Los prdecesores de este proyecto, lanzaron un test A/B,y luego lo abandonaron. Mediante las  especificaciones técnicas y los resultados de las pruebas, probaremos cambios relacionados con la introducción de un sistema de recomendaciones mejorado, para llegar a  conclusiones precisas y de alto valor que sobretodo nos de  una clara idea sobre si este cambio, esta generando comportaminetos diferentes entre los usuarios,o si encargados anteriores
sabian que no iba a resultar como epseraban y debido a ello lo abandonaron,


4. Finalmente, completaremos el pryecto principal que nos confio la empresa Callmemaby. La cual, considera que un operador es ineficaz si tiene una gran cantidad de llamadas entrantes perdidas
(internas y externas) y un tiempo de espera prolongado para las llamadas entrantes. Además, si se supone que un operador debe realizar llamadas salientes, 
un número reducido de ellas también será un signo de ineficacia. Mediante visualizasiones a lo largo del tiempo y la categorizasion de aoperadores basandonos en las metricas más  relevnates mencionadas anteriormente, evaluaremos el compórtamiento de los operadores para identificar a los mas ineficases, y tambien llevaremos a cabo ua prueba de hipótesis estadística.
  

Todas estas tareas idependintes, seran un emocinante y entretenido reto para mis habilidades como analista de datos ya que cada uno de los proyectos realizados y requeridos  por las empresas, requieren de cierta hablidad  de pensamineto critico y saber usar los datos en beneficio de la empresa, de esta manera abordare una a una las tareas cotidianas que un analista de datos tiene, y destacare en cda una de ellas, ya que me permitiran demostar que soy la mejor opcion que pudieron tomar a la hora de tomar decisiones importantes basandose en las recomnedaciones que proporcionare al final de cada proyecto 
indepnediente.

0.1 ES NECESARIO  CREAR UN ARCHIVO `.env`, para la coneccion a la base de datos en el proyecto de SQL. Llenando las siguintes variables para crear el motor de busqueda

```Python 
tripleten_sql_user=""
tripleten_sql_pwd=""
tripleten_sql_host=""
tripleten_sql_port=""
tripleten_sql_db=""
```

Asi como utlizar la libreria dotenv.

# pip install python dotenv

para utilizar la  funcion load_dotenv(), y conectarse correctamente a las base de datos, mediante el modulo create engine de la libreria sqlalchemy

# from sqlalchemy import create_engine 
# from dotenv import load_dotenv()

0.2  DE LA MISMA FORMA   DEBERA CREARSE UN AMBINETE VIRTUAL .venv para crear un espacio en el que nuestro codigo,
pueda ser ejecutado sin ningun error de dependencia y obtener los mismos resultados;Sigiendo los siguinetes pasos,
peimero para crear el ambiente.

# ```Python -m venv .venv```
se crea el ambinete VIRTUAL

# ```Python .venv\Scripts\activate```
se activa el ambiente virtual

# ```Python pip freeze > requirements.txt```
 medianete este comado, se verificara  ver qué paquetes están instalados y sus versiones locales;
 antes de instalar el archivo de requeriminetos, lo que te ayudará a identificar posibles conflictos o dependencias no deseadas.

# ```Python pip install requirements.txt``` 
 0.3 Luego se instala el  archivo de requerimientos para trabajar con las mismas veriones que utilice al ejecutar el codigo
  
VERSIONES Y DEPENDENCIAS UTILIZADAS:
```Python contourpy==1.3.0
cycler==0.12.1
fonttools==4.54.1
greenlet==3.1.1
kiwisolver==1.4.7
matplotlib==3.9.2
numpy==2.1.3
packaging==24.1
pandas==2.2.3
patsy==0.5.6
pillow==11.0.0
pyparsing==3.2.0
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
pytz==2024.2
scipy==1.14.1
seaborn==0.13.2
six==1.16.0
SQLAlchemy==2.0.36
statsmodels==0.14.4
typing_extensions==4.12.2
tzdata==2024.2 ```

0.4 Luego deberemos ejecutar cada uno de los archivos desde el directorio de nuestro repositorio

DEBIDO A QUE LOS ARCHIVOS DE DATOS ESTAN EN EL MISMO DIRECTOTIO DE LOS ARCHIVOS DE EJECUSION, ESTOS DEBERIAN LEERSE AL EJECURARLOS SIN NINGUN INCONVENIENTE.