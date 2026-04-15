#Oppgave 2f
import numpy as np
import opg_2c as opg2c

def usadel_boundary(v_left, v_right, epsilon, gamma_left, gamma_thilde_left, gamma_right, gamma_thilde_right, l, zeta):
    gamma_0, gamma_thilde_0, omega_0, omega_thilde_0 = opg2c.one_vec_to_four_M(v_left)
    gamma_l, gamma_thilde_l, omega_l, omega_thilde_l = opg2c.one_vec_to_four_M(v_right)

    N_L = np.linalg.inv((np.identity(2, dtype = complex)-gamma_left(epsilon) @ gamma_thilde_left(epsilon)))
    N_thilde_L = np.linalg.inv((np.identity(2, dtype = complex)-gamma_thilde_left(epsilon) @ gamma_left(epsilon)))

    m1 = omega_0 + 1/(l*zeta)*(np.identity(2, dtype=complex)-gamma_0 @ gamma_thilde_left(epsilon)) @ N_L @ (gamma_l - gamma_left(epsilon))
    m2 = omega_thilde_0 + 1/(zeta*l)*(np.identity(2, dtype= complex)-gamma_thilde_0 @ gamma_left)