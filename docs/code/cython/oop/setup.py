from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("fruit.pyx", annotate = True) # annotate 参数可以生成一个html文件, 查看哪些地方被Cython编译过了.
)
