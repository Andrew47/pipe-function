A Pipe Function for Python
============================

This code seeks to leverage partial functions to create a pipe function, where the user first inputs the data they would like to process and then inputs a series of functions that they would like to apply to the data.

The aim is to simplify syntax. Suppose we have functions `f`, `g` and `h` and we wish to apply them as follows `f(g(h(x)))`. Instead our `pipe` allows this to be written as `pipe(x)([f,g,h])`.

##Usage

Download the folder either as a zipped folder or using git. From the file pipe import the function pipe.

We can then replace the following:

````
def plus1(arg): return arg + 1
def plus2(arg): return arg + 2
def plus3(arg): return arg + 3

plus3(plus2(plus1(30)))

````

With this:

````
from pipe import pipe

pipe(30)([plus1
        , plus2
        , plus3])
````

Note that the first function need not have an argument, and `pipe` can be applied to just one function - i.e., `pipe()(some_function_without_argument)` matches `some_function_without_argument()`.

The first function applied must only have one argument.

##Author

* [Andrew Burnie](https://github.com/Andrew47)
