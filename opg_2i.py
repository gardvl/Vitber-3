#Oppgave 2i
import numpy as np
import matplotlib.pyplot as plt
import opg_2g
from Opg_2h import make_D_over_D_0

delta = 0.01

def make_v_minus(epsilon):
    return np.arctan(-1/(epsilon + 1j*delta))

def make_v_plus(epsilon):
    return np.arctan(1/(epsilon + 1j*delta))

def make_c_minus(epsilon):
    return np.cosh(make_v_minus(epsilon))

def make_c_plus(epsilon):
    return np.cosh(make_v_plus(epsilon))

def make_s_minus(epsilon):
    return np.sinh(make_v_minus(epsilon))

def make_s_plus(epsilon):
    return np.sinh(make_v_plus(epsilon))


def make_gamma_left(epsilon, theta_L):
    return np.array([[0, make_s_plus(epsilon)/(1+make_c_plus(epsilon))], [make_s_minus(epsilon)/(1+make_c_minus(epsilon)), 0]], dtype=complex)*np.exp(1j*theta_L)

def make_gamma_thilde_left(epsilon, theta_L):
    return np.array([[0, make_s_minus(epsilon)/(1+make_c_minus(epsilon))], [make_s_plus(epsilon)/(1+make_c_plus(epsilon)), 0]], dtype=complex)*np.exp(-1j*theta_L)

def make_gamma_right(epsilon, theta_R):
    return np.array([[0, make_s_plus(epsilon)/(1+make_c_plus(epsilon))], [make_s_minus(epsilon)/(1+make_c_minus(epsilon)), 0]], dtype=complex)*np.exp(1j*theta_R)

def make_gamma_thilde_right(epsilon, theta_R):
    return np.array([[0, make_s_minus(epsilon)/(1+make_c_minus(epsilon))], [make_s_plus(epsilon)/(1+make_c_plus(epsilon)), 0]], dtype=complex)*np.exp(-1j*theta_R)


l = 1
m = 101
eps_list = [0,1,2]
gamma_left = make_gamma_left()
solutions = opg_2g.usadel_solution(eps_list,l,m, gamma_left, gamma_thilde_left, gamma_right, gamma_thilde_right, delta)

x_vec = np.linspace(0, l, m)

densities = make_D_over_D_0(x_vec, eps_list, solutions)


