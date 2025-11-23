import numpy as np
from scipy.signal import TransferFunction

num = [0.5, -0.8, 0.315]
den = [1, -1.0, 0.24]

system = TransferFunction(num, den)
poles = system.poles
print("Poles of H(z):", poles)

stable = all(np.abs(p) < 1 for p in poles)
print("System Stability:", "Stable" if stable else "Unstable")
