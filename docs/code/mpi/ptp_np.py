from mpi4py import MPI
import numpy as np 

comm = MPI.COMM_WORLD

size = comm.size
rank = comm.rank

if rank == 0: 
    data = np.arange(10, dtype = np.float64)
    comm.Send(data, dest = 1, tag = 13)
elif rank == 1: 
    data = np.empty(10, dtype = np.float64)
    print("rank of current process is % d" % rank)
    print("data before recv", data)
    recv = comm.Recv(data, source = 0, tag = 13)
    print("data after recv", data)
