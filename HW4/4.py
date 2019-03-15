import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

x = [1, 2, 1, 0]
y = [0, 1, 1, 0]

h , r = signal.deconvolve(y, x)

t = np.arange(0, 4, 1)
# Show charts
chart1 = plt.subplot(311)
plt.title('Draw X')
plt.stem(t, x)

print(h)
t2 = np.arange(0, 1, 1)
chart3 = plt.subplot(312)
plt.title('Draw h')
print(h)
plt.stem(t2, h)

t3 = np.arange(0, 4, 1)
chart3 = plt.subplot(313)
plt.title('Draw y')
plt.stem(t3, y)

plt.show()
