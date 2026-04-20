#Oppgave 2i
import numpy as np
import matplotlib.pyplot as plt
import opg_2g
from Opg_2h import make_D_over_D_0
import opg_2f
import opg_2e
from scipy.integrate import solve_bvp

delta = 0.01

def make_v_minus(epsilon):
    return np.arctanh(-1/(epsilon + 1j*delta))

def make_v_plus(epsilon):
    return np.arctanh(1/(epsilon + 1j*delta))

def make_c_minus(epsilon):
    return np.cosh(make_v_minus(epsilon))

def make_c_plus(epsilon):
    return np.cosh(make_v_plus(epsilon))

def make_s_minus(epsilon):
    return np.sinh(make_v_minus(epsilon))

def make_s_plus(epsilon):
    return np.sinh(make_v_plus(epsilon))


def make_gamma_left(theta_L):
    def gamma_left(epsilon):
        return np.array([[0, make_s_plus(epsilon)/(1+make_c_plus(epsilon))], [make_s_minus(epsilon)/(1+make_c_minus(epsilon)), 0]], dtype=complex)*np.exp(1j*theta_L)
    return gamma_left

def make_gamma_thilde_left(theta_L):
    def gamma_thilde_left(epsilon):
        return np.array([[0, make_s_minus(epsilon)/(1+make_c_minus(epsilon))], [make_s_plus(epsilon)/(1+make_c_plus(epsilon)), 0]], dtype=complex)*np.exp(-1j*theta_L)
    return gamma_thilde_left

def make_gamma_right(theta_R):
    def gamma_right(epsilon):
        return np.array([[0, make_s_plus(epsilon)/(1+make_c_plus(epsilon))], [make_s_minus(epsilon)/(1+make_c_minus(epsilon)), 0]], dtype=complex)*np.exp(1j*theta_R)
    return gamma_right

def make_gamma_thilde_right(theta_R):
    def gamma_thilde_right(epsilon):
        return np.array([[0, make_s_minus(epsilon)/(1+make_c_minus(epsilon))], [make_s_plus(epsilon)/(1+make_c_plus(epsilon)), 0]], dtype=complex)*np.exp(-1j*theta_R)
    return gamma_thilde_right

l = 1
m = 101
zeta = 3
eps_list = [2]
theta_l = 0
theta_r = 0


def usadel_solution_general(l, m, zeta, theta_l, theta_r, eps_list,make_gamma_left, make_gamma_thilde_left, make_gamma_right, make_gamma_thilde_right):
    solutions = []
    x = np.linspace(0,l,m)
    y = np.zeros((32,m))
    for epsilon in eps_list:
        gamma_left = make_gamma_left(theta_l)
        gamma_right = make_gamma_right(theta_r)
        gamma_thilde_left = make_gamma_thilde_left(theta_l)
        gamma_thilde_right = make_gamma_thilde_right(theta_r)
        bc = opg_2f.make_bc(opg_2f.usadel_boundary, epsilon, gamma_left, gamma_thilde_left, gamma_right,
             gamma_thilde_right, l, zeta)
        fun = opg_2e.make_function(opg_2e.better_function, epsilon)
        sol = solve_bvp(fun, bc, x, y)
        solutions.append(sol)
    return solutions


'''

x_vec = np.linspace(0, l, m)

løsninger = usadel_solution_general(l, m, zeta, theta_l, theta_r, eps_list, make_gamma_left, make_gamma_thilde_left, make_gamma_right, make_gamma_thilde_right)

densities = make_D_over_D_0(x_vec, eps_list, løsninger)

x_vec = np.linspace(0, l, m)

fig1 = plt.figure(figsize= (12,6))
plt.title("Densities for each $\\epsilon$")
for i, epsilon in enumerate(eps_list):
    plt.plot(x_vec, densities[i], label = f"$\\epsilon$ = {epsilon}")
plt.xlabel("x")
plt.ylabel("$D/D_0$")
plt.grid()
plt.legend()
plt.show()

'''

