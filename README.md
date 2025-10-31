# data-analytics-portfolio-case

Este repositorio demuestra mis habilidades como **analista de datos**, aplicadas en un entorno real con diferentes casos de negocio.  
Cada módulo representa un reto analítico independiente enfocado en **extracción, limpieza, análisis y comunicación de resultados** basados en datos reales de startups. 

A través de varios proyectos prácticos, evaluaré diferentes **KPI** de manera individual, brindando soporte analítico de alto valor a las empresas y startups que me confiaron sus datos.

---
## 🚀 Objetivos del proyecto

1. **Conexión a bases de datos (SQL + Pandas)**  
   Conexión segura a una base de datos PostgreSQL real para extraer y consultar datos relacionados con el comportamiento de usuarios de una aplicación de lectura digital.

2. **Preprocesamiento y optimización operativa (Callmemaby)**  
   Identificación de operadores con bajo desempeño mediante métricas clave de eficiencia y desempeño operativo.

3. **Análisis experimental (Test A/B)**  
   Evaluación de un test A/B abandonado por un equipo anterior.  
   Determinar si los cambios implementados modificaron el comportamiento de los usuarios o si los resultados eran previsibles.

4. **Evaluación de desempeño (Callmemaby)**  
   Detección de operadores ineficaces a partir de KPIs específicos, visualización temporal y pruebas estadísticas de hipótesis.

---

## 🧠 Conclusiones generales

Estos proyectos integran conocimientos de:
- Análisis exploratorio y descriptivo.
- SQL para consultas avanzadas.
- Python (pandas, numpy, matplotlib, seaborn, scipy).
- Pruebas estadísticas.
- Comunicación visual mediante dashboards interactivos (Tableau).

📄 [Explicación detallada del proyecto (documento técnico)](https://1drv.ms/b/c/75c608b03a43bf35/EZuSE_xWAuZLoCc2VUamYGEBYXiPYyLEe9MVovMmdWxwOA?e=NHceOs)  
📊 [Dashboard interactivo - Callmemaby en Tableau](https://public.tableau.com/views/DashboraddeduracinytipodellamadasCallmemaby/Dashboard1)

---

## ⚙️ Requisitos del entorno

Antes de ejecutar los scripts, asegúrate de tener **Python 3.10+** instalado.

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/code-ALX79/final_analitic_proyect.git
cd final_analitic_proyect

- Es importante ejecutar los siguientes comandos desde el mismo directorio donde se ha clonado este repositorio.

Para desplazarse al directorio del proyecto:

```sh
cd nombre_del_directorio

2️⃣ Crear y activar entorno virtual

1.1 Crear un entorno virtual

Se recomienda crear un entorno virtual .venv para garantizar un espacio de ejecución aislado, libre de errores de dependencia.

``` sh
# Crear entorno
python -m venv .venv

# Activar entorno (Windows)
.venv\Scripts\activate

# Activar entorno (Linux/Mac)
source .venv/bin/activate
```
3️⃣ Instalar dependencias

``` sh 
pip install -r requirements.txt

```
Si aún no existe un archivo de requerimientos, puedes generarlo así:
 
``` sh 
pip freeze > requirements.txt

``` 
Instalar dependencias desde el archivo:


Luego se instalara el  archivo de requerimientos para trabajar con las mismas dependecnias  utilizadas al ejecutar el codigo.

Deberemos primero mostar el contenido de nuestrois archivos, y  ejecutar cada uno de los estos desde el directorio de nuestro repositorio.
  DEBIDO A QUE LOS ARCHIVOS DE DATOS ESTAN EN EL MISMO DIRECTOTIO DE LOS ARCHIVOS DE EJECUSION, ESTOS DEBERIAN LEERSE AL EJECURARLOS SIN NINGUN INCONVENIENTE.

🔐 Variables de entorno

Crea un archivo .env en la raíz del proyecto con las siguientes variables para conectar tu base de datos:

``` Python 
tripleten_sql_user="usuario"
tripleten_sql_pwd="contraseña"
tripleten_sql_host="host"
tripleten_sql_port="puerto"
tripleten_sql_db="nombre_bd"
```
Ejemplo de conexión en Python:

``` Python
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
user = os.getenv("tripleten_sql_user")
pwd = os.getenv("tripleten_sql_pwd")
host = os.getenv("tripleten_sql_host")
port = os.getenv("tripleten_sql_port")
db = os.getenv("tripleten_sql_db")

engine = create_engine(f"postgresql://{user}:{pwd}@{host}:{port}/{db}")

```

▶️ Ejecución de los módulos
**Conexión a base de datos:**

``` sh 
python conection-t.py
```
**Consultas SQL:**

``` sh 
python queries.py

```
**Test A/B internacional:**

``` sh 
python project_test_A-B.py

```
**Evaluación de operadores:**

``` sh 
python project_telecom.py

```
🧪 Tecnologías utilizadas

Python 3.10+

- Pandas

- NumPy

- Matplotlib / Seaborn

- SQLAlchemy

- Dotenv

- SciPy

- Tableau

🤝 Contribución

**1. Haz un fork del repositorio.**

**2. Crea una nueva rama: git checkout -b feature/nueva-funcionalidad.**

**3. Realiza tus cambios y commitea: git commit -m "Descripción del cambio."**

**4. Envía un pull request para revisión.**
