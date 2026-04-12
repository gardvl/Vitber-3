import numpy as np
import opg_2a
import opg_2b
import opg_2c


def usadel_1d(v,epsilon):
    gamma, gamma_tilde, omega, omega_tilde = opg_2c.vec_to_four_M(v)

    I = np.identity(2, dtype=complex)
    N = np.linalg.inv(I-gamma @ gamma_tilde)
    N_tilde = np.linalg.inv(I - gamma_tilde @ gamma)

    delta = 0.01

    delta_gamma = omega
    delta_gamma_tilde = omega_tilde
    delta_omega = -2j*(epsilon + 1j*delta)*gamma - 2*(omega @ N_tilde @ gamma_tilde @ omega)
    delta_omega_tilde = -2j*(epsilon + 1j*delta)*gamma_tilde - 2*(omega_tilde @ N @ gamma @ omega_tilde)

    return opg_2c.four_M_to_one_vec(delta_gamma, delta_gamma_tilde, delta_omega, delta_omega_tilde )





    