Title: Installing Bokeh on Ubuntu 12.04 LTS
Date: 2013-11-27 20:24
Modified: 2015-05-22 15:29
Author: Steven Maude
Tags: plot, Python, Bokeh
Slug: installing-bokeh-on-ubuntu-1204-lts
Summary: Fixing a problem with installing Bokeh on Ubuntu.
Alias: /2013/11/installling-bokeh-on-ubuntu-1204-lts.html

Today I plotted some data which I intend to use in a blog post. The
Google Docs output I was working with wasn't exactly that pleasant to
look at, so I figured it was a good excuse to give
[Bokeh](http://bokeh.pydata.org/) a try.

I was [installing from source](http://bokeh.pydata.org/quickstart.html)
and found that on doing
`pip install -r requirements.txt` that the install of gevent was failing:

```shell
gevent:
gevent/libevent.h:9:19: fatal error: event.h: No such file or directory

compilation terminated.

error: command 'gcc' failed with exit status 1
```

Thanks to this
[post](https://groups.google.com/d/msg/plivo-users/z20NWkgW_v8/exWwFb7WIMwJ)
for the fix which was simply to `apt-get install libevent-dev` before
doing the `pip install`.

Not done much with yet apart from installing it and getting the bundled
examples to run, but it's quite nice that you can embed plots directly
into HTML. Take a look at the demo
[here](http://continuum.io/blog/painless_streaming_plots_w_bokeh).

!!! article-edit ""
    Edit 11/12/2013: I forgot to add that on trying out Bokeh, I couldn't
    actually get [one of their
    tutorials](http://bokeh.pydata.org/tutorial.html#simple-script-based-plotting)
    to work as it should. Rather than two plots on the same set of axes, I
    was getting two separate plots on two different sets of axes... As this
    is something I actually needed for work, I reverted back to `matplotlib`
    as a result. So Bokeh looks promising, but might be worth trying again
    in a few months.
