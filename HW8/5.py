import numpy as np
import matplotlib.pyplot as plt
import math


j = np.complex(0, 1)
pi = np.pi
e = np.e

def function(n):
    if n>=0 and n<=5:
        return n
    elif n>5 and n<=10:
        return 10-n
    else:
        return 0
    
x = []
range_cnt = 5000
for i in range(-1*range_cnt, 1*range_cnt):
    x.append(function(i))
y = np.fft.fft(x)

phase = np.arctan(np.imag(y), np.real(y))*180/pi


# draw coefficinets
x2 = np.arange(-1*range_cnt, 1*range_cnt, 1)
plt.stem(x2, t)

# # Show
plt.show()