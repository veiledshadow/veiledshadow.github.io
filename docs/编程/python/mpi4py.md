# mpi4py 的安装以及初步使用

## 在 macOS 系统上安装mpi4py并测试

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

## 死锁

当两个或多个进程都在阻塞并等待对方释放自己想要的资源的情况,会面临死锁, 程序员必须遵守一定当编码的规则, 来避免死锁问题.

下面的代码中介绍了一种典型的死锁问题

```python
rank = comm.rank
print("my rank is : " , rank)

if rank==1:
    data_send= "a"
    destination_process = 5
    source_process = 5
    data_received=comm.recv(source=source_process)
    comm.send(data_send,dest=destination_process)
    print("sending data %s " %data_send + "to process %d" %destination_process)
    print("data received is = %s" %data_received)

if rank==5:
    data_send= "b"
    destination_process = 1
    source_process = 1
    data_received=comm.recv(source=source_process)
    comm.send(data_send,dest=destination_process)
    print("sending data %s :" %data_send + "to process %d" %destination_process)
    print("data received is = %s" %data_received)
```

运行这个程序会发现两个进程都无法完成. 会发生这种情况是因为MPI的 comm.recv() 函数和 comm.send() 函数都是阻塞的. 它们的调用者都在等待它们完成. 对 comm.send() MPI来说, 只有数据发出之后函数才会结束, 对于 comm.recv() 函数来说, 只有接收到数据函数才会结束. 为了避免死锁, 通常有两种方法, 第一种将上面代码修改如下：

```python
rank = comm.rank
print("my rank is : " , rank)

if rank==1:
    data_send= "a"
    destination_process = 5
    source_process = 5
    comm.send(data_send,dest=destination_process)
    data_received=comm.recv(source=source_process)
    print("sending data %s " %data_send + "to process %d" %destination_process)
    print("data received is = %s" %data_received)

if rank==5:
    data_send= "b"
    destination_process = 1
    source_process = 1
    comm.send(data_send,dest=destination_process)
    data_received=comm.recv(source=source_process)
    print("sending data %s :" %data_send + "to process %d" %destination_process)
    print("data received is = %s" %data_received)
```

或者使用`Sendrecv` 函数, 这个函数统一了向一特定进程发消息和从一特定进程接收消息的功能, 
```python
Sendrecv(self, sendbuf, int dest=0, int sendtag=0, recvbuf=None, int source=0, int recvtag=0, Status status=None)
```
可以将之前的程序发送和接收的过程直接改写如下：

``` python 
if rank==1:
    data_send= "a"
    destination_process = 5
    source_process = 5
    data_received=comm.sendrecv(data_send,dest=destination_process,source =source_process)

if rank==5:
    data_send= "b"
    destination_process = 1
    source_process = 1
    data_received=comm.sendrecv(data_send,dest=destination_process, source=source_process)
```
## 集体通讯

在并行代码的开发中，我们会经常发现需要在多个进程间共享某个变量运行时的值，或操作多个进程提供的变量（可能具有不同的值)。


### 使用 broadcast 函数进行通讯

![](broadcast.png) 

将所有进程变成通讯者的这种方法叫做集体交流. 因此, 一个集体交流通常是2个以上的进程. 我们也可以叫它广播—— 一个进程发送消息给其他的进程. `mpi4py` 模块通过以下的方式提供广播的功能：

```python
buf = comm.bcast(data_to_share, rank_of_root_process)
```

具体使用方式如下: 我们有一个root进程, rank 等于0, 保存自己的数据 variable_to_share, 以及其他定义在通讯组中的进程.

```python
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.rank

if rank == 0:
    data_to_share = "hellow world"
else:
    data_to_share = None
data_to_share = comm.bcast(data_to_share, root=0)

print("process id % d" % rank + " data shared % s" % data_to_share)
```
运行结果如下:
```
process id  0 data shared hellow world
process id  1 data shared hellow world
process id  2 data shared hellow world
process id  3 data shared hellow world
process id  4 data shared hellow world
process id  5 data shared hellow world
process id  6 data shared hellow world
process id  7 data shared hellow world
```

### 使用 scatter 函数进行通讯
`scatter` 函数和 `broadcast` 函数很像, 但是有一个很大的不同, `comm.bcast` 将相同的数据发送给所有在监听的进程, `comm.scatter` 可以将数据放在数组中, 发送给不同的进程. 下图展示了`scatter`函数的功能：

![](scatter.png) 

`comm.scatter` 函数接收一个`array`, 根据进程的`rank`将其中的元素发送给不同的进程. 比如第一个元素将发送给进程0, 第二个元素将发送给进程1, 等等. `mpi4py` 中的函数原型如下:

```python
recvbuf  = comm.scatter(sendbuf, rank_of_root_process)
```
得到以下输出结果:

```
process id  0 recvbuf =  1
process id  1 recvbuf =  2
process id  2 recvbuf =  3
process id  3 recvbuf =  4
process id  4 recvbuf =  5
process id  6 recvbuf =  7
process id  7 recvbuf =  8
process id  5 recvbuf =  6
```
需要注意的是, comm.scatter 有一个限制, 发送数据的列表中元素的个数必须和接收的进程数相等. 举个例子, 如果列表中的个数比进程数多, 就会报错.

### 使用 gather 函数进行通讯

`gather` 函数是反向的 `scatter` 函数, 即收集所有进程发送向root进程的数据. `mpi4py` 实现的 `gather` 函数如下:



![](gather.png) 

