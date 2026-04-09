import numpy as np

def g(z):
    return z + np.sin(z) + np.cos(z)

def secant(g,z0,z1,tol):
    g0 = g(z0)
    g1 = g(z1)

    while abs(z1-z0) > tol:
        z2 = (z0*g1 - z1*g0) / (g1 - g0)

        z0 = z1
        z1 = z2

        g0 = g1
        g1 = g(z1)
    return z1

z1 = secant(g, -1, 1, 1e-7)
print(z1)