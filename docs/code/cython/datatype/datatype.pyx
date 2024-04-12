import cython
from libc.math cimport abs

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
    print("norm of c is", abs(c))

def display_arr():
    cdef int[10] arr
    for i in range(10):
        arr[i] = i
    print(arr) # 这里不同于C可以直接输出arr
    

cdef struct Person:
    char *name
    int age

def display_struct():
    cdef Person p = Person(name="Tom", age=20)
    print(f"My name is {p.name}, age is {p.age}")


def display_pointer():
    cdef int a = 10 
    cdef int* pa = &a
    # 在python中, *var 已经表示了对变量解包对操作, 因此不能用 *var 对一个指针解引用, 
    # 对指针解引用对操作改为 pa[0]
    pa[0] = 5
    print(f"current a is : {a}")

    


