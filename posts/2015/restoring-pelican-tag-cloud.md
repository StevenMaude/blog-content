Title: Restoring a tag cloud dispersed by Pelican 3.6.0
Date: 2015-07-12 11:51
Author: Steven Maude
Tags: Pelican, tag cloud, plugin
Summary: How to fix tag clouds in Pelican 3.6.0.

## The case of the disappearing tag cloud

As you can probably tell — if not from the posts mentioning Pelican,
then the giveaway is the footer of each page — my site is currently
built using [Pelican](https://github.com/getpelican/pelican).

Noticing there was a new version this week, I eagerly updated and then
tried building my site. No errors, I thought, so everything must be
fine.

Unfortunately, on loading the site, the tag cloud had vanished[^1].

Over the next twenty minutes or so, I slowly figured out the cause: the
Pelican code that creates this had been moved out to a separate plugin.
(If only I'd checked the [Pelican
docs](http://docs.getpelican.com/en/3.6.0/faq.html#my-tag-cloud-is-missing-broken-since-i-upgraded-pelican)
first, I would have saved the time...) From there, it's a simple fix.
Install the plugin, add it to your `PLUGINS` in `pelicanconf.py` and the
tag cloud will be restored.

## Installing Pelican plugins

One small frustration is that the official plugin
[repository](https://github.com/getpelican/pelican-plugins) is, if maybe
not monolithic, a substantial size. The appeal of a central repository
does make some sense. It provides a single location for developers to
add functionality to Pelican and means users can issue one command to
get access to everything at once.
 
But my hunch is that users probably only want a few of the numerous
plugins: seventy at the time of writing. Also, when a plugin is updated
by its author, they additionally have to put a pull request into the
plugins repository to keep the submodule or files stored there in sync,
which is extra work for everyone involved too.

## My tag cloud plugin fork

One solution for installing the plugin would be to write a simple shell
script that does the cloning and just keeps the tag plugin. Instead, I
felt that it would be both simpler and more sensible — rather than
retrieving many plugins that I don't need — to install the plugin via
the existing `requirements.txt` in my blog configuration. (The other
plugin I use, [pelican-alias](https://github.com/Nitron/pelican-alias/),
is installed this way in my setup.) 

So, I made the plugin  `pip` installable (available
[here](https://github.com/StevenMaude/pelican-tag-cloud)) and added that
to my requirements for what seems like a neater solution. The only
downside is that I have to ensure that this plugin is updated when the
original code is. For this plugin however, I suspect that updates would
be irregular.

[^1]: If the site's not changed since I wrote this, then it's the one
that shows up in the upper right sidebar.
