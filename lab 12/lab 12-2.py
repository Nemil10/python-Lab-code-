import numpy as np
import matplotlib.pyplot as plt

fs = 500
t = np.arange(0, 2, 1/fs)

x1 = np.sin(2*np.pi*5*t)     # 5 Hz sine
x2 = np.cos(2*np.pi*10*t)    # 10 Hz cosine
y = x1 * x2                  # element-wise multiplication

plt.plot(t, y)
plt.title("Product of 5 Hz Sine and 10 Hz Cosine")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show() 
