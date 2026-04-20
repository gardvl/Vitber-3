#Oppgave 2f
import numpy as np
import opg_2c as opg2c

def usadel_boundary(v_left, v_right, epsilon, gamma_left, gamma_thilde_left, gamma_right, gamma_thilde_right, l, zeta):
    gamma_0, gamma_thilde_0, omega_0, omega_thilde_0 = opg2c.one_vec_to_four_M(v_left)
    gamma_l, gamma_thilde_l, omega_l, omega_thilde_l = opg2c.one_vec_to_four_M(v_right)

    N_L = np.linalg.inv((np.identity(2, dtype = complex)-gamma_left(epsilon) @ gamma_thilde_left(epsilon)))
    N_thilde_L = np.linalg.inv((np.identity(2, dtype = complex)-gamma_thilde_left(epsilon) @ gamma_left(epsilon)))

    N_R = np.linalg.inv((np.identity(2, dtype = complex)-gamma_right(epsilon) @ gamma_thilde_right(epsilon)))
    N_thilde_R = np.linalg.inv((np.identity(2, dtype = complex)-gamma_thilde_right(epsilon) @ gamma_right(epsilon)))

    m1 = omega_0 + 1/(l*zeta)*(np.identity(2, dtype=complex)-gamma_0 @ gamma_thilde_left(epsilon)) @ N_L @ (gamma_left(epsilon) - gamma_0)
    m2 = omega_thilde_0 + 1/(l*zeta)*(np.identity(2, dtype=complex)-gamma_thilde_0 @ gamma_left(epsilon)) @ N_thilde_L @ (gamma_thilde_left(epsilon) - gamma_thilde_0)

    m3 = omega_l - 1/(l*zeta)*(np.identity(2, dtype=complex)-gamma_l @ gamma_thilde_right(epsilon)) @ N_R @ (gamma_right(epsilon) - gamma_l)
    m4 = omega_thilde_l - 1/(l*zeta)*(np.identity(2, dtype=complex)-gamma_thilde_l @ gamma_right(epsilon)) @ N_thilde_R @ (gamma_thilde_right(epsilon) - gamma_thilde_l)

    return opg2c.four_M_to_one_vec(m1, m2, m3, m4)

def make_bc(boundary, epsilon, gamma_left, gamma_thilde_left, gamma_right, gamma_thilde_right, l, zeta):
    def bc(v_left, v_right):
        return boundary(v_left, v_right, epsilon, gamma_left, gamma_thilde_left, gamma_right, gamma_thilde_right, l, zeta)
    return bc