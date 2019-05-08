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

def signal(a, k_range):
    xx = []
    T = len(x)
    for n in range(len(x)):
        temp = 0
        for k in range(-1*k_range, k_range, 1):
            temp += a[n]*(e**(j*k*2*pi*n/T))
        xx.append(temp)
    return xx

# input
print("Please enter the array of y1:")
x = list(map(float, input().split()))
k_range = 5
print(x, k_range)

# calculate fourie coefficients
a = coefficients(x, k_range)
xx = coefficients(a, k_range)
print(len(a))

# draw coefficinets
x2 = np.arange(-1*k_range, 1*k_range, 1)
plt.stem(x2, np.real(xx))

# Show
plt.show()