import numpy as np
import matplotlib.pyplot as plt

fs=1000
t=np.arange(0,1,1/fs)

x=np.sin(2*np.pi*10*t)
y=3*x

plt.plot(t,x)
plt.plot(t,y)
plt.show()
