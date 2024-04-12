import numpy as np 
from numpy.fft import fft

def test_fft()
    cdef double[::1] arr = np.arange(10, dtype = np.float64)
    cdef complex[::1] fft_arr = fft(arr)
    print(np.array(arr))
    print(np.array(fft_arr))
