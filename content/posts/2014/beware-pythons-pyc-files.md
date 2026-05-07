+++
title = "Beware Python's pyc files"
date = 2014-05-09T21:29:00
show_lastmod = true
lastmod = 2014-05-09T22:35:00
author = "Steven Maude"
summary = "When Python's pyc files cause errors, it's time to remove them."
slug = "beware-pythons-pyc-files"
url = "/posts/beware-pythons-pyc-files/"
tags = ["Python", "pyc"]
aliases = ["/2014/05/beware-pythons-pyc-files.html"]
+++

A quick reminder to myself more than anything.

Had the issue of a strange `ImportError: from itertools import tee`.
It's a little odd because `itertools` is a Python built-in module.

Running Python and doing the import from the directory where I was
running code worked fine. However, running a script in that directory
that was importing a package, that itself imported itertools gave this
behaviour.

I wasn't really sure what was causing it, but on a whim I deleted the
existing `itertools.pyc` file in that directory. When I looked, it turns
out that `itertools` had a `pyc` file in the package directory. If you
have inexplicable errors like this with no obvious explanation, it's
worth perhaps deleting the cached `.pyc` files. That is, unless
[this](https://www.youtube.com/watch?v=wsczq6j3_bA#t=22m15s) applies to
your coding workflow.
