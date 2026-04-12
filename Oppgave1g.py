#Oppgave 1g
import numpy as np
import matplotlib.pyplot as plt
import rk3_2_1_f as opg1f
import rk3_2_1c as opg1c

x_span = [0,12]
h_0 = 0.1
tol = 1e-7
alpha = 0.8

def g(x,y):
    return np.array([y[1], y[0]+np.sin(x)])

'''
x_list_list, y_list_list, h_list_list = opg1f.secant_RK(opg1c.rk3_2,-3,4,1e-7, x_span, h_0, tol,g, alpha)

y_vals = y_list_list[-1]
y_vals = list(np.array(y_vals)[:, 0])
plt.plot(x_list_list[-1], y_vals)
plt.grid()
plt.xlabel("x")
plt.ylabel("y")
plt.title("Boundary value problem")
plt.show()
'''
