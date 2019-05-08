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
lengeth = np.sqrt(np.real(y)**2+np.imag(y)**2)

x2 = np.arange(-1*range_cnt, 1*range_cnt, 1)
# draw coefficinets
chart1 = plt.subplot(311)
plt.title("Original signal")
plt.stem(x2, x)
chart1 = plt.subplot(312)
plt.title("FT length")
plt.stem(x2, lengeth)
chart1 = plt.subplot(313)
plt.title("FT phase")
plt.stem(x2, phase)

# # Show
plt.show()