import numpy as np

def vector_combine(m1, m2, m3, m4):
    return np.concatenate([m1, m2, m3, m4])

def vector_uncombine(m):
    m1 = m[:8]
    m2 = m[8:16]
    m3 = m[16:24]   
    m4 = m[24:32]
    return m1, m2, m3, m4

'''

m1 = [1,2,3,4,5,6,7,8]
m2 = [1,2,3,4,5,6,7,8]
m3 = [1,2,3,4,5,6,7,8]
m4 = [1,2,3,4,5,6,7,8]

v = vector_combine(m1, m2, m3, m4)
m1_, m2_, m3_, m4_ = vector_uncombine(v)

print(np.allclose(m1, m1_))
print(np.allclose(m2, m2_))
print(np.allclose(m3, m3_))
print(np.allclose(m4, m4_))

'''