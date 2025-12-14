---
title: A Python Primer for Matlab Users
date: 2013-01-20 10:55
filetags: python matlab
---

> Why would you want to use Python over Matlab?

- Because Python is free and Matlab is not.
- Because Python is a general purpose programming language and Matlab is not.

Let me qualify that a bit. Matlab is a very useful programming environment for numerical problems. For a very particular set of problems, Matlab is an awesome tool. For many other problems however, it is just about unusable. For example, you would not write a complex GUI program in Matlab, you would not write your blogging engine in Matlab and you would not write a web service in Matlab. You can do all that and more in Python.

# Python as a Matlab replacement

The biggest strength of Matlab is its matrix engine. Most of the data you work with in Matlab are matrices and there is a host of functions available to manipulate and visualize those matrices. Python, by itself, does not have a convenient matrix engine. However, there are three packages (think Matlab Toolboxes) out there that will add this capability to Python:

- Numpy (the matrix engine)
- Scipy (matrix manipulation)
- Matplotlib (plotting)

You can either grab the individual installers for [Python](http://python.org), [Numpy](http://numpy.org), [Scipy](http://scipy.org) and [Matplotlib](http://matplotlib.org) from their respective websites, or get them pre-packaged from [pythonxy()](https://code.google.com/p/pythonxy/) or [EPD](http://www.enthought.com/products/epd.php).

# A 30,000 foot overview

Like Matlab, Python is _interpreted_, that is, there is no need for a compiler and code can be executed at any time as long as Python is installed on the machine. Also, code can be copied from one machine to another and will run without change.

Like Matlab, Python is _dynamically typed_, that is, every variable can hold data of any type, as in:

```python
    # Python
    a = 5         # a number
    a = [1, 2, 3] # a list
    a = 'text'    # a string
```

Contrast this with C, where you can not assign different data types to the same variable:

```c
    // C
    int a = 5;
    float b[3] = {1.0, 2.0, 3.0};
    char c[] = "text";
```

Unlike Matlab, Python is _strongly typed_, that is, you can not add a number to a string.
In Matlab, adding a single number to a string will convert that string into an array of numbers, then add the single number to each of the numbers in the array. Python will simply throw an error.

```octave
    % Matlab
    a = 'text'
    b = a + 5 % [121 106 125 121]
```

```python
    # Python
    a = 'text'
    b = a + 5 # TypeError: Can't convert 'int' object to str implicitly
```

Unlike Matlab, every Python file can contain as many functions as you like. Basically, you can organize your code in as many files as you want. To access functions from other files, use `import filename`.

Unlike Matlab, Python is very quick to start. In fact, most operating systems automatically start a new Python process whenever you run a Python program and quit that process once the program has finished. Thus, every Python program behaves as if it indeed were an independent program. There is no need to wait for that big Matlab mother ship to start before writing or executing code.

Unlike Matlab, the source code of Python is readily available. Every detail of Python's inner workings is available to everyone. It is thus feasible and encouraged to actively participate in the development of Python itself or some add-on package. Furthermore, there is no dependence on some company deciding where to go next with Python.

# Reading Python

When you start up Python, it is a rather empty environment. In order to do anything useful, you first have to `import` some functionality into your workspace. Thus, you will see a few lines of `import` statements at the top of every Python file. Moreover, Python has _namespaces_, so if you `import numpy`, you will have to prefix every feature of Numpy with its name, like this:

```python
    import numpy
    a = numpy.zeros(10, 1)
```

This is clearly cumbersome if you are planning to use Numpy all the time. So instead, you can import all of Numpy into the global environment like this:

```python
    from numpy import *
    a = ones(30, 1)
```

Better yet, there is a pre-packaged namespace that contains the whole Numpy-Scipy-Matplotlib stack in one piece:

```python
    from pylab import *
    a = randn(100, 1)
    plot(a)
    show()
```

Note that Python does not plot immediately when you type `plot()`. Instead, it will collect all plotting information and only show it on the screen once you type `show()`.

So far, the code you have seen should look pretty familiar. A few differences:

- No semicolons at the end of lines;
  In order to print stuff to the console, use the `print()` function instead.

- No `end` anywhere.
  In Python, blocks of code are identified by indentation and they always start with a colon like so:

```python
    sum = 0
    for n in [1, 2, 3, 4, 5]:
        sum = sum + n
    print(sum)
```

- Function definitions are different.
  They use the `def` keyword instead of `function`.
  You don't have to name the output variable names in the definition and instead use `return()`.

```python
    # Python
    def abs(number):
        if number > 0:
            return number
        else:
            return -number
```

```octave
    % Matlab
    function [out] = abs(number)
        if number > 0
            out = number
        else
            out = -number
        end
    end
```

- There is no easy way to write out a list or matrix.
  Since Python only gains a matrix engine by importing Numpy, it does not have a convenient way of writing arrays or matrices.   This sounds more inconvenient than it actually is, since you are probably using mostly functions like `zeros()` or `randn()` anyway and those work just fine. Also, many places accept Python lists (like this `[1, 2, 3]`) instead of Numpy arrays, so this rarely is a problem. Note that you _must_ use commas to separate items and can not use semicolons to separate lines.

```python
    # create a numpy matrix:
    m = array([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
    # create a Python list:
    l = [1 2 3]
```

- Arrays access uses brackets and is numbered from 0.
  Thus, ranges _exclude_ the last number (see below).
  Mostly, this just means that array access does not need any `+1` or `-1` when indexing arrays anymore.

```python
    a = linspace(1, 10, 10)
    one = a[0]
    two = a[1]

    # "6:8" is a range of two elements:
    a[6:8] = [70, 80] # <-- a Python list!
```

# Common traps

- Array slicing does not copy.

```python
    a = array([1 2 3 4 5])
    b = a[1:4] # [2 3 4]
    b[1] = rand() # this will change a and b!
    # make a copy like this:
    c = array(a[1:4], copy=True) # copy=True can be omitted
    c[1] = rand() # changes only c
```
- Arrays retain their data type.
  You can slice them, you can dice them, you can do math on them, but a 16 bit integer array will never lose its data type. Use `new = array(old, dtype=double)` to convert an array of any data type to the default `double` type (like in Matlab).

```python
    # pretend this came from a wave file:
    a = array([1000, 2000, 3000, 4000, 5000], dtype=int16)
    a = a * 10 # int16 only goes to 32768!
    # a is now [10000, 20000, 30000, -25536, -15536]
```


# Going further

Now you should be able to read Python code reasonably well. Numpy, Scipy and Matplotlib are actually modeled after Matlab in many ways, so many functions will have a very similar name and functionality. A lot of the numerical code you write in Python will look very similar to the equivalent code in Matlab. For a more in-depth comparison of Matlab and Python syntax, head over to [the Numpy documentation for Matlab users](http://www.scipy.org/NumPy_for_Matlab_Users).

However, since Python is a general purpose programming language, it offers some more tools. To begin with, there are a few more data types like associative arrays, tuples (unchangeable lists), proper strings and a full-featured object system. Then, there is a plethora of add-on packages, most of which actually come with your standard installation of Python. For example, there are [internet protocols](http://docs.python.org/3/library/internet.html), [GUI programming frameworks](http://www.riverbankcomputing.com/software/pyqt/intro), [real-time audio interfaces](https://people.csail.mit.edu/hubert/pyaudio/), [web frameworks](https://www.djangoproject.com) and [game development libraries](http://www.pygame.org/). Even [this very blog](https://github.com/bastibe/bastibe.github.com/tree/source) is created using a Python [static site generator](http://pelican.readthedocs.org).

Lastly, Python has a great [online documentation site](http://docs.python.org/3/) including a [tutorial](http://docs.python.org/3.3/tutorial/), there are [many books](http://wiki.python.org/moin/PythonBooks) [on Python](http://www.learnpythonthehardway.org/) and there is a helpful [Wiki on Python](http://wiki.python.org/moin/BeginnersGuide). There is also a [tutorial](http://scipy.org/Cookbook) and [documentation](http://scipy.org/Getting_Started) for Numpy, Scipy and [Matplotlib](http://matplotlib.org/contents.html).

A great way to get to know any programming language is to solve the first few problems on [project euler](https://projecteuler.net/).
