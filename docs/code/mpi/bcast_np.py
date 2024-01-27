from mpi4py import MPI
import numpy as np 

comm = MPI.COMM_WORLD
rank = comm.rank 

if rank == 0: 
    data = np.arange(100, dtype = np.float64)
else:
    data = np.empty(100, dtype = np.float64)

comm.Bcast(data, root = 0)

print("rank of current process is % d" % rank + "\n" + "data is", data, "\n")

