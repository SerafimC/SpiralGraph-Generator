import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('seaborn-pastel')

X_CENTER, Y_CENTER, RADIUS = 50, 50, 20
X_CENTER2, Y_CENTER2, RADIUS2 = 50, 50, 3

height, width = 100, 100
frm = 200

last_x = -1

X_IMAGE, X_IMAGE2 = [], []
Y_IMAGE, Y_IMAGE2 = [], []

images = []

fig = plt.figure()
ax = plt.axes(xlim=(0, width), ylim=(0, height))
images.append(ax.plot([], [], lw=3)[0])
images.append(ax.plot([], [], lw=3)[0])


def calc_image(a, b, r, x):
    delta = (-2*b)**2 - 4*( b**2 - r**2 + (x-a)**2)
    r1 = (2*b + np.sqrt(delta)) / 2
    r2 = (2*b - np.sqrt(delta)) / 2

    return r1, r2

def plot_circle(j):
    half_time = int(frm /2)
    i = j if j < half_time else j - half_time
    
    if j < half_time:
        x = np.linspace(X_CENTER-RADIUS, X_CENTER+RADIUS, half_time)
        y1, y2 = calc_image(X_CENTER, Y_CENTER, RADIUS, x[i])

        global last_x

        X_IMAGE2.append(x[i])
        Y_IMAGE2.append(y1)

        # ===========================================
        # TESTE CIRCULO INTERNO
        x2 = np.linspace(x[i]-RADIUS2, x[i]+RADIUS2, half_time)
        for k in range(half_time):
            if k+i < half_time and (k+i)%2 == 0:
                if x2[k+i] > last_x:
                    y1_2, y2_2 = calc_image(x[i], y1, RADIUS2, x2[k+i])

                    X_IMAGE.append(x2[k+i])
                    Y_IMAGE.append(y1_2)
                    # X_IMAGE.append(x2[k+i])
                    # Y_IMAGE.append(y2_2)

            else:
                if k+i < frm and (k+i)%2 == 0:
                    if x2[k+i] > last_x:
                        y1_2, y2_2 = calc_image(x[i], y1, RADIUS2, x2[k+i])

                        X_IMAGE.append(x2[k+i])
                        Y_IMAGE.append(y2_2)
                        # X_IMAGE.append(x2[k+i])
                        # Y_IMAGE.append(y2_2)

        
        last_x = x2[-1:] if last_x > x2[-1:] else -1
        # ===========================================
        
    else :
        x = np.linspace(X_CENTER-RADIUS, X_CENTER+RADIUS, half_time)
        y1, y2 = calc_image(X_CENTER, Y_CENTER, RADIUS, x[(half_time-1)-i])

        X_IMAGE2.append(x[(half_time-1)-i])
        Y_IMAGE2.append(y2) 
    
    images[0].set_data(X_IMAGE, Y_IMAGE)
    images[1].set_data(X_IMAGE2, Y_IMAGE2)


def init():
    images[0].set_data([], [])
    images[1].set_data([], [])
    
    return images[0], images[1]
def animate(i):
    
    plot_circle(i)
    
    return images[0], images[1]

anim = FuncAnimation(fig, animate, init_func=init, frames=frm, interval=20, blit=True)

anim.save('cir.gif', writer='imagemagick')