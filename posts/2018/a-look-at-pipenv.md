Title: A look at Pipenv
Date: 2018-08-26 14:06
Modified: 2020-06-19 12:39
Author: Steven Maude
Tags: Pipenv, Python
Summary: A quick look at Pipenv, a tool to manage Python packages.

!!! article-edit ""
    Edit 2020-06-19: These days, I just tend to use a manually created
    virtualenv when working on Python, and a bash one-liner to activate
    the appropriate virtualenv.

    As mentioned below, [poetry](https://github.com/python-poetry/poetry) is
    another option for managing dependencies and I've seen a lot of
    positive things written about poetry since I originally wrote this
    post.

[Pipenv](https://github.com/pypa/pipenv)[^1] is a tool that aims to
remove the hassle of using
[virtualenvs]({filename}../2013/explaining-python-virtualenv-in-under.md)
(Python runtime environments to keep separate Python setups for
different projects independent), and also help manage requirements. It
also aims to help provide deterministic builds of software.

I had read about Pipenv previously, but couldn't ever really understand
how it worked from just reading about it. So I switched from my existing
virtualenv setup to this to try it out and figure out whether I can
replicate the same behaviour I had with virtualenv and
virtualenvwrapper.

## Differences

The main difference of Pipenv to the way you might work with virtualenvs
— which, for me, is switch to a particular virtualenv for a project, then
run commands in the shell as normal, just with a self-contained Python
setup — is that Pipenv is more contextual.

With Pipenv, you change to the appropriate project directory and then
run commands directly in that virtualenv by preceding them with `pipenv
run`, e.g. `pipenv run myscript.py`. Pipenv knows which virtualenv to
use based on the location you're in.

(You can also get more virtualenv-like behaviour by going to a project
directory and doing `pipenv shell` where it effectively activates the
virtualenv in the shell. However, one downside with this is that the
subshell command history there only exists within that subshell; it is
not stored in your main shell.)

Another difference is that you would also tend to favour using `pipenv`
over `pip` for installing packages; `pipenv install <SOME_PACKAGE>` also
adds packages to your project's
[`Pipfile`](https://github.com/pypa/pipfile), which replaces the older
`requirements.txt` file of specifying dependencies.

## Usage

You can create a new Pipenv either implicitly by `pipenv install --dev`
which installs dependencies for that project (including dev
dependencies) in a new virtualenv it creates, or more explicitly by:
`pipenv --two` or `pipenv --three` which gets you a new virtualenv with
that version of Python.

You can also use `--python <VERSION_NUMBER>` to use a specific point
release of Python of your choice you have installed, e.g. 3.7.
Furthermore, if you have pyenv installed, it will install the requested
version of Python for you, if that version is not installed already.

There are two broad uses of virtualenvs I had:

1. for Python development to avoid any clash of package versions, which
   is covered quite well by the default behaviour of Pipenv.

2. for running standalone Python software I want to run, e.g.
   Docker Compose, but keeping their installations entirely independent
   of each other to avoid any conflicts. This isn't quite covered as
   well, because `pipenv run` requires you to be in the directory or a
   subdirectory of that directory[^2] where you've already run Pipenv
   and a Pipfile exists, as that's how I assume it figures out which
   virtualenv to use. Otherwise, running Pipenv creates a new
   virtualenv! I think `pipenv shell` works around this dropping you
   into a new subshell where the virtualenv is activated.

    Alternatively, in bash, you can do `source $(pipenv
    --venv)/bin/activate` in the directory with the virtualenv, to work
    at a slightly lower level, with the virtualenv directly, without
    `pipenv shell`.

These use cases are both handled reasonably well by Pipenv.

## Summary

Pipenv seems to work well enough if you want to simplify using
virtualenvs and management of dependencies. I think there are two groups
of users that it might particularly suit: those who are newer to
managing Python packaging and virtualenvs — as a means of abstracting
away virtualenv management — and those who are more experienced but want
to have a tool that integrates other features, e.g. checking for
dependency vulnerabilities via `pipenv check` (which is provided by the
[safety](https://github.com/pyupio/safety) package).

However, if you read around, there is still some contention about Pipenv
being [recommended by the
PyPA](https://packaging.python.org/guides/tool-recommendations/).
Certainly, there are a considerable number of small issues that remove
some of Pipenv's sheen; [I encountered a small one already
reported](https://github.com/pypa/pipenv/issues/2753) within just a
short time of using Pipenv. There are also several issues relating to
dependency resolution, which seem a little more critical seeing as
dependency management is one of the tool's core goals.

Pipenv then is no panacea for Python's still byzantine dependency
management. [PEP 20](https://www.python.org/dev/peps/pep-0020/)'s call
for "one obvious way to do it" is not yet fully heeded. But maybe it's a
step roughly in the right direction, even if there's still some
meandering to do before there's a really simple and transparent workflow
for Python. (However, I don't think it's uncommon for dependency
management being tricky to get right either; Go has been around for a
decade and is only just [getting
there](https://blog.golang.org/versioning-proposal). Python's had
considerably longer than Go to get it right though.)

Finally, it is worth noting that there are other alternatives too.
[Poetry](https://github.com/python-poetry/poetry) is a newer, and perhaps
less well known, tool whose goals intersect with those of Pipenv. It
fixes some of the existing issues of dependency resolution that
pip-tools has (pip-tools is the underlying package that pipenv actually
uses for this task), and therefore may be another useful contender to
keep in mind.

[^1]: Confusingly, Pipenv's name is capitalised, while pip's is not.

[^2]: Caveat: it only looks a certain number of subdirectories deep by
default, though [this number is configurable](
https://github.com/pypa/pipenv/issues/1634).
