from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

colsize = 10
sendbuf = np.arange(colsize, dtype=np.float64) + 10 * rank

recvbuf = None
if rank == 0:
    recvbuf = np.empty((size, colsize), dtype=np.float64)

comm.Gather(sendbuf, recvbuf, root=0)

print("rank of current process is % d" % rank + "\n recvbuf is : \n", recvbuf)
