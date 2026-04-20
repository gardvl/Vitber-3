import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import opg_2f as opg_2f
import opg_2e as opg_2e
import Opg_2h as opg_2h
import opg_2i as opg_2i


def usadel_solution_general_2(l, m, zeta, theta_l, theta_r, eps_list,make_gamma_left, make_gamma_thilde_left, make_gamma_right, make_gamma_thilde_right):
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
        x = sol.x
        y = sol.y
    return solutions


m = 101
zeta = 3
theta_l = 0
theta_r = 0

eps_list = np.linspace(2, 0, 101)
l_list = [0.5, 1, 2]


solutions = []

for l in l_list:
    x_vec = np.linspace(0, l, m)
    sol = usadel_solution_general_2(l, m, zeta, theta_l, theta_r, eps_list, opg_2i.make_gamma_left, opg_2i.make_gamma_thilde_left, opg_2i.make_gamma_right, opg_2i.make_gamma_thilde_right)
    solutions.append(sol)

plt.figure()

for l, sol_list in zip(l_list, solutions):
    x_vec = np.linspace(0, l, m)
    x_mid_index = len(x_vec) // 2

    D_over_D0 = opg_2h.make_D_over_D_0(x_vec, eps_list, sol_list)

    plt.plot(eps_list, D_over_D0[:, x_mid_index], label=f"l = {l}")

plt.xlabel("epsilon")
plt.ylabel("D/D0 at x = l/2")
plt.title("Density of states at the midpoint")
plt.legend()
plt.grid()
plt.show()



