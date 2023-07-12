import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA



df = pd.read_excel("C:/Users/oscar/OneDrive/Escritorio/Proyecto/last_uci_diario.xlsx")
print(df.head())

#calcular valores faltantes en cada columna y los almacena en val_faltsante
val_faltante=df.isnull().sum()


#elimina las filas con valores faltantes
df_limpio=df.dropna()


#las columnas ya están en formato de fecha
#transpone el dataframe con df_limpio.transpose y almacena el resultado en la var. transpuesto (esto cambia las filas por columnas)
traspuesto=df_limpio.transpose()

#establece el nombre de las columnas
traspuesto.columns=traspuesto.iloc[0]
#elimina la primera fila de transpuesto
traspuesto=traspuesto[1:]

print(traspuesto)

#renombra la columna index a fecha
traspuesto= traspuesto.rename(columns={'index':'fecha'})

#calcula el valor medio de la columna total y lo almacena en la var., valor_medio
valor_medio=traspuesto['Total'].mean()
print(valor_medio)

plt.hist(traspuesto['Total'])
plt.show()

traspuesto["Total"] = pd.to_numeric(traspuesto["Total"])
traspuesto["Región Metropolitana de Santiago"] = pd.to_numeric(traspuesto["Región Metropolitana de Santiago"])

correlacion = traspuesto["Total"].corr(traspuesto["Región Metropolitana de Santiago"])
print(correlacion)

traspuesto.plot(x='Total', y='Región Metropolitana de Santiago')
plt.show()

# Descompone una columna de series temporales
descomposicion = seasonal_decompose(traspuesto['Total'],model='additive', period=1)
descomposicion.plot()
plt.show()

# Crea y ajusta un modelo ARIMA
modelo = ARIMA(traspuesto['Total'], order=(5,1,0))
modelo_ajustado = modelo.fit
