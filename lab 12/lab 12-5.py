import numpy as np
import matplotlib.pyplot as plt

fs=1000
t=np.arange(0,1,1/fs)

x=np.sin(2*np.pi*5*t)
x_rev=x[::-1]   # reverse signal

plt.plot(t,x)
plt.plot(t,x_rev)
plt.show()
