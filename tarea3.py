import matplotlib.pyplot as plt
import scipy.stats
import csv
import numpy as np
import pandas as pd
df=pd.read_csv("C:/Users/oscar/OneDrive/Escritorio/github/Covid-19.csv")
print(df.head())

#con la funcion melt convierte las columnas de valores vals en una unica columna llamada value y las columnas de identificacion ids se mantienen
#ESTO se guarda en df_tidy
vals = list(df.columns)[5:-1]
ids = list(df.columns)[:5]

df_tidy = pd.melt(df, value_vars=vals, id_vars=ids)
print(df_tidy)

#elimina filas con valores faltantes con la funcion dropna
df_tidy = df_tidy.dropna()
print(df_tidy)
df_tidy.info()
#convierte la columna variable en tipo fecha y hora
list(df_tidy.dtypes)
df_tidy['variable'] = pd.to_datetime(df_tidy['variable'])

#le da un formato a la fecha y hora, del tipo %Y-%m-%d, con pd.to_datetime
df_tidy['variable'] = pd.to_datetime(df_tidy['variable'], format='%Y-%m-%d')

#crea un dateframe que contiene las filas de df_tidy correspondiente a un rango especifico de fechas
df_tidy_rango=df_tidy[(df_tidy['variable']>='2020-03-01') & (df_tidy['variable']<='2020-06-30')]

#crea una lista llamada data y traza un histograma con esta, con 100 bins y densidad habilitada
data=[]
plt.hist(data, bins=100, density=True)

#ajuste de distribucion normal y guarda los valores de media y desviacion estandar
[mean_fit, std_fit]=scipy.stats.norm.fit(data)

print(mean_fit)
print(std_fit)

#muestr histograma
plt.show