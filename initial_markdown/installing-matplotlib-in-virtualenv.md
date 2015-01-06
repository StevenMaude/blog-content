Title: Installing matplotlib in a virtualenv
Date: 2013-09-30 18:57
Modified: 2013-10-01 19:38
Author: Steven Maude
Tags: dependency, virtualenv, install, matplotlib, solution, Python, PyGTK
Slug: installing-matplotlib-in-virtualenv
Summary: Solving matplotlib's plotting backends being inaccessible in virtualenvs.

Today I've been spending far too long installing
[matplotlib](http://matplotlib.org/) into a Python virtualenv on Ubuntu
12.04, but I finally have it working as I want now. matplotlib lets you
make nice data plots with a few lines of Python, but it has [several
dependencies](http://matplotlib.org/users/installing.html#build-requirements)
and this makes it trickier than some packages to get going.

The first obstacle is getting [numpy](http://www.numpy.org/) installed.
I suspect there were some dependencies I had to install to be able to
successfully
`pip install numpy` in my virtualenv. It was only a couple of hours ago, but I
have forgotten completely if I had to install anything to get numpy
working. Not very helpful, but if you search for any error messages that
come up here, you should find the relevant Stack Overflow posts that
helped me solve that initial problem.

You also need `freetype` and `libpng` installed to be able to `pip install
matplotlib`. I had `libpng12-0` already installed, but needed `libpng12-dev`;
likewise, I had `libfreetype6` installed, but also needed the development
package, `libfreetype6-dev`.

That wasn't too difficult to solve and matplotlib seemed to install
fine. [As described
elsewhere](http://stackoverflow.com/questions/7534453/matplotlib-does-not-show-my-drawings-although-i-call-pyplot-show),
one problem I had was that matplotlib was generating plots with savefig,
but not showing them when I was trying to `show()` them. I changed the
backend to GTK as the solution suggested, but matplotlib then complained
that with an `ImportError` that "`Gtk* backend requires pygtk to be
installed`".

So, how to solve this. First of all, you'll need to
`pip uninstall matplotlib` in your virtualenv if you've installed
matplotlib already. You also need to
`sudo apt-get install python-gtk2-dev`.

I found [this post discussing using PyGTK in a
virtualenv](http://stackoverflow.com/questions/249283/virtualenv-on-ubuntu-with-no-site-packages)
which helped fix this. Activate the virtualenv you want to use
matplotlib in, then do:

```shell
ln -sf /usr/lib/python2.7/dist-packages/{glib,gobject,cairo,gtk-2.0,pygtk.py,pygtk.pth} $VIRTUAL_ENV/lib/python2.7/site-packages
```

This creates symbolic links
to the required globally installed Python packages and solves the
problem of them being inaccessible.
You have to do this
**before** you `pip install matplotlib`. Otherwise it won't detect at
compile time that you have the backend GTK dependencies in the
virtualenv. Finally, you need to set the backend to GTKAgg in
`~/.config/matplotlib/matplotlibrc` (I had to copy matplotlibrc from
`/lib/python2.7/site-packages/matplotlib/mpl-data` in the
virtualenv.) If you run this [test
plot](http://matplotlib.org/examples/pylab_examples/simple_plot.html),
it should now save it and display it in an interactive window.

Update: Going away and coming back to this problem, I found that using
the [`--system-site-packages
option`](http://www.virtualenv.org/en/latest/#the-system-site-packages-option)
when creating a new virtualenv should also allow the GTK backend to
work. The method I've detailed above has the advantage of copying over
the minimum of required packages.
