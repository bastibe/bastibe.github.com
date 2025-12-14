---
title: Installing Python/Numpy/Scipy/Matplotlib on OSX
date: 2011-02-03 16:23
filetags: compiling python macos
---

For numerical analysis and signal processing prototyping, you would use [Matlab](http://www.mathworks.com/products/matlab/). However, Matlab has some downsides that might make it unsuitable for your project. It might be too expensive. You might be a snobbish programmer that can't stand less-than-elegant programming languages. I certainly am.

So, you look for alternatives. You could take [Octave](http://www.gnu.org/software/octave/), which is free, but that would not solve that ugly-code issue. You could take any scripting language you fancy, but Ruby, Perl and Python are too slow to do serious number crunching.

Then, you stumble upon that Python package called [Numpy](http://numpy.scipy.org/), which seems to be nearly as fast as Matlab when it comes to matrix processing and linear algebra. You then discover [SciPy](http://www.scipy.org/), which would add all that signal processing prowess of Matlab (do quick transformations, random numbers, statistics) to your toolbox. Last but not least, you need plotting. That would be [Matplotlib](http://matplotlib.sourceforge.net/) then, which provides quick plotting facilities in Python.

And the best thing is, these three systems work really well together. They seem to be the perfect replacement for Matlab that could even be superiour to it in many regards.

Next up, you need to install all that stuff. If you are like me, you naturally want to do all that on a Mac. Also, you kind of dislike all these installer-thingies, which install stuff to unknown places and are nigh impossible to uninstall or update cleanly. Even though, you could of course just go to the individual websites, download Python, Numpy, SciPy and Matplotlib, run them installers, and be done. You would save yourself a lot of trouble that way.

But since you allegedly are like me, you instead fire up [`brew`](http://mxcl.github.com/homebrew) and try to install all that stuff using that. Again, you could use [MacPorts](http://www.macports.org) or [Fink](http://www.finkproject.org/) instead, but you probably had some bad experiences with them and you generally love the hackishness of Homebrew, so this is your natural first try.

So you set about this, you believe in packet managers and trust them to take care of every obstacle that might be lying in your way. First of all, install the latest developer tools from [developer.apple.com](http://developer.apple.com). You might need to register (for free) to get them. Also, you need to install [Homebrew](http://mxcl.github.com/homebrew).

To cut this short, here is what you need to get that Python running:

```sh
    brew install python
```

This one should be obvious. At the time of writing, it will install Python 2.7.1. You could take Python 3, but matplotlib is not compatible to it, so you kind of have to stick with 2.7.1 instead.

You also need to put `/usr/local/bin` and `/usr/local/sbin` in the beginning of your path to make sure the new Python gets loaded instead of the pre-installed one. You do that by writing

```sh
    export PATH=/usr/local/bin:/usr/local/sbin:$PATH
```

in your `\`/.bash_profile~. (Create it if its not there--it is just a simple text file).

Now, if you type `python --version`, you should get `Python 2.7.1` as a response.

Alright, next up, install the python package manager:

```sh
    brew install distribute
    brew install pip
```

This will come preconfigured for your newly installed Python. In an ideal world, this should be all. The world being as it is, the pip package of Matplotlib is severely broken and has one other unstated dependency:

```sh
    brew install pkg-config
```

Also, SciPy is using some FORTRAN sources, so you need a fortran compiler:

```sh
    brew install gfortran
```

Alright. That was enough. Now on to pip. With all these dependencies cleared, pip should be able to download Numpy and Scipy without trouble:

```sh
    pip install numpy
    pip install scipy
```

Matplotlib, on the other hand, is more difficult to install. You see, pip is looking at the Python package repository [PyPi](http://pypi.python.org/) for each package. PyPi then provides a URL. Pip then scans that website for links to suitable package files. But, [Sourceforge](http://sourceforge.net/) changed its links a while ago, so pip gets confused and will download an outdated version. Sourceforge says, its new links are way better and no way we will change them back; Pip says, well, if Sourceforge can't provide proper links, that's not our problem. Oh My. Silly children.

So we have to do this manually:

```sh
    pip install -f http://sourceforge.net/projects/matplotlib/files/matplotlib/matplotlib-1.0.1/matplotlib-1.0.1.tar.gz matplotlib
```

That URL comes straight from Sourceforge. Look for the latest version of Matplotlib, search for the download link to the source distribution (`*.tar.gz`), copy that link and strip any trailing '/download'.

UPDATE:

It seems the matplotlib package was updated in the meantime, so you can just run `pip install matplotlib` now.

This should now download and install matplotlib.

Thank you for reading.
