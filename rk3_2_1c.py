import numpy as np
import matplotlib.pyplot as plt

y_0 = np.array([0,2])
tol = 10e-7
alpha = 0.8
x_span = [0 ,2*np.pi]
h_0 = 0.1

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
'''
x_values, y_values, h_values = rk3_2(x_span, y_0, h_0 , tol, f, alpha)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_values, y_values[:, 0], label='y_1')
plt.plot(x_values, y_values[:, 1], label='y_2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.title('Solution of the ODE')

plt.subplot(1, 2, 2)
plt.plot(x_values, h_values, label='Step Size')
plt.xlabel('x')
plt.ylabel('h')
plt.grid()
plt.legend()
plt.title('Step Size Evolution')

plt.tight_layout()
plt.show()

'''