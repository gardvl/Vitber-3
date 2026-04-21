#Oppgave 2n
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson
import opg_2k
import opg_2i
import opg_2l
m = 101
zeta = 3


eps_list = np.linspace(2, 0, 101)
l = 1

x_vec = np.linspace(0, l, m)

theta_l_arr = np.linspace(0, 2*np.pi, 21)
theta_r = 0
fig1 = plt.figure(figsize= (12,6))
current_integrand = []
for theta_l in theta_l_arr:
    solutions = opg_2k.usadel_solution_general_2(l, m, zeta, theta_l, theta_r, eps_list, opg_2i.make_gamma_left, opg_2i.make_gamma_thilde_left, opg_2i.make_gamma_right, opg_2i.make_gamma_thilde_right)
    current_densities = opg_2l.j(eps_list, solutions)
    current_integrand.append(simpson(-1*current_densities[:, 50], eps_list)) #ganger med -1 siden epsilon går fra 2 til 0, istedenfor 0 til 2
plt.plot(theta_l_arr, np.array(current_integrand))
plt.title("Current integrands as function of phase differense")
plt.xlabel("$\\Delta \\Phi \\in $[0, 2$\\pi$]")
plt.ylabel("$I/I_0$")
plt.grid()
plt.legend()
plt.show()