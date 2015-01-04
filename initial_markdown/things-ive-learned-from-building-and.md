Title: Things I've learned from building (and rebuilding) a PC.
Date: 2014-01-16 18:30
Author: Steven Maude (noreply@blogger.com)
Tags: Bitlocker, build, PC, learning, heatsink, motherboard, ASUS, assembly
Slug: things-ive-learned-from-building-and

<div class="separator" style="clear: both; text-align: center;">
[![Image of an assembled
PC.](http://3.bp.blogspot.com/--Nrs1AU4HC4/UsKt5fnIvcI/AAAAAAAAAIY/6-No16qaVS8/s1600/PC.jpg "The finished PC.")](http://3.bp.blogspot.com/--Nrs1AU4HC4/UsKt5fnIvcI/AAAAAAAAAIY/6-No16qaVS8/s1600/PC.jpg)

</div>
Delving into the inside of PCs isn't that new to me, I've swapped in and
out pretty much every part at some point individually. But, building a
PC entirely from scratch was new to me and I'd decided to do this for a
Christmas gift since I couldn't find any off-the-shelf PCs for the
recipient that had the specification I was looking for.  
  
<a name="more"></a>It's rewarding when you throw a lot of individual
pieces into a box, assemble them and find that **it actually works**when
you power it up. Disappointingly, this victory was shortlived. One of
the issues with buying lots of separate components is that you have to
cross your fingers to some extent and hope that there aren't any issues
with any individual one (bad drivers, firmware issues) and that they all
work well together.  
  
In my case, I found two cases of odd behaviour. First, case fans would
properly start almost every time the machine was powered on, but
wouldn't always. When this happened, I could see the rear fan trying to
twitch, but not doing anything useful. Forcing the fans to full speed in
the BIOS and restarting made the fans operational again, and you could
then reset them back to normal speed with them still running. Not great
though.  
  
Second, I was getting strange, and random, failures to restore the
system from hibernate under Windows, often with the message "Your
system's firmware did not preserve the system memory map across the
hibernate transition". Sometimes it would work, others not. It might
have been linked with entering the BIOS settings first before booting,
but I'm not entirely sure of that.  
  
Anyway, my hunch was that both of these issues seemed to be some problem
with the motherboard^[1](#f1)^, I tried a BIOS update provided by
technical support, it didn't improve things. I'd wasted that much time
on it, I just gave up and just ordered another board instead, and
(fingers crossed) everything seems OK at the minute.  
  

### So, some things I learned:

  
1. Unless you constantly keep track of what's going on in the world of
PC components, **the choice of PC components is a little overwhelming**.
For me, getting several use out of a PC isn't unreasonable with some
minor upgrades. My desktop is over six years old and I'm not that
interested in keeping up with what's going on if my current setup works
well enough...^[2](#f2)^  
  
For me, it kept feeling like I was always on the verge of making a poor
purchasing choice. There are plenty of reviews online, but it takes time
to delve into them. On the other hand,
[PCPartPicker](http://pcpartpicker.com/) didn't exist the last time I'd
bought lots of PC components and I found that useful for price
comparisons.  
  
2. When I first applied thermal compound to the heatsink, I used this
[two parallel lines
method](http://archive.benchmarkreviews.com/index.php?option=com_content&task=view&id=150&Itemid=62&limit=1&limitstart=5)
as I was using a heatpipe direct touch (HDT) cooler. After removing the
heatsink from the CPU when rebuilding, I found that it had worked well,
giving a good uniform coating across the CPU.  
  
3. Small **70% isopropyl alcohol medical wipes do a great job of
removing thermal compound**: the alcohol evaporates really quickly and
the wipes didn't leave fibres everywhere. You'll probably need a couple
of wipes for your CPU and another couple for your heatsink; they're sold
in huge packs very cheaply (I paid a couple of pounds for a hundred).  
  
4. **I didn't understand why there were so many complaints about Intel's
push pin cooler design until I had to install it the second time.**  
  

<div class="separator" style="clear: both; text-align: center;">
[![Close-up image of an Intel heatsink showing the push pin that holds
the heatsink in place in a
motherboard.](http://3.bp.blogspot.com/-TaeYmkgyNfI/UsKuhxFvIZI/AAAAAAAAAIk/ZdvrHB72SQA/s1600/Cooler_push_pin.jpg "An Intel cooler push pin.")](http://3.bp.blogspot.com/-TaeYmkgyNfI/UsKuhxFvIZI/AAAAAAAAAIk/ZdvrHB72SQA/s1600/Cooler_push_pin.jpg)

</div>
<div class="separator" style="clear: both; text-align: center;">
[  
](http://3.bp.blogspot.com/-TaeYmkgyNfI/UsKuhxFvIZI/AAAAAAAAAIk/ZdvrHB72SQA/s1600/Cooler_push_pin.jpg)

</div>
You put the pins of the cooler through the motherboard then click them
in place to open out the pins and lock them there. Sounds easy, until
you find that all but one pin are through the board while one side of
the final pin has bent completely out of shape. (Specifically, the force
I was putting on the pin had pushed one of the two bits of pointed white
plastic at the bottom of the pin to a near ninety degree angle against
the motherboard. It was still fixable though.)  

<div class="separator" style="clear: both; text-align: center;">
  

</div>
\5. **Motherboard and case manufacturers don't write the greatest
documentation.** There were some steps missing entirely from the case
instructions, e.g. how to pop out a front panel cover of the case to
make room for a DVD drive which was less than obvious. I was lucky that
I found a couple of YouTube videos where people were showing how they
built their PCs using that case step-by-step.  
  
ASUS decided to helpfully show a nice large pinout of the front panel to
motherboard wiring in the manual (e.g. HDD LED, power switch) so that
you didn't have to squint at the tiny print directly on the motherboard.
Unfortunately, the manual didn't bother to label the positive and
negative sides of the LEDs meaning I still had to stare at the
motherboard to figure this out...  
  
6. **Windows activation seems to tolerate motherboard changes when the
boards have identical chipsets.** It needed reactivating once I swapped
the board, but this was just another online activation.  
  
7. (**Unsurprisingly,) formatting a Bitlocker encrypted drive removes
the encryption.** I'm not sure why I thought it might be otherwise,
though Windows doesn't bother to warn you about this. My use case was
that I'd already encrypted an external backup drive for use with this
PC. However, as I'd carried out a fresh install after the rebuild, I
wanted to wipe the useless existing backups. (It was just the old
Windows install there, no user files). The quickest way is to delete
everything is to format.  
  
However, if it's taken a long time to encrypt the drive, it's probably
better to just delete the existing files on the drive instead. (Windows
8 gives you the [option of encrypting used space
only](http://winsupersite.com/article/windows8/windows-8-tips-protect-portable-storage-bitlocker-143777)
which would have made this is a bit less painful. Fortunately, I'd
tested on a small USB drive first to discover this rather than the 2 TB
backup drive which had taken several hours to encrypt.)  
<span style="font-size: x-small;">  
</span><span style="font-size: x-small;">^<a name="f1">1</a>^ For
reference, it was a Gigabyte H87-HD3. I couldn't find any reports of the
same problems, so the hibernate problem at least could have been some
rogue driver or problem of a combination of hardware. I still think the
fan control issue points to a buggy BIOS.</span>  
<span style="font-size: x-small;">^<a name="f2">2</a>^ Though having
just built this PC, it's quite tempting to build one for myself...
</span>

</p>

