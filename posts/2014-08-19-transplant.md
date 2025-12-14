---
title: Transplant
date: 2014-08-19 00:00
filetags: python matlab
---

In academia, a lot of programming is done in Matlab. Many very interesting algorithms are only available in Matlab. Personally, I prefer to use tools that are more widely applicable, and less proprietary, than Matlab. My weapon of choice at the moment is Python.

But I still need to use Matlab code. There are [a few ways](http://stackoverflow.com/a/23762412/1034) of interacting with Matlab out there already. Most of them focus on being able to eval strings in Matlab. Boring. The most interesting one is [mlab](https://github.com/ewiger/mlab), a full-fledget bridge between Python and Matlab! Had I found this earlier, I would probably not have written my own.

But write my own I did: [Transplant](https://github.com/bastibe/transplant). Transplant is a very simple bridge for calling Matlab functions from Python. Here is how you start Matlab from Python:

```python
import transplant
matlab = transplant.Matlab()
```

This `matlab` object starts a Matlab interpreter in the background and connects to it. You can call Matlab functions on it!

```python
matlab.eye(3)
>>> array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])
```

As you can see, Matlab matrices are converted to Numpy matrices. In contrast to most other Python/Matlab bridges, matrix types are preserved[^dtypes]:

```python
matlab.randi(255, 1, 4, 'uint8')
>>> array([[246,    2, 198, 209]], dtype=uint8)
```

All matrix data is actually transferred in binary, so both Matlab and Python work on bit-identical data. This is very important if you are working with precise data! Most other bridges do some amount of type conversion at this point.

This alone accounts for a large percentage of Matlab code out there. But not every Matlab function can be called this easily from Python: Matlab functions behave differently depending the number of output arguments! To emulate this in Python, every function has a keyword argument `nargout` [^nargout]. For example, the Matlab function `max` by default returns both the maximum value and the index of that value. If given `nargout=1` it will only return the maximum value:

```python
data = matlab.randn(1, 4)
matlab.max(data)
>>> [1.5326, 3] # Matlab: x, n = max(...)
matlab.max(data, nargout=1)
>>> 1.5326      # Matlab: x = max(...)
```

If no `nargout` is given, functions behave according to `nargout(@function)`. If even that fails, they return the content of `ans` after their execution.

Calling Matlab functions is the most important feature of Transplant. But there is a more:

- You can save/retrieve variables in the global workspace:

```python
  matlab.value = 5 # Matlab: value = 5
  x = matlab.value # Matlab: x = value
```

- You van eval some code:

```python
  matlab.eval('class(value)')
  >>> ans =
  >>>
  >>> double
  >>>
```

- The help text for functions is automatically assigned as docstring. In IPython, this means that `matlab.magic?` displays the same thing `help magic` would display in Matlab.

Under the hood, Transplant is using a very simple messaging protocol based on [0MQ](http://zeromq.org/), [JSON](https://en.wikipedia.org/wiki/Json), and some [base64](https://en.wikipedia.org/wiki/Base64)-encoded binary data. Sadly, Matlab can deal with none of these technologies by itself. Transplant therefore contains a full-featured JSON [parser](https://github.com/bastibe/transplant/blob/master/parsejson.m)/[serializer](https://github.com/bastibe/transplant/blob/master/dumpjson.m) and base64 [encoder](https://github.com/bastibe/transplant/blob/master/base64encode.m)/[decoder](https://github.com/bastibe/transplant/blob/master/base64decode.m) in pure Matlab. It also contains a minimal [mex-file](https://github.com/bastibe/transplant/blob/master/messenger.c) for interfacing with 0MQ.

There are a few [JSON parsers](http://iso2mesh.sourceforge.net/cgi-bin/index.cgi?jsonlab) available for Matlab, but virtually all of them try parse JSON arrays as matrices. This means that these parsers have no way of differentiating between a list of vectors and a matrix (want to call a function with three vectors or a matrix? No can do). Transplant's JSON parser parses JSON arrays as cell arrays and JSON objects as structs. While somewhat less convenient in general, this is a much better fit for transferring data structures between programming languages.

Similarly, there are a few [base64 encoders](http:/home.online.no/~pjacklam/matlab/software/util/datautil/) available. Most of them actually use Matlab's built-in Java interface to encode/decode base64 strings. I tried this, but it has two downsides: Firstly, it is pretty slow for short strings since the data has to be copied over to the Java side and then back. Secondly, it is limited by the Java heap space. I was not able to reliably encode/decode more than about 64 Mb using this[^heap]. My base64 encoder/decoder is written in pure Matlab, and works for arbitrarily large data.

All of this has been about Matlab, but my actual goal is bigger: I want transplant to become a library for interacting between more than just Python and Matlab. In particular, Julia and PyPy would be very interesting targets. Also, it would be useful to reverse roles and call Python from Matlab as well! But that will be in the future.

For now, head over to [Github.com/bastibe/transplant](https://github.com/bastibe/transplant) and have fun! Also, if you find any bugs or have any suggestions, please open an issue on Github!

[^dtypes]: Except for integer complex numbers, since those are not supported by Numpy.

[^nargout]: Like the Matlab function `nargout`

[^heap]: At 192 Mb of Java heap space. And even those 64 Mb were pretty unreliable if I didn't call `java.lang.Runtime.getRuntime.gc` all the time.
