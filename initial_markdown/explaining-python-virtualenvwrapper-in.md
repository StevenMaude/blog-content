Title: Explaining Python virtualenvwrapper (in a couple of minutes)
Date: 2013-09-19 17:56
Author: Steven Maude
Tags: virtualenv, development, Python, Ubuntu
Slug: explaining-python-virtualenvwrapper-in

As I wrote previously,
[virtualenv](http://www.stevenmaude.co.uk/2013/08/explaining-python-virtualenv-in-under.html)
in Python simplifies development life and dependency handling by
allowing you to effectively use a fresh Python install for each project
you work on.  

<div>
  

</div>
<div>
In turn, [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)
simplifies the use of virtualenvs! (Thanks
[Morty](https://twitter.com/morty_uk) for pointing it out!) Like my
previous post, I'll keep any exposition to the minimum.  

<div>
  

</div>
### How do you install virtualenvwrapper?

<div>
On my Ubuntu 12.04 LTS system, I installed it via the apt package
manager. It was a little bit more of a pain since it sticks it in a
non-standard location:^1^  
not the expected
<span style="font-family: Courier New, Courier, monospace;">/usr/local/bin/virtualenvwrapper.sh</span>  
[but the unexpected
<span style="font-family: Courier New, Courier, monospace;">/etc/bash\_completion\_d/virtualenvwrapper</span>](http://askubuntu.com/questions/251378/where-is-virtualenvwrapper-sh).

</div>
</div>
<div>
  

</div>
<div>
Once installed, add the following two lines to
your<span style="font-family: inherit;"> shell startup file e.g.
.bashrc</span>

</div>
<div>
<div>
<span style="font-family: Courier New, Courier, monospace;">source
/etc/bash\_completion\_d/virtualenvwrapper</span>

</div>
<div>
<span style="font-family: Courier New, Courier, monospace;">export
WORKON\_HOME=\~/path/to/your/virtualenvs</span>

</div>
</div>
<div>
  
(Replace
<span style="font-family: Courier New, Courier, monospace;">/etc/bash\_completion\_d/virtualenvwrapper</span>
in the source line with
<span style="font-family: Courier New, Courier, monospace;">/usr/local/bin/virtualenvwrapper.sh</span>
depending on where the virtualenvwrapper script is actually located.)

</div>
<div>
  
Save your newly modified
<span style="font-family: Courier New, Courier, monospace;">.bashrc</span>
and re-source it by entering in your bash terminal:
<span style="font-family: Courier New, Courier, monospace;">source
\~/.bashrc</span>

</div>
<div>
  

</div>
<div>
virtualenvwrapper is now ready to go!  
  

</div>
### What does virtualenvwrapper offer?

<div>
<div>
After using it briefly, the stand out features are:

</div>
<div>
  

</div>
<div>
**List your available virtualenvs (provided they are located in
$WORKON\_HOME):**
<span style="font-family: Courier New, Courier, monospace;">[workon](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#workon)</span>

</div>
<div>
  

</div>
<div>
**Quick switch to a virtualenv:**
<span style="font-family: Courier New, Courier, monospace;">[workon
virtualenvname](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#workon)</span>

</div>
<div>
  

</div>
<div>
<div>
Another really cool thing with virtualenvwrapper is that it allows you
to specify
<span style="font-family: Courier New, Courier, monospace;">preactivate</span>
and
<span style="font-family: Courier New, Courier, monospace;">postactivate</span>
scripts. This is really useful. One handy shortcut is to make
<span style="font-family: Courier New, Courier, monospace;">workon</span>
not only switch to a particular virtualenv, but to also change directory
to whereever the virtualenv is.  
  
This makes a lot of sense: it's probably more often than not that you'd
want to switch to the virtualenv without working on that project.

</div>
<div>
  
To set this up: do
<span style="font-family: Courier New, Courier, monospace;">cd
$VIRTUALENVWRAPPER\_HOOK\_DIR</span>  
You'll find the
<span style="font-family: Courier New, Courier, monospace;">postactivate</span>
file in there. Add the following two lines to it:

</div>
<div>
<div>
<span style="font-family: Courier New, Courier, monospace;">proj\_name=$(echo
$VIRTUAL\_ENV|awk -F'/' '{print $NF}') </span>

</div>
<div>
<span style="font-family: Courier New, Courier, monospace;">cd
\~/project\_dir\_name/$proj\_name</span>

</div>
</div>
</div>
<div>
(taken from
[http://pynash.org/2013/02/18/quick-hit-virtualenvwrapper-auto-dir.html](http://pynash.org/2013/02/18/quick-hit-virtualenvwrapper-auto-dir.html))  
  
Replace
<span style="font-family: Courier New, Courier, monospace;">\~/project\_dir\_name</span>
with the path to your Python virtualenvs.  
  
Even in my case, where I only have a few projects right now, this
shortcut saves you a lot of typing
<span style="font-family: Courier New, Courier, monospace;">cd</span>
and
<span style="font-family: Courier New, Courier, monospace;">activate</span>
commands.  
  

</div>
<div>
<div>
**Make a new virtualenv in $WORKON\_HOME (this also activates it):**
<span style="font-family: Courier New, Courier, monospace;">[mkvirtualenv](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#mkvirtualenv)
newvirtualenvname</span>

</div>
<div>
  

</div>
<div>
**Delete a virtualenv:**
<span style="font-family: Courier New, Courier, monospace;">[rmvirtualenv](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#rmvirtualenv)
virtualenvname</span>

</div>
<div>
  

</div>
</div>
### Other interesting virtualenv management features I've not used yet:

<div>
**Show installed packages in currently active virtualenv:**
[<span style="font-family: Courier New, Courier, monospace;">lssitepackages</span>](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#lssitepackages)  
  
**Wipe third party packages from the current virtualenv:**
[<span style="font-family: Courier New, Courier, monospace;">wipeenv</span>](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#wipeenv)

</div>
<div>
  

</div>
<div>
**Add directories to the PYTHONPATH of the current virtualenv:**
[add2virtualenv](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#add2virtualenv)<span style="font-family: Courier New, Courier, monospace;">
directory1 directory2</span>

</div>
<div>
  
**Toggle the current virtualenv's access to your globally installed
Python packages**:
<span style="font-family: Courier New, Courier, monospace;">[toggleglobalsitepackages](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#toggleglobalsitepackages)</span>

</div>
<div>
  

</div>
<div>
**Run a command in all virtualenvs in WORKON\_HOME:**
<span style="font-family: Courier New, Courier, monospace;">[allvirtualenv](http://virtualenvwrapper.readthedocs.org/en/latest/command_ref.html#allvirtualenv)
command</span>  
  

</div>
</div>
<div>
There are further features [detailed in the
documentation](http://virtualenvwrapper.readthedocs.org/), but these
tricks alone make taking the time to install it worthwhile.

</div>
<div>
  
<span style="font-size: x-small;">^1^I also ran into a strange issue
whereby in this confusion I removed virtualenvwrapper, reinstalled it,
but the virtualenvwrapper file in bash\_completion\_d didn't reappear. I
had to
<span style="font-family: Courier New, Courier, monospace;">apt-get
purge virtualenvwrapper</span> and then
<span style="font-family: Courier New, Courier, monospace;">sudo apt-get
install virtualenvwrapper</span> to fix this. (Also note that if you
have pip installed, you can do
<span style="font-family: Courier New, Courier, monospace;">sudo pip
install virtualenvwrapper</span>, which presumably installs it to the
standard location and should circumvent this problem entirely.)</span>

</div>
</p>

