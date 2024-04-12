from mpi4py import MPI
import numpy


def matvec(comm, A, x):
    m = A.shape[0]  # local rows
    p = comm.Get_size()
    xg = numpy.zeros(m*p, dtype=numpy.float64)
    comm.Allgather([x, MPI.DOUBLE], [xg, MPI.DOUBLE])

    print("rank = % d" % comm.rank)
    print(A)
    print(x)
    print(xg)
    y = numpy.dot(A, xg)
    return y


if __name__ == "__main__":
    A = numpy.arange(16, dtype=numpy.float64).reshape(4, 4)
    x = numpy.arange(4, dtype=numpy.float64)
    comm = MPI.COMM_WORLD
    y = matvec(comm, A, x)
    print(y)
