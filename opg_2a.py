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
    M = np.zeros((2,2), dtype=complex)
    k = 0
    for i in range(2):
        for j in range(2):
            M[i,j] = m[k]
            k += 1
    k = 0
    for i in range(2):
        for j in range(2):
            M[i,j] += 1j * m[4 + k]
            k += 1

    return M

'''

M = np.array([[1+2j, 3+4j],
              [5+6j, 7+8j]])

m = Matrix_to_vec(M)
M_back = vec_to_Matrix(m)
print(np.allclose(M, M_back))
'''