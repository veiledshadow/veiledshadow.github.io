
import numpy as np 

def display_data():
    a = np.array([1, 2, 3], dtype = np.float64)
    cdef double[:] b = a
    b[1] = 100
    print(b)
    print(a)

def change_data(double [:] view):
    view[1] = 10000

