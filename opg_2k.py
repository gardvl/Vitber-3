import numpy as np

eps_list = np.linspace(0, 2, 101)
y_guess = np.zeros((32, m))

solutions = []

for eps in eps_list:
    bc = opg2f.make_bc(opg2f.usadel_boundary,
         eps, gamma_left, gamma_thilde_left, gamma_right,
         gamma_thilde_right, l, zeta)
    fun = opg2e.make_function(opg2e.better_function, eps)
    sol = solve_bvp(fun, bc, x_vec, y_guess)
    solutions.append(sol)
    y_guess = sol.y