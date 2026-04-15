#Oppgave 2i
import numpy as np
import matplotlib.pyplot as plt

zeta = 3

def make_v_minus(epsilon):
    return np.arctan(-1/(epsilon + 1j*zeta))

def make_v_plus(epsilon):
    return np.arctan(1/(epsilon + 1j*zeta))

def make_c_minus(epsilon):
    return np.cosh(make_v_minus(epsilon))

def make_c_plus(epsilon):
    return np.cosh(make_v_plus(epsilon))

def make_s_minus(epsilon):
    return np.sinh(make_v_minus(epsilon))

def make_s_plus(epsilon):
    return np.sinh(make_v_plus(epsilon))

theta_L = 0
theta_R = 0

def make_gamma_left(epsilon):
    return np.array([[0, make_s_plus(epsilon)/(1+make_c_plus(epsilon))], [make_s_minus(epsilon)/(1+make_c_minus(epsilon)), 0]], dtype=complex)*np.exp(1j*theta_L)

def make_gamma_thilde_left(epsilon):
    return np.array([[0, make_s_minus(epsilon)/(1+make_c_minus(epsilon))], [make_s_plus(epsilon)/(1+make_c_plus(epsilon)), 0]], dtype=complex)*np.exp(-1j*theta_L)

def make_gamma_right(epsilon):
    return np.array([[0, make_s_plus(epsilon)/(1+make_c_plus(epsilon))], [make_s_minus(epsilon)/(1+make_c_minus(epsilon)), 0]], dtype=complex)*np.exp(1j*theta_R)

def make_gamma_thilde_right(epsilon):
    return np.array([[0, make_s_minus(epsilon)/(1+make_c_minus(epsilon))], [make_s_plus(epsilon)/(1+make_c_plus(epsilon)), 0]], dtype=complex)*np.exp(-1j*theta_R)