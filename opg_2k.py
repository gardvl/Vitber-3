import numpy as np
import matplotlib.pyplot as plt
import opg_2i as opg2i

m = 101
zeta = 3
theta_l = 0
theta_r = 0

eps_list = np.linspace(2, 0, 101)
l_list = [0.5, 1, 2]

solutiondict = {}



for l in l_list:
    y_guess = np.zeros((32, m))
    solutions = []
    for eps in eps_list:
        sol = opg2i.usadel_solution_general(l, m, zeta, theta_l, theta_r, eps_list, opg2i.make_gamma_left, opg2i.make_gamma_thilde_left, opg2i.make_gamma_right, opg2i.make_gamma_thilde_right)
        solutions.append(sol)
        y_guess = sol.y
    solutiondict[l] = solutions


