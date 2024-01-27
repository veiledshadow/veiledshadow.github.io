from mpi4py import MPI 
import numpy as np 

comm = MPI.COMM_WORLD 
size = comm.size
rank = comm.rank 

if rank == 0:
    sendbuf = np.arange(size * 10, dtype = np.float64).reshape(size, 10)
else:
    sendbuf = None

recvbuf = np.empty(10, dtype = np.float64)
comm.Scatter(sendbuf, recvbuf, root = 0)

print("rank of current process is : % d" % rank + " data is : ", recvbuf)
