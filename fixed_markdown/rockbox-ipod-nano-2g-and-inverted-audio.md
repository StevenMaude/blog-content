Title: Rockbox, iPod Nano 2G and inverted audio channels
Date: 2014-04-08 21:24
Modified: 2014-04-08 21:25
Author: Steven Maude
Tags: Rockbox, Nano, iPod, bug
Slug: rockbox-ipod-nano-2g-and-inverted-audio
Summary: Discovering an (old) bug in Rockbox swapping audio channels on iPod Nano 2G.
Alias: /2014/04/rockbox-ipod-nano-2g-and-inverted-audio.html

![Rockbox logo]({filename}/images/rockbox3540.jpg)

I do a lot of listening to music and podcasts with a trusty old second
generation iPod Nano running [Rockbox](http://www.rockbox.org). What
[XBMC](http://xbmc.org) is to video playback, Rockbox is for audio
playback. (I should get around to writing up what makes it that much
better than stock firmware.)

Anyway, I thought I'd leave a note here about the issue I discovered
today since it took me several searches to yield anything relevant and I
spent a good half-hour or so diagnosing the problem.

When I was listening to something I'd recorded myself, I noticed that
the left and right channels were switched. After checking the original
audio I recorded on my PC, different headphones, and several different
versions of Rockbox I realised it was actually a Rockbox problem.
Earlier versions don't suffer from this issue (for example, the much
older 3.7.1).

In the end, searching Rockbox's issue tracker eventually confirmed this:
the swapping of channels is a known bug, [though no-one's fixed it
yet](http://www.rockbox.org/tracker/task/12708). Not a big deal, and the
easy fix, of course, is to just switch headphones around.
