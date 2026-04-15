#Oppgave 2h
import numpy as np
import matplotlib.pyplot as plt
import opg_2c


def make_4_by_4_matrix(m1, m2, m3, m4):
    return np.block([[m1, m2], [m3, m4]])


def make_p_hat():
    ident = np.identity(2, dtype=complex)
    zero = np.zeros((2,2), dtype = complex)
    return make_4_by_4_matrix(ident, zero, zero,  -1*ident)


def make_D_over_D_0(x_vec, epsilons, solutions):
    densities = []
    for epsilon, solution in zip(epsilons, solutions):
        gamma, gamma_thilde, omega, omega_thilde = opg_2c.one_vec_to_four_M(solution.y) 
        
        N = np.zeros((x_vec.size, 2,2), dtype= complex)
        N_thilde = N
        g_hat = np.zeros((x_vec.size, 4,4), dtype= complex)
        density = []
        for i, x in enumerate(x_vec):
            N[i] = np.invert(np.identity(2, dtype= complex) - gamma[i] @ gamma_thilde[i])
            N_thilde[i] = np.invert(np.identity(2, dtype= complex) - gamma_thilde[i] @ gamma[i])
            g_hat[i] = make_4_by_4_matrix(2*N[i]-np.identity(2, dtype=complex), 2*N[i]@gamma[i], -2*N_thilde[i]@gamma_thilde[i], -2*N_thilde[i] + np.identity(2, dtype=complex))
            density.append(np.trace(make_p_hat() @ g_hat[i]).real/4)
        
        densities.append(np.array(density))
    return np.array(densities)


