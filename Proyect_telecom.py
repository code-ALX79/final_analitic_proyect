# %% [markdown]
# # 1.Proyecto Telecom. Ineficiencia de Operadores de CallMeMaby.

# %% [markdown]
# ## 2. Etapas del proyecto.

# %% [markdown]
# ### 1.Definir el Objetivo.

# %% [markdown]
# **EL OBEJTIVO PRINCIPAL DE ESTA TAREA ES IDENTIFIAR A LOS OPERADORES MAS INEFICADES DE LA EMPRESA CALLMEMABY, BASANDONOS EN LOS DATOS QUE NOS BRINDAN TANTO DE LOS OPERADORES COMO DE LOS CLIENTES. PARA ELLO, PRIMERAMENTE LIMPIAREMOS NUESTROS DATOS DE INCONTINGENCIAS INESPERADAS, PARA OBTENER RESULTADOS MAS PRECISOS.**
#
# **Esta informacion ayudara al equipo que esta desarrollando una nueva función que brindará a los supervisores y las supervisores información sobre los operadores menos eficaces.**
#
# ***Con base en este analisis los supervisores tomaran decisiones importantes para su equipo de trabajo que van desde un programa de capacitacion intensivo y personalizado para cada operador, hasta la toma de decisiones drasticas como presindir de los servicios  de un operador en caso de que presente constasntes niveles de ineficasia prologada.***

# %% [markdown]
# ### 1.2 Proponer Hipotesis

# %% [markdown]
# **CONSIDERAMOS LA UNA GRAN CANTIDAD DE LLAMADAS ENTRANTES PERDIDAS COMO UN INDICADOR DE INEFICASIA PARA CADA OPERADOR, YA SEAN ESTAS INTERNAS O EXTERNAS**
#
# **TAMBIEN UN TIEMPO DE ESPERA PROLOGADO ENTRE LLAMDAS PODRIA SER UN BUEN INDICADOR DE LA INEFICASIA DEL OPERADOR EN SI**
#
# **DEBIDO A QUE LOS OPERADORES TAMBIEN DEBEN HCAER LLAMDAS SALIENTES, UN UMERO REDUCIDO DE ESTAS LLAMADAS TAMBINE ES UN GRAN INDICADOR DE LA INEFICASIA DE LOS OPERADORES TELEFONICOS.**

# %% [markdown]
# ### 1.3 Plan de accion

# %% [markdown]
# ***Para llevar a cabo nuestras hipoteisis y lograr el obejetivo esperados es importante tener claro el plan de accion claro para obtener resultados objetivos.***

# %% [markdown]
# *Para esto podriamos visualizar la cantidad de llamadas de los operadores, y separar en grupos a los que tengan una mayor cantidad de los que tienen pocas llamadas en sus registros.*
#
# *Luego de este grupo con una cantidad de llamdas reducida, podriamos podriamos tambien analizar las llamadas entrantes que se perdieron en ambos grupos*
#
# *Tambien podriamos realizar visualizasiones para analizar la relacion entre la cantida de llamdas en general y el tiempo de espera entre cada una de ellas.*

# %% [markdown]
# ### Luego de definir un obejetivo claro, y proponer algunas hipotesis. Vamos a realizar las etapas obligatorias al trabajar con datos para su posterior analisis en este notebook

# %% [markdown]
# ### 1. Preprocesamineto de datos

# %% [markdown]
# *Importamos las librerias para este paso*

# %%
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns
import numpy as np
from scipy import stats

# %%
clmby = pd.read_csv('telecom_dataset_us.csv')
display(clmby.info(memory_usage='deep'))
display(clmby.head())

# %% [markdown]
# Tenemos un archivo con 9 columnas y mas de 50000 registros con un peso de aproximadamente 10.4 megabytes.
#
# Vamos ahora a verificar si tenemos valores ausentes o duplicados.

# %%
clmby.isna().sum()

# %% [markdown]
# Tenemos en este caso valores ausentes en la columna que indica si la llamada fue internal entre los operadores de un cliente o  no. En este caso no represnetan mas que 0.2% de los datos en esta columna. Sin embargo los 8172 operadores que faltan en la columna 'operator_id', si representan mas de  un 10% la totalidad de datos en esta columna.

# %% [markdown]
# En el caso de los datos ausentes de la columna del operador,'operator_id' vamos ha eliminarlos

# %%

clmby['internal'] = clmby['internal'].isnull()
clmby.isna().sum()


# %%
operator_counts = clmby['operator_id'].value_counts()
clmby['count'] = clmby['operator_id'].map(operator_counts)
clmby.head()


# %% [markdown]
# *Y para el los datos de operadores crearemos la columna [count], que cuanta la cantidad de registros que ha generado cada operador en el dataframe, lo cual nos sera muy util, para realizar calculos y visualizasiones proximante.*

# %% [markdown]
# Ahora vamos a aseguarnos de los datos duplicados y evaluar una descripcion  general e los datos.

# %%
clmby.duplicated().sum()

# %%
clmby.describe()

# %% [markdown]
# Tenemos algunos datos  duplicados, y tambien notamos buenas metricas en nuestra descripcion, en el caso de los duplicados, los eliminaremos de ser necesario para evitar resultados inexactos en nuestras conclusiones.

# %%
clmby = clmby.drop_duplicates()
display(clmby.duplicated().sum())

display(clmby.info(memory_usage='deep'))
display(clmby.head())

# %% [markdown]
# De esta manera tenemos un dataframe mas ligero al desasernos de valores ausentes y duplicados, y antes de pasar a evaluar el dataframe de clientes, vamos a verificar una ultima descripcion general de los datos.

# %%
clmby.describe()

# %% [markdown]
# **Observamos tambien, ciertas diferencias en comparacion con la anterior descripcion como en el comnteo de usuarios o la media de la cantidad de llamadas, los mismos resultados maximos y minimos asi como una desviacion estandar std. sin muchas alteraciones relevantes.**

# %% [markdown]
# ***Ahora realizaremos el mismo proceso con el Dataframe de clientes***

# %%
cllmemaby_clients = pd.read_csv('telecom_clients_us.csv')
display(cllmemaby_clients.info(memory_usage='deep'))
display(cllmemaby_clients.head())

# %% [markdown]
# En este dataframe tenemos 3 columnas que nos indican en id del usuario 'id', la tarifa de cada uno de los usuarios 'tariff_plan', asi como la fecha de registro de la clientela  con alrededor de 732 registros. Vamos a verificar datos ausentes y nulos asi como la decripcion de los datos.

# %%
cllmemaby_clients.isna().sum()

# %%
cllmemaby_clients.duplicated().sum()

# %% [markdown]
# Al verifcar que no tenemos valores ausentes o duplicados en este DataFrame, realizaremos una decripcion general de los datos y luego transformaremos la  columna con el registro de fecha de registro del cliente 'date_start', a formato datetime, para poder trabajar con ella en el futuro.

# %%
cllmemaby_clients.describe()

# %%
cllmemaby_clients['date_start'] = pd.to_datetime(
    cllmemaby_clients['date_start'], format='%Y-%m-%d')

# %%
display(cllmemaby_clients.info(memory_usage='deep'))
display(cllmemaby_clients.head())

# %% [markdown]
# **De esta forma obtenemos una tabla mas practica con la columna de la fecha de registro en formato datetime y con presision de nanosegundos, como modificasion mas importante para este dataframe de clientes.**

# %% [markdown]
# **Ahora realizaremos algunas visualizasions para tener una vision mejorada y mas practica las metricas mas importantes o las distribuciones de las mismas.**

# %%
grouped_data = clmby.groupby(['operator_id', 'date']).agg({
    'count': 'mean',
    'call_duration': 'mean',
    'calls_count': 'sum'})

grouped_data.columns = ['count', 'avg_call_duration', 'total_calls']

display(grouped_data)

# %% [markdown]
# *Para generar nuestro grafico de lineas para saber las gestiones telefonicas, creamos un dataframe con las columnas relevantes para realizar visualizasiones, y le añadimos la fecha para evaluar su comportamineto a los largo del tiempo,despues.*

# %%
sns.lineplot(x='count', y='total_calls', data=grouped_data, color='gray')
plt.title('Distribución de gestionnes telefonicas totales por operador')
plt.xlabel('gestion del operador')
plt.ylabel('Número total de llamadas')
plt.show()

# %% [markdown]
# **De esta forma observamos que de las veces que el operador realiza una gestion en el CallMeMaybe la mayoria son llamdas telefonicas,lo que quiere decir que entre menos gestiones tenga el operador, menos cantidad de llmadas realizadas tendra tambien.**

# %% [markdown]
# *Ahora generaremos un histograma para evualar la distribusion de llmadas por dia.Utilizaremos nuestro dataframe con las columnas necesarias para la evalucaion [grouped_data], para agrupar por fecha y de esta forma tambien sumar el total de llamadas realizadas y observarlas mejor en el grafico.*

# %%
clmby['date'] = pd.to_datetime(clmby['date'], format='ISO8601')
day_of_month = clmby['date'].dt.day
daily_calls = clmby.groupby(day_of_month)['calls_count'].sum()

display(daily_calls.head().reset_index())

plt.hist(daily_calls, bins=10, color='magenta')
plt.title('Distribución de llamadas totales por día')
plt.xlabel('Número total de llamadas')
plt.ylabel('dia del mes')
plt.show()

# %% [markdown]
# **Determinamos la ditribucion de llmadas a lo largo de los dias del mes mediante un histograma que nos indica un promedio ascilante entre las 20000, y 3000 llamadas realizadas en los primeros dias del mes**

# %% [markdown]
# *Ahora realizaremos Un mapa de calor o heatmap. En el que primeramente ingresamos una columna creada que calcula el tiempo de espera de la llamada; restando el timepo de la columna [total_call_duration] que tiene el timepode llamda inlcuyendo el timepo de espera de la llamda, con la columna [call_duration], que tienen la duracion de llamada sin incluir el timepo de espera. Para despues este resultado que corresponde al timepo de spera de cada llamada en minutos[tiempo_espera], correlacionarlo con la [call_duration], que tiene la duracion de llamada sin incluir el timepo de espera, y con la columna boleana [is_missed_call]; y de esta forma generar nuestro mapa de calor*

# %%
clmby['tiempo_espera'] = clmby['total_call_duration'] - clmby['call_duration']


correlation_matrix = clmby[['tiempo_espera',
                            'call_duration', 'is_missed_call']].corr()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor de Correlaciones')
plt.show()

# %% [markdown]
# *En este  mapa de calor  crean una variable de correlacion entre la columna que tiene el tiempo de espera de la llamda (columna que insetamos al dataframe calculando la diferencia entre ['call_duration], ['total_call_duration])coreelacionado estas metricas por las llamadas que soin o no perdidas[is_missed_call].*

# %% [markdown]
# **Determinamos de esta forma que los colores rojos intensos indican una fuerte correlacion positiva con las llamadas que no fueron perdidas y el resto de variables indicando que la duracion y de llamadas, tiene cierta correlacion positiva con estas llamadas no perdidas; pero sin embargo existe una correlacion negativa ente el tiempo de espera de  la llamada con la duracion de la misma, lo que nos puede llevar a pensar que un operador ineficaz debe tener  un tiempo de espera prolongado entre llamdas, para considaderse ineficiente.**

# %% [markdown]
# *Para evualuar las siguinetes metrcias, uniremos los dataframes de operadores y de clientes para tener una vision mas panoramica de los datos para obtner y comenzar a establecer los primeros paramettros para considerar a un operador como ineficaz.*

# %% [markdown]
# En primera instancia, evaluaremos la cantidad de llamdas pedidas y no perdidas que tenemos en nuestro dataframe y lo visualizaremos mejor mediante graficos de barras y de dispersion

# %%

display(clmby['is_missed_call'].value_counts())

# Gráfico de barras para comparar llamadas perdidas y no perdidas
plt.bar(['Perdidas', 'No perdidas'],
        clmby['is_missed_call'].value_counts(), color='gold')
plt.xlabel('Estado de la llamada')
plt.ylabel('Cantidad')
plt.show()

# Gráfico de dispersión entre calls_count e is_missed_call
plt.scatter(clmby['calls_count'], clmby['is_missed_call'], color='silver')
plt.xlabel('Número de llamadas')
plt.ylabel('Llamada perdida (1) o no perdida (0)')
plt.show()

# %% [markdown]
# **Determinamos de esta forma que existe mayor cantidad de llamdas perdidas que de llamdas no perdidas en nuestro Dataframe.**

# %% [markdown]
# Ahora agregaremos una columna que nos indique la taza de llamadas perdidas, para lo cual transformaremos a tipo numerico la columna ['is_missed_call'], para que poder dividirla entee la cantidad de llamdas y calcular la taza de llamadas perdidas.

# %%
clmby['is_missed_call'] = clmby['is_missed_call'].astype(
    int)  # Convertir a numérico
clmby['missed_call_rate'] = clmby['is_missed_call'] / clmby['calls_count']

clmby['average_call_duration'] = clmby['total_call_duration'] / \
    clmby['calls_count']

callme_maby_data = pd.merge(clmby, cllmemaby_clients, on='user_id')
display(callme_maby_data.head())
display(callme_maby_data.info(memory_usage='deep'))

# %% [markdown]
# *Ahora tenemos un dataframe conjunto, con la informacion, tanto de los clientes, asi como la informacion de las llamaras y operadores.Con este daframe ya podremos definir umbrales, y metricas para evaluar la eficasia o ineficasia de los operadores de callmemaby.
# En este caso, si quisieramos establecer que un sistema de puntuacion que evalue la eficiencia o ineficiencia de cada operador.Nos basariamos en la taza de llamdas perdidas que tiene este y en la duracion promedio de cada llamda, este puntaje [score] indicara un valor bajo si  tiene una cantidad de llamamas perdidas alta y una duracion prolongadad de llamdas y una puntuacion alta en el caso de que hayan demasiatas llamdas perdidas en [missed_call_rate] y una duracion lñarga de llamdas. D es esta forma podremos categorizar a los operadores como [Excelemte/Satisfactorio/Necesita Mejora]*

# %%
callme_maby_data['normalized_missed_call_rate'] = callme_maby_data['missed_call_rate'] / \
    callme_maby_data['missed_call_rate'].max()
callme_maby_data['normalized_avg_call_duration'] = 1 - \
    callme_maby_data['average_call_duration'] / \
    callme_maby_data['average_call_duration'].max()

callme_maby_data['score'] = 0.5 * callme_maby_data['normalized_missed_call_rate'] + \
    0.5 * callme_maby_data['normalized_avg_call_duration']

# Categorización (ejemplo)
callme_maby_data['performance'] = pd.cut(callme_maby_data['score'], bins=[
                                         0.3, 0.5, 0.7, 0.9], labels=['Excelente', 'Satisfactorio', 'Necesita mejora'])

callme_maby_data.head()

# %% [markdown]
# *basicamente esta funciion nos indica que, si tanto la tasa de llamadas perdidas como la duración promedio de las llamadas están por debajo de los umbrales establecidos, se considera que el operador es "Ineficiente".
# Si alguna de las dos métricas supera el umbral, se considera que el operador "Necesita mejora.*

# %% [markdown]
# Realizaremos un pequeño preprocesamiento de datos y verificaremos valores ausentes y duplicados en este dataframe completo, asi como la descripcion general del mismo y comprobaremos los tipo de datos que tenemos.

# %%
callme_maby_data.isna().sum()

# %% [markdown]
# *Para nuestra prueba de hipoteisis necesitaremos un dataframe sin valores ausentes, asi que  valos a liminarlos para no tener problemas con el test estadistico.*

# %%
callme_maby_data = callme_maby_data.dropna()
callme_maby_data.isna().sum()

# %% [markdown]
# *De esta forma obtenemos un dataframe sin valores asuentes en ninguna columnas, y con la gran mayoria de nuestros datos presnetes en todas ellas. Ahora verificaremos los tipos de datos de las columnas con las que estamos trabajando.*

# %%
display(callme_maby_data.head())
display(callme_maby_data.info(memory_usage='deep'))

# %% [markdown]
# *Ahora tenemos un dataframe que no tienen valores ausnetes y con informacion muy importante sobre la cual podremos realizar calculos practicos para determinar los operadores ineficinetes; agrupando por operador, definiendo humbrales segun metricas especificas, y realizando visualizasiones de los resultados obtenidos*

# %%
callme_maby_data['count_range'] = pd.cut(callme_maby_data['count'], bins=[
                                         20.0, 40.0, 60.0, 80.0], labels=['Bajo', 'Medio', 'Alto'])

sns.boxplot(x='count_range', y='missed_call_rate', data=callme_maby_data)
plt.xticks(rotation=45)
plt.show()

# %% [markdown]
# **Determinamos mediante el corte de la cantidad de llamdas de cada operador los humbrales que se consideran bajos, medios y altos para la cantidad de llamadas perdidas de cada operador**

# %% [markdown]
# Ahora, antes de realizar la prueba de hipotesis estadistica, primero filtratremos el dataframe, por la columna [performance], que indica el estado el operador segun el umbrar definido, basandonos en la duracion  promedio de la llamada y si en la taza de llamadas perdidas.

# %%
efficient_df = callme_maby_data[callme_maby_data['performance'] == 'Excelente']
satisfactory_df = callme_maby_data[callme_maby_data['performance']
                                   == 'Satisfactorio']
needs_improvement_df = callme_maby_data[callme_maby_data['performance']
                                        == 'Necesita mejora']

display(efficient_df.head())
display(efficient_df.info())

display(satisfactory_df.head())
display(satisfactory_df.info())

display(needs_improvement_df.head())
display(needs_improvement_df.info())


# %% [markdown]
# **Ahora tenemos dataframes separados por cada una de las categorias definidas previamnete que nos indican basicamatente cuales son los operadores que necesitan mejora, los que son satisfactorios, y los que segun los calculos, tienen excelentes resultados.Sin embago para realizar nuestra prueba de hipotesis estadisticas, vamos a utilizar el dataframe excelente y el satisfactorio, para evaluar si hay una significansia estadistica importante entre estos grupos de operadores, y definir si estan bien establecidas estas metricas.**

# %% [markdown]
# *Antes de realizar la prueba estadistica, realizaremos un grafico similar al atenriror, en el que se visualizaba la taza de llamdas perdidas en el dataframe total, sin embargo, ahora vamos a realizarlo por cadda uno de estos dataframes, filtrados por la columna performance, para rectificar nustras metricas*

# %%
mean_efficient = efficient_df['missed_call_rate'].mean()
mean_satisfactory = satisfactory_df['missed_call_rate'].mean()
mean_needs_improvement = needs_improvement_df['missed_call_rate'].mean()

categories = ['Excelente', 'Satisfactorio', 'Necesita Mejora']
values = [mean_efficient, mean_satisfactory, mean_needs_improvement]

plt.bar(categories, values, color='purple')
plt.xlabel('Categoría de Desempeño')
plt.ylabel('Tasa de Llamadas Perdidas')
plt.title('Comparación de Tasa de Llamadas Perdidas por Categoría')

# Mostrar el gráfico
plt.show()

# %% [markdown]
# **Los resultados se ven bien, ya que es logico pensar que los operadores con una menor taza de cancelacion de llamadas, son los mas eficinete y a mmedida que esta metrica va aumnetado, pues se desglosan las otras categorias.**

# %% [markdown]
# Ahora podremos realizar nustra prueba de hipostesis estaditicas enfocandonos en encontar diferencia estadisticamente significativa, entre los operadores con un resultado 'Excelente' y los operadores con un resultado satisfactorio.

# %% [markdown]
# ***(H0): No hay diferencia significativa en la tasa de llamadas perdidas entre los operadores clasificados como "Excelente" y "Satisfactorio".***
#
#  ***(H1): Sí hay una diferencia significativa en la tasa de llamadas perdidas entre los operadores clasificados como "Excelente" y "Satisfactorio".***

# %%

aplha = 0.05

t_statistic, p_value = stats.ttest_ind(
    efficient_df['missed_call_rate'], satisfactory_df['missed_call_rate'], equal_var=False)

display('t-statistic:', t_statistic)
display('p-value:', p_value)

# %% [markdown]
# **El valor p de la prueba en este caso es menor que el avlor de alpha de signnificancia, el cual; al ser superado nos llevaria a una acepatcion de la hipotesist nula. Pero como es mejor a este pues nustra prueba de hipotesis alternativa, que nos indica que efecftivamente** ***hay una diferencia significativa en la tasa de llamadas perdidas entre los operadores clasificados como "Excelente" y "Satisfactorio"*** **es la correcta**

# %% [markdown]
# LINK A LA PRESENTACION DE PROYECTO: https://1drv.ms/b/c/75c608b03a43bf35/EZuSE_xWAuZLoCc2VUamYGEBYXiPYyLEe9MVovMmdWxwOA?e=cLA2YN
#
# LINK  AL DASHBOARD: https://public.tableau.com/views/DashboraddeduracinytipodellamadasCallmemaby/Dashboard1?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
