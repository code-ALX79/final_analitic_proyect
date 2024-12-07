# final_proyect_tripleteen.

En este repositorio voy a poner a prueba mis habilidades como analista aprendidas en todo mi trayecto como estudiante, en un caso real de analítica de datos. Mediante varios proyectos  practicos, que evaluarán cada una de mis KPI por separado, brindando una excelente soporte a la corporación que solicitó mis servicios. 

1. PRIMERO nos vamos a conectar a una base de datos para realizarle  consultas mediante SQL de forma idependiente al proyecto principal ya que en esta ocasion una startup, que aprevecho el coronavirus 
para desarrollar una aplicación para los amantes de los libros, debido a que las personas en este tiempo recurrieron a soluciones saludables para quedarse en casa. Nos han brindado una base de datos de uno de los servicios que compiten en este mercado.  medinete pandas y SQL,llegaremos a resultados precisos y de alto valor para la startup que solicito nuestos servicios.

2. Despues realizaremos un preprocesamiento de datos para una empresa que intenta desarrollar una nueva función que brindará a los supervisores y las supervisoras información sobre los operadores menos eficaces, para que puedan tomar decisiones importantes sobre aquellos operadores menos eficientes.

3. Tambien vamos a retomar un proyecto de analitica de linea internacional, que no se logro completar, y que además de culminarlo también lo  mejoraremos. Los prdecesores de este proyecto, lanzaron un test A/B, y luego lo abandonaron. Mediante las  especificaciones técnicas y los resultados de las pruebas, probaremos cambios relacionados con la introducción de un sistema de recomendaciones mejorado, para llegar a  conclusiones precisas y de alto valor que sobretodo nos de  una clara idea sobre si este cambio, esta generando comportaminetos diferentes entre los usuarios, o si los  encargados anteriores
sabian que no iba a resultar como epseraban y debido a ello lo abandonaron,


4. Finalmente, completaremos el pryecto principal que nos confio la empresa Callmemaby. La cual, considera que un operador es ineficaz si tiene una gran cantidad de llamadas entrantes perdidas
(internas y externas) y un tiempo de espera prolongado para las llamadas entrantes. Además, si se supone que un operador debe realizar llamadas salientes, 
un número reducido de ellas también será un signo de ineficacia. Mediante visualizasiones a lo largo del tiempo y la categorizasion de aoperadores basandonos en las metricas más  relevnates mencionadas anteriormente, evaluaremos el compórtamiento de los operadores para identificar a los mas ineficases, y tambien llevaremos a cabo ua prueba de hipótesis estadística.
  

Todas estas tareas idependintes, seran un emocinante y entretenido reto para mis habilidades como analista de datos ya que cada uno de los proyectos realizados y requeridos  por las empresas, requieren de cierta hablidad  de pensamineto critico y saber usar los datos en beneficio de la empresa, de esta manera abordare una a una las tareas cotidianas que un analista de datos tiene, y destacare en cda una de ellas, ya que me permitiran demostar que soy la mejor opcion que pudieron tomar a la hora de tomar decisiones importantes basandose en las recomnedaciones que proporcionare al final de cada proyecto 
indepnediente.

0.1 ES NECESARIO  CREAR UN ARCHIVO `.env`, para la coneccion a la base de datos en el proyecto de SQL. Llenando las siguintes variables para crear el motor de busqueda

``` Python 
tripleten_sql_user=""
tripleten_sql_pwd=""
tripleten_sql_host=""
tripleten_sql_port=""
tripleten_sql_db=""
```

Asi como utlizar la libreria dotenv.

``` Python
pip install python dotenv
```

para utilizar la  funcion load_dotenv(), y conectarse correctamente a las base de datos, mediante el modulo create engine de la libreria sqlalchemy

``` Python 
from sqlalchemy import create_engine
```

``` Python 
from dotenv import load_dotenv()
```

0.2  DE LA MISMA FORMA   DEBERA CREARSE UN AMBINETE VIRTUAL .venv para crear un espacio en el que nuestro codigo,
pueda ser ejecutado sin ningun error de dependencia y obtener los mismos resultados;Sigiendo los siguinetes pasos,
peimero para crear el ambiente.

``` Python 
-m venv .venv
```
se crea el ambinete VIRTUAL

```Python 
.venv\Scripts\activate
```
se activa el ambiente virtual

``` Python 
pip freeze > requirements.txt
```
 medianete este comado, se verificara  ver qué paquetes están instalados y sus versiones locales;
 antes de instalar el archivo de requeriminetos, lo que te ayudará a identificar posibles conflictos o dependencias no deseadas.

``` Python 
pip install -r requirements.txt
``` 

 0.3 Luego se instala el  archivo de requerimientos para trabajar con las mismas dependecnias  utilizadas al ejecutar el codigo.
0.4 Luego deberemos ejecutar cada uno de los archivos desde el directorio de nuestro repositorio
DEBIDO A QUE LOS ARCHIVOS DE DATOS ESTAN EN EL MISMO DIRECTOTIO DE LOS ARCHIVOS DE EJECUSION, ESTOS DEBERIAN LEERSE AL EJECURARLOS SIN NINGUN INCONVENIENTE.

# 1.1 Ejecuatar el archivo conection-t.py

 Este archivo compacta el codigo neceario para conectarse a la base de datos, desde la cual realizaremos nuestras consultas. Para su correcta ejecusion,
 sera importante, que llenemos nuestars credenciales en el arcivo de variables de ambiente .env mencionado con aterioridad. especifiicando, ademas de su usuario y comtraseña tambien la direccion del servidor de la base de datos, o Host. el numero de puerto en el que se esta ecuchando el servidor de la bse de datos, asi como el nommbre de la misma, en la estructura:

 ``` Python 
tripleten_sql_user=""
tripleten_sql_pwd=""
tripleten_sql_host=""
tripleten_sql_port=""
tripleten_sql_db=""
```
El atchivo conectyion_t.py, cuenta con una consulta de prueba que traera las 5 primeas filas de la base de datos al ser ejecutada. Esto fue eimplementado en este archivo, comprobar su correcto funsionamiento.

``` query = pd.read_sql("SELECT * FROM public.books LIMIT 5", con=engine)
print(query)
```
si el reessultado de esta linea de codigo son las 5 primeras filas de nuestra base de datos. Entonces podremos pasar a ejecutar el siguinete archivo de datos.

# 1.2 Ejecuatar el queries.py
``` Python 
code queries.py
```

Despues de haber comprobado nuestro arcchivo de coneccion a la base de datos funsiona, podremos ejecutar nuestro archivo de consuktas a la tabla de datos respondiendo los siguinetes requerimientos.

  1.-el número de libros publicados después del 1 de enero de 2000;  query_1.
  2.-el número de reseñas de usuarios y la calificación promedio para cada libro; query_2.
  3.-a editorial que ha publicado el mayor número de libros con más de 50 páginas query_3. Esto ayudara tambien a a excluir folletos y publicaciones similares de tu análisis
  3.-El autor que tiene la más alta calificación promedio del libro;  query_4.
  4.-El número promedio de reseñas de texto entre los usuarios que calificaron más de 50 libros; query_5
 
 EN ESTE APARTADO LAS HABILIDADES CON SQL ADQUIRIDAS EN PROYECTOS Y LECIIONES SON PUESTA A PRUEBA CON REQUERIMIENTOS REALES DE UNA STARTUP, TENR UNA EXCELENTE CRECIEMINETO Y MEJORANDO EL FUNCIONAMINETO DE LA MISMA.

# 2. Ejecuatr el archivo project_test_A-B.py
  ``` Python 
code proyect_testA-B.py
```

Entonces podremos pasar a ejecuatar nuestro archivo de test A/B, el cual tiene ocomo objetivo econtar un resultado de comportamiento diferente,
al grupo de control en los usuarios al que se les aplico el test. Aunque se esta retomando un proyecto ateriomente postulado, debemos describir nuestros obejivos 
y realizar un analisis expoloratorio de datos, solo asi podremos asegurarnos que tendremos datos correctos. Para seguir con el archivo de ejecusion lo siguinete sera;

1.- Estudiar la conversión en las diferentes etapas del embudo

2.- Evaluar los resultados de la prueba A/B

3.- Describir tus conclusiones con respecto a la etapa EDA y los resultados de la prueba A/B

CADA UNO DE ESTPS ITEMS TIENE VARIAS PREGUNTAS A RESPONDER, LAS CUALRES SERAN GENERADA, EXPLORADAS Y RESPONDIDAS EN EL MISMO ARCHIVO; MEDIANTE UNA DESCRIPCION EN MARKDOWN BACO CADA CELDA DE EJECUSION DEL CODIGO.

# 3. Ejecutar el archivo project_telecom.py
``` Python 
code proyect_telecom.py
```
Al ejecutar este archivo de proyecto general se observara los pasos y procesos a realizar ordenados y puntualedsa medida que se van desarrolando las variables necesarias, utilizaremos el analisis exploratorio de datos EDA, y algunas graficas para obtner nuestras propias conslusiones meediante los siguinetes procesos:
 
- realizar el análisis exploratorio de datos
- Identificar operadores ineficaces
- Prueba las hipótesis estadísticas

en estos items se utilizaran graficas interactivas para una mejor visibilidad y cuando sea ejecutado, el archivo descrbira de forma precisa los resultados que se iran obteniendo gradualmente.

En el siguiente link, se observara una explicasion detallada del desarrollo y resolucion del proyecto, especificando los resultados obtenidos en el mismo.
 https://1drv.ms/b/c/75c608b03a43bf35/EZuSE_xWAuZLoCc2VUamYGEBYXiPYyLEe9MVovMmdWxwOA?e=NHceOs

En el siguinte link se observara un Dashboard de la duracion de llamda con avrios graficos explicativos que permitiran filtrar y tener una vision mas puntual sobre este item importente.
https://public.tableau.com/views/DashboraddeduracinytipodellamadasCallmemaby/Dashboard1?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link.