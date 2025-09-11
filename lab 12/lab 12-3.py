import numpy as np
import matplotlib.pyplot as plt

fs = 1000
t = np.arange(0,1,1/fs)

x = np.sin(2*np.pi*5*t)
x_shift = np.sin(2*np.pi*5*(t-0.1))

plt.plot(t,x,label="original")
plt.plot(t,x_shift,label="shifted")
plt.legend()
plt.show()
