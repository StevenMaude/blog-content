Title: Installing pip, virtualenv and virtualenvwrapper tidily in Linux
Date: 2016-12-30 00:10
Author: Steven Maude
Tags: Linux, Ubuntu, Python, pip, virtualenv, virtualenvwrapper
Summary: Don't want to clutter up your system's Python install? Install
         what you need for Python development cleanly.

When I reinstalled my PC, I was thinking about the "cleanest" way that I
could get the Python tools I needed on there. Previously, I'd used the
pip bundled in the Ubuntu repositories, then found it was left to
languish, and was hideously out of date. (I think it is possible to
update if you've installed that way, but involves using `sudo pip
install -U` all the time, which didn't seem sensible.)

A better option might be to install pip directly from the installer
that's provided by the pip developers, using pip to install virtualenv
and virtualenvwrapper, and then using the virtualenv tools to create
virtualenvs to actually install Python packages for development. This
way should create the minimum level of clutter you're adding to your
system's Python installation.

But, reading around, the suggestions here on [doing a clean
installation](https://stackoverflow.com/questions/4324558/whats-the-proper-way-to-install-pip-virtualenv-and-distribute-for-python)
seemed an even better idea. You download the virtualenv package from
PyPI yourself, use Python to run the `virtualenv` Python code directly
and use that to create a "bootstrap" virtualenv that you can then create
new virtualenvs from.  Note that these virtualenvs all include pip; no
need for extra work to get it installed.

All of this is possible without doing any installation into the system's
Python at all, not even requiring any `pip install --user` commands.
It's pretty simple to do. If you want to follow this along further and
add virtualenvwrapper too, see the Stack Overflow post for more details
(essentially, you need to get a copy of virtualenv via downloading it,
e.g. from PyPI, using curl or a web browser and then run `python
virtualenv.py $YOUR_CHOSEN_VIRTUALENV_DIRECTORY`), then continue here.

## Getting virtualenvwrapper working

Though [it's not recommended in the
documentation](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#basic-installation),
someone in the Stack Overflow comments said they'd got it working, so I
thought worth trying.

What I did was create a Python virtualenv purely for virtualenvwrapper
using the method in the Stack Overflow answer. I called the virtualenv
"virtualenvwrapper" and created it inside `$HOME/.virtualenvs`.

Next, I then activated this new virtualenv using `source
$HOME/.virtualenvs/virtualenvwrapper/bin/activate` and did `pip install
virtualenvwrapper`.

If you modify your shell startup files as suggested in the
virtualenvwrapper documentation, you'll find you get an error:

```text
virtualenvwrapper.sh: There was a problem running the initialization
hooks.     

If Python could not import the module virtualenvwrapper.hook_loader,
check that virtualenvwrapper has been installed for
VIRTUALENVWRAPPER_PYTHON=$VIRTUALENVWRAPPER_PYTHON and that PATH is
set properly.
```

As virtualenvwrapper isn't installed in the default Python, the script
looks for it and understandably can't find it. It's a simple fix: just
activate the virtualenvwrapper virtualenv before this shell script is
sourced.

Even if you immediately deactivate the virtualenvwrapper virtualenv
again, you'll still have commands like `workon` that function correctly
in your shell environment.

So what I first tried was doing what the virtualenvwrapper documentation
suggests, and modifying shell startup files, but with extra activate and
deactivate steps:

```sh
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/.local/src 
source $HOME/.virtualenvs/virtualenvwrapper/bin/activate
source $HOME/.virtualenvs/virtualenvwrapper/bin/virtualenvwrapper.sh
deactivate                                                          
```

You will need to switch to some virtualenv first with the virtualenv
package installed, before commands that require the Python virtualenv
package to be installed will work (e.g. to create new virtualenvs). It's
simple enough to do `workon py3venv` and then e.g. `mkvirtualenv
virtualenv_name` when you want to create one. However, `workon` to
switch virtualenvs should always work.

## Limitations with this clean solution

This works pretty well, but:

1. The bootstrap environments are the ones you base your other
   virtualenvs on.  If, for some reason, you suddenly need some system
   site package installed for some particular Python package, then
   you'll need to create a new bootstrap virtualenv first, with the
   `--system-site-packages` option. (Even if you've already got a
   "system site packages" virtualenv, if you subsequently updated the
   system packages and want a virtualenv to reflect this, you'll have to
   go back to the bootstrapping stage.)

2. You'll likely need to recreate the bootstrap environments in addition
   to any actual in-use virtualenvs if you want to move to a new Python
   version. I've read in places things that suggest the Python binary is
   a symlink to the system one; on my current virtualenvs, there are
   only symlinks to the local virtualenv copy of the python binary.

## Fixing virtualenvwrapper slowing terminal startup

virtualenvwrapper does slightly delay bash starting up. On
investigation, this is principally due to virtualenvwrapper.sh itself,
not the activate/deactivate step. You can check this by running `time`
on each of the commands, `source bin/activate` and `deactivate` are
basically instant, whereas this script slows things down considerably.

```sh
$ time source $HOME/.virtualenvs/virtualenvwrapper/bin/virtualenvwrapper.sh

real	0m0.304s
user	0m0.248s
sys     0m0.032s
```

A 0.3 s delay isn't particularly long. But, for me, it makes bash feel
slightly less snappy on opening a new terminal.

To solve this, you can use the ["lazy
loading"](https://virtualenvwrapper.readthedocs.io/en/latest/install.html#lazy-loading)
script provided with virtualenvwrapper. For my setup, this means I would
need to hack that lazy loading script to add the activate and deactivate
command there.

I tried this and it did work. But, it didn't seem like a good solution.
In part, it just felt hacky and, more importantly, these commands would
be removed if you upgrade virtualenvwrapper, breaking it until you again
hacked the script.

Instead, my preferred option to work around the slightly slow loading
was to create another script that I can `source` whenever wanting to
work with Python virtualenvs:

```sh
#!/bin/sh -e
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/.local/src
source $HOME/.virtualenvs/venvwrapper/bin/activate
source $HOME/.virtualenvs/venvwrapper/bin/virtualenvwrapper.sh
deactivate
```

This is less direct. You can't just directly access virtualenvs.
Insteaad, you must source this script first so that you can then
`workon` a virtualenv to `workon`. However, it keeps the clean install
we have made, doesn't slow bash from loading at all, and isn't a hack of
the existing virtualenvwrapper. Provided we keep it installed in the
same place, it'll work.

## Keeping clean

Despite the few drawbacks, I do like the idea of this approach overall.
You don't even need to install any Python packages, even as a user, into
Python outside of a virtualenv.

Bear in mind if you're intent on being particularly rigorous in keeping
your system Python clean: installing software that is built on Python
via your package manager (e.g. apt) may well end up pulling in the
package manager's version of dependencies that the software may use. A
way around this is to install whatever software you want to use in a
virtualenv instead manually, although this may be awkward if that
software uses system packages.
