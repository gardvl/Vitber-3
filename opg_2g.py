import numpy as np
import scipy as sp
import opg_2e as opg2e
import opg_2f as opg2f

l = 1
m = 101

x = np.linspace(0,l,m)
y = np.zeros((32,m))

eps = [0,1,2]

solutions = []

for i in eps:
    solve = sp.solve_bvp(opg_2e.better_function,)
