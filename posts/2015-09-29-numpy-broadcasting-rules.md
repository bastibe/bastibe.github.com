---
title: Numpy Broadcasting Rules
date: 2015-09-29 00:00
filetags: python
---

They say that all arithmetic operations in Numpy behave like their element-wise cousins in Matlab. This is wrong, and seriously tripped me up last week.

In particular, this is what happens when you multiply an array with a matrix[1] in Numpy:

```
     [[  1],           [[1, 2, 3],       [[ 1,    2,   3],
      [ 10],       *    [4, 5, 6],   =    [ 40,  50,  60],
      [100]]            [7, 8, 9]]        [700, 800, 900]]

 [  1,  10, 100]       [[1, 2, 3],       [[  1,  20, 300],
        OR         *    [4, 5, 6],   =    [  4,  50, 600],
[[  1,  10, 100]]       [7, 8, 9]]        [  7,  80, 900]]
```

They behave as if each row was evaluated separately, and singular dimensions are repeated where necessary. It helps to think about them as row-wise, instead of element-wise. This is particularly important in the second example, where the _whole_ 1d-array is multiplied with _every row_ of the 2d-array.

Note that this is _not_ equivalent to multiplying every _element_ as in `[a[n]*b[n] for n in range(len(a))]`. I guess that's why this is called _broadcasting_, and not _element-wise_.

[1] "matrix" here refers to a 2-d `numpy.array`. There is also a `numpy.matrix`, where multiplication is matrix multiplication, but this is not what I'm talking about.
