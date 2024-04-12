import numpy as np
from createview import display_data, change_data

display_data()

a = np.array([1, 2, 3, 4, 5], dtype = np.float64)
change_data(a.copy())
print(a)
