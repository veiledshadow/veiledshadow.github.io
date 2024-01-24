# mpi4py 的安装以及初步使用

## 在 MACOS 系统上安装mpi4py并测试

1. 安装`homebrew`
2. 在终端中运行命令 `brew install open-mpi` 安装 `open-mpi`
3. 在终端中运行命令 `conda install mpi4py` 安装 `mpi4py`
4. 测试:新建第一个名为 `hello_parallel.py` 的 python 文件, 输入以下内容:

```python
from mpi4py import MPI 

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print("hellow world parallel, rank = ", rank)
```
在终端中输入
```
mpiexec -n 4 python hello_parallel.py
```
来运行 `hello_parallel.py` 文件, 返回以下结果
```
hellow world parallel, rank =  0
hellow world parallel, rank =  2
hellow world parallel, rank =  3
hellow world parallel, rank =  1
```
表示已经安装并运行成功.

在 MPI 中, 并行程序中不同进程用一个非负的整数来区别, 叫做rank. 如果我们有p个进程, 那么rank会从 0 到 p-1 分配。MPI 中获取 rank 的函数为 `comm.Get_rank()`

这个函数返回调用他的进程的 rank.

## 点对点通讯
两个不同的进程之间可以通过点对点通讯交换数据:一个进程是接收者,一个进程是发送者.

`mpi4py` 通过以下两个函数实现了点对点通讯:

- `Comm.Send(data, process_destination)` 发送数据给指定进程.

- `Comm.Recv(process_source)` 从源进程接收数据.

点对点通讯点代码示例: 创建 `python` 文件 `point_to_point.py`
```
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank
print("my rank is : ", rank)

if rank == 0: 
    # 发送者进程, rank 0 的进程发送数据给 rank4 进程.
    data = 10000
    destination_process = 4 
    comm.send(data, dest = destination_process) # 发送数据,需要指定接收者的rank
    print("sending data % s " % data + "to process % d" % destination_process)

if rank == 1: 
    # 发送者进程, rank 1 的进程发送数据为 rank7 进程.
    destination_process = 7 
    data = "hello"
    comm.send(data, dest = destination_process)
    print("sending data % s :" % data + "to process % d" % destination_process)

if rank == 4: 
    # 接收者进程, 从 rank 0 进程接收数据.
    data = comm.recv(source = 0) # 接收数据,需要指定发送者的rank.
    print("data received is = % s" % data)


if rank == 7: 
    # 接收者进程, 从 rank 1 进程接收数据.
    data1 = comm.recv(source = 1)
    print("data received is = % s" % data1)
```
设置最大进程数为8来运行文件
```
mpiexec -n 8 python point_to_point.py
```
得到如下运行结果:
```
my rank is :  4
my rank is :  6
my rank is :  5
my rank is :  2
my rank is :  3
my rank is :  7
my rank is :  0
sending data 10000 to process  4
data received is = 10000
my rank is :  1
sending data hello :to process  7
data received is = hello
```

总的来说,整个点对点通讯过程分为两部分,发送者发送数据,接收者接收数据,二者必须都指定发送方/接收方.
