import sympy as sp

# Define symbols
n, z, w = sp.symbols('n z w')

# Define the sequence x[n] = cos(w*n) * u[n]
x_n = sp.cos(w * n)

# Compute the Z-transform
X_z = sp.summation(x_n * z**(-n), (n, 0, sp.oo))

# Print the result
print("Z-transform of x[n] = cos(w*n) u[n]:")
sp.pprint(X_z, use_unicode=True)
