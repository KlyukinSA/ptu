import matplotlib.pyplot as plt
import numpy as np


seq = [1, 0, 1, 0, 0, 1, 1, 0]
Fs = 8000
f = 1
sample = 30
n = len(seq)
x = np.arange(sample * n)
y = np.sin(2 * np.pi * 1.5 * x[0:sample] / sample)
z = np.array([seq[0]] * sample)
state = 1
for i in range(n - 1):
    ny = np.sin(2 * np.pi * 1.5 * x[sample * (i + 1):sample * (i + 2)] / sample)
    if (seq[i+1] == 0):
        state *= -1
    nz = np.array([seq[i+1]] * sample)
    y = np.concatenate((y, state * ny), axis=None)
    z = np.concatenate((z, nz), axis=None)
plt.subplot(2, 1, 1)
plt.plot(x, y)
for xc in sample * np.arange(n):
    plt.axvline(x=xc)
plt.xlabel('sample(n)')
plt.ylabel('voltage(V)')

plt.subplot(2, 1, 2)
plt.plot(x, z)
plt.xlabel('sample(n)')
plt.ylabel('seq(i)')
plt.show()
