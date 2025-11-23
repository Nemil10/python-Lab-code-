import numpy as np
from scipy.signal import TransferFunction

def z_transform_unit_step(z):
    return 1 / (1 - 1/z)

def check_stability(den):
    system = TransferFunction([1], den)
    poles = system.poles
    print("Poles:", poles)
    stable = all(np.abs(p) < 1 for p in poles)
    print("System Stability:", "Stable" if stable else "Unstable")

print("U(Z) =", z_transform_unit_step(2))
