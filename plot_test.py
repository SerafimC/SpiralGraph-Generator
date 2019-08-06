import matplotlib.pyplot as plt
import numpy as np

x_centro = 1
y_centro = 1
raio = 1

def get_coordinates(raio, angulo):
    return (raio*np.cos(angulo), raio*np.sin(angulo))

angulos = np.arange(0, 2*np.pi, 0.01)

x = []
y = []

for angulo in angulos:
    x_i, y_i = get_coordinates(raio, angulo)
    
    x_i += x_centro
    y_i += y_centro
    
    x.append(x_i)
    y.append(y_i)

x.append(2.0)
y.append(1.0)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)  

ax.plot(x, y)
plt.show()