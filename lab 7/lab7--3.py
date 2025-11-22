import numpy as np

a = np.array([1, 2, 3, 5])
b = np.array([3, 4, 5, 7])

common = np.intersect1d(a, b)
print("Common values:", common)
