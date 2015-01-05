Title: Securely erasing SSD drives
Date: 2014-01-04 11:22
Modified: 2014-01-12 15:13
Author: Steven Maude
Tags: hdparm, ATA, Secure, erase
Slug: securely-erasing-ssd-drives
Summary: How to securely erase drives with the ATA Secure Erase function via hdparm.

So, it turns out that [I was wrong about the motherboard being the cause
of my recent Windows hibernate
issues](http://www.stevenmaude.co.uk/2013/12/things-ive-learned-from-building-and.html).
The failure to resume on hibernate still occurred after that, although
perhaps more rarely. There's always the possibility that there's some
strange problem common to the chipset (both boards are based on Intel's
H87 chipset). However, since I've not seen anyone other reporting of
this, I'm going to assume it's another piece of hardware to blame.

I spent several hours running [memtest86+](http://www.memtest.org/) on the
RAM and it didn't show up any problems. I also couldn't find any reports
of the graphics card (Radeon 7870) or the Catalyst drivers causing
hibernate issues, so my suspicion has moved to the solid state drive.
(Apart from the CPU itself and the DVD drive, there's nothing else in
the PC!) Because of this, I needed to return the SSD and this, of
course, meant that I had to ensure that any data on it was wiped
completely.

I'd previously written about using [DBAN to wipe
drives](http://www.stevenmaude.co.uk/2013/08/dariks-boot-and-nuke-unrecognized.html).
What I learned this week is that using the [ATA Secure
Erase](https://en.wikipedia.org/wiki/Write_amplification#Secure_erase)
function is the best way to go. [This is particularly the case for SSDs
due to the way in which they write
data](https://en.wikipedia.org/wiki/Data_remanence#Data_on_solid-state_drives).

How to use hdparm to do this is well explained
[here](https://ata.wiki.kernel.org/index.php/ATA_Secure_Erase): an easy
way is to access hdparm is via a Linux boot CD.

The important things to
remember are to make sure that you've selected the correct drive (the
safest way is to only have the drive connected which you want to be
wiped) and that you might have to "unfreeze" your drive by power cycling
it to allow you to execute the hdparm commands successfully.

For the SSD
I was using, the secure erase took about 45 seconds. If you worry about
whether the manufacturer has implemented this function correctly, you
might also want to [write over the drive with random data
twice](http://security.stackexchange.com/questions/12503/can-wiped-ssd-data-be-recovered)
using shred or dd.
