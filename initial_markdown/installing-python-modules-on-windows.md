Title: Installing Python modules on Windows: unable to find vcvarsall.bat
Date: 2013-06-09 13:43
Modified: 2013-10-05 21:42
Author: Steven Maude
Tags: scikit-learn, install, Python
Slug: installing-python-modules-on-windows
Summary: How to install scientific modules in Python on Windows.

I'm in the middle of taking the [Coursera Data
Science](https://www.coursera.org/course/datasci) course which is
currently discussing [machine
learning](https://en.wikipedia.org/wiki/Machine_learning). The current
assignment is to have a go at a [Kaggle](http://www.kaggle.com/)
competition and write up the attempt. (Kaggle is a site where data
modelling competitions are posted: participants are given some existing
data set and the aim is to develop models to make predictions or
decisions for unknown data.)

This is why, earlier today, I was trying to install
[scikit-learn](http://scikit-learn.org/), a Python machine learning
module. Unfortunately, when using
[pip](http://esmithy.net/2012/08/25/python-packaging-demystified/) to
install it, I was getting the unhelpful error: "unable to find
vcvarsall.bat". [This blog
post](http://slacy.com/blog/2010/09/python-unable-to-find-vcvarsall-bat/)
pointed out the issue: you need a C++ compiler installed and configured
correctly (e.g. MinGW or Visual Studio).

Instead of having to do more installation and setup, the quickest
solution was to use a portable Python distribution, like
[WinPython](http://code.google.com/p/winpython/) or
[Anaconda](https://store.continuum.io/cshop/anaconda/); these have
several scientific modules installed already. Another option to using an
existing Python distribution is to just install a precompiled package:
there's also [Christoph
Gohlke's](http://www.lfd.uci.edu/~gohlke/pythonlibs/) collection of
compiled Python scientific packages available.
