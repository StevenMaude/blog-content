Title: Explaining Python virtualenv (in under two minutes)
Date: 2013-08-30 22:02
Author: Steven Maude
Tags: virtualenv, development, Linux, programming, Python, Ubuntu, coding
Slug: explaining-python-virtualenv-in-under

I've been busy the last couple of weeks. Recently, I started a late
summer/early autumn internship at
[ScraperWiki](https://scraperwiki.com/), who are building a data science
platform. I should have a blog post (it's drafted!) describing how I've
found working there so far posted soon on their
[blog](http://blog.scraperwiki.com/).  
  
Anyway, I've been
[pairing](https://en.wikipedia.org/wiki/Pair_programming) with the very
helpful and patient [David Jones](https://twitter.com/drjtwit) who has
been helping me out hugely by sharing some of his knowledge with me. For
the last two days, I've been learning a lot, and somehow forgetting even
more, about [vim](http://www.vim.org/). However, David also showed me
how to use virtualenv today. This was far easier for me to get my head
round, so I'd figured I'd write up a quick start guide while it was
fresh in mind.  
  

#### What is virtualenv?

As the [homepage describes it](http://www.virtualenv.org/), "virtualenv
is a tool to create isolated Python environments". These environments
are also referred to as virtualenvs.  
  

#### Why is this useful for software development?

It greatly simplifies dependencies on other modules for different
software projects you are working on. *Each virtualenv can have its own
installed modules.* If projects require different versions of the same
module, it would be a real pain to manage this at a system level. You
might need, say, two different versions of the same module for two
different projects. Using virtualenv, it's simple for every project you
work on to have its own set of modules independently of any others.  
  
You can also use this to safely test new versions of modules with your
software: make a new virtualenv and install the newer version of the
module there.  
  
Furthermore, you can also [setup virtualenvs that use different Python
versions](http://stackoverflow.com/questions/1534210/use-different-python-version-with-virtualenv),
particularly handy considering that the change from Python 2 to Python 3
is a substantial one.  
  
Another plus is that using virtualenvs stops you polluting your system's
actual Python installation with lots of packages that you're using only
to develop certain software.  
  

#### **How do you install it?**

On Debian-based distributions, e.g. Ubuntu, you can use apt-get:
<span>sudo apt-get install python-virtualenv</span>  
  

#### How do you use it?

In a terminal, make a directory for the project you're working on (or
enter an existing directory), e.g. newproject. Creating a new virtualenv
is as easy as entering <span>virtualenv newproject</span>  
  
When this command is entered, a Python distribution will be setup within
the specified directory, in this case <span>newproject</span>. The
current default behaviour of virtualenv is not to copy any system
installed packages here, so it's like a fresh install.  
  
To activate a virtualenv, you then change to your project directory
(e.g. <span>cd newproject</span>), then enter the command: <span>.
bin/activate</span> (notice the space between the dot and
bin/activate).  
  
It's easy to tell you're running a virtualenv: the terminal will show
(<span>newproject</span>) before the command prompt. While the
virtualenv is active, any [pip install
packagename](http://www.pip-installer.org/en/latest/quickstart.html)
command will install a Python package into that particular virtualenv.
This is another nice benefit of virtualenv: you don't need to run *sudo*
pip install packagename as you will already be working in a
user-writeable directory.  
  
To deactivate a virtualenv, simply enter <span>deactivate</span> at the
terminal. To use in future, just run the activate command again in the
project directory: <span>. bin/activate</span>  
  
Simple, but incredibly useful.   
  
<span style="font-size: x-small;">(Bonus note: Since creating a
virtualenv creates directories such as /bin, /include, /lib and /local,
you may wish to add these to a
[.gitignore](https://help.github.com/articles/ignoring-files) file if
you're using git so that you don't accidentally commit these files to a
repository.)  
  
(Bonus note 2: After initially posting this, [it was later pointed out
to me](https://twitter.com/morty_uk/status/370653794054320128) that
[virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/index.html)
is a handy way to manage virtualenvs.)</span>

</p>

