from mpi4py import MPI
import numpy as np 


# 利用并行的方式将 arr 中的所有元素进行平方
def parallel_ele_square(arr):
    # 先将元素进行分组, 对于 i % size == r, 则将 arr[i] 分配到第 r 个处理器上.
    comm = MPI.COMM_WORLD
    rank = comm.rank 
    size = comm.size
    if rank == 0:
        data_to_share = []
        for i in range(size):
            data_to_share.append(arr[i::size])
    else:
        data_to_share = None
    # 利用 scatter 函数将数据发配到每个处理器上
    recvbuf = comm.scatter(data_to_share, root = 0)
    print("process id is % d; " % rank + " data is ", recvbuf)
    square_data = recvbuf ** 2
    square_data = comm.gather(square_data, root = 0)
    if rank == 0: 
        res = np.empty(arr.shape)
        print("receiving data : ", square_data, "from other process ...")
        # 将数据在 process 0 上合并
        for i in range(size):
            res[i::size] = square_data[i]
        return res
    else: 
        res = None
if __name__ == "__main__":
    a = parallel_ele_square(np.arange(20))
    print(a)


