
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import random
import csv

#genera datos uniformes random desde 0 a 10
data_uniforme=stats.uniform.rvs(size=10000,loc=0,scale=10) 
pd.DataFrame(data_uniforme).plot(kind='density', figsize=(9,9), xlim=(-5,15))
stats.uniform.cdf(x=2.5, loc=0, scale=10) 
stats.uniform.ppf(q=0.4, loc=0, scale=10) 

#se hace un ciclo for para sacar la densidad de los valores dentro del rango
for x in range(-1,12,2): 
    print("densidad en valor de x" + str(x))
    print( stats.uniform.pdf(x, loc=0, scale=10))

random.randint(0,10)
random.choice([2,3,4,5,6,7,8])
random.random()
random.uniform(0,10)

random.seed(12)
print([random.uniform(0,10) for x in range(4)])


plt.rcParams["figure.figsize"]=(7,7)

plt.fill_between(x=np.arange(-4,-1,0.01),y1=stats.norm.pdf(np.arange(-4,-1,0.01)), facecolor='orange', alpha=0.35)
plt.fill_between(x=np.arange(1,4,0.01),y1=stats.norm.pdf(np.arange(1,4,0.01)), facecolor='orange', alpha=0.35)
plt.fill_between(x=np.arange(-1,1,0.01),y1=stats.norm.pdf(np.arange(-1,1,0.01)), facecolor='blue', alpha=0.35)


#encuentra el valor en x para el 2.5% de los valores a la izquierda y derecha
print(stats.norm.ppf(q=0.025)) 
print(stats.norm.ppf(q=0.975)) 

print(stats.norm.cdf(x=-1)) 
print(stats.norm.cdf(x=1)) 




#distribucion normal

coin_flip=stats.binom.rvs(n=10,p=0.5,size=1000) #1000 intentos con probabilidad 0.5 
print(pd.crosstab(index="counts", columns=coin_flip))
#ploteo en un histograma
pd.DataFrame(coin_flip).hist(range=(-0.5,10.5), bins=11); 


#ahora usemos una moneda cargada en 0.8 para obtener cara 
coin_flip=stats.binom.rvs(n=10,p=0.8,size=1000)
print(pd.crosstab(index="counts", columns=coin_flip))
pd.DataFrame(coin_flip).hist(range=(-0.5,10.5), bins=11);
#con 1000 intentos, nunca hubo 0 sellos, debido a la carga que le dimos a la moneda

#con .cdf podemos ver la probabilidad de obtener debajo de x cantidad de caras
stats.binom.cdf(k=5, n=10, p=0.8) #pedimos la probabilidad de obtener 5 aciertos (caras)
1-stats.binom.cdf(k=5, n=10, p=0.8) #pedimos la probabilidad de obtener 5 aciertos (caras)



# geometrica y exponencial.

random.seed(12)
flips_till_heads=stats.geom.rvs(size=100, p=0.5)
print(pd.crosstab(index="counts", columns=flips_till_heads))
pd.DataFrame(flips_till_heads).hist(range=(-0.5, max(flips_till_heads + 0.5), bins:=max(flips_till_heads)+1))

first_five = stats.geom.cdf(k=5, p=0.5)

#plotear la distribucion exponencial
plt.fill_between(x=np.arange(0,1,0.01), y1=stats.expon.pdf(np.arange(0,1,0.01)), facecolor='blue', alpha=0.35)
plt.fill_between(x=np.arange(1,7,0.01), y1=stats.expon.pdf(np.arange(1,7,0.01)), facecolor='red', alpha=0.35)


#poission 


arrival_rate_1=stats.poisson.rvs(size=10000, mu=1)
print(pd.crosstab(index='counts', columns=arrival_rate_1))
pd.DataFrame(arrival_rate_1).hist(range=(-0.5, max(arrival_rate_1)+0.5), bins=max(arrival_rate_1)+1);


arrival_rate_1=stats.poisson.rvs(size=10000, mu=10)#ahora con mas arrivals por time
print(pd.crosstab(index='counts', columns=arrival_rate_1))
pd.DataFrame(arrival_rate_1).hist(range=(-0.5, max(arrival_rate_1)+0.5), bins=max(arrival_rate_1)+1);




