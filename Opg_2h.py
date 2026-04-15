#Oppgave 2h


import numpy as np
import matplotlib.pyplot as plt

def make_4_by_4_matrix(m1, m2, m3, m4):
    return np.block([[m1, m2], [m3, m4]])


def make_p_hat():
    ident = np.identity(2, dtype=complex)
    zero = np.zeros((2,2), dtype = complex)
    return make_4_by_4_matrix(ident, zero, zero,  -1*ident)


def make_D_over_D_0(x, epsilon, gamma, gamma_thilde, ):
