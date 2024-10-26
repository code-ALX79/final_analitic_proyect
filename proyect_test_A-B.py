
# # Proyecto de Test A/B

# objetivos del estudio

# Segun las especificasiones tecniccas que tenemos nuestro proyecto consiste en analizar una prueba A/B abandonada a mitad de camino.
# Esto puede ser un desafío interesante y revelado, pero vamos ha ser precisos y breves con los objetivos y solciones especificas para obtner un excelente resultado.

# Prueba: Se introdujo un nuevo sistema de recomendaciones en un grupo de usuarios (grupo B) para mejorar la conversión en diferentes etapas del embudo de compra.
# Hipótesis: Se esperaba que el grupo B tuviera una tasa de conversión al menos 10% mayor en cada etapa del embudo comparado con el grupo control (A).
# Objetivo:Comprobar si se ha realizado correctamente y analizar los resultados.Para determinar si estamos obteniendo resultados favorables,
#  y determinar si el grupo (B), en realidad tiene   el 10% de aumento en la cantidad de eventos a comparacion con el grupo de control.

#  Explora los datos

# 1.Importamos las librerias necesarias

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.stats.proportion as sm
import itertools


# cargar los datos
users = pd.read_csv("final_ab_new_users.csv")
events = pd.read_csv("final_ab_events.csv")
participants = pd.read_csv("final_ab_participants.csv")
marketing_events = pd.read_csv("ab_project_marketing_events.csv")

# mostrar la infromacion general y las primeras 5 filas del datarame sobre todos los nuevos usuarios que se registraron durante el período de la prueba
print(users.info(memory_usage='deep'))
print(users.head())


print(users.isna().sum())
print(users.duplicated().sum())

# De esta forma nos sersioramos que no existan valores ausentes ni duplicados en el Dataframe de usuarios y podremos trabajar con el sin tener este tipo problemas

# mostrar la infromacion general y las primeras 5 filas del datarame tiene los eventos realizados por los nuevos usuarios durante el período de la prueba
print(events.info(memory_usage='deep'))
print(events.head())

print(events.isna().sum())
print(events.duplicated().sum())

# Asi mismo verificamos estas metricas importantes en el Dataframe de eventos ye fectivamente no  tenmos problemas de valores duplicados o ausentes en este Dataframe tampoco.

# mostrar la infromacion general y las primeras 5 filas del datarame que vincula a los usuarios con sus respectivos grupos de prueba (A o B).
print(participants.info(memory_usage='deep'))
print(participants.head())

print(participants.isna().sum())
print(participants.duplicated().sum())

# De la misma forma verificamos que no hayan valores ni ausentes ni dupliacdos tampoco en el dataframe de participantes de los test A/B

# mostrar la infromacion general y las primeras 5 filas del datarame con  las campañas de marketing que se ejecutaron durante el período de la prueba A/B
print(marketing_events.info(memory_usage='deep'))
print(marketing_events.head())

marketing_events.isna().sum()

# De esta forma ahora nos sersioramos que en este dataframe, no haya valores ausentes.

marketing_events.duplicated().sum()

# Y asi verificamos que tampoco hayan valores duplicados en este dataframe

marketing_events.describe()


# 1.Uniremos los datasets final_ab_new_users_upd_us.csv y final_ab_participants_upd_us.csv por el user_id para obtener un dataset completo de usuarios y sus grupos de prueba,
# para despues realizar otro .merge() y unir el dataframe de  eventos.

all_data = users.merge(participants, on='user_id').merge(events, on='user_id')
print(all_data.info())
print(all_data.head())

# Hemos creado el dataframe all_data con todas las columna y datos pertinentes para su analisis.Haremos el preprocesamineto de datos con esta tabla.
all_data.isna().sum()

all_data.duplicated().sum()

# Nos sersioramos de que no hayan valores duplicados antes de revisar la informacion general de cada columna.

all_data.describe()

all_data.head()

# La descripcion general de los datos solo nos da inforamcion de la columna 'details',
# ya que es un metodo que descibe columnas en formato numerico o en este caso un numero de coma flotante y esta es la unica columna que con este formato,
# asi que este no es el mejor metodo para describir  nuestros datos. Asi que a continuacion cambiaremos los formatos de las columnas para visualizar metricas especificas.
all_data['event_dt'] = pd.to_datetime(all_data['event_dt'])
all_data['first_date'] = pd.to_datetime(all_data['first_date'])
all_data.info()

# Al trasformar las columnas de tiempon al formato correcto, podremos realizar calculos entorno al tiempo en el que se dio el evento.Por ejemplo,
# si queremos calcular el tiempo transcurrido desde la fecha de inscripcion hasta el evento, procederiamos de la siguiente manera.

all_data['time_to_event'] = all_data['event_dt'] - all_data['first_date']
print(all_data.head())
print(all_data.info(memory_usage='deep'))

# Ahora no solo tenemos la fecha de inscripcion del usuario asi como la fecha del evento realizado por eel usuario,
# si no tambien generamos una columna en formato timedelta, con precision de nanosegundos,
# que nos indica el tiempo transcurrido desde la inscripcion hasta que se efectuo el primer evento importante del susuario.

# Aanálisis exploratorio de datos:

# En este apartado, vamos a estudiar la conversión en las diferentes etapas del embudo.

conversion_rates = all_data.groupby(
    ['group', 'event_name']).size().reset_index(name='counts')
conversion_rates['total_users'] = conversion_rates.groupby('group')[
    'counts'].transform('sum')
conversion_rates['conversion_rate'] = conversion_rates['counts'] / \
    conversion_rates['total_users']

# Ahora,creamos una pivot table para visualizar las tasas de conversión.
conversion_pivot = conversion_rates.pivot_table(
    index='group', columns='event_name', values='conversion_rate')
print(conversion_pivot)

# Ahora, calcularemos la dritribusion de los eventos en cada uno de los grupos del test A/B para verificar si se encuentran distribuidos equitativamente

events_per_user = all_data.groupby(
    ['group', 'user_id']).size().reset_index(name='event_count')
sns.boxplot(x='event_count', y='group', hue='group', data=events_per_user)

# Determinamos de esta forma que el numero de eventos se encuentra ditribuido de forma equitativa entre los grupos del test A/B,
# proporcionados, ya que apesar de que el grupo de control tiene mayor cantidad e valores atipicos; pues las cajas tienen la misma media.

# Para observar de forma mas precisa las diferencias entre los eventos y los grupos crearemos un grafico de densidad para tener una mejor perspectiva.

all_data['time_to_event_seconds'] = all_data['time_to_event'].dt.total_seconds()
sns.kdeplot(data=all_data, x='time_to_event_seconds', hue='group', fill=True)
plt.show()

# De esta forma tambien obtenemos un grafico  de densidad que nos da una visualización clara de cómo se distribuye el tiempo transcurrido hasta el evento en diferentes grupos y para diferentes eventos, notando una mejor distribusion para el grupo de control(A).*

# Como en el analisis exploratorio anterior verificamos que no existan datos duplicados en este dataframe, determinamos que No hay usuarios que esten presentes en ambas pruebas como tal.*** *asi que vamos a salatarnos esa parte para pasar a verificar la distribusion de los eventos por dia, mediante un grafico de linea.*

grouped_data = all_data.groupby(
    'event_dt').size().reset_index(name='event_count')
df_for_plot = grouped_data.copy()
df_for_plot['event_day'] = df_for_plot['event_dt'].dt.day
print(df_for_plot.head())
sns.lineplot(x='event_day', y='event_count', data=df_for_plot)
plt.title('Eventos por día')
plt.xlabel('Día')
plt.ylabel('Número de Eventos')
plt.show()

# Se crea un nuevo dataframe agrupando los datos por la fecha del evento y se cuenta la cantidad de eventos, asignando el resultado a la columna 'event_day',

#  luego creamos una copia  llamada 'data_for_plot', para evitar modificar el DataFrame original y la mostramos, para finalmente crear un grafico de linea basado en este dataframe.
# De esta forma determinamos el numero de eventos por dia, y notamos que tenemos una linea que parece ser continua pero al final del mes Acsiende hasta alcanzar la mayor cantidad de eventos el dia 30.

# Antes de pasar al analisis del desde A/b y como aparatado adicional, eliminaremos la columna 'details' de nuestro dataframe ya que conteiene valores ausentes y al eliminar estas filas,
#  estariamos omitiendo una importante cantidad de datos en otras columnas. Asi que como solo hay valores ffaltantes en esta columnas; se crea un Dataframe que no la contenga.

all_data = all_data.drop('details', axis=1)

print(all_data.head())
print(all_data.isna().sum())

# Utilizando el metodo .drop() acompañado del parametro axis, eliminamos la columna con valores nulo de nuestro dataframe, para de esta manera realizar y evaluar los resultados del test A/B.

# %%
total_usuarios_por_grupo = all_data.groupby(
    'group')['user_id'].nunique().reset_index(name='users_total')
conversion_pivot = conversion_pivot.merge(
    total_usuarios_por_grupo, on='group', how='left')
print(conversion_pivot.head())
print(conversion_pivot.info())

#  Evaluar los resultados de la prueba A/B

# 1. Definimos las hipotesis nula y la alternativa.

# H0: La proporción de usuarios que completan cada etapa del embudo es igual en ambos grupos (A y B).
# H1: La proporción de usuarios que completan al menos una etapa del embudo es diferente entre los grupos A y B.

# Para este apartado evaluaremos las tazas de coversion calculadas anteriormente en el analisis exploratorio de datos,
# mediante una funcion que itere sobre las osibles conbinaciones de grupos y eventos en este Dataframe.


# Definimos una funcion que itera sobre los drupos de la preva A/b y utilizamos intertools para acceder a todaas las posibles combinaciones grupos ene los eventos,
# para luego iterar sobre los grupos y convertirlos en variables numericas 0, para el grupo A y 1 para el grupo B.
# realizamos la peruba Z  en cada evento por idenpendiente y nuestro resltado es un datacframe cuyas columnas contiene el grupo del tetst A/B,
# asi como el evento con su respectivo significancia estadisticas (Z), y el valor p de cadad evento.


def realizar_prueba_z(conversion_pivot, alpha=0.05, effect_size=0.1, events=None):
    """
    Realizamos una prueba Z para comparar las proporciones de conversión entre dos grupos.

    Args:
        conversion_pivot: Es la tabla pivote con las tasas de conversión.
        alpha: Es el Nivel de significancia.
        effect_size: correspon de al amaño del efecto esperado.
        events: Es la lista de eventos a comparar.

    Returns:
        Resultados de las pruebas Z.
    """

    results = []
    for group1, group2 in itertools.combinations(conversion_pivot.index, 2):
        for event in events:
            # Obtener los conteos de éxitos y tamaños de muestra
            successes = conversion_pivot.loc[[group1, group2], event]
            nobs = conversion_pivot.loc[[group1, group2], 'users_total']

            # Realizar la prueba Z
            z_stat, p_value = sm.proportions_ztest(
                count=successes, nobs=nobs, alternative='two-sided')

            results.append([group1, group2, event, z_stat, p_value])

    return pd.DataFrame(results, columns=['Grupo 1', 'Grupo 2', 'Evento', 'Z', 'p-value'])


results_df = realizar_prueba_z(conversion_pivot, events=[
                               'login', 'product_cart', 'purchase'])
print(results_df)

# Devido a que los  p valores de cada una de las tazas de conversion obtenidas son mayores que el nivel alpha de significansia estadistica.No hay evidencia estadísticamente significativa para rechazar la hipótesis nula en ninguna de las comparaciones.
# Por los cual se concluye que:** ***LA PROPORCION DE USUARIOS QUE COMPLETAN CADA ETAPA DEL EMBUDO ES IGUAL EN AMBOS GRUPOS;(A y B).
# Ya que no se encontraron diferencias significativas entre las tazas de conversion para ninguno de los eventos ('login','product_cart','puchase').

# **Basados en estos resultados, podríamos concluir que el nuevo sistema de recomendaciones (Grupo B) no tuvo un impacto significativo en las tasas de conversión en comparación con el sistema actual (Grupo A.
