import numpy as np
from scipy.integrate import solve_bvp
import opg_2e as opg2e
import opg_2f as opg2f

def usadel_solution(eps_list,l,m,gamma_left, gamma_thilde_left, gamma_right, gamma_thilde_right, zeta):
    solutions = []
    x = np.linspace(0,l,m)
    y = np.zeros((32,m))
    for i in eps_list:
        bc = opg2f.make_bc(opg2f.usadel_boundary,
             i, gamma_left, gamma_thilde_left, gamma_right,
             gamma_thilde_right, l, zeta)
        fun = opg2e.make_function(opg2e.better_function, i)
        sol = solve_bvp(fun, bc, x, y)
        solutions.append(sol)

def gamma_left(epsilon):
    return np.zeros((2,2), dtype=complex)

def gamma_thilde_left(epsilon):
    return np.zeros((2,2), dtype=complex)

def gamma_right(epsilon):
    return np.zeros((2,2), dtype=complex)

def gamma_thilde_right(epsilon):
    return np.zeros((2,2), dtype=complex)
zeta = 3

l = 1
m = 101
eps_list = [0,1,2]