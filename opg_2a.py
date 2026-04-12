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

def vec_to_Matrix(m):
    M = np.zeros((4,4), dtype=complex)
    for i in range(4):
        for j in range(4):
            M[i,j] = m[i*4+j]
    return M