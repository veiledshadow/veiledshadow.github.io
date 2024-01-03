# 编译

## 编译第一个 C++ 文件

```c++
# include <iostream>

int main(int argc, char* argv[])
{
    // Print "Hellow World" to the screen
    std::cout<< "Hellow World \n" <<std::endl;
    return 0;
}
```

- 编译 C++ 文件

在终端中输入

```shell
    g++ -o HelloWorld HelloWorld.cpp
```

使用 `./HelloWorld` 运行生成的可执行文件.

## 编译器标识

如果我们试图编译一段没有使用正确 C++ 语法编写的代码、 那么编译器就会报错，无法生成可执行文件。因此，我们可以把编译器看作是能够 对代码的正确性进行验证的有利工具。

假设我们编写的代码将计算结果存储为一个变量，但这个变量后来从未被使用过。虽然这可能是用正确的 C++ 语法编写的，但这很可能是一个错误--我们希望每次计算的结果都会在代码的某个地方被使用，否则就没有必要执行这个计算了。否则就没有必要进行计算了。编译器可以通过使用编译器标志来警告我们出现类似的意外情况。下面的编译命令就会对此类情况发出警告。

```shell
    g++ -Wall -o HelloWorld HelloWorld.cpp
```
上述编译标志 -Wall 是 warning all 的缩写。上述编译命令会对任何实际上不是错误的意外情况发出警告，但仍会创建可执行文件。

假设我们希望比这更严格，希望编译器将任何意外情况都视为错误，因此在出现这种情况时不创建可执行文件。这可以通过下面的编译命令来实现。

```shell
    g++ -Wall -Werror -o HelloWorld HelloWorld.cpp
```

大多数编译器都有大量的编译器标志。在现阶段，除了基本的标志外，我们没有必要了解更多。我们已经展示了如何使用编译器标志对编写的代码进行一些验证。现在，我们将讨论另外三个在编写科学计算应用程序时尤为重要的标志。

第一个标志可用于优化可执行文件的性能。(默认情况下不进行优化)。如下所示，使用"-O"（大写 o）标志，可执行文件的执行速度会更快 尽管编译时间可能更长。

```shell
    g++ -O -o HelloWorld HelloWorld.cpp
```

如果我们要调试程序，可执行文件和调试器必须掌握源代码中哪一行产生了特定机器指令的信息。通常，编译后不会保留这些信息。为了生成保留调试信息的非优化代码版本，我们使用"-g "标记

```shell
    g++ -g -o HelloWorld HelloWorld.cpp
```

最后一个标志允许我们链接到一个数学例程库。我们使用下面的命令指示编译器链接到这个库。

```shell
    g++ -lm -o HelloWorld HelloWorld.cpp
```
# 变量

## 基本数值变量

- 整形, 浮点型数据的声明和初始化

```c++
/**
 *  allocate memory for two integer variables row and column
 *  and one double precision floating point variable temperature
 * **/
int row, column;
double temperature;

row = 1;
column = 2;
temperature = 3.0;
```

- 初始化变量的几种方式

在定义变量时初始化
```c++
int row = 1, column = 2;
double temperature = 3.0;
```

每个语句可以分配多个变量的值
```c++
int row = 1, column = 2; 
row = column = 3; 
/**
 * <=> row = (column = 3); 
 * mistake: (row = column) = 3
 * **/ 
```

定义常值变量
```c++
    const double density = 45.621
```

科学计数法

```c++
    double tolerance = 1.0e-12; 
```

## 数值类型的运算

```c++
#include <cmath>
#include <iostream>

using namespace std;

int main(){

    double a = 1.0, b = 2.0;
    double z = M_PI;

    cout << "PI is equal to " << z << endl;

    cout << " a + b is " << a + b << endl;
    cout << " a / b is " << a / b << endl;
    cout << " square root of b is " << sqrt(b) << endl;
    cout << " b power a is " << pow(b, a) << endl;
    cout << " exp a is " << exp(a) << endl;

    return 0;
}

```

## 数组

```c++
#include <iostream>

using namespace std;

int main(){

    // initialize a 1d array 

    const int len = 3;

    const int row = 2; 
    const int col = 2;

    int arr1d[len];
    double arr2d[row][col] = { {0.0, 1.0}, {2.0, 3.0} };

    arr1d[0] = 1;
    arr1d[1] = 2;
    arr1d[2] = 3;

    // print the array 
    for (int ii = 0; ii < len; ii++)
    {
        cout << "the  " << ii << "  element of the arr1d:  " << arr1d[ii] << endl;
    }
    
    return 0;
}

```

## ASCII 字符

```c++

#include <iostream>

int main(){

    char s = 'a';

    std::cout << s << std::endl;
    
    return 0;
}
```

## 布尔变量

```c++
int main(){

    bool flag1, flag2;

    flag1 = true;
    flag2 = false;

    return 0;
}

```

## 字符串

```c++
#include <iostream>
#include <string>

int main(int argc, char* argv[]){

    std::string city = "Oxford";

    std::cout << "size of total string: " << sizeof(city) << std::endl;
    std::cout << "size of a char of string " << sizeof(city[0]) << std::endl;

    // 遍历字符串

    // 用 city.length() 或 city.size() 均可以获得字符串对象的长度.
    // size() 函数还可以用于获得 vector 类型的长度.

    int length = city.length();

    for (int i = 0; i < length; i++){
        std::cout << std::to_string(i) + "th element of string:" << city[i] << std::endl;
    }

    return 0;
}
```

# 输入输出

## 简单终端输出

在终端中打印 "Hellow World!" 并换行.

```c++
#include <iostream>

int main(){
    std::cout<< "Hellow World!\n";
}
```
C++ 的输出是缓冲的。有时，例如，如果计算机忙于进行大量计算，程序可能不会立即将输出打印到屏幕上。如果希望立即输出，可在任何 std::cout 命令后使用语句 `std::cout.flush();`，以确保在执行任何其他语句前打印输出，如下所示。

```c++

#include <iostream>

int main(){
    std::cout<< "Hellow World!\n";
    std::cout.flash();
}

```
## 简单键盘输入

数字变量和字符的键盘输入使用输入流 `std::cin`，其中 cin 是 console in 的缩写。与控制台输出一样，必须包含 iostream 头文件。下面的代码会提示输入个人识别码（通常称为 PIN 码），然后将输入的数字赋值给整数变量 pin。

```c++
#include <iostream>
#include <string>

int main(){
    
    int pin;

    std::cout << "Input an integer number \n";
    std::cin >> pin;
    std::cout << "Your input is " + std::to_string(pin) + "\n";

    return 0;
}
```
`std::cin` 可用于一次请求多个输入, 如下所示:

```c++
#include <iostream>
#include <string>

int main(){
    
    int account_number, pin;

    std::cout << "Input an integer number \n";
    std::cin >> account_number >> pin;
    std::cout << "Your input is " + std::to_string(account_number) + "\n";
    std::cout << "Your input is " + std::to_string(pin) + "\n";

    return 0;
}
```
字符串类型变量的键盘输入略有不同。下面举例说明如何输入字符串。这里暂时不试图解释为什么要以这种方式输入字符串.这一点在之后 C++ 更高级特性时会讲解清楚。


```c++
#include <iostream>
#include <string>

int main(int argc, char* argv[]){


    std::string name;
    std::cout << "Please input your name \n";
    std::getline(std::cin, name);
    std::cout << "Your name is " + name + "\n";

    return 0;
}
```

# Assert 语句

科学计算应用通常需要进行大量复杂的数学计算。如果其中任何一项计算出现错误，那么计算的最终结果通常也会出现错误。查找错误源是一个极其繁琐的过程，因此强烈建议使用 C++ 语言的功能来识别意外情况，例如尝试计算负数的平方根。

在之后的章节中，我们指出了存在不同层次或程度错误的概念。我们特别介绍了异常，它是 C++ 语言的一个特性，可以非常有效地处理代码运行过程中出现的意外情况。一种不太复杂的方法是使用断言语句，如下所示 代码所示。请注意，要使用 assert 语句，必须包含额外的头文件 cassert。

```c++
#include <iostream>
#include <cassert>
#include <cmath>

int main(int argc, char* argv[]){

    double a;

    std::cout << "Please input a positive number \n";
    std::cin >> a; 
    assert( a >= 0.0 );
    std::cout << "The square root of a is : \n";
    std::cout << sqrt(a) << std::endl;

    return 0;
}
```
编译运行上面这段代码,如果输入为负,则直接报错:

```
a.out: Assert.cpp:11: int main(int, char**): Assertion `a >= 0.0' failed.
```

输入正数则能成功执行程序

```
Please input a positive number 
2
The square root of a is :
1.41421
```
与断言结合使用的另一个 C++ 函数是函数 `std::isfinite`。该函数允许确认变量 x 包含有限值，而不是无限值（例如，用非零数除以零得到的值）或其他未定义为数的值（例如负数的平方根或对数）。下面的代码片段说明了如何使用该函数和断言语句


```c++

#include <iostream>
#include <cassert>
#include <cmath>

int main(int argc, char* argv[]){

    double a;
    double b = 0.0;

    std::cout << "Please input a positive number \n";
    std::cin >> a; 
    assert( a >= 0.0 );
    std::cout << "The square root of a is : \n";
    std::cout << sqrt(a) << std::endl;

    // if a/b is infinity, the stop the program
    assert( !std::isinf(a/b) );

    std::cout << std::isinf(a/b) << std::endl;
    std::cout << a/b << std::endl;

    return 0;
}

```
虽然我们强调这只是识别错误的初级技术，我们稍后会引入更复杂的技术，但 `assert` 语句可以提供重要信息：在上面的错误信息中，我们可以看到发生问题的确切代码行已经被识别出来。

`assert` 语句的另一个优点是，当使用 `-DNDEBUG` 标志编译代码时，它们会被自动删除。这样，你就可以测试激活断言的代码，并通过使用命令 `-DNDEBUG` 编译来发布停用 `assert` 的更快程序。

```shell
g++ -DNDEBUG program.cpp

```
有许多工具旨在帮助代码的调试。其中最基本的是编译器，以及与编译器相关的标志，如第1.3.2节和第1.3.3节所述。还有更复杂的工具，但它们面向更大规模的项目，比如本书后面章节中将要开发的项目。与其在学习C++早期阶段学习如何使用复杂的调试工具，不如在本书早期章节中处理练习时采用一些更简单的调试技巧。

经常编译你的代码。经常保存你的代码，并且每次添加了几条语句后，使用第1.3.3节中描述的警告编译器标志进行编译，这是一种有用的诊断方法，可以查看是否引入了任何潜在问题。如果有任何问题，请注释掉新的语句并重新编译。然后逐一添加语句，直到确定问题所在。当你第一次在C++中编写代码时，你可能会惊讶地发现自己经常会忘记基本的语法，比如在语句末尾加上分号。

经常保存你的项目。如果你有一个可行的代码，并且需要添加新功能，那么不要丢弃旧版本。如果出现问题，你将能够准确地看到你做了哪些改动，如果其他方法都失败了，你还将有一个可工作的版本可以回滚到。如果有必要能够回滚到代码的工作版本，或者你正在进行协作项目，我们建议你使用版本控制系统。

始终使用简单的示例测试代码。例如，如果你正在编写代码以添加两个数组的元素，请通过与你自己进行的计算进行比较来验证输出。

了解执行代码时出现的错误。如果你的程序在执行时报`segmentation error`，那么很可能你尝试访问了数组的一个超出范围的成员：也就是说，你可能尝试访问一个只声明了有4个元素的数组的第6个条目。

使用输出。如果你需要知道程序在哪里崩溃，以及为什么崩溃，那么在执行过程中的关键点打印出一些变量的值。不要忘记刷新输出，以便在程序崩溃之前输出出现！

使用断言。如果你在代码段的开头期望某个属性，例如比例因子非零或平方根的参数非负，你可以使用 `assert` 来进行检查（在第1.6节介绍）。

C++数组从零开始索引。如果数组temperature被声明为有4个元素，则语句 `temperature[4] += 1.0;` 会引起问题。

使用调试器。如果其他方法都失败了，那么使用调试器来调试你的程序。关于如何使用调试器的提示可以在第7.7节找到。