import numpy as np
import opg_2a
import opg_2b

def four_M_to_one_vec(M1,M2,M3,M4):
    v1 = opg_2a.Matrix_to_vec(M1)
    v2 = opg_2a.Matrix_to_vec(M2)
    v3 = opg_2a.Matrix_to_vec(M3)
    v4 = opg_2a.Matrix_to_vec(M4)
    return opg_2b.vector_combine(v1, v2, v3, v4)

def one_vec_to_four_M(v):
    v1, v2, v3, v4 = opg_2b.vector_uncombine(v)
    M1 = opg_2a.vec_to_Matrix(v1)
    M2 = opg_2a.vec_to_Matrix(v2)
    M3 = opg_2a.vec_to_Matrix(v3)
    M4 = opg_2a.vec_to_Matrix(v4)
    return M1, M2, M3, M4

'''
M1 = np.array([[1+2j, 3+4j],
               [5+6j, 7+8j]])

M2 = np.array([[2+1j, 4+3j],
               [6+5j, 8+7j]])

M3 = np.array([[1+1j, 2+2j],
               [3+3j, 4+4j]])

M4 = np.array([[5+0j, 0+5j],
               [1+2j, 2+1j]])

v = four_M_to_one_vec(M1, M2, M3, M4)
M1_, M2_, M3_, M4_ = one_vec_to_four_M(v)

print("M1:", np.allclose(M1, M1_))
print("M2:", np.allclose(M2, M2_))
print("M3:", np.allclose(M3, M3_))
print("M4:", np.allclose(M4, M4_))
'''

