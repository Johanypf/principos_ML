import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.plotting import scatterplotmatrix

df = pd.read_csv('./housing.data.txt', sep=r'\s+',engine='python')
df.columns = ['CRIM', 'ZN', 'INDUS', 'CHAS','NOX', 'RM', 'AGE', 'DIS', 'RAD',
            'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
print(df.head())
