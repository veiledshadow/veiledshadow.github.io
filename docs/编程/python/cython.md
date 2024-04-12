# Cython 初步

## 安装并利用 Cython 打印 Hellow World

1. 安装 `cython` 

在终端下运行 `pip install cython` 即可安装.

2. 新建名为 `hello.pyx` 的文件, 输入以下内容:

```Cython
def hellow():
    print("Hellow Cython!")
```

3. 编译 `.pyx` 文件

创建 `setup.py`，它是一个类似 Python Makefile 的文件（更多信息请看源文件和编译过程, 在 `setup.py` 中输入以下内容:

```
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("hello.pyx")
)
```


```
python setup.by build_ext --inplace

or 

python setup.by build_ext -if
```

如果是 Unix 系统, 执行过后会砸当前文件夹下生成一个 `.so` 文件, 该文件可以直接当作 python 库调用, 具体如下. 首先新建 `test.py` 文件, 在该文件中输入以下内容:

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







