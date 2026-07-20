---
title: A Story about Schemes
date: 2012-09-20 20:21
filetags: scheme
---

*Disclaimer:* If you are a programmer, or wanting to be a programmer, or interested in programming, or, well, reading this, you should absolutely, positively watch the 1986 MIT lecture about [The Structure and Interpretation of Computer Programs](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-001-structure-and-interpretation-of-computer-programs-spring-2005/). (Most conveniently available [here](http://ia600401.us.archive.org/8/items/MIT_Structure_of_Computer_Programs_1986/))

I tried reading [the book](http://mitpress.mit.edu/sicp/full-text/book/book.html) numerous times, but it was too dry for my taste. The lecture however is juicy, brain-bending bliss. Especially if you don't know much functional programming yet. It certainly blew my mind. Frequently. Like, every ten minutes. Basically, I feel reborn as a programmer, with a new sense of what I am doing and how it should be done.

However, this is not about SICP, it is about Scheme, which happens to be the programming language that SICP uses to preach its sermons. Above all, Scheme beautiful. It is an astounding marriage of simplicity and power. It is also a mess in terms of implementations. There are dozens of implementations and they all implement a different, partly overlapping set of features that may or may not be part of the canonical Scheme--if there is such a thing.

So, how to select the correct Scheme? Naively, I first chose the one SICP uses, [MIT-Scheme](http://www.gnu.org/software/mit-scheme/). However, I soon found out that it does not work well with Emacs (that is, it did not work at all with `scheme-mode` and `run-scheme`). Also, its prompt is weird: `]=>`. Whatever.

So next, I tried [Gambit Scheme](https://gambitscheme.org/), which works a lot better with Emacs. But then, I soon found out that it does not support functions like `filter`, which are kind of essential. I was quick to write my own version of that, but really, this stuff should be provided. Turns out, `filter` is part of a Scheme Request For Implementation, or SRFI. `filter` is part of SRFI1. There is a [huge list](http://web.archive.org/web/20210620154132/https://srfi.schemers.org/srfi-implementers.html) of different Schemes and the SRFIs they support. Also, there is a list of [Schemes sorted by performance](http://www.cs.utah.edu/~mflatt/benchmarks-20100126/log3/Benchmarks.html). With [plots](http://www.cs.utah.edu/%7Emflatt/benchmarks-20100126/log3/Benchmarks-plot.html), even. It's a mess.

So this left me profoundly confused. What Scheme would I use? Ideally, it should be fast, work with Emacs and implement a reasonable set of SRFIs. Homebrew lists these:

|               |              |             |
| ------------- | ------------ | ----------- |
| bigloo        | chibi-scheme | chicken     |
| gambit-scheme | gauche       | guile       |
| kawa          | mit-scheme   | plt-racket  |
| scheme48      | scsh         | sisc-scheme |
| stklos        | tinyscheme   |             |

Difficult decision. Frankly, I don't have an answer. That said, I found `plt-racket` to be a joy to work with. `(help filter)` will open your browser with the appropriate help page for `filter`. Amazing. Also, it implements [a long list](http://web.archive.org/web/20210620154132/https://srfi.schemers.org/srfi-implementers.html) of SRFIs that will probably satisfy my simplistic needs. And the [documentation](http://docs.racket-lang.org/) is excellent. And then there is DrRacket, which is a nice REPL that comes right with [Racket](http://racket-lang.org/). I like it.
