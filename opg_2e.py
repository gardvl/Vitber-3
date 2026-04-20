#Oppgave 2e)
import numpy as np
import scipy as sp
import opg_2d as opg2d


# def function(x_vec, vec, epsilon):
#     del_vec = np.zeros_like(vec)
#     for i in range(len(vec)):
#         del_vec[i] = opg2d.usadel_eq_1d(vec[i], epsilon)
#     return del_vec


def better_function(x_vec, vec, epsilon):
    return np.array([opg2d.usadel_eq_1d(v, epsilon) for v in np.transpose(vec)]).T

# def best_function(x_vec, vec, epsilon):
#     return opg2d.usadel_eq_1d(vec, epsilon)

# def bestest_function():
#     pass

def make_function(f, epsilon):
    def func(x_vec, vec):
        return f(x_vec, vec, epsilon)
    return func