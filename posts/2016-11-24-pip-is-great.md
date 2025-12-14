---
title: Pip is great
date: 2016-11-24 00:00
filetags: python
---

[Installing](http://bastibe.de/2011-02-03-installing-python-slash-numpy-slash-scipy-slash-matplotlib-on-osx.html) [Python](http://bastibe.de/2011-03-04-installing-pygame-using-homebrew.html) [packages](http://bastibe.de/2011-08-01-compiling-scipy-and-matplotlib-using-pip-on-lion.html) [used](http://bastibe.de/2011-10-13-compiling-scipy-and-matplotlib-again.html) to be a pain. Very surprisingly, this is no longer the case. Nowadays, `pip install whatever` will reliably install pretty much anything without any trouble.

To recap, the problem is that many Python packages rely on C code, which needs to be compiled before installation. In the past, this burden was mostly on the user. Depending on the user's knowledge of C and compilers, and the user's operating system, this could become almost arbitrarily hairy.

This problem was solved, to some extent, using pre-compiled packages, first as [binary installers](http://www.lfd.uci.edu/~gohlke/pythonlibs/) on the package websites, then pre-packaged [Python](http://winpython.github.io/) [distributions](https://www.continuum.io/anaconda-overview), and later through third-party package managers such as [conda](http://conda.pydata.org/docs/).

This worked well, but it fractured the ecosystem into several different mostly-compatible package sources. This was no big problem, but users had to decide on a package-by-package basis whether to download an installer, use conda, or use pip.

But I am happy to announce that these dark days are behind us now. Pip now automatically installs binary Python packages called [wheels](http://wheel.readthedocs.io/en/latest/), and most package developers [do now provide](http://pythonwheels.com/) wheels on [PyPI](https://pypi.python.org/pypi). This is so obviously superior to the past that many high-profile packages don't even provide binary installers any more.

For me, this means I don't have to rely on conda any longer. I don't have to keep a mental list of which packages to install though conda and which packages to install through pip any longer. I can go back to using virtualenv instead of conda-envs[^1] again. I don't have to tell students to download pre-packaged Python distributions any longer. Pip is great!

[^1]: Not because I dislike conda, just to simplify my development environment.
