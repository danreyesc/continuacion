
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import bernoulli,norm
#%%

N=120
S=norm(0,1).rvs(size=N)
H=norm(0,0.5*abs(S)).rvs(size=N)
sns.scatterplot(S)
sns.scatterplot(H)

plt.hist(H, bins=100)
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.title('distribucion normal')
plt.show()

D=np.random.binomial(n=1, p=0.5, size=N)
Hstar=H.copy()
Hstar[D==1]=np.nan




# Define the parameters
N = 100
S = np.random.normal(size=N)
H = np.random.normal(loc=(1-np.exp(-0.7*S)), size=N)
D = np.random.binomial(1, p=np.where(S > 0, 1, 0), size=N)
Hstar = H.copy()
Hstar[D == 1] = np.nan

# Plot the data
#plt.plot(S, H, color='gray', linewidth=2)
plt.scatter(S, Hstar, color='red', s=30, linewidth=3)

# Add labels and title
plt.xlabel('S')
plt.ylabel('H and Hstar')
plt.title('Normal Distributions')

# Display the plot
plt.show()

# %%
#Dog eats homework itself:
N = 100
S = np.random.normal(size=N)
H = np.random.normal(loc=0.5*S, size=N)
D = np.random.binomial(1, p=np.where(H<0, 0.9, 0), size=N)
Hstar = H.copy()
Hstar[D == 1] = np.nan

# Plot the data
#plt.plot(S, H, color='gray', linewidth=2)
plt.scatter(S, Hstar, color='red', s=30, linewidth=3)

# Add labels and title
plt.xlabel('S')
plt.ylabel('H and Hstar')
plt.title('Normal Distributions')

# Display the plot
plt.show()
# %%
#Dog eats random homework
N = 100
S = np.random.normal(size=N)
H = np.random.normal(loc=0.5*S, size=N)
D = np.random.binomial(1, p=0.5, size=N)
Hstar = H.copy()
Hstar[D == 1] = np.nan

# Plot the data
#plt.plot(S, H, color='gray', linewidth=2)
plt.scatter(S, Hstar, color='red', s=30, linewidth=3)

# Add labels and title
plt.xlabel('S')
plt.ylabel('H and Hstar')
plt.title('Normal Distributions')

# Display the plot
plt.show()
sns.histplot(S, kde=True, stat="density")
# %%
N = 100
S = np.random.normal(size=N)

# Generate the plot
sns.histplot(S, kde=True, stat="density")
# %%