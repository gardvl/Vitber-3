#Oppgave 2l
import numpy as np
import matplotlib.pyplot as plt
import opg_2c
import Opg_2h
import opg_2k
import opg_2i

def j(epsilons, solutions):
    currents_list = []
    p_hat = Opg_2h.make_p_hat()
    for epsilon, solution in zip(epsilons, solutions):
        x_vec = solution.x
        gamma = []
        gamma_thilde = []
        omega = []
        omega_thilde = []
        for i in range(len(x_vec)):
            m1, m2, m3, m4 = opg_2c.one_vec_to_four_M(solution.y[:,i])
            gamma.append(m1)
            gamma_thilde.append(m2)
            omega.append(m3)
            omega_thilde.append(m4)
        gamma = np.array(gamma)
        gamma_thilde = np.array(gamma_thilde)
        omega = np.array(omega)
        omega_thilde = np.array(omega_thilde)
        N = np.zeros((x_vec.size, 2,2), dtype= complex)
        N_thilde = N.copy()
        del_N = N.copy()
        del_N_thilde = N.copy()
        g_hat = np.zeros((x_vec.size, 4,4), dtype= complex)
        del_g_hat = g_hat.copy()
        current = []
        for i, x in enumerate(x_vec):
            N[i] = np.linalg.inv(np.identity(2, dtype= complex) - gamma[i] @ gamma_thilde[i])
            N_thilde[i] = np.linalg.inv(np.identity(2, dtype= complex) - gamma_thilde[i] @ gamma[i])
            del_N[i] = N[i] @ (omega[i] @ gamma_thilde[i] + gamma[i] @ omega_thilde[i]) @ N[i]
            del_N_thilde[i] = N_thilde[i] @ (omega_thilde[i] @ gamma[i] + gamma_thilde[i] @ omega[i]) @ N_thilde[i]
            g_hat[i] = Opg_2h.make_4_by_4_matrix(2*N[i]-np.identity(2, dtype=complex), 2*N[i]@gamma[i], -2*N_thilde[i]@gamma_thilde[i], -2*N_thilde[i] + np.identity(2, dtype=complex))
            del_g_hat[i] =  2*Opg_2h.make_4_by_4_matrix(del_N[i], N[i] @ omega[i] + del_N[i] @ gamma[i], -1*N_thilde[i] @ omega_thilde[i] - del_N_thilde[i] @ gamma_thilde[i], -1*del_N_thilde[i])
            current.append(np.trace(p_hat @ (g_hat[i] @ del_g_hat[i] - del_g_hat[i]@ g_hat[i])).real)
        currents_list.append(np.array(current))
    return np.array(currents_list)


# m = 101
# zeta = 3
# theta_l = 0
# theta_r = 0

# eps_list = np.linspace(2, 0, 101)
# l = 1


# solutions = []

# fig = plt.figure(figsize = (12,6))

# x_vec = np.linspace(0, l, m)
# solutions = opg_2k.usadel_solution_general_2(l, m, zeta, theta_l, theta_r, eps_list, opg_2i.make_gamma_left, opg_2i.make_gamma_thilde_left, opg_2i.make_gamma_right, opg_2i.make_gamma_thilde_right)

# # D_over_D0 = Opg_2h.make_D_over_D_0(x_vec, eps_list, solutions)
# current_densities = j(eps_list, solutions)

# fig1 = plt.figure(figsize = (12,6))
# eps_index_list = [0, 25, 50, 75, 100]
# plt.title("Current densities of position")
# for i in eps_index_list:
#     plt.plot(x_vec, current_densities[i], label = f"$\\epsilon$ = {eps_list[i]}")
# plt.xlabel("x")
# plt.ylabel("$j$")
# plt.grid()
# plt.legend()
# plt.show()

# # plt.plot(eps_list, D_over_D0[:, x_mid_index], label=f"l = {l}")