from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

data = (rank + 1) ** 2
data = comm.gather(data, root=0)

if rank == 0:
    print ("rank = %s " %rank + "...receiving data from other process")
    print(data)
    for i in range(1, size):
        data[i] = (i+1)**2
    print(data)

