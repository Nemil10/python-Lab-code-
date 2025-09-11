import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0, 1, 1/fs)

x1 = np.sin(2*np.pi*5*t)     # 5 Hz sine
x2 = np.sin(2*np.pi*10*t)    # 10 Hz sine
y = x1 + x2                  # combined signal

plt.plot(t, y)
plt.title("5 Hz + 10 Hz Sine Wave")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.show()

