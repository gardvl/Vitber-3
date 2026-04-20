#Oppgave 2h
import numpy as np
import matplotlib.pyplot as plt
import opg_2c
import opg_2g 


def make_4_by_4_matrix(m1, m2, m3, m4):
    return np.block([[m1, m2], [m3, m4]])


def make_p_hat():
    ident = np.identity(2, dtype=complex)
    zero = np.zeros((2,2), dtype = complex)
    return make_4_by_4_matrix(ident, zero, zero,  -1*ident)


def make_D_over_D_0(x_vec, epsilons, solutions):
    densities = []
    for epsilon, solution in zip(epsilons, solutions):
        gamma = []
        gamma_thilde = []
        omega = []
        omega_thilde = []
        for i in range(len(solution.x)):
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
        g_hat = np.zeros((x_vec.size, 4,4), dtype= complex)
        density = []
        for i, x in enumerate(x_vec):
            N[i] = np.linalg.inv(np.identity(2, dtype= complex) - gamma[i] @ gamma_thilde[i])
            N_thilde[i] = np.linalg.inv(np.identity(2, dtype= complex) - gamma_thilde[i] @ gamma[i])
            g_hat[i] = make_4_by_4_matrix(2*N[i]-np.identity(2, dtype=complex), 2*N[i]@gamma[i], -2*N_thilde[i]@gamma_thilde[i], -2*N_thilde[i] + np.identity(2, dtype=complex))
            density.append(np.trace(make_p_hat() @ g_hat[i]).real/4)
        
        densities.append(np.array(density))
    return np.array(densities)

'''
zeta = 3

l = 1
m = 101
eps_list = [0,1,2]

solutions = opg_2g.usadel_solution(eps_list,l,m,opg_2g.gamma_left, opg_2g.gamma_thilde_left, opg_2g.gamma_right, opg_2g.gamma_thilde_right, zeta)

x_vec = np.linspace(0, l, m)

densities = make_D_over_D_0(x_vec, eps_list, solutions)

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