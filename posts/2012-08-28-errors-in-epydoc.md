---
title: Fixing Errors in Epydoc
date: 2012-08-28 12:14
filetags: python
---

I ran into this error twice now and wasted an hour both times, so it is time to put this on my universal scratchpad, i.e. this blog.

If you ever get this error when using [epydoc](http:_epydoc.sourceforge.net_):

```
    UNEXPECTED ERROR:
    'Text' object has no attribute 'data'
```

You are probably running a version of Python that is greater than the latest one that is supported by epydoc. This is because epydoc has not been updated since 2008 and Python 2.5.

Luckily, some [fine](http://www.agapow.net/programming/python/epydoc-go-boom) [folks](http://stackoverflow.com/questions/6704770/epydoc-attributeerror-text-object-has-no-attribute-data) on the internet have figured out how to fix these things.

Short answer: Find your _site-packages_ directory:

```python
    from distutils.sysconfig import get_python_lib
	print(get_python_lib())
```

Go there, navigate to the /epydoc\_markup_ directory and change line 307 of the file _restructuredtext.py_ from

```python
	m = self._SUMMARY_RE.match(child.data)
```

to

```python
	try:
		m = self._SUMMARY_RE.match(child.data)
	except AttributeError:
		m = None
```

This should fix that problem.
