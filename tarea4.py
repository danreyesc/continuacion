
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import bernoulli,norm

#
M=120
S=norm(0,1).rvs(size=M)
H=norm(0,0.5*abs(S)).rvs(size=M)
sns.scatterplot(S)
sns.scatterplot(H)

plt.hist(H, bins=100)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('distribucion normal')
plt.show()

D=np.random.binomial(n=1, p=0.5, size=M)
Hstar=H.copy()
Hstar[D==1]=np.nan


M= 100
S = np.random.normal(size=M)
H = np.random.normal(loc=(1-np.exp(-0.7*S)), size=M)
D = np.random.binomial(1, p=np.where(S > 0, 1, 0), size=M)
Hstar = H.copy()
Hstar[D == 1] = np.nan


plt.scatter(S, Hstar, color='red', s=30, linewidth=3)


plt.xlabel('S')
plt.ylabel('H and Hstar')
plt.title('Normal Distributions')


plt.show()


M = 120
S = np.random.normal(size=M)
H = np.random.normal(loc=0.5*S, size=M)
D = np.random.binomial(1, p=np.where(H<0, 0.9, 0), size=M)
Hstar = H.copy()
Hstar[D == 1] = np.nan


plt.scatter(S, Hstar, color='red', s=30, linewidth=3)


plt.xlabel('S')
plt.ylabel('H and Hstar')
plt.title('Normal Distributions')


plt.show()

M = 120
S = np.random.normal(size=M)
H = np.random.normal(loc=0.5*S, size=M)
D = np.random.binomial(1, p=0.5, size=M)
Hstar = H.copy()
Hstar[D == 1] = np.nan


plt.scatter(S, Hstar, color='red', s=30, linewidth=3)


plt.xlabel('S')
plt.ylabel('H and Hstar')
plt.title('Normal Distributions')


plt.show()
sns.histplot(S, kde=True, stat="density")

M = 100
S = np.random.normal(size=M)


sns.histplot(S, kde=True, stat="density")
