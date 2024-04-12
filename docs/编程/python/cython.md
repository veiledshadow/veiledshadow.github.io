# Cython

## Beginning

安装并利用 Cython 打印 Hellow World

1. 安装 `cython` 

在终端下运行 `pip install cython` 即可安装.

2. 新建名为 `hello.pyx` 的文件, 输入以下内容:

```Cython
def hellow():
    print("Hellow Cython!")
```

3. 编译 `.pyx` 文件

创建 `setup.py`, 它是一个类似 Python Makefile 的文件（更多信息请看源文件和编译过程, 在 `setup.py` 中输入以下内容:

```
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("hello.pyx", annotate = True) # annotate 参数可以生成一个html文件, 查看哪些地方被Cython编译过了.
)
```


```
python setup.by build_ext --inplace

or 

python setup.by build_ext -if
```

如果是 Unix 系统, 执行过后会在当前文件夹下生成一个 `.so` 文件, 该文件可以直接当作 python 库调用, 具体如下. 首先新建 `test.py` 文件, 在该文件中输入以下内容:

```python
from hello import hellow
hellow()
```

在终端中输入

```
python test.py
```

就可以成功打印

```
Hellow Cython!
```

## Cython 的基本数据类型

### 基本变量(数, 字符)
在Cython 中用`cdef`进行变量声明: 

```cython 
cdef int a_global_variable

def func():
    cdef int i, j, k
    cdef float f
    cdef float[42] g
    cdef float *h
    # cdef float f, g[42], *h  # 不推荐混合使用指针,数组和值

    i = j = 5
```

可以在定义变量的同时进行初始化

```cython
cdef int a_global_variable = 42

def func():
    cdef int i = 10, j, k
    cdef float f = 2.5
    cdef int[4] g = [1, 2, 3, 4]
    cdef float *h = &f
    cdef double complex c = 2 + 3j
```

Cython 常用数据类型的四则运算(强制转换)以及复数的常用方法.
```cython 

@cython.wraparound(False) # Don't check negative index in looping
@cython.boundscheck(False) # Don't check index out of bound in looping
@cython.cdivision(True) # use the division in c
def display_values():

    cdef int a = 1 
    cdef int a2 = 2
    cdef double b = 3.14159
    cdef double complex c = 1.0 + 2.0j
    cdef double complex d = 2.0 + 3.0j

    # 测试输出
    print("a is a integer and a = ", a)
    print("b is a double and b = ", b)
    print("c is a complex valued double and c = ", c)
    print("d is a complex valued double and c = ", d)

    # 自动类型转换
    print("a divide a2 = ", a / a2) # 和C语言不同的是, 这边两个int作除法自动会转换为double型
    print("d multiply c = ", d * c)
    print("b multiply c = ", b * c)
    print("c divide b = ", c / b)
    print("c multiply d = ", c / d )
    print("a multiply b = ", a * b)

    # 复数的运算
    print("real part of c is", c.real, "imag part of c is", c.imag)
    print("conjugate of c is", c.conjugate())
    print("norm of c is", abs
```
### 数组

```cython
# 定义和打印数组
def display_arr():

    cdef int[10] arr
    for i in range(10):
        arr[i] = i
    print(arr) # 这里不同于C可以直接输出arr
```

### 结构体数组

在 Cython 中可以使用 `struct` 来定义结构体数组, 可以通过如下方式来定义和初始化一个结构体数组

```
cdef struct Person:
    char *name
    int age

def display_struct():
    # 初始化结构体的几种方法
    cdef Person p = Person(name="Tom", age=20)

    cdef Person p1 
    p1 = Person("Tom", 20)

    cdef Person p2 
    p2 = Person(name="Tom", age=20)

    print(f"My name is {p.name}, age is {p.age}")
```

### 指针变量

定义指针变量和对指针变量进行解引用

```
def display_pointer():
    cdef int a = 10 
    cdef int* pa = &a
    pa[0] = 5
    print(f"current a is : {a}")
```

 注意在Cython中对指针对解引用不能用`*var`, 因为 在python中, `*var` 已经表示了对变量解包对操作, 因此不能用 `*var` 对一个指针解引用. 对指针解引用对操作将改为`pa[0]`.

 ### 结构体指针

 Cython 中定义结构体指针对方式与C类似. 不同对是在Cython中可以通过`.`来直接访问成员变量, 无需使用 `->`.

 ## OOP in Cython (使用Cython扩展类)

 ### 定义简单的Cython扩展类

 定义一个扩展类: Cython 中定义扩展类用 `cdef class` 来进行声明, 作为示范, 下面是一个简单的水果类以及其在 Cython 内部的调用

```cython 
cdef class Fruit(object):
    cdef char* name 
    cdef double qty 
    cdef double price

    def __init__(self, nm, qt, pc):
        self.name = nm
        self.qty = qt
        self.price = pc

    def amount(self):
        return self.qty * self.price

def display_amount():
    cdef Fruit apple = Fruit(b"apple", 10, 2.5)
    print(f"The amount of {apple.name} is {apple.amount()}")
```

### 类成员访问控制

由Cython关键字`cdef class`生成的模版类集成了C++ `class` 的类成员访问控制特性, 因此在成员变量不加任何修饰符(默认为私有变量)时, 无法在外部直接使用点运算来访问成员变量. 如果想要成员变量能够在外部访问,需要加上`public`修饰符. Cython与C++访问控制修饰符具有如下对应关系

- `private`:对于Cython编译器来说, 任何使用cdef定义的类属性/方法默认是私有的, 类外部代码无法访问之,并且在声明类成员时,Cython语法层面不提供显式的`private`关键字声明, 因为像`cdef private double price` 等同画蛇舔足. 

- `public`: Cython编译器继承了C++这一特性, 例如类内声明`cdef public double price`,表示外部代码可以自由访问和修改该属性值. 

- `protected`:要在Cython中实现类似C++类继承的`protected`访问控制特性, 在Cython中不能使用`protected`, 而是使用`cppclass`关键字,关于此方面内容以后再说. 

## 容器

### vector 


### 内存视图

Cython的类型化内存视图允许对内存缓冲區有效地访问, Cython的內存视图比它集成的Numpy访问內存缓冲区数据更为底层和绝对的高效, 而不会引起任何Python开销, 因为这一切在Cython內部完成的. 内存视图类似于当前的NumPy数组缓冲区支持 (`np.ndarray[np.float64_t, ndim=2]`). 但是它们有更多的特性和更干净的语法. 

内存视图比NumPy数组缓冲区支持更通用, 因为它们可以处理更广泛的数组数据源. 例如, 它们可以处理C数组和Cython数组类型(Cython数组). 

内存视图可以在任何上下文中使用(函数参数、模块级、cdef类属性等), 并且几乎可以从任何通过PEP 3118缓冲区接口公开可写缓冲区的对象中获得. 


内存视图的类型声明:

使用Python切片语法和C數據類型的方式, 在Cython的上下文聲明內存視圖, 並且內存試圖的數據初始化操作, Cython會自動完成numpy的ndarray到內存視圖的數據類型轉換. 例如:


```cython
cdef int[:] arr = np.array([1, 2, 3])

cdef double arr[:, :] = np.array([[1.1, 1.2, 1.3], [1.4, 1.5, 1.6]])
```

内存视图可可以作为任意Python, Cython或混合函数的参数, 而返回值仅支持`cdef`关键词修饰的Cython函数. 举例如下:

```cython 
from libc.math import sqrt

cdef double calc_norm(double [:] x):

    double res = 0.0
    
    for i in range(x.shape[0]):
       res += x[i]  ** 2

    return sqrt(res)

```






