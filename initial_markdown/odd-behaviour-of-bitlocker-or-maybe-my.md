Title: Odd behaviour of Bitlocker, or maybe my HDD...
Date: 2013-10-13 20:55
Author: Steven Maude
Tags: partition, Bitlocker, backup, enclosure, bug, drive
Slug: odd-behaviour-of-bitlocker-or-maybe-my

As [I'd previously
mentioned](http://www.stevenmaude.co.uk/2013/09/how-to-secure-your-storage-and-backup.html),
I'd had issues with a USB 3 drive enclosure when trying to set up a
backup drive with Bitlocker on Windows 7. When I replaced the USB 3
enclosure with a slower, USB 2 enclosure, I found exactly the same
problem. On trying to enable Bitlocker, I got the message: "A drive
attached to the system is not functioning."  
  
Hmm. What I discovered is that if I tried a different Bitlocker
partition size, e.g. 3072750500 MB rather than 307200 MB, it worked!
There were no other partitions present on the drive; this NTFS partition
was the only one.  
  
Furthermore, this "fix" applied to the USB 3 enclosure, so it seems it's
an issue with my drive (Samsung ST1000LM024) or Windows itself.  
  
It's a really peculiar issue: partition sizes of 307200, 307250 to
307255 and 307265 to 307269 MB gave me this error, but a 307270 MB
partition would have been fine. Likewise, I got errors at 153600, 460800
and 76800 MB; it certainly doesn't like multiples of roughly 150 GB...
([it's possible that this is a red herring
though](https://en.wikipedia.org/wiki/Confirmation_bias) — I couldn't
realistically try **every** possible partition size).  
  
I haven't observed any other issues having setup the drive, but this is
unusual nonetheless, and I couldn't find anyone documenting anything
similar.
