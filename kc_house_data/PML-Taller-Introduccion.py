#!/usr/bin/env python
# coding: utf-8

# # Manipulación y visualización de datos
# 
# En este taller estudiarás los conceptos mostrados en el tutorial de Introducción a librerías de manipulación de datos, ahora con un nuevo conjunto de datos. Específicamente, realizarás los siguientes pasos:
# 
# 1. Cargar un conjunto de datos en formato .csv.
# 2. Analizar los datos y las variables que los conforman.
# 3. Consultar y manipular el conjunto de datos mediante localización por etiquetas y por índices.
# 4. Crear gráficas sencillas con Matplotlib y Seaborn.
# 
# El conjunto de datos a utilizar es un repositorio de música. Este conjunto representa canciones mediante su popularidad, bailabilidad, volumen, acústica, entre otras propiedades cuantificables.
# 
# Primero vamos a importar las librerías necesarias:

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from importlib.metadata import version


# Luego, revisamos la versiones de las librerías. Las librerías se actualizan frecuentemente y es útil saber esta información al momento de consultar documentación sobre las librerías. Además, facilita ejecutar este taller en otros entornos como un computador personal o Google Colab.

# In[2]:


print(f"Versión de Pandas: {version('pandas')}")
print(f"Versión de Seaborn: {version('seaborn')}")
print(f"Versión de Matplotlib: {version('matplotlib')}")
print(f"Versión de Numpy: {version('numpy')}")


# ## 1. Carga de datos
# 
# Iniciaremos con la importación de nuestro conjunto de datos.
# 
# ### Ejercicio 1.1.
# 
# Utiliza Pandas para importar el archivo que contiene el conjunto de datos de canciones.
# 
# * La ruta del archivo .csv es: `./data/song_data.csv`, y ya se encuentra en el entorno de Coursera, solo debes importarlo.
# * La variable resultante debe tener el nombre `data`.
# 
# Recuerda que usarás esta variable para todas las consultas sobre los datos.

# In[23]:


ruta = 'song_data.csv'
# Escribe tu código aquí
data = pd.read_csv(ruta)
data


# Para este y los siguientes ejercicios encontrarás celdas, como la que se muestra a continuación, con pruebas unitarias para evaluar tu respuesta. Estas pruebas verificarán que tu respuesta tenga las dimensiones correctas y el tipo de dato correcto según la pregunta. Si todas las pruebas son exitosas, se ejecutará la línea con la función `print()` y el mensaje que indica que tu respuesta tiene el formato esperado.

# In[7]:


#---------- Celda de Pruebas ----------
# La variable "data" existe
# El resultado es un DataFrame
# El resultado tiene las dimensiones correctas
#--------------------------------------

# Se verifica que la variable está definida
assert data is not None, "Asegúrate de definir la variable data."
assert ruta is not None, "Asegúrate de definir la variable con la ruta al archivo."

# Se verifica que sea un DataFrame
assert isinstance(data, pd.DataFrame), "El resultado es un DataFrame."

# Se evalúan las dimensiones de la variable data
assert data.shape == (18835,15), "¿Verificaste que la ruta del archivo CSV y el nombre de la variable son correctos?"
print("¡Los datos tienen las dimensiones correctas!")


# Para tener una idea del contenido de los datos, vamos a visualizar nuestro DataFrame utilizando `data.head()`:

# In[8]:


data.head()


# ## 2. Descripción de los datos
# 
# Como vimos anteriormente, también podemos utilizar Pandas para describir los datos utilizando una función.
# 
# ### Ejercicio 2.1.
# 
# En la siguiente celda, obtén una descripción de los datos utilizando Pandas. Utiliza el resultado para responder a las preguntas que se muestran más adelante.
# * Define una variable con el nombre `p21` y asígnale el valor correspondiente.
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[25]:


# Escribe tu código aquí

p21 = data.describe()
p21


# In[21]:


#---------- Celda de Pruebas ----------
# La variable "p21" existe
# El resultado es un DataFrame
# El resultado tiene las dimensiones correctas
#--------------------------------------

# Se verifica que la variable está definida
assert p21 is not None, "Asegúrate de definir la variable correctamente."

# Se verifica que sea un DataFrame
assert isinstance(p21, pd.DataFrame), "El resultado es un DataFrame."

# Se evalúan las dimensiones de la respuesta 2.1
assert p21.shape == (8,14), "Utiliza una función de Pandas para obtener una descripción general de los datos."
print("¡Las dimensiones son correctas!")


# #### Pregunta 2.1.1.
# 
# ¿Qué bailabilidad media tienen las canciones?
# 
# * La bailabilidad corresponde a la variable `danceability`.
# * Para responder a la pregunta, define una variable con el nombre `p211` y asígnale el valor correspondiente. (**Ejemplo: `p211 = 1`**)
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[26]:


# Escribe tu código aquí

p211 = data["danceability"].mean()
p211


# In[31]:


#---------- Celda de Pruebas ----------
# La variable "p211" existe
# El resultado es un número de tipo "float"
# El resultado se encuentra en el rango [0,1]
#--------------------------------------

# Se verifica que la variable está definida
assert p211 is not None, "Asegúrate de definir la variable correctamente."

# Se evalúa el tipo de dato
assert type(p211) == float or type(p211) == np.float64, "Recuerda que tu respuesta debe ser un número."

# Se evalúa el rango de respuesta
assert (p211 >= 0 and p211 <= 1), "Verifica los límites de la variable que aparecen en el ejercicio 2.1."
print("¡El tipo y rango de la respuesta son correctos!")


# #### Pregunta 2.1.2.
# 
# ¿Cuál es la puntuación máxima de popularidad?
# 
# * Para responder a la pregunta, define una variable con el nombre `p212` y asígnale el valor correspondiente. (**Ejemplo: `p212 = 10`**)
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[32]:


# Escribe tu código aquí

p212 = data["song_popularity"].max()
p212


# In[33]:


#---------- Celda de Pruebas ----------
# La variable "p212" existe
# El resultado es un número entero
# El resultado está en el rango [0,100]
#--------------------------------------

# Se verifica que la variable está definida
assert p212 is not None, "Asegúrate de definir la variable correctamente."

# Se evalúa el tipo de dato
assert type(p212) == int or type(p212) == np.int64, "Recuerda que tu respuesta debe ser un número entero."

# Se evalúa el rango de respuesta
assert (p212 >= 0 and p212 <= 100), "Verifica los límites de la variable que aparecen en el ejercicio 2.1."
print("¡El tipo de dato y el rango de la respuesta son correctos!")


# #### Pregunta 2.1.3.
# 
# ¿Cuál es el valor de energía mínima?
# 
# * Para responder a la pregunta, define una variable con el nombre `p213` y asígnale el valor correspondiente. (**Ejemplo: `p213 = 0.5`**)
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[34]:


# Escribe tu código aquí

p213= data['energy'].min()

p213


# In[35]:


#---------- Celda de Pruebas ----------
# La variable "p213" existe
# El resultado es un número de tipo "float"
# El resultado está en el rango [0,1]
#--------------------------------------

# Se verifica que la variable está definida
assert p213 is not None, "Asegúrate de definir la variable correctamente."

# Se evalúa el tipo de dato
assert type(p213) == float or type(p213) == np.float64, "Recuerda que tu respuesta debe ser un número."

# Se evalúa el rango de respuesta
assert (p213 >= 0 and p213 <= 1), "Verifica los límites de la variable que aparecen en el ejercicio 2.1."
print("¡El tipo y rango de la respuesta son correctos!")


# ### Ejercicio 2.2.
# 
# #### Pregunta 2.2.1.
# 
# Primero, utiliza la siguiente celda para obtener un conteo de la cantidad de apariciones de cada puntuación de popularidad.
# 
# * Define una variable con el nombre `p221` y asígnale la consulta correspondiente (`p221 = <<Consulta>>`).
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[40]:


# Escribe tu código aquí
p221 = data['song_popularity'].value_counts()
p221
print(p221)

# In[41]:


#---------- Celda de Pruebas ----------
# La variable "p221" existe
# El resultado tiene las dimensiones correctas
#--------------------------------------

# Se verifica que la variable está definida
assert p221 is not None, "Asegúrate de definir la variable correctamente."

# Se verifican las dimensiones de la variable "p221"
assert p221.shape == (101,), "Pandas ofrece una función para el conteo de datos, que recibe como argumento una consulta sobre el DataFrame. Esta consulta tiene que usar la variable \'song_popularity\'"
print("¡La respuesta tiene las dimensiones correctas!")


# #### Pregunta 2.2.2.
# 
# Utiliza la información obtenida para responder: ¿Cuántas canciones tienen la máxima puntuación?
# 
# * Para responder a la pregunta, define una variable con el nombre `p222` y asígnale el valor correspondiente. (**Ejemplo: `p222 = 50`**)
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[86]:


# Escribe tu código aquí
valor_maximo= data["song_popularity"].max()
p222 = (data["song_popularity"] == valor_maximo).sum()
print(p222)

# In[46]:


#---------- Celda de Pruebas ----------
# La variable "p22" existe
# El resultado es un número entero
# El resultado está en el rango [0,18835]
#--------------------------------------

# Se verifica que la variable está definida
assert p222 is not None, "Asegúrate de definir la variable correctamente."

# Se evalúa el tipo de dato
assert type(p222) == int or type(p222) == np.int64, "Recuerda que tu respuesta debe ser un número entero."

# Se evalúa el rango de respuesta
assert (p222 >= 0 and p222 <= 18835), "La respuesta debe ser menor o igual al total de datos."
print("¡La respuesta tiene el tipo y rango correcto!")


# ## 3. Consulta y modificación de datos
# 
# Después de visualizar y analizar los datos de forma general, realiza algunas consultas sobre ellos:
# 
# ### Ejercicio 3.1.
# 
# Utiliza la localización por índices para obtener el dato con índice 300.
# 
# * Define una variable con el nombre `p31` y asígnale la consulta (`p31 = <<Consulta>>`). Esto permitirá que puedas acceder al resultado de la consulta en cualquier momento (simplemente colocando el nombre de la variable).
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[47]:


# Escribe tu código aquí
p31 = data.iloc[300]
p31


# In[48]:


#---------- Celda de Pruebas ----------
# La variable "p31" existe
# El resultado es una Serie de Pandas
# El resultado tiene las dimensiones correctas
#--------------------------------------

# Se verifica que la variable está definida
assert p31 is not None, "Asegúrate de definir la variable correctamente."

# Se verifica que sea una Serie
assert isinstance(p31, pd.Series), "El resultado es una Serie de Pandas, resultado de una consulta."

# Se verifican las dimensiones de la respuesta
assert p31.shape == (15,), "Recuerda utilizar 300 como argumento de tu consulta."
print("¡La respuesta tiene las dimensiones correctas!")


# ### Ejercicio 3.2.
# 
# Obtén las canciones en el intervalo definido por los índices 400 y 500.
# 
# * Define una variable con el nombre `p32` y asígnale la consulta (`p32 = <<Consulta>>`).
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[51]:


# Escribe tu código aquí
p32 = data[400:500]

p32


# In[52]:


#---------- Celda de Pruebas ----------
# La variable "p32" existe
# El resultado es un DataFrame
# El resultado tiene las dimensiones correctas
#--------------------------------------

# Se verifica que la variable está definida
assert p32 is not None, "Asegúrate de definir la variable correctamente."

# Se verifica que sea un DataFrame
assert isinstance(p32, pd.DataFrame), "El resultado es un DataFrame con 100 filas."

# Se evalúan las dimensiones de la respuesta
assert p32.shape == (100, 15), "Recuerda usar el intervalo 400:500."
print("¡La respuesta es un DataFrame con las dimensiones correctas!")


# ### Ejercicio 3.3.
# 
# Utiliza la localización por etiquetas para obtener la duración de la canción con índice 1000.
# 
# * Define una variable con el nombre `p33` y asígnale la consulta (`p33 = <<Consulta>>`). El resultado de esta consulta debe ser un número.
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[55]:


# Escribe tu código aquí
p33 = data.loc[1000,'song_duration_ms']
p33


# In[58]:


#---------- Celda de Pruebas ----------
# La variable "p33" existe
# El resultado es un número entero
# El resultado está en el rango [0,1799346]
#--------------------------------------

# Se verifica que la variable está definida
assert p33 is not None, "Asegúrate de definir la variable correctamente."

# Se evalúa el tipo de dato
assert type(p33) == np.int64 or type(p33) == int, "En este caso tienes que localizar una celda del DataFrame. Es decir, tienes que consultar una fila (índice) y una columna (variable)."

# Se evalúa el rango de respuesta
assert (p33 >= 0 and p33 <= 1799346), "Verifica los límites de la variable \'song_duration_ms\' que aparecen en el ejercicio 2.1."
print("¡La respuesta tiene el rango correcto!")


# ### Ejercicio 3.4.
# 
# Filtra el DataFrame para obtener todas las canciones con popularidad mayor a 95.
# 
# * Define una variable con el nombre `p34` y asígnale la consulta (`p34 = <<Consulta>>`). En este caso, `p34` es un nuevo DataFrame.
# * Encontrarás una línea solo con el nombre de la variable. Esta línea se usa para que puedas visualizar tu respuesta, por lo que siempre debe ir al final y no la debes modificar.

# In[64]:


# Escribe tu código aquí
p34 = data[data['song_popularity'] > 95]
p34


# In[65]:


#---------- Celda de Pruebas ----------
# La variable "p34" existe
# El resultado es un DataFrame
# El resultado tiene las dimensiones correctas
#--------------------------------------

# Se verifica que la variable está definida
assert p34 is not None, "Asegúrate de definir la variable correctamente."

# Se verifica que sea un DataFrame
assert isinstance(p34, pd.DataFrame), "El resultado es un DataFrame con 164 filas."

# Se evalúan las dimensiones de la respuesta
assert p34.shape == (164, 15), "Utiliza doble localización por etiquetas para evaluar la condición y filtrar el DataFrame"
print("¡La respuesta es un DataFrame con las dimensiones correctas!")


# ## 4. Visualización de datos
# 
# Finalmente, vamos a utilizar tres tipos de gráficos para visualizar algunas características del conjunto de datos.
# 
# ### Ejercicio 4.1.
# 
# Completa el siguiente código para generar una gráfica de distribución de popularidad. En el eje `x` deben estar los valores posibles de popularidad, y en el eje `y` debe estar la cantidad de apariciones de cada popularidad.
# 
# A continuación puedes observar cómo se debe ver la gráfica resultante:
# 
# ![Gráfica E4.1](./img/41.png "Gráfica resultante para E4.1.")
# 
# **Nota:** `% matplotlib inline` es un llamado a una función que permite que las gráficas se muestren correctamente en Jupyter Notebooks. Si en algún momento no aparecen tus gráficas, puedes regresar a esta celda, ejecutarla nuevamente y volver al punto en el que estabas.

# In[66]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[77]:


plt.figure(figsize=(16,6))

# Para resolver este punto, define dos variables x, y.
# Cada variable debe estar igualada a una consulta:
#   x = data[...].funcion()
#   y = data[...].funcion()
# Puedes usar localización por etiquetas o por índices, pero no es necesario.
# Igualmente, puedes usar la misma consulta para las dos variables, cambiando el atributo correspondiente
# Escribe tu código aquí

plot_data = data['song_popularity'].value_counts()
x = plot_data.index
y = plot_data.values
plt.bar(x,y)
plt.title('Distribución de Popularidad de Canciones')
plt.xticks(rotation=90)

plt.show()


# In[68]:


#---------- Celda de Pruebas ----------
# La variables "x", "y" existen
# Las variables tienen las dimensiones correctas
#--------------------------------------

# Se verifica que las variables están definidas
assert x is not None, "Asegúrate de definir la variable correctamente."
assert y is not None, "Asegúrate de definir la variable correctamente."

# Se evalúan las dimensiones de la variable X
assert x.shape == (101,), "El eje x corresponde a los valores posibles de la popularidad. Encuentra una función que retorne los valores únicos de una variable."

# Se evalúan las dimensiones de la variable Y
assert y.shape == (101,), "El eje y corresponde a la cantidad de apariciones de un valor. Encuentra una función que cuente esas apariciones."
print("¡Las variables tienen las dimensiones correctas!")


# ### Ejercicio 4.2.
# 
# Completa el siguiente código, usando Seaborn, para generar un histograma de la energía de las canciones (variable `energy`).
# 
# La gráfica resultante se debe ver de la siguiente manera:
# 
# ![Gráfica E4.2](./img/42.png "Gráfica resultante para E4.2.")

# In[80]:


plt.figure(figsize=(16,6))
plt.tight_layout()

# Define una sola variable x.
# La variable debe estar igualada a una consulta:
#   x = data[...]

# Nota: en este punto estás reasignando (sobreescribiendo) la variable x del punto anterior.
#       En este caso no es importante, pero siempre debes tenerlo en cuenta.
# Escribe tu código aquí
x = data['energy']


sns.distplot( x, kde=True)


# In[81]:


#---------- Celda de Pruebas ----------
# La variable "x" existe
# El resultado es una Serie de Pandas
# El resultado tiene las dimensiones correctas
#--------------------------------------

# Se verifica que la variable está definida
assert x is not None, "Asegúrate de definir la variable correctamente."

# Se verifica que sea una Serie
assert isinstance(x, pd.Series), "El resultado es una Serie de Pandas, resultado de una consulta."

# Se evalúan las dimensiones de la variable X
assert x.shape == (18835,), "Debes consultar la columna de la variable \'energy\'."
print("¡Las dimensiones de X son correctas!")


# ### Ejercicio 4.3.
# 
# Completa el siguiente código para visualizar la relación entre energía (variable `energy`) y volumen (variable `loudness`). 
# * Este gráfico debe tener los valores de energía en el eje `x`, y los valores de volumen en el eje `y`. 
# * La forma de las marcas utilizadas debe ser de estrella.
# 
# El resultado de este ejercicio debe ser como se muestra a continuación:
# 
# ![Gráfica E4.3](./img/43.png "Gráfica resultante para E4.3.")

# In[84]:


plt.figure(figsize=(10,10))

# Para resolver este punto, define dos variables x, y.
# Cada variable debe estar igualada a una consulta:
#   x = data[...]
#   y = data[...]

# Además, define una variable 'forma'.
# Esta variable debe estar igualada a un String.
# Por ejemplo, para que los marcadores tengan forma de punto:
#   forma = '.'

# Escribe tu código aquí
x = data['energy']
y = data['loudness']
forma = '*'
plt.plot(x,y,forma, color='blue')
plt.title('Energía vs Volumen')
plt.xlabel('Energía')
plt.ylabel('Volumen')
plt.show()


# In[85]:


#---------- Celda de Pruebas ----------
# El resultado tiene tres variables que existen
# Las variables "x", "y" tienen dimensiones correctas
# La variable "forma" es un String
#--------------------------------------

# Se verifica que las variables están definidas
assert x is not None, "Asegúrate de definir la variable correctamente."
assert y is not None, "Asegúrate de definir la variable correctamente."
assert forma is not None, "Asegúrate de definir la variable correctamente."

# Se evalúan las dimensiones de la variable X
assert x.shape == (18835,), "El eje x corresponde a la variable \'energy\'. Puedes usar loc, iloc, o consultar directamente."

# Se evalúan las dimensiones de la variable Y
assert y.shape == (18835,), "El eje y corresponde a la variable \'loudness\'. Puedes usar loc, iloc, o consultar directamente."

# Se evalúa el tipo de la variable forma
assert type(forma) == str, "Recuerda que este argumento describe la forma de los marcadores usando un caracter. Revisa la documentación de Matplotlib: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html"
print("¡Las dimensiones de las variables y el tipo del argumento son correctas!")


# ## Cierre 
# 
# Al desarrollar los ejercicios de este taller, has practicado tus habilidades para cargar, analizar y consultar un conjunto de datos en Python. Además, lograste crear algunas visualizaciones básicas que te serán de ayuda en el análisis de tus datos para, en un futuro, crear modelos de aprendizaje automático a partir de ellos.
# 
# ---
# 
# *Creado por: Nicolás Díaz*
# 
# *Última edición: Camilo Rozo*
# 
# *Revisado por: Haydemar Nuñez*
# 
# *Versión de: Enero 20, 2025*
# 
# *Universidad de los Andes*  
