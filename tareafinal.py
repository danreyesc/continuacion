import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA


df = pd.read_excel("C:/Users/oscar/OneDrive/Escritorio/Proyecto/last_uci_diario.xlsx")
print(df.head())

#calcular valores faltantes en cada columna y los almacena en val_faltsante
val_faltante=df.isnull().sum()
print(val_faltante)

#elimina las filas con valores faltantes
df_clean=df.dropna()

#las columnas ya están en formato de fecha
#transpone el dataframe con df_clean.transpose y almacena el resultado en la var. transpuesto (esto cambia las filas por columnas)
traspuesto=df_clean.transpose()
print(traspuesto)
#establece el nombre de las columnas
traspuesto.columns=traspuesto.iloc[0]
#elimina la primera fila de transpuesto
traspuesto=traspuesto[1:]

#renombra la columna index a fecha
traspuesto= traspuesto.rename(columns={'index':'fecha'})

#convierte la columna fecha al formato utilizado %d-%m-%Y
traspuesto['fecha']=pd.to_datetime(traspuesto['fecha'], format='%d-%m-%Y')

#calcula el valor medio de la columna total y lo almacena en la var., valor_medio
valor_medio=traspuesto['total'].mean()
print(valor_medio)

#histograma columna total
plt.hist(traspuesto['total'])
plt.show()

#Calcula la correlación entre las columnas total y XII Región de Magallanes y de la Antártica Chilena
#  almacena el resultado en la variable correlacion.
correlacion = traspuesto['total'].corr(traspuesto['total'].astype(float))

#Crea un gráfico de línea con la columna total en el eje x y la columna XII Región de Magallanes y de la Antártica Chilena en el eje y
traspuesto.plot(x='total', y='XII Región de Magallanes y de la Antártica Chilena')
plt.show()


# Descompone una columna de series temporales
descomposicion = seasonal_decompose(traspuesto['total'],model='additive', period=1)
descomposicion.plot()
plt.show()


# Crea y ajusta un modelo ARIMA
modelo = ARIMA(traspuesto['total'], order=(5,1,0))
modelo_ajustado = modelo.fit

