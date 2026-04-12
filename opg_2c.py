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

