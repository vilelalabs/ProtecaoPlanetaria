import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time

plt.style.use("dark_background")
plt.rc('font', size=15)

data = pd.read_csv('asteroid_data.txt', sep=',')

print(data)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='polar')
ax.scatter(data['angle[deg]']*np.pi/180, data['dist[AU]'], color='#FF6900', s=15)

theta = np.linspace(0,2*np.pi,1000)
r_T = 1 #orbita da terra = 1 [AU]

ax.plot(theta, np.repeat(r_T, 1000), color='blue')
ax.scatter(0,0, marker='o', color='yellow', s=100)





plt.show()
