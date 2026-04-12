#Solving initial boundary problem with scipy

import scipy.integrate as sp
import numpy as np
import matplotlib.pyplot as plt
import Oppgave1g as opg1g
import rk3_2_1c as opg1c
import rk3_2_1_f as opg1f


def f(x,y):
    return np.array([y[1], y[0]+np.sin(x)])

def boundary_cond(ya, yb):
    return np.array([ya[0], yb[0]])



x_list_list, y_list_list, h_list_list = opg1f.secant_RK(opg1c.rk3_2,-3,4,1e-7, np.array([0,12]), 0.1, 1e-7,opg1g.g, 0.8)
y_vals = np.array(y_list_list[-1])[:, 0]

x_arr = np.array(x_list_list[-1])
y_start_arr = np.zeros((2,x_arr.size))


scipyLøsning = sp.solve_bvp(f, boundary_cond, x_arr, y_start_arr)


fig = plt.figure(figsize=(12,6))
plt.subplot(1,2,1)
plt.plot(x_arr, scipyLøsning.y[0], label = "Scipy sol")
plt.plot(x_list_list[-1], y_vals, label = "RK3,2 sol", linestyle = "--")
plt.legend()
plt.grid()
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(1,2,2)
plt.plot(x_arr, y_vals-scipyLøsning.y[0])
plt.grid()
plt.xlabel("x")
plt.ylabel("Differense between solutions")


plt.show()