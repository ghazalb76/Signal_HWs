import numpy as np
import matplotlib.pyplot as plt
import math


j = np.complex(0, 1)
pi = np.pi
e = np.e

def avvali():
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-1,1,1):
            if k==0:
                temp += 0
            else:
                temp += (np.cos(2*pi/3)*k-np.cos(pi/3)*k)*(e**(j*2*pi*pi*n/3))/(j*pi*k)
        y.append(temp)
    return y

def dovvomi():
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-1,1,1):
            if k==0:
                temp += 0
            else:
                temp += (np.cos(2*pi/3)*k-np.cos(pi/3)*k)*(e**(j*k*6*n))/(j*pi*k)
        y.append(temp)
    return y

# calculate fourie coefficients
g1 = avvali()
g2 = dovvomi()
# draw coefficinets
x2 = np.arange(-10,10,0.001)
# np.subpl
chart1 = plt.subplot(311)
plt.plot(x2, np.real(g1))
chart2 = plt.subplot(312)
plt.plot(x2, np.real(g2))

# Show
plt.show()