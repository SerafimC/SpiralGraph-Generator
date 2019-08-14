import numpy as np
from matplotlib import pyplot as plt

X_CENTER, Y_CENTER, RADIUS = 50, 50, 20
X_CENTER2, Y_CENTER2, RADIUS2 = 50, 50, 3

switch_radius = True

X, Y = [], []
X2, Y2 = [], []

def calc_image(a, b, r, x):
    delta = (-2*b)**2 - 4*( b**2 - r**2 + (x-a)**2)
    r1 = (2*b + np.sqrt(delta)) / 2
    r2 = (2*b - np.sqrt(delta)) / 2

    return r1, r2

def plot_circle(a, b, r, k, dir):
    y1, y2 = calc_image(a, b, r, k)
        
    if dir == 'reversed':
        X2.append(k)
        Y2.append(y2)
    else:
        X2.append(k)
        Y2.append(y1)

def get_linspace_limits(w, a, r):

    if w >= 0 and w < 45:
        return a - r, a, 1
    elif w >= 45 and w < 90:
        return r, a + r, 0
    elif w >= 90 and w < 135:
        return a - r, a, 1
    elif w >= 135:
        return r, a + r, 0

w = 0
image = 1

for i in np.linspace(X_CENTER-RADIUS, X_CENTER+RADIUS, 180 ):
    y1, y2 = calc_image(X_CENTER, Y_CENTER, RADIUS, i)

    wa, wb, image = get_linspace_limits(w, i, RADIUS2)
    
    if image == 1:
        for j in np.linspace(wa, wb, 50):
            plot_circle(i, y1, RADIUS2, i, 'normal')
    else:
        for j in np.linspace(wa, wb, 50):
            plot_circle(i, y1, RADIUS2, i, 'reversed')
    w += 1
    X.append(i)
    Y.append(y1)
    
# for i in reversed(np.linspace(X_CENTER-RADIUS, X_CENTER+RADIUS, 20 )):
#     y1, y2 = calc_image(X_CENTER, Y_CENTER, RADIUS, i)

#     # if switch_radius:
#     #     RADIUS2 = 10
#     #     switch_radius = False
#     # else:
#     #     RADIUS2 = 3
#     #     switch_radius = True

#     for j in np.linspace(i-RADIUS2, i+RADIUS2, 20 ):
#         y1_2, y2_2 = calc_image(i, y2, RADIUS2, j)
        
#         X2.append(j)
#         Y2.append(y1_2)

#     for j in reversed(np.linspace(i-RADIUS2, i+RADIUS2, 20 )):
#         y1_2, y2_2 = calc_image(i, y2, RADIUS2, j)
        
#         X2.append(j)
#         Y2.append(y2_2)

#     X.append(i)
#     Y.append(y2)

plt.plot(X, Y)
plt.plot(X2, Y2)
plt.show()