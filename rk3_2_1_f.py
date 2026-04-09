#Oppgave 1f)
import numpy as np
import matplotlib.pyplot as plt
import rk3_2_1c as opg1c


#Parameters
y_0 = np.array([0,2])
tol = 10e-7
alpha = 0.8
x_span = [0 ,2*np.pi]
h_0 = 0.1

def secant_RK(RK,b_0,b_1,b_tol, x_span, h_0, tol, alpha):
    x_list_list = []
    y_list_list = []
    h_list_list = []

    x_vals, y_vals, h_vals = RK(x_span, np.array([0,b_0]), h_0, tol, opg1c.f, alpha)
    x_list_list.append(x_vals)
    y_list_list.append(y_vals)
    h_list_list.append(h_vals)

    x_vals, y_vals, h_vals = RK(x_span, np.array([0,b_1]), h_0, tol, opg1c.f, alpha)
    x_list_list.append(x_vals)
    y_list_list.append(y_vals)
    h_list_list.append(h_vals)
    

    while abs(b_1-b_0) > b_tol:

        b_2 = (b_0*y_list_list[-1][-1] - b_1*y_list_list[-2][-1]) / (y_list_list[-1][-1] - y_list_list[-2][-1])

        b_0 = b_1
        b_1 = b_2

        x_vals, y_vals, h_vals = RK(x_span, np.array([0,b_1]), h_0, tol, opg1c.f, alpha)
        x_list_list.append(x_vals)
        y_list_list.append(y_vals)
        h_list_list.append(h_vals)
    return x_list_list, y_list_list, h_list_list


