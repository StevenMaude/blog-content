Title: Explaining Python virtualenvwrapper (in a couple of minutes)
Date: 2013-09-19 17:53
Modified: 2013-09-19 17:56
Author: Steven Maude
Tags: virtualenv, development, Python, Ubuntu
Slug: explaining-python-virtualenvwrapper-in
Summary: How to use virtualenvwrapper to manage your Python virtualenvs.
Alias: /2013/09/explaining-python-virtualenvwrapper-in.html

As I wrote previously,
[virtualenv](http://www.stevenmaude.co.uk/2013/08/explaining-python-virtualenv-in-under)
in Python simplifies development life and dependency handling by
allowing you to effectively use a fresh Python install for each project
you work on.

In turn, [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)
simplifies the use of virtualenvs! (Thanks
[Morty](https://twitter.com/morty_uk) for pointing it out!) Like my
previous post, I'll keep any exposition to the minimum.

## How do you install virtualenvwrapper?

On my Ubuntu 12.04 LTS system, I installed it via the apt package
manager. It was a little bit more of a pain since it sticks it in a
non-standard location:[^1] not the expected
`/usr/local/bin/virtualenvwrapper.sh`
[but the unexpected `/etc/bash_completion_d/virtualenvwrapper`](http://askubuntu.com/questions/251378/where-is-virtualenvwrapper-sh).

Once installed, add the following two lines to
your shell startup file e.g. `.bashrc`

```shell
source /etc/bash_completion_d/virtualenvwrapper
export WORKON_HOME=~/path/to/your/virtualenvs
```

(Replace `/etc/bash_completion_d/virtualenvwrapper` in the source line with
`/usr/local/bin/virtualenvwrapper.sh`
depending on where the virtualenvwrapper script is actually located.)

Save your newly modified `.bashrc` and re-source it by entering in your
bash terminal: `source ~/.bashrc`

virtualenvwrapper is now ready to go!

## What does virtualenvwrapper offer?

After using it briefly, the stand out features are:

**List your available virtualenvs (provided they are located in
`$WORKON_HOME`):**
[`workon`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#workon)

**Quick switch to a virtualenv:**
[`workon virtualenvname`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#workon)

Another really cool thing with virtualenvwrapper is that it allows you
to specify `preactivate` and `postactivate`
scripts. This is really useful. One handy shortcut is to make
`workon`
not only switch to a particular virtualenv, but to also change directory
to whereever the virtualenv is.

This makes a lot of sense: it's probably more often than not that you'd
want to switch to the virtualenv without working on that project.

To set this up: do
`cd $VIRTUALENVWRAPPER_HOOK_DIR`

You'll find the `postactivate`
file in there. Add the following two lines to it:

```shell
proj_name=$(echo $VIRTUAL_ENV|awk -F'/' '{print $NF}')
cd ~/project_dir_name/$proj_name
```

(taken from
[http://pynash.org/2013/02/18/quick-hit-virtualenvwrapper-auto-dir.html](http://pynash.org/2013/02/18/quick-hit-virtualenvwrapper-auto-dir.html))

Replace
`~/project_dir_name`
with the path to your Python virtualenvs.

Even in my case, where I only have a few projects right now, this
shortcut saves you a lot of typing `cd` and `activate` commands.

### Make a new virtualenv in $WORKON_HOME (this also activates it):
[`mkvirtualenv newvirtualenvname`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#mkvirtualenv)

### Delete a virtualenv:
[`rmvirtualenv virtualenvname`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#rmvirtualenv)

## Other interesting virtualenv management features I've not used yet:

### Show installed packages in currently active virtualenv:
[`lssitepackages`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#lssitepackages)

### Wipe third party packages from the current virtualenv:
[`wipeenv`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#wipeenv)

### Add directories to the PYTHONPATH of the current virtualenv:
[`add2virtualenv directory1 directory2`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#add2virtualenv)

### Toggle the current virtualenv's access to your globally installed Python packages:
[`toggleglobalsitepackages`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#toggleglobalsitepackages)

### Run a command in all virtualenvs in WORKON_HOME:
[`allvirtualenv command`](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#allvirtualenv)

There are further features [detailed in the
documentation](http://virtualenvwrapper.readthedocs.org/), but these
tricks alone make taking the time to install it worthwhile.

[^1]: I also ran into a strange issue
whereby in this confusion I removed `virtualenvwrapper`, reinstalled it,
but the `virtualenvwrapper` file in `bash_completion_d` didn't reappear. I
had to `apt-get purge virtualenvwrapper` and then
`sudo apt-get install virtualenvwrapper` to fix this. (Also note that if you
have pip installed, you can do
`sudo pip install virtualenvwrapper`, which presumably installs it to the
standard location and should circumvent this problem entirely.)
