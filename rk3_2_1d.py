import numpy as np
import matplotlib.pyplot as plt

y_0 = np.array([0,2])
alpha = 0.8
x_span = [0 ,2*np.pi]
h_0 = 0.1

def real_solution(x):
    return np.array([np.sin(2*x), 2*np.cos(2*x)])

def f(x,y):
    return np.array([y[1], -4*np.sin(2*x)])

def rk3_2(x_span, y_n, h_0, tol, f, alpha):

    x_values = [x_span[0]]
    y_values = [y_n]
    h_values = [h_0]

    x_n = x_span[0]
    x_end = x_span[1]
    h = h_0
    k1 = f(x_n, y_n)
    
    while x_end - x_n > tol:
        h = min(h, x_end - x_n)

        k2 = f(x_n + h/2, y_n + h/2 * k1)
        k3 = f(x_n + 3/4*h, y_n + 3/4*h*k2)
        y_n1 = y_n + h/9 * (2*k1 + 3*k2 + 4*k3)

        k4 = f(x_n + h, y_n1)
        z_n1 = y_n + h/24*(7*k1 + 6*k2 + 8*k3 + 3*k4)

        est = np.linalg.norm(y_n1 -z_n1)
        
        if est < tol:
            x_n += h
            y_n = y_n1
            k1 = k4

            x_values.append(x_n)
            y_values.append(y_n)
            h_values.append(h)  
            
        h_new = alpha * h * (tol/est)**(1/3)
        h = h_new
    return (np.array(x_values),
            np.array(y_values),
            np.array(h_values))

tol_list = np.logspace(-8, -2,50)
errors = []

for tol in tol_list:
    x_values, y_values, h_values = rk3_2(x_span, y_0, h_0 , tol, f, alpha)
    y_exact = real_solution(x_values).T
    error_total = np.max(np.abs(y_values - y_exact))
    errors.append(error_total)

plt.figure()
plt.loglog(tol_list, errors, 'o-')
plt.xlabel('tol')
plt.ylabel('error')
plt.title('Error vs tolerance')
plt.grid()
plt.show()