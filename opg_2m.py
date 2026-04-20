import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_bvp
import opg_2k as opg_2k
import opg_2c
import Opg_2h
import opg_2k
import opg_2i
import opg_2l


m = 101
zeta = 3
theta_l = 1
theta_r = 0

eps_list = np.linspace(2, 0, 101)
l = 1

x_vec = np.linspace(0, l, m)
solutions = opg_2k.usadel_solution_general_2(l, m, zeta, theta_l, theta_r, eps_list, opg_2i.make_gamma_left, opg_2i.make_gamma_thilde_left, opg_2i.make_gamma_right, opg_2i.make_gamma_thilde_right)

# D_over_D0 = Opg_2h.make_D_over_D_0(x_vec, eps_list, solutions)
current_densities = opg_2l.j(eps_list, solutions)
middle_index = 50

fig1 = plt.figure(figsize = (12,6))
plt.plot(eps_list, current_densities[:, 50])
plt.title("Current densities at x = 1/2")
plt.title("Current densities of position")
plt.xlabel("$\\epsilon$")
plt.ylabel("$j$")
plt.grid()
plt.legend()
plt.show()
