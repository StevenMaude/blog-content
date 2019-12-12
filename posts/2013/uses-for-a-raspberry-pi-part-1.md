Title: Uses for a Raspberry Pi (part 1)
Date: 2013-07-10 21:21
Modified: 2013-07-14 13:45
Author: Steven Maude
Tags: adapter, Pi, Airprint, Raspberry, wireless, wifi
Slug: uses-for-a-raspberry-pi-part-1
Summary: A few simple, but useful, applications for a Raspberry Pi, including a wireless adapter and AirPrint server.
Alias: /2013/07/uses-for-a-raspberry-pi-part-1.html

<img class="article-image" src="{static}/images/2013/Raspberry_Pi.jpg" alt="A powered on Raspberry Pi.">

<blockquote>
  <p>Don’t buy one and put it in the cupboard; buy one and do an
  interesting thing with it and tell the world what you did.
  </p>
  <cite><a href="http://www.dailybrink.com/?p=3304">Eben Upton</a></cite>
</blockquote>

When I finally got my hands on the low priced Raspberry Pi computer, it
was autumn. Although it had been released in February, its low price and
the engagement of the Raspberry Pi Foundation with the user and
developer community meant that people were clamouring for them and
supplies were scarce. This explains why it was very difficult to get
hold of for several months. Since then, I've found several uses for my
Pi, and I thought it might be useful, in the spirit of the opening
quote, to briefly discuss them.

My uses for the Pi are fairly simple, especially in comparison to those
that frequently adorn the official [Raspberry
Pi](http://www.raspberrypi.org/) site, but I've still found them very
handy nonetheless. I wouldn't have been particularly unhappy if I'd
spent £30 on a device that does just one of the tasks that I using the
Pi for. It's no surprise that a device that does all of these tasks, and
*can still do more*, makes the Pi one of my favourite bits of recent
hardware. I'm certainly not alone in that view: the driving force behind
the Pi, Eben Upton, was [quoted as initially hoping for 1,000
sales](http://www.zdnet.com/we-thought-wed-sell-1000-the-inside-story-of-the-raspberry-pi-7000009718/);
a huge underestimate from the *hundreds of thousands*it has sold.

One of the most obvious uses for a Pi is to run [XBMC](http://xbmc.org),
the fantastic open source media center software. The fact that XBMC was
shown to run pretty smoothly prior to the Pi's release no doubt played a
part in the Pi's early popularity, considering the feature set that XBMC
alone offers. That said, my assumption is that anyone with a Pi already
knows about XBMC — in the unlikely event that you don't, make sure to
try [Raspbmc](http://www.raspbmc.com/) out — therefore I'll skip over it
here and leave that discussion to the many pages that discuss XBMC on
the Pi. Instead, I'll focus on other useful functions.

For reference, at the time of writing, Raspbian is the [officially
recommended](http://www.raspberrypi.org/downloads) operating system and
that's what I'm running on my Pi. All of the uses for my Pi use it
[headless](https://en.wikipedia.org/wiki/Headless_system). I usually
connect to the Pi via an
[SSH](https://en.wikipedia.org/wiki/Secure_Shell) client, though you
could attach a keyboard and TV/monitor to it and enter terminal commands
directly.

So, what can you use a Pi for?

* * * * *

## 1. Access to useful Linux command line tools

Even just installing a Linux distribution like Raspbian, *without
installing anything else*, gives you access to [several powerful
programs](https://en.wikipedia.org/wiki/List_of_Unix_utilities)
(particularly the [text processing
commands](https://github.com/nschneid/unix-text-commands)) that you
might not have ready access to, if you don't already have another PC
running Linux available.

Yes, you can get access to some of these tools within Windows if you
install something like [GnuWin32](http://gnuwin32.sourceforge.net/) or
[Cygwin](http://www.cygwin.com/), or go to the trouble of installing
Linux in a [virtual machine](https://www.virtualbox.org/), but it's nice
to just power on a device and start working with these tools immediately
and without any further setup.

Another example is that when I started using
[github](https://github.com/StevenMaude), I found it easy to just run
the [git](http://git-scm.com/) command line tool from the Pi. *It just
worked.* In my case, git had already been installed, so I didn't even
need to type `sudo apt-get install git`. This was a lot
simpler than me trying to decide on the best way to run git on Windows.

## 2. Wireless adapter for a device without onboard wifi

I installed a cheap Ralink wifi adapter (around £4 from eBay) to connect
my Pi to a wireless network. Because of this, the Pi's onboard Ethernet
port was going unused. It's relatively straightforward to configure the
Pi to enable a device connected to it by Ethernet to use the Pi's wifi
connection to access the network

<img class="article-image" src="{static}/images/2013/Wifi_dongle.jpg" alt="Wifi adapter for the Pi.">

Wifi is a common feature of networked devices these days, but the Xbox
360 is an exception to this rule. Earlier this year, I explained in [a
Stack Exchange post](http://unix.stackexchange.com/a/64353) how to
configure the Pi such that the Xbox can access the network. There's no
reason why the same procedure couldn't be used for other networked
devices without wifi.

## 3. AirPrint server

Earlier this year, I was asked, "How can I print something from my
iPad?"
My reply was along the lines of, "Not easily: we don't have a printer
that supports [AirPrint](http://support.apple.com/kb/ht4356)."

That conversation inspired me to have a look around in case it was
actually possible. After a quick search, I found
[airprint-generate](https://github.com/tjfontaine/airprint-generate),
along with a [step-by-step
guide](http://the.taoofmac.com/space/blog/2012/12/16/1730) explaining
how to install this on the Pi. Even with having to install
[CUPS](http://www.cups.org/) and testing a couple of
[iDevices](https://en.wikipedia.org/wiki/IDevice), I don't think the
whole setup took more than thirty minutes or so. With this AirPrint
solution, printing from an iPad is integrated just as if we used an
AirPrint-compatible printer; no third party app is necessary to print.

* * * * *

As its price suggests, the Pi isn't hugely powerful, but that doesn't
hinder it from being incredibly useful for applications where computing
power isn't critical, like the AirPrint server. (Here, even if it runs a
little slow, the response time isn't really an issue: would a user
really notice the extra few seconds that a document might take to print,
compared with a much faster PC?) The Pi is also very [cheap to
run](http://www.raspberrypi.org/phpBB3/viewtopic.php?t=18043), as well
as being silent, making it ideal for server applications with modest
computing power requirements.

Even if you are starting from scratch, and need to run the Pi's
operating system installer first, it should only take you, at most, a
couple of hours to get everything here running. In a single evening, you
can complete a small project that you get something back from almost
immediately, which is really encouraging.

On that upbeat tone, that's probably a good place to end this post! When
I write about the Pi next, I'll cover uses of the Pi as a file server
(using [Samba](http://www.samba.org/)), and how I've found
[get_iplayer](http://www.infradead.org/get_iplayer/html/get_iplayer.html)
to be a great alternative to the BBC's officially supported service.
