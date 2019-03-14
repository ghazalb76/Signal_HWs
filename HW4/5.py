import numpy as np
import matplotlib.pyplot as plt

signal = [0, 2, 2, 2, 0]
h1 = [0, 1, -1, 0, 0]
h2 = [0, 0, 1, -1, 0]
h = [0, 1, 0, -1, 0]

r1 = np.convolve(signal, h1)
r2 = np.convolve(signal, h2)
r = [x11 + x22 for (x11, x22) in zip(r1, r2)]

rt = np.convolve(signal, h)

x = np.arange(0, 5, 1)

# Show charts
chart1 = plt.subplot(311)
plt.title('Draw X')
plt.stem(x, signal)

chart3 = plt.subplot(312)
plt.title('Draw h')
plt.stem(x, h)

t = np.arange(0, 9, 1)
chart3 = plt.subplot(313)
plt.title('Draw y')
plt.stem(t, rt)

plt.show()
