Title: Some <s>spring</s> winter Ubuntu cleaning
Date: 2013-12-24 00:04
Modified: 2015-07-31 13:10
Author: Steven Maude
Tags: clean, free, LTS, TRIM, space, 12.04, kernel, encryption, dm-crypt, Ubuntu, boot
Slug: some-spring-winter-ubuntu-cleaning
Summary: Some Ubuntu tips: setting up TRIM on an encrypted drive for 12.04 LTS and freeing up space on the boot partition.
Alias: /2013/12/some-spring-winter-ubuntu-cleaning.html

Did a little quick maintenance to my Ubuntu install[^1] today.

First, I'd noticed that the boot partition was starting to get a little
full, meaning that cleaning out old kernel images was overdue. If it
gets completely full, you won't be able to upgrade to newer kernel
versions.

[This is a fairly simple way from the command line; I'll summarise it
here.](http://askubuntu.com/a/153193)

Check which kernel is currently in use:

```shell
uname -r
```

**Do not remove the kernel image that uname returns!**

List the other kernels that are installed:

```shell
dpkg --list | grep linux-image
```

You'll see a list that includes the kernel image in use, along with
others that aren't. These are safe to remove.

To remove a kernel image, **not the one listed from the
`uname` command:**

```shell
sudo apt-get purge linux-image-x.x.x.x-generic
```

I've seen it recommended that you keep one or two older images installed
in case you need to revert to an older version for any reason, which
seems sensible.

You can also remove the corresponding kernel headers too:

```shell
sudo apt-get purge linux-headers-x.x.x.x-generic
```

* * * * *

Second, I'd read a couple of days ago that [Ubuntu 14.04
LTS](http://news.ycombinator.com/item?id=6948536) is going to get [TRIM
support](https://en.wikipedia.org/wiki/Trim_%28computing%29). If you use
a solid state drive, TRIM[^2] is a useful feature that stops the
performance of your drive degrading over time.

**Great, but hang on, 12.04 LTS never did?**

Hmm, better fix that. If you're using an unencrypted file system, then
running `fstrim` on the relevant partitions manually or
setting up a cron job to do so isn't too difficult. If you're using a
dm-crypt encrypted file system as I am, it's not quite as
straightforward. It's still only a two minute job, but it's not quite as
obvious what you need to do to get this working. [There's a nice guide
here](http://blog.neutrino.es/2013/howto-properly-activate-trim-for-your-ssd-on-linux-fstrim-lvm-and-dmcrypt/)
that explains each step; you enable TRIM for both dm-crypt itself and
the Logical Volume Manager, and then create a cron job that TRIMs the
drive weekly.

Before choosing to do this, note that enabling TRIM with dm-crypt can be
a [security
risk](http://asalor.blogspot.co.uk/2011/08/trim-dm-crypt-problems.html).
There are potential issues in terms of leaking file system information,
which may be a concern if you have hidden volumes.

[^1]: Incidentally, why have I not
got some nice Ubuntu logo here to make this post look nicer? Incidents
[like
this](http://arstechnica.com/information-technology/2013/11/canonical-abused-trademark-law-to-target-a-site-critical-of-ubuntu-privacy/)
aren't exactly encouraging, even if later admission of mistakes are made...
[^2]: Reading "TRIM" so many times just meant I had to [listen to
this](https://www.youtube.com/watch?v=dBcCXX0aWhc) while writing.
