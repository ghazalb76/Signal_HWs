import numpy as np
import matplotlib.pyplot as plt
import math


j = np.complex(0, 1)
pi = np.pi
e = np.e

def coefficients(x, k_range):
    a = []
    T = len(x)
    for k in range(-1*k_range, k_range, 1):
        temp = 0
        for n in range(len(x)):
            temp += x[n]*(e**(-1*j*k*2*pi*n/T))
        temp = temp/T
        a.append(temp)
    return a


def avvali(r, a):
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-1*r,1*r,1):
            if k==0:
                temp += 0
            else:
                temp += a[k]*(e**(j*2*pi*pi*n/3))/(pi*k)
        y.append(temp)
    return y

def dovvomi(a):
    y = []
    for n in np.arange(-10,10,0.001):
        temp = 0
        for k in range(-1,1,1):
            if k==0:
                temp += 0
            else:
                temp += a[k]*(e**(j*k*6*n))/(pi*k)
        y.append(temp)
    return y

# input
print("Please enter the array of y1:")
x = list(map(float, input().split()))
k_range = 5
print(x, k_range)

# calculate fourie coefficients
a = coefficients(x, k_range)
print(len(a))

# calculate fourie coefficients
g1 = avvali(1, a)
g2 = avvali(2, a)
g3 = avvali(5, a)
g4 = avvali(10, a)
g5 = avvali(50, a)

g6 = dovvomi(a)
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
