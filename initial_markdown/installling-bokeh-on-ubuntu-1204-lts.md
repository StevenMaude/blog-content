Title: Installling Bokeh on Ubuntu 12.04 LTS
Date: 2013-12-11 09:55
Author: Steven Maude (noreply@blogger.com)
Tags: plot, Python, Bokeh
Slug: installling-bokeh-on-ubuntu-1204-lts

Today I plotted some data which I intend to use in a blog post. The
Google Docs output I was working with wasn't exactly that pleasant to
look at, so I figured it was a good excuse to give
[Bokeh](http://bokeh.pydata.org/) a try.  
  
I was [installing from source](http://bokeh.pydata.org/quickstart.html)
and found that on doing
<span style="font-family: Courier New, Courier, monospace;">pip install
-r requirements.txt</span> that the install of gevent was failing:  
  

<div class="bgcode">
gevent:  
gevent/libevent.h:9:19: fatal error: event.h: No such file or directory  
  
compilation terminated.  
  
error: command 'gcc' failed with exit status 1

</div>
  
Thanks to this
[post](https://groups.google.com/d/msg/plivo-users/z20NWkgW_v8/exWwFb7WIMwJ)
for the fix which was simply to
<span style="font-family: Courier New, Courier, monospace;">apt-get
install libevent-dev </span><span style="font-family: inherit;">before
doing the
</span><span style="font-family: Courier New, Courier, monospace;">pip
install</span>.  
  
Not done much with yet apart from installing it and getting the bundled
examples to run, but it's quite nice that you can embed plots directly
into HTML. Take a look at the demo
[here](http://continuum.io/blog/painless_streaming_plots_w_bokeh).  
  
Edit 11/12/2013: I forgot to add that on trying out Bokeh, I couldn't
actually get [one of their
tutorials](http://bokeh.pydata.org/tutorial.html#simple-script-based-plotting)
to work as it should. Rather than two plots on the same set of axes, I
was getting two separate plots on two different sets of axes... As this
is something I actually needed for work, I reverted back to matplotlib
as a result. So Bokeh looks promising, but might be worth trying again
in a few months.

</p>

