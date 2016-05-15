Title: PyPI: releasing frustration 
Date: 2016-05-15 12:34
Author: Steven Maude
Tags: Python, PyPI
Summary: My first attempt at publishing a Python package on PyPI.

A while back I wrote an [automatic tracklisting downloader for BBC radio
shows](https://github.com/StevenMaude/bbc-radio-tracklisting-downloader) in
Python. It's simple to use and it also hooks well into
[get_iplayer](https://github.com/get-iplayer/get_iplayer) to retrieve or tag
tracklistings when you download a radio show.

[One of the outstanding
issues](https://github.com/StevenMaude/bbc-radio-tracklisting-downloader/issues/21)
was to actually release it on PyPI — the official source for third party Python
packages — to make it a bit simpler to install, and to make it easier for
Python users to find. It was already packaged such that it could be installed
using `pip`, but this was via GitHub rather than PyPI.

I remembered I never got round to releasing my package on PyPI and, for some
reason yesterday, thought it would be a good time to see what the process was
like. Maybe it'll only take half an hour, I thought, naively. It actually took
me more like double to triple that time to complete the task.

Anyway, perhaps documenting this process, along with the numerous errors I
encountered, might help save anyone else running up against the same painful
brick walls that I did, and allow them to share their work with the Python
community.
  
## Starting out

A good starting point is a
[guide](https://packaging.python.org/en/latest/distributing/#uploading-your-project-to-pypi)
on the official Python site that's fairly comprehensive.

The first thing you notice when reading it is that there are lots of options
that are labelled "not recommended" and instead suggest using the
[`twine`](https://github.com/pypa/twine/) package instead. This is because
older versions of Python will happily submit your PyPI credentials in plaintext
when uploading packages. More recent versions are OK, but you're best to check.

It's clearly a good thing to warn people about this. But it would be much nicer
if they didn't even need such warnings in the first place. (I'm also willing to
bet there's still a non-zero number of people on affected versions of Python
who follow instructions elsewhere without even being aware of sending their
passwords in the clear.)

## Testing times

As the Python packaging guide mentions, there's a [PyPI test
site](https://testpypi.python.org) that you can use to test out uploading your
package before you do the same on the live site.

Why's this useful? If you make mistakes in your setup and your package doesn't
install, the only real recourse is to release a new version. Rather than having
to create new versions, you're really best using the test PyPI site first to
make sure everything's OK before you begin.

The test site looks to be an exact duplicate of the main site albeit with a
different selection of packages. This also means that you have the same
restriction as on the live site: that is, you can't replace an existing
version. You have to bump the version in `setup.py` and upload it as a new
version.

I understand why this is in place for the live site. But, it's a little
frustrating when testing: every change requires you to also increase the
version number. Or, as I more often did, forget to do so, then see the error
message telling you that the version already exists and only then increase the
version number.

The details in the guide show the structure of the `.pypirc` configuration.
However, they don't point out that you can also add the PyPI test site too:

```text
[distutils]
index-servers=
    pypi
    testpypi

[testpypi]
repository = https://testpypi.python.org/pypi

[pypi]
repository = https://pypi.python.org/pypi
```

You can also add your username and password to each entry too, although you may
not want it lying around in plain text in a configuration file. If you don't
already have accounts on the live and test PyPI sites, this point is a
good time to create them. You won't be able to progress much further otherwise.

### Building the project distribution

Provided you've got `setup.py` configured correctly, it's not too difficult to
build for distribution. I used the example from the [PyPA sample
project](https://github.com/pypa/sampleproject) as a starting point. It's also
sensible to have tagged the commit in your repository that marks the version to
be released.  

The Python packaging guide linked above is also really helpful in  determining
which arguments you should use with `setup.py` to build your package.

If you're trying to build Python wheels, one hiccup is that you likely need the
`wheel` package installed. Otherwise, you may find with a command like:

```sh
python setup.py sdist bdist_wheel
```

you get the error:

```text
error: invalid command 'bdist_wheel'
```

### Registering the project

Since `twine` is recommended, it seemed sensible to use that. As my
package is for Python 2 only — since a dependency doesn't support Python
3 yet — it also seemed sensible to do the distribution upload using
Python 2.7.

The first problem I hit was running `twine register dist/* -r testpypi` to
register the project. Note that you need to specify the repository using `-r`
if you want to use something other than the default, and the name is taken from
your `.pypirc`.

```text
Registering bbc-radio-tracklisting-downloader-0.0.1.tar.gz
UnicodeDecodeError: 'ascii' codec can't decode byte 0xc2 in position 27:
ordinal not in range(128)
```

That's the entirety of the error message from the `register` command. There was
nothing to indicate where the problem lay at all, making it very difficult to
start fixing it.

Switching to Python 3.4 for the upload avoided the Unicode error, but instead
gave me:

```text
HTTPError: 401 Client Error: You must login to access this feature for
url: https://pypi.python.org/pypi
```

It still could have been a problem with the way I was inputting my password.
I'd tried both typing it at the command line `-p PASSWORD` and pasting it into
the prompt which appears if no password is entered. I'd even tried entering it
directly into `.pypirc`. It's possible I was just doing something wrong, but,
to me, it implies that `twine` wasn't correctly handling one of the characters
in my password.

At this stage, I gave up trying at this point and went directly to the test
site to register the package so I could at least make some progress and feel
slightly less incompetent. That worked without a hitch.

### Adding a description

On to the next problem. Unfortunately, the PyPI site doesn't support the
display of Markdown READMEs for package descriptions. So, before you actually
upload a package, you should provide the package description in a form that
PyPI can use.

To me, Markdown always seemed much simpler than reStructuredText (reST), so I
naturally gravitate to writing documentation in it. My README for this project
was no different.

The main options I was aware of for solving this were:

* specifying a `long_description` in your `setup.py` which uses reST markup,
whether read in from a file, or included in full in the `setup.py` itself, or

* converting `README.md` to a reStructuredText `README.rst`.

I went for the latter for simplicity.

Using `pandoc`, it's pretty simple to convert an existing Markdown file:

```sh
pandoc --from=markdown --to=rst --output=README.rst README.md
```

On checking the output from `pandoc` in an online viewer, everything
looked the same as it did when using Markdown. I also edited the README
slightly to use nicer looking markup for headings than the source Pandoc
generated. 

### Uploading

Whew! Back to `twine`, and now the project's registered, let's try uploading it
via:

```sh
twine upload dist/* -r testpypi
```

I was still having the same problem as before: the 401 error. Systematically
removing unusual characters from my password until the upload worked fixed
this.  (Note that the PyPI site itself was OK with me logging in with the same
password, this seemed a `twine` problem, or something I was just doing wrong.)

OK. Now it's uploaded, let's check what everything looks like on the test PyPI
site.

What? Where's the description taken from the README? There's **nothing** there
at all. The README's not even present as plain text instead of formatted HTML!

What I then did first was to replace my `README.rst` with one borrowed from
someone else's package that I knew displayed correctly on PyPI. Then, I
uploaded a new version of my package to the test site to make sure that I had
everything configured and uploaded correctly.

Once I'd proved that the problem was with the content of my README, I
somehow instinctively figured that it was the transition markers that
I'd added that were to blame. Again, this was the second time in this
entire process that I had little or no indication of where the problem
actually was.

Anyway, removing these transition markers, running `setup.py` and uploading yet
again **finally** enabled my README to be correctly displayed as the package
description.

### Releasing

Once that worked, all I had to do was revert the change to the version number
I'd made in `setup.py` during testing, and then repeat the whole process on the
real PyPI site. Having negotiated all the obstacles the first time, I was
relieved to find this just worked.

The end result of all that is that you can finally do `pip install
bbc-radio-tracklisting-downloader` instead of having to install it from GitHub.

Obviously in a process like this, there's going to be a couple of configuration
hoops to jump through, especially the first time you attempt the process. Now
I've been through it, I could actually probably release a new project in the
thirty minutes I originally estimated. 

On the other hand, the number of barriers I faced, along with the cases of
little or no helpful error information was frustrating. Every stumbling block
encountered is a point where someone could decide that they've had finally
enough and just give up. In those cases, it's the community's loss. Developers
who may well have useful packages to contribute may ultimately decide that it's
not worth the trouble to release on PyPI.
