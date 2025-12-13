---
title: Calling Matlab from Python
date: 2015-11-03 15:05
filetags: matlab python
---

For my latest experiments, I needed to run both Python functions and Matlab functions as part of the same program. As I [noted earlier](http://bastibe.de/2015-10-29-matlab-engine-leaks.html), Matlab includes the [Matlab Engine for Python](http://mathworks.com/help/matlab/matlab-engine-for-python.html) (MEfP), which can call Matlab functions from Python. Before I knew about this, I created [Transplant](https://github.com/bastibe/transplant), which does the very same thing. So, how do they compare?

## Usage

As it's name suggests, Matlab is a **mat**rix **lab**oratory, and matrices are the most important data type in Matlab. Since matrices don't exist in plain Python, the MEfP implements it's own as `matlab.double` et al., and you have to convert any data you want to pass to Matlab into one of those. In contrast, Transplant recognizes the fact that Python does in fact know a really good matrix engine called [Numpy](http:_scipy.org_), and just uses that instead.

```
       Matlab Engine for Python        |              Transplant
---------------------------------------|---------------------------------------
import numpy                           | import numpy
import matlab                          | import transplant
import matlab.engine                   |
                                       |
eng = matlab.engine.start_matlab()     | eng = transplant.Matlab()
numpy_data = numpy.random.randn(100)   | numpy_data = numpy.random.randn(100)
list_data = numpy_data.tolist()        |
matlab_data = matlab.double(list_data) |
data_sum = eng.sum(matlab_data)        | data_sum = eng.sum(numpy_data)
```

Aside from this difference, both libraries work almost identical. Even the handling of the number of output arguments is (accidentally) almost the same:

```
       Matlab Engine for Python        |              Transplant
---------------------------------------|---------------------------------------
eng.max(matlab_data)                   | eng.max(numpy_data)
>>> 4.533                              | >>> [4.533 537635]
eng.max(matlab_data, nargout=1)        | eng.max(numpy_data, nargout=1)
>>> 4.533                              | >>> 4.533
eng.max(matlab_data, nargout=2)        | eng.max(numpy_data, nargout=2)
>>> (4.533, 537635.0)                  | >>> [4.533 537635]
```

Similarly, both libraries can interact with Matlab objects in Python, although the MEfP can't access object properties:

```
       Matlab Engine for Python        |              Transplant
---------------------------------------|---------------------------------------
f = eng.figure()                       | f = eng.figure()
eng.get(f, 'Position')                 | eng.get(f, 'Position')
>>> matlab.double([[ ... ]])           | >>> array([[ ... ]])
f.Position                             | f.Position
>>> AttributeError                     | >>> array([[ ... ]])
```

There are a few small differences, though:

- Function documentation in the MEfP is only available as `eng.help('funcname')`. Transplant will populate a function's `__doc__`, and thus documentation tools like IPython's `?` operator just work.
- Transplant converts empty matrices to `None`, whereas the MEfP represents them as `matlab.double([])`.
- Transplant represents `dict` as `containers.Map`, while the MEfP uses `struct` (the former is more correct, the latter arguable more useful).
- If the MEfP does not know `nargout`, it assumes `nargout=1`. Transplant uses `nargout(func)` or returns whatever the function writes into `ans`.
- The MEfP can't return non-scalar structs, such as the return value of `whos`. Transplant can do this.
- The MEfP can't return anonymous functions, such as `eng.eval('@(x, y) x>y')`. Transplant can do this.

## Performance

The time to start a Matlab instance is shorter in MEfP (3.8 s) than in Transplant (6.1 s). But since you're doing this relatively seldomly, the difference typically doesn't matter too much.

More interesting is the time it takes to call a Matlab function from Python. Have a look:

![execution-time](http://bastibe.de/static/2015-11/execution-time.png)

This is running `sum(randn(n,1))` from Transplant, the MEfP, and in Matlab itself. As you can see, the MEfP is a constant factor of about 1000 slower than Matlab. Transplant is a constant factor of about 100 slower than Matlab, but always takes at least 0.05 s.

There is a gap of about a factor of 10 between Transplant and the MEfP. In practice, this gap is highly significant! In my particular use case, I have [a function](http://www.ee.ic.ac.uk/hp/staff/dmb/voicebox/doc/voicebox/fxpefac.html) that takes about one second of computation time for an audio signal of ten seconds (half a million values). When I call this function with Transplant, it takes about 1.3 seconds. With MEfP, it takes 4.5 seconds.

Transplant spends its time serializing the arguments to JSON, sending that JSON over [ZeroMQ](http:_zeromq.org_) to Matlab, and parsing the JSON there. Well, to be honest, only the parsing part takes any significant time, overall. While it might seem onerous to serialize everything to JSON, this architecture allows Transplant to run over a network connection.

It is a bit baffling to me that MEfP manages to be slower than _that_, despite being written in C. Looking at the number of function calls in the profiler, the MEfP calls 25 functions (!) on each value (!!) of the input data. This is a shockingly inefficient way of doing things.

## TL;DR

It used to be very difficult to work in a mixed-language environment, particularly with one of those languages being Matlab. Nowadays, this has thankfully gotten much easier. Even Mathworks themselves have stepped up their game, and can interact with Python, C, Java, and FORTRAN. But their interface to Python does leave something to be desired, and there are better alternatives available.

If you want to try Transplant, just head over to [Github](https://github.com/bastibe/transplant) and use it. If you find any bugs, feature requests, or improvements, please let me know in the Github issues.
