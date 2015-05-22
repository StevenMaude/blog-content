Title: Darik's Boot and Nuke: fixing an "unrecognized device" error
Date: 2013-08-29 22:32
Modified: 2014-01-06 11:21
Author: Steven Maude
Tags: device, unrecognized, error, HDD, erase, DBAN
Slug: dariks-boot-and-nuke-unrecognized
Summary: Fixing unrecognized device errors in Darik's Boot and Nuke.
Alias: /2013/08/dariks-boot-and-nuke-unrecognized.html

!!! article-edit ""
    Edit 2014/01/04: I've written a [more recent
    post](http://www.stevenmaude.co.uk/2014/01/securely-erasing-ssd-drives.html)
    which describes how to use hdparm and ATA Secure Erase to wipe drives,
    which might be of interest if you're thinking of using DBAN, and
    particularly if you're erasing an SSD.

Over last Bank Holiday weekend, I'd been trying to install a dual boot
system and having lots of fun. Actually, for "lots of", read none,
though at least it works how I want it to now; maybe a subject for a
later post. One issue I thought I might be having was remnants of
[partition tables](https://en.wikipedia.org/wiki/GUID_Partition_Table)
still [sticking on the
drive](http://www.rodsbooks.com/gdisk/wipegpt.html), despite me doing a
fresh install. I decided it would be sensible to obliterate everything
and start from a completely empty drive as installing two operating
systems can be a fairly lengthy process (and a tedious one, if you've
done it several times as I had done).

[Darik's Boot and Nuke](http://sourceforge.net/projects/dban/) (DBAN) is
a free, Linux-based boot disk that lets you do just that. It needs to be
used with great care since it can wipe data from drives irrecoverably.
In my case, this wasn't an issue as, if anything, I *wanted* to start
from scratch.

Unfortunately, on booting DBAN, I was presented with an "unrecognized
device" showing up along with my hard disk. I was able to select my hard
disk to erase it, but then the erase immediately failed.

As this [support
thread](http://sourceforge.net/p/dban/discussion/208932/thread/332bf1d2/)
describes, this can be caused by internal media (e.g. SD) card readers.
So, anyway that you can deactivate the card reader might resolve this
problem. Disconnecting the reader from the PC (not necessarily so easy
if you're working with a laptop) or temporarily disabling the reader in
the BIOS are two options. In my case, the BIOS didn't let me do this and
I didn't really want to bother getting out screwdrivers unless I
absolutely had to.

For me, the solution that worked was also pointed out in the same
thread, **entering the command `dban nousb` at the DBAN
`boot:` prompt**. Then, only my hard disk showed up and the
process went smoothly. Using `nousb` means that you are
unable to erase any USB devices with DBAN but, if you're only interested
in wiping the HDD, this isn't an issue.
