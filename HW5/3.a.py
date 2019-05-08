import numpy as np
import matplotlib.pyplot as plt
import math


j = np.complex(0, 1)
pi = np.pi
e = np.e

def avvali(r):
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-1*r,1*r,1):
            if k==0:
                temp += 0
            else:
                temp += (np.sin(2*pi/3)*k-np.sin(pi/3)*k)*(e**(j*2*pi*pi*n/3))/(pi*k)
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
                temp += (np.sin(2*pi/3)*k-np.sin(pi/3)*k)*(e**(j*k*6*n))/(pi*k)
        y.append(temp)
    return y

# calculate fourie coefficients
g1 = avvali(1)
g2 = avvali(2)
g3 = avvali(5)
g4 = avvali(10)
g5 = avvali(50)

g6 = dovvomi()
# draw coefficinets
x2 = np.arange(-10,10,0.001)
# np.subpl
# chart1 = plt.subplot(311)
plt.plot(x2, np.real(g1))
# chart2 = plt.subplot(312)
plt.plot(x2, np.real(g2))
# chart1 = plt.subplot(313)
plt.plot(x2, np.real(g3))
# chart2 = plt.subplot(314)
plt.plot(x2, np.real(g4))



# Show
plt.show()