import pandas as pd
import matplotlib as plt
import seaborn as sns

from importlib.metadata import version

print(f"Version de Pandas: {version('pandas')} ")
print(f" Version de Matplolib: {version('matplotlib')}")
print(f" Version de Seaborn: { version('seaborn')}")

data = pd.read_csv('/Users/johanypenaflorez/Downloads/Files/kc_house_data.csv')

print(data.shape)
print(data.info())
print(data.describe())

# Filas filtrar  iloc
# print(data.iloc[3:5])

# # # Filtrar columnas loc
# print(data.loc[0:2,"price"])


# plot_data = data['yr_built'].value_counts()

# # Retorna todos los valores únicos que puede tomar la variable yr_built
# # x = plot_data.index
# print(x)
#  # Retorna las veces que cada valor aparece en los datos
# y = plot_data.values
# print(y)

p221 = data['price'].value_counts()
print(p221)
print(p221.max())


#filtrar de acuerdo a una condicion
# Escribe tu código aquí
p34 = data[data['song_popularity'] > 95]
p34