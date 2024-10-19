# %% [markdown]
# Hola &#x1F600;
#
# Soy **Hesus Garcia**  como "Jesús" pero con H. Sé que puede ser confuso al principio, pero una vez que lo recuerdes, ¡nunca lo olvidarás! &#x1F31D;	. Como revisor de código de Triple-Ten, estoy emocionado de examinar tus proyectos y ayudarte a mejorar tus habilidades en programación. si has cometido algún error, no te preocupes, pues ¡estoy aquí para ayudarte a corregirlo y hacer que tu código brille! &#x1F31F;. Si encuentro algún detalle en tu código, te lo señalaré para que lo corrijas, ya que mi objetivo es ayudarte a prepararte para un ambiente de trabajo real, donde el líder de tu equipo actuaría de la misma manera. Si no puedes solucionar el problema, te proporcionaré más información en la próxima oportunidad. Cuando encuentres un comentario,  **por favor, no los muevas, no los modifiques ni los borres**.
#
# Revisaré cuidadosamente todas las implementaciones que has realizado para cumplir con los requisitos y te proporcionaré mis comentarios de la siguiente manera:
#
#
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si todo está perfecto.
# </div>
#
# <div class="alert alert-block alert-warning">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si tu código está bien pero se puede mejorar o hay algún detalle que le hace falta.
# </div>
#
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class=“tocSkip”></a>
# Si de pronto hace falta algo o existe algún problema con tu código o conclusiones.
# </div>
#
# Puedes responderme de esta forma:
# <div class="alert alert-block alert-info">
# <b>Respuesta del estudiante</b> <a class=“tocSkip”></a>
# </div>
#
# </br>
#
# **¡Empecemos!**  &#x1F680;
#
#
#

# %% [markdown]
# # Proyecto de Test A/B

# %% [markdown]
# ## Describe los objetivos del estudio

# %% [markdown]
# **Segun las especificasiones tecniccas que tenemos nuestro proyecto consiste en analizar una prueba A/B abandonada a mitad de camino. Esto puede ser un desafío interesante y revelado, pero vamos ha ser precisos y breves con los objetivos y solciones especificas para obtner un excelente resultado.**

# %% [markdown]
# ***Prueba: Se introdujo un nuevo sistema de recomendaciones en un grupo de usuarios (grupo B) para mejorar la conversión en diferentes etapas del embudo de compra.***
#
# ***Hipótesis: Se esperaba que el grupo B tuviera una tasa de conversión al menos 10% mayor en cada etapa del embudo comparado con el grupo control (A).***
#
# ***Objetivo:Comprobar si se ha realizado correctamente y analizar los resultados.Para determinar si estamos obteniendo resultados favorables y determinar si el grupo (B), en realidad tiene   el 10% de aumento en la cantidad de eventos a comparacion con el grupo de control.***

# %% [markdown]
# ### Explora los datos

# %% [markdown]
# * *1.Importamos las librerias necesarias*

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import statsmodels.stats.proportion as sm
import itertools

# %%
# cargar los datos
users = pd.read_csv("final_ab_new_users.csv")
events = pd.read_csv("final_ab_events.csv")
participants = pd.read_csv("final_ab_participants.csv")
marketing_events = pd.read_csv("ab_project_marketing_events.csv")

# mostrar la infromacion general y las primeras 5 filas del datarame sobre todos los nuevos usuarios que se registraron durante el período de la prueba
display(users.info(memory_usage='deep'))
display(users.head())

# %%
display(users.isna().sum())
display(users.duplicated().sum())

# %% [markdown]
# *De esta forma nos sersioramos que no existan valores ausentes ni duplicados en el Dataframe de usuarios y podremos trabajar con el sin tener este tipo problemas*

# %%
# mostrar la infromacion general y las primeras 5 filas del datarame tiene los eventos realizados por los nuevos usuarios durante el período de la prueba
display(events.info(memory_usage='deep'))
display(events.head())

# %%
display(events.isna().sum())
display(events.duplicated().sum())

# %% [markdown]
# *Asi mismo verificamos estas metricas importantes en el Dataframe de eventos ye fectivamente no  tenmos problemas de valores duplicados o ausentes en este Dataframe tampoco.*

# %%
# mostrar la infromacion general y las primeras 5 filas del datarame que vincula a los usuarios con sus respectivos grupos de prueba (A o B).
display(participants.info(memory_usage='deep'))
display(participants.head())

# %%
display(participants.isna().sum())
display(participants.duplicated().sum())

# %% [markdown]
# *De la misma forma verificamos que no hayan valores ni ausentes ni dupliacdos tampoco en el dataframe de participantes de los test A/B*

# %%
# mostrar la infromacion general y las primeras 5 filas del datarame con  las campañas de marketing que se ejecutaron durante el período de la prueba A/B
display(marketing_events.info(memory_usage='deep'))
display(marketing_events.head())

# %%
marketing_events.isna().sum()

# %% [markdown]
# *De esta forma ahora nos sersioramos que en este dataframe, no haya valores ausentes.*

# %%
marketing_events.duplicated().sum()

# %% [markdown]
# *Y asi verificamos que tampoco hayan valores duplicados en este dataframe*

# %%
marketing_events.describe()

# %% [markdown]
# Tenemos buenas metricas y este pequeño preprocesamineto lo hicimos en este dataframe por que lo vammos a dejar de lado y es un recurso de la empresa para hacer uso de el cuando sea necesario.

# %% [markdown]
# **Los datos se ven bien y el dataframe que mas espacio ocupa es el de eventos, pero para realizar un analisis exploratorio mas practico, realizaremos la union de estos dataframes, para verificar valores ausentes/nulos y observar una descripcion general de nuestros datos**

# %% [markdown]
# *1.Uniremos los datasets final_ab_new_users_upd_us.csv y final_ab_participants_upd_us.csv por el user_id para obtener un dataset completo de usuarios y sus grupos de prueba,para despues realizar otro .merge() y unir el dataframe de  eventos.*

# %%
all_data = users.merge(participants, on='user_id').merge(events, on='user_id')
display(all_data.info())
display(all_data.head())

# %% [markdown]
# *Hemos creado el dataframe all_data con todas las columna y datos pertinentes para su analisis.Haremos el preprocesamineto de datos con esta tabla.* ***Hay que tomae en cuenta que la mayoria de datosson de tipo objeto, asi que deberemos cambiar de formato algunas columnas, despues de verificar la descripcion general de esta nbla completa y compacta.***

# %% [markdown]
# <div class="alert alert-block alert-danger"> <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# El proceso de unir los datasets está bien planteado, pero hay un error crítico en la columna event_dt cuando la transformas a timedelta. La función pd.to_timedelta se usa para convertir diferencias de tiempo, pero aquí estás calculando una diferencia entre dos columnas de tipo datetime. En lugar de usar pd.to_timedelta, simplemente deberías calcular la diferencia directamente usando all_data['event_dt'] - all_data['first_date'], ya que este proceso ya genera un formato timedelta.
#
# </div>

# %%
all_data.isna().sum()

# %% [markdown]
# **Notamos que en la columna detalles que nos da infromacion adicional del evento en especifico tenemos alderedor de 87984 valores ausentes, esto se debe a que  14000 de los eventos fueron efectuados sin mayor detalle.**
#
# ***No vamos a eliminar estos valores de esta columna,por que a pesar de que no considero importante los adicionales de un evento si no solo el evento en particular. Pues si eliminamos las filas que tiene valores ausentes en esta columna pues tambien podrian elimiarse valores importantes de otras columnas. Asi que haremos la eliminacion de estos valores de ser necesario solamente.***

# %%
all_data.duplicated().sum()

# %% [markdown]
# Nos sersioramos de que no hayan valores duplicados antes de revisar la informacion general de cada columna.

# %%
all_data.describe()

# %%
all_data.head()

# %% [markdown]
# *La descripcion general de los datos solo nos da inforamcion de la columna 'details', ya que es un metodo que descibe columnas en formato numerico o en este caso un numero de coma flotante y esta es la unica columna que con este formato, asi que este no es el mejor metodo para describir  nuestros datos. Asi que a continuacion cambiaremos los formatos de las columnas para visualizar metricas especificas.*

# %%
all_data['event_dt'] = pd.to_datetime(all_data['event_dt'])
all_data['first_date'] = pd.to_datetime(all_data['first_date'])
all_data.info()

# %% [markdown]
# Al trasformar ls columnas de tiempon al formato correcto, podremos realizar calculos entorno al tiempo en el que se dio el evento.Por ejemplo, si queremos calcular el tiempo transcurrido desde la fecha de inscripcion hasta el evento, procederiamos de la siguiente manera.

# %%
all_data['time_to_event'] = all_data['event_dt'] - all_data['first_date']
display(all_data.head())
display(all_data.info(memory_usage='deep'))

# %% [markdown]
# **Ahora no solo tenemos la fecha de inscripcion del usuario asi como la fecha del evento realizado por eel usuario, si no tambien generamos una columna en formato timedelta, con precision de nanosegundos, que nos indica el tiempo transcurrido desde la inscripcion hasta que se efectuo el primer evento importante del susuario.**

# %% [markdown]
# <div class="alert alert-block alert-success"> <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# El proceso de carga de datos está bien organizado, mostrando claramente los pasos para inspeccionar la información general y realizar verificaciones básicas como valores nulos y duplicados. Esto es importante para garantizar que los datos estén en buen estado antes de continuar con el análisis.
#
# </div> <div class="alert alert-block alert-warning"> <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Aunque los pasos son correctos, hay algunos detalles que podrías mejorar. Por ejemplo, en lugar de hacer la verificación de valores duplicados y nulos solo en el dataframe marketing_events, sería útil hacerlo en todos los dataframes. Esto te aseguraría que no haya problemas en los datos que utilizarás más adelante.
#
# </div>

# %% [markdown]
# ### Aanálisis exploratorio de datos:

# %% [markdown]
# ***En este apartado, vamos a estudiar la conversión en las diferentes etapas del embudo.***

# %% [markdown]
# *Agrupando los datos por grupo (A o B) y por tipo de evento (product_page, product_cart, purchase. Para obtener la taza de conversion, y la proporción de usuarios que completaron cada etapa del embudo dividiendo el número de eventos de esa etapa entre el número total de usuarios en cada grupo*

# %%
conversion_rates = all_data.groupby(
    ['group', 'event_name']).size().reset_index(name='counts')
conversion_rates['total_users'] = conversion_rates.groupby('group')[
    'counts'].transform('sum')
conversion_rates['conversion_rate'] = conversion_rates['counts'] / \
    conversion_rates['total_users']

# %% [markdown]
# *Ahora,creamos una pivot table para visualizar las tasas de conversión.*

# %%
conversion_pivot = conversion_rates.pivot_table(
    index='group', columns='event_name', values='conversion_rate')
display(conversion_pivot)

# %% [markdown]
# **De esta forma determinamos la taza de conversion que hay de un evento a otro en cada uno de n uestros grupos de test A/B.Aunque hay una ligero aumento en la estama de logearse a la etapa de acregar el producto al carrito en el grupo B, pues el resto de eventos tienen una conversion casi identica al grupo de control.**

# %% [markdown]
# *Ahora, calcularemos la dritribusion de los eventos en cada uno de los grupos del test A/B para verificar si se encuentran distribuidos equitativamente*

# %%
events_per_user = all_data.groupby(
    ['group', 'user_id']).size().reset_index(name='event_count')
sns.boxplot(x='event_count', y='group', hue='group', data=events_per_user)

# %% [markdown]
# **Determinamos de esta forma que el numero de eventos se encuentra ditribuido de forma equitativa entre los grupos del test A/B, proporcionados, ya que apesar de que el grupo de control tiene mayor cantidad e valores atipicos; pues las cajas tienen la misma media.**

# %% [markdown]
# Para observar de forma mas precisa las diferencias entre los eventos y los grupos crearemos un grafico de densidad para tener una mejor perspectiva.

# %%
all_data['time_to_event_seconds'] = all_data['time_to_event'].dt.total_seconds()
sns.kdeplot(data=all_data, x='time_to_event_seconds', hue='group', fill=True)
plt.show()

# %% [markdown]
# *De esta forma tambien obtenemos un grafico  de densidad que nos da una visualización clara de cómo se distribuye el tiempo transcurrido hasta el evento en diferentes grupos y para diferentes eventos, notando una mejor distribusion para el grupo de control(A).*

# %% [markdown]
# *Como en el analisis exploratorio anterior verificamos que no existan datos duplicados en este dataframe, determinamos que* ***No hay usuarios que esten presentes en ambas pruebas como tal.*** *asi que vamos a salatarnos esa parte para pasar a verificar la distribusion de los eventos por dia, mediante un grafico de linea.*

# %%
grouped_data = all_data.groupby(
    'event_dt').size().reset_index(name='event_count')
df_for_plot = grouped_data.copy()
df_for_plot['event_day'] = df_for_plot['event_dt'].dt.day
display(df_for_plot.head())
sns.lineplot(x='event_day', y='event_count', data=df_for_plot)
plt.title('Eventos por día')
plt.xlabel('Día')
plt.ylabel('Número de Eventos')
plt.show()

# %% [markdown]
# <div class="alert alert-block alert-success"> <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# La visualización de la distribución de eventos por día utilizando un gráfico de líneas es un buen enfoque para entender las tendencias temporales. Esto te permite observar fácilmente patrones a lo largo del tiempo, lo que es clave para cualquier análisis temporal en una prueba A/B.
#
# </div>

# %% [markdown]
# *Se crea un nuevo dataframe agrupando los datos por la fecha del evento y se cuenta la cantidad de eventos, asignando el resultado a la columna 'event_day', luego creamos una copia  llamada 'data_for_plot', para evitar modificar el DataFrame original y la mostramos, para finalmente crear un grafico de linea basado en este dataframe.*

# %% [markdown]
# **De esta forma determinamos el numero de eventos por dia, y notamos que tenemos una linea que parece ser continua pero al final del mes Acsiende hasta alcanzar la mayor cantidad de eventos el dia 30.**

# %% [markdown]
# *Antes de pasar al analisis del desde A/b y como aparatado adicional, eliminaremos la columna 'details' de nuestro dataframe ya que conteiene valores ausentes y al eliminar estas filas, estariamos omitiendo una importante cantidad de datos en otras columnas. Asi que como solo hay valores ffaltantes en esta columnas; se crea un Dataframe que no la contenga.*
#

# %%
all_data = all_data.drop('details', axis=1)

display(all_data.head())
display(all_data.isna().sum())

# %% [markdown]
# *Utilizando el metodo .drop() acompañado del parametro axis, eliminamos la columna con valores nulo de nuestro dataframe, para de esta manera realizar y evaluar los resultados del test A/B.*

# %%
total_usuarios_por_grupo = all_data.groupby(
    'group')['user_id'].nunique().reset_index(name='users_total')
conversion_pivot = conversion_pivot.merge(
    total_usuarios_por_grupo, on='group', how='left')
display(conversion_pivot.head())
display(conversion_pivot.info())

# %% [markdown]
# <div class="alert alert-block alert-success"> <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# El análisis exploratorio está bien planteado. Agrupar los datos por eventos y grupos es una excelente manera de visualizar las tasas de conversión en diferentes etapas del embudo. La visualización mediante pivot_table es una forma clara y concisa de mostrar los resultados, lo que facilita el análisis comparativo entre los grupos A y B.
#
# </div> <div class="alert alert-block alert-warning"> <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# La descripción de la distribución de eventos y su relación con los grupos A/B es buena, pero podrías mejorar la visualización utilizando gráficos adicionales como histogramas o gráficos de dispersión para entender mejor las distribuciones entre eventos. El gráfico de caja y bigotes (boxplot) es útil, pero podrías también usar gráficos de densidad o KDE para visualizar las diferencias en los eventos entre los grupos.
#
# </div>

# %% [markdown]
# ## Evaluar los resultados de la prueba A/B

# %% [markdown]
# **1. Definimos las hipotesis nula y la alternativa.**

# %% [markdown]
# ***H0: La proporción de usuarios que completan cada etapa del embudo es igual en ambos grupos (A y B).***
#
# ***H1: La proporción de usuarios que completan al menos una etapa del embudo es diferente entre los grupos A y B.***

# %% [markdown]
# *Para este apartado evaluaremos las tazas de coversion calculadas anteriormente en el analisis exploratorio de datos, mediante una funcion que itere sobre las osibles conbinaciones de grupos y eventos en este Dataframe.*

# %% [markdown]
# *Definimos una funcion que itera sobre los drupos de la preva A/b y utilizamos intertools para acceder a todaas las posibles combinaciones grupos ene los eventos, para luego iterar sobre los grupos y convertirlos en variables numericas 0, para el grupo A y 1 para el grupo B.  realizamos la peruba Z  en cada evento por idenpendiente y nuestro resltado es un datacframe cuyas columnas contiene el grupo del tetst A/B, asi como el evento con su respectivo significancia estadisticas (Z), y el valor p de cadad evento.*

# %%


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

# %% [markdown]
# *Devido a que los  p valores de cada una de las tazas de conversion obtenidas son mayores que el nivel alpha de significansia estadistica.No hay evidencia estadísticamente significativa para rechazar la hipótesis nula en ninguna de las comparaciones.*
#
# **Por los cual se concluye que:** ***LA PROPORCION DE USUARIOS QUE COMPLETAN CADA ETAPA DEL EMBUDO ES IGUAL EN AMBOS GRUPOS;(A y B).***
#
# *Ya que no se encontraron diferencias significativas entre las tazas de conversion para ninguno de los eventos ('login','product_cart','puchase').*
#
#
# **Basados en estos resultados, podríamos concluir que el nuevo sistema de recomendaciones (Grupo B) no tuvo un impacto significativo en las tasas de conversión en comparación con el sistema actual (Grupo A).**

# %% [markdown]
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# ¡Hola, Edwin!
#
# Primero que todo, quiero reconocer tu esfuerzo en esta sección. Sin embargo, he notado algunos puntos críticos que necesitan atención inmediata para asegurar que los resultados de tu prueba A/B sean válidos y precisos. A continuación, te detallo las áreas que requieren corrección:
#
# ### **1. Definición de las Hipótesis**
# - **Problema**: Las hipótesis están definidas de manera muy general, lo que puede causar confusión. Necesitas que estén más enfocadas en las tasas de conversión en cada etapa del embudo.
# - **Áreas de oportunidad**: Reformula las hipótesis para que reflejen con precisión lo que estás evaluando. Te sugiero que plantees:
#   - **H0**: No existe una diferencia significativa en las tasas de conversión en cada etapa del embudo entre los grupos A y B.
#   - **H1**: Existe una diferencia significativa en al menos una etapa del embudo entre los grupos A y B.
#
# Si las hipótesis no están bien definidas, podrías estar analizando datos sin una base clara.
#
# ---
#
# ### **2. Cálculo de las Tasas de Conversión**
# - **Problema**: Estás calculando las tasas de conversión usando las medias, lo cual no es correcto para una prueba Z de proporciones. Esto puede generar resultados erróneos.
# - **Áreas de oportunidad**: En lugar de usar las medias, debes calcular los conteos absolutos de usuarios que completaron cada evento en cada grupo. Este paso es fundamental para obtener resultados estadísticamente válidos.
#
# Si no lo corriges, las conclusiones que obtengas serán inválidas y podrías llegar a conclusiones incorrectas.
#
# ---
#
# ### **3. Uso de la Prueba Z**
# - **Problema**: Actualmente, estás pasando las medias de las tasas de conversión a la función `proportions_ztest`, lo cual es un error crítico. Esto está afectando gravemente la validez de tus resultados.
# - **Áreas de oportunidad**: Debes pasar los **números absolutos de éxitos (usuarios que completaron el evento)** y los **tamaños de muestra** a la función `proportions_ztest`. Si no lo haces, los resultados que obtengas de la prueba Z no serán fiables.
#
# ---
#
# ### **4. Iteración sobre los Eventos**
# - **Problema**: La iteración sobre varios eventos a la vez en tu código está mal estructurada y esto dificulta la interpretación adecuada de los resultados.
# - **Áreas de oportunidad**: Realiza una prueba Z separada para cada evento, como `product_page`, `product_cart`, y `purchase`. Cada etapa del embudo debe ser evaluada individualmente para garantizar un análisis preciso.
#
# ---
#
# ### **5. Documentación del Código**
# - **Problema**: Los comentarios en el código no son lo suficientemente claros y pueden generar confusión tanto para ti como para otros que revisen tu trabajo.
# - **Áreas de oportunidad**: Mejora los comentarios explicando detalladamente qué hace cada bloque de código.
# ---
#
# ### **Conclusión**
# Si bien estás en el buen camino, estos detalles deben corregirse lo antes posible para evitar que tus conclusiones sean erróneas. Es esencial que trabajes en estos puntos para garantizar que tu análisis de prueba A/B sea válido. Sé que puedes hacerlo, y una vez que apliques estos cambios, estarás en una posición mucho más sólida para obtener resultados confiables.
#
# Si necesitas apoyo, no dudes en preguntar a tu tutor. Estamos aquí para ayudarte y que  avances con éxito. ¡Tú puedes, sigue adelante!
#
# </div>

# %% [markdown]
# <div class="alert alert-block alert-danger">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# Hola Edwin,
#
# Primero que nada, quiero felicitarte por el esfuerzo y la dedicación que has puesto en este proyecto. Es evidente que has trabajado duro para implementarlo, lo cual siempre es admirable. Dicho esto, lamentablemente, tu proyecto no puede ser aprobado en su estado actual debido a algunos errores críticos que impactan directamente en la validez de los resultados de la prueba A/B.
#
# ### **Puntos Positivos**:
# - **Esfuerzo en la Estructura del Código**: Has realizado un buen trabajo al organizar el código y seguir un flujo lógico para el análisis. Esto facilita su comprensión.
# - **Uso de Técnicas Estadísticas**: Te has esforzado por implementar técnicas estadísticas, lo cual es clave para evaluar adecuadamente una prueba A/B. La intención de usar la prueba Z es correcta.
# - **Visualización de Datos**: Has aplicado correctamente técnicas de visualización de datos, lo que te permite ver las diferencias entre los grupos de manera más clara.
#
# ### **Áreas de Oportunidad**:
# 1. **Corrección de la Prueba Z**: Como te mencioné anteriormente, la prueba Z debe realizarse sobre los conteos absolutos de usuarios y no sobre medias pre-calculadas. Esta es una corrección esencial para asegurar que los resultados sean válidos.
# 2. **Definición de las Hipótesis**: Las hipótesis deben estar más alineadas con las tasas de conversión en cada etapa del embudo de compra. Esto te ayudará a plantear de manera más precisa el objetivo de tu análisis.
# 3. **Mejora en la Iteración sobre Eventos**: En lugar de calcular todos los eventos de forma conjunta, deberías realizar la prueba Z para cada etapa del embudo por separado (product_page, product_cart, purchase). Esto proporcionará un análisis más claro y detallado.
# 4. **Documentación del Código**: Sería útil mejorar los comentarios en el código, explicando cada paso de manera más clara para que sea comprensible tanto para ti como para quienes revisen tu trabajo en el futuro.
#
# ### **Conclusión**:
# Edwin, aunque este proyecto no puede ser aprobado en este momento, estoy seguro de que con estas correcciones lograrás obtener un resultado sólido y confiable. Te animo a que sigas adelante, porque estás en el camino correcto y cada ajuste que hagas te ayudará a mejorar tus habilidades y conocimientos.
#
# Si necesitas apoyo para realizar estos cambios, no dudes en contactar a tu tutor . Estamos aquí para apoyarte en tu proceso de aprendizaje. ¡Confío en tu capacidad para seguir mejorando y alcanzar el éxito en tus próximos proyectos!
#
# ¡Sigue adelante, Edwin! 😊💪
#
# </div>
#
# ---
#

# %% [markdown]
# <div class="alert alert-block alert-success">
# <b>Comentario del revisor</b> <a class="tocSkip"></a>
#
# ¡Qué gran trabajo has hecho!  &#128077;  Podemos aprobar el proyecto. <br>
# Has demostrado un excelente conocimiento en la construcción del proyecto. <br>
# <br>Quiero felicitarte por un trabajo excepcional y por la calidad de tu análisis. Te animo a que sigas aprendiendo y desafiando tu potencial en los próximos sprints. Estoy seguro de que tus habilidades y conocimientos serán valiosos en el futuro y te permitirán abordar problemas cada vez más complejos con éxito.
# </div>
