from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data_to_share = "hellow world"
else:
    data_to_share = None
data_to_share = comm.bcast(data_to_share, root=0)

print("process id % d" % rank + " data shared % s" % data_to_share)
