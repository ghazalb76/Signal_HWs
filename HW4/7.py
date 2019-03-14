import random
import numpy as np
import matplotlib.pyplot as plt


# Create random signal
t = random.randint(3, 20)
y = []
for i in range(0,t):
    y.append(random.randint(1, 100))

# Create h
h = []
for i in range(0,t):
    h.append(0.25)

# Calculate output 
out = np.convolve(y, h)

# Show charts
chart1 = plt.subplot(311)
x = np.arange(0, t, 1)
plt.stem(x,y)

chart2 = plt.subplot(312)
plt.stem(x,h)

chart3 = plt.subplot(313)
x = np.arange(0, 2*t-1, 1)
plt.stem(x,out)
plt.show()
