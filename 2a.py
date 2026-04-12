import numpy as np

def Matrix_to_vec(M):
    m = []
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            m.append(np.real(M[i,j]))
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            m.append(np.imag(M[i,j]))
    return np.array(m)
