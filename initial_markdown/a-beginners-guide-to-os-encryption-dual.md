Title: A beginner's guide to OS encryption: dual booting and encrypting Windows and Ubuntu
Date: 2013-11-22 20:01
Author: Steven Maude
Tags: disk, Bitlocker, Linux, Windows, encryption, TrueCrypt, drive, Ubuntu
Slug: a-beginners-guide-to-os-encryption-dual

<div class="separator" style="clear: both; text-align: center;">
[![A padlock with a
key](http://1.bp.blogspot.com/-t3K6UGY0kPw/UjifYLhA4QI/AAAAAAAAAFc/LmSQqgxC6Xg/s1600/Padlock+and+key.jpg "Padlock and key")](http://1.bp.blogspot.com/-t3K6UGY0kPw/UjifYLhA4QI/AAAAAAAAAFc/LmSQqgxC6Xg/s1600/Padlock+and+key.jpg)

</div>
  
The beginner in the title of this post may or may not refer to you. It
certainly describes me. Since I was about to setup a new PC, I decided
it was about time to think a little more seriously about how to secure
my data. If someone got hold of my PC or external drives, without
encryption, it's trivial for them to read anything from them.  
  
Data encryption that is difficult to break if currently implemented and
used with strong passphrases is pretty much cost free these days, both
financially and in terms of the hit on computer performance (the latter
particularly so if you have a CPU that supports the [AES instruction
set](https://en.wikipedia.org/wiki/AES_instruction_set). As Wikipedia
points out, despite your CPU being one that supports this feature, you
might find that the manufacturer has neglected to enable it; it's worth
checking for BIOS updates that deal with this.)  
  
Getting an encrypted PC running with just one operating system is
relatively simple to setup. Complicating matters is the fact that I
wanted to dual boot Windows with a Linux distribution — in my case, I'd
chosen Ubuntu — and encrypt both. In the process, I ended up undergoing
a ridiculous number of installs over several days to actually get this
working as I wanted.  
  
If you're struggling to do the same, I hope that some of the pointers
here might save you some time rather than having to learn the hard way.
There are a few subtle caveats documented here that I hadn't seen
collated together elsewhere. Also, many blog posts and articles I'd read
were horribly out of date or didn't have sufficient information for me
to follow them. (A note to anyone who kindly shares guides:
**step-by-step guides with screen grabs are invaluable**when a reader is
way out of their depth.)  
  
Here's details of the three approaches I tested.  
  

* * * * *

  

### Approach 1: Encrypt Windows 8 Pro with Bitlocker; encrypt Ubuntu with [LUKS](https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup)

I followed [this guide](http://linuxtutorialscratchpad.blogspot.com/)
with some success in that I was able to encrypt both systems.  
  
Instead of the Ubuntu minimal CD in those instructions, I used [Ubuntu
12.04 LTS alternate CD](http://releases.ubuntu.com/precise/); using the
long term support version isn't a bad idea if you're not bothered about
the latest shiny things.  
  
Why the alternate CD? What Ubuntu's standard installer (as of 13.04)
seems to offer is either the installation of Ubuntu *unencrypted* on a
PC side-by-side with an existing Windows install. Alternatively, you can
wipe the Windows install and install Ubuntu *encrypted*, **but you can't
*encrypt* Ubuntu when Windows is already installed**.  
  
However, I found Windows 8 was fairly broken, even ignoring the
clunkiness of the user interface. All kinds of [Volume Shadow
Cop](https://en.wikipedia.org/wiki/Shadow_Copy)y service errors were
occurring. This meant that I couldn't backup anything with the built-in
Windows tools and the System Restore feature presumably wouldn't work
either. Even when Windows wasn't Bitlocker-encrypted, I was still
getting these errors. I couldn't find much support for the problems I
found, so perhaps it was some dual booting issue; if you have any ideas,
please comment or [let me know via
Twitter](https://twitter.com/StevenMaude).   

### 

### Approach 2: Encrypt Windows 7 Enterprise/Ultimate with Bitlocker; encrypt Ubuntu with LUKS

  

<div class="separator" style="clear: both; text-align: center;">
[![Screengrab of Bitlocker's user interface in Windows
7](http://2.bp.blogspot.com/-YHovckl_t6k/UjigsXdI86I/AAAAAAAAAFo/0vB8LUzdrsc/s1600/Bitlocker.png "Bitlocker in Windows 7")](http://2.bp.blogspot.com/-YHovckl_t6k/UjigsXdI86I/AAAAAAAAAFo/0vB8LUzdrsc/s1600/Bitlocker.png)

</div>
  
The first issue here is that the only versions of Windows 7 that support
Bitlocker are Enterprise and Ultimate. If you have Windows 7 Pro, you're
out of luck. You may also find issues on trying to boot the Windows 7
installer on a PC with UEFI, in which case you may have to drop back to
legacy mode to work round this.   
  
Here, I never even got to install Ubuntu and stopped at attempting to
encrypt Windows for one big reason. Unlike Windows 8, if your PC — like
mine — doesn't have a [Trusted Platform
Module](https://en.wikipedia.org/wiki/Trusted_Platform_Module), the only
way to unlock the Bitlocker drive on boot is to use a USB key.  
  

<div style="text-align: center;">
**Without a TPM, you cannot use a password for Bitlocker in Windows 7**.

</div>
  
This isn't ideal. If you forget the key, you're locked out of your PC.
It's also something else to have to carry around (though I suppose it
might be possible to use a phone as USB storage...). If I was just lazy
and just left it plugged in the whole time, it could easily be stolen
with the PC. So, it was best that I didn't spend any more time
considering this option.  
  

### Approach 3: Encrypt Windows 7 (any version) with TrueCrypt; encrypt Ubuntu with LUKS

  

<div class="separator" style="clear: both; text-align: center;">
[![TrueCrypt program window showing options to create a new encrypted
volume](http://1.bp.blogspot.com/-9V9A7i8abJQ/UjihnwXL6WI/AAAAAAAAAFw/0Ld12GK1RyI/s1600/TrueCrypt.png "TrueCrypt volume creation menu")](http://1.bp.blogspot.com/-9V9A7i8abJQ/UjihnwXL6WI/AAAAAAAAAFw/0Ld12GK1RyI/s1600/TrueCrypt.png)

</div>
  
The fact that TrueCrypt has its source available is a plus. I'm nowhere
near smart enough to start understanding the internals of cryptographic
software, but there are people out there who are. And I would certainly
hope that they would raise the alarm if they spot anything
suspicious.^1,2^  
  
Unlike Bitlocker on Windows 7, TrueCrypt allows you to use a
user-entered password to unlock the PC. However, at the moment, [it
doesn't work with a PC booting in UEFI
mode](http://www.truecrypt.org/future).  
  
Rather than duplicate information already available, I'll just point you
to Maarten Mastbroek's [excellent
guide](http://techblog.mastbroek.com/all-articles/dualboot-encrypted-windows-and-ubuntu/).  
  
My only comments on that guide are that you don't need to worry too much
about the 100 MB partition that Windows installs, you can simply leave
it rather than use it as a /boot partition. Also, when installing
TrueCrypt, you can tell it you have a single boot machine.  
  
**The only other issue is that you should ensure that both installers
are run in legacy (non-UEFI mode)**. If your PC supports
[UEFI](https://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface),
there should be BIOS options, or options that appear when you booting
installation media, to select this. During my install, the Ubuntu
installer never asked me where to install the GRUB bootloader. I suspect
that having put Ubuntu onto a USB drive, it was booting straight into
UEFI mode without asking me and this was fouling up the GRUB install.  
  
My workround was to burn a DVD copy of the Ubuntu installer and this
gave me the option to select UEFI or legacy mode at boot. Alternatively,
and maybe more easily, [you can just delete the <span>efi</span> folder
from the Ubuntu USB stick you
prepare](http://askubuntu.com/questions/338894/how-to-disable-the-efi-check-in-13-04-x64).  
  

### Issues

In terms of usability, apart from having to enter another password
before I boot either OS, everything seems pretty much as if the drives
weren't encrypted. Otherwise, the only issues I have with this setup
are:  

-   The only feature I haven't got working yet is hibernate on Ubuntu
    with drive encryption (it works on Windows), though there's a [guide
    on how to do
    this](http://ubuntuforums.org/showthread.php?p=12062069#post12062069)
    which I may try when I have time to investigate it further.
-   My setup doesn't use UEFI. This isn't a big deal for me, though.
-   The Windows boot/system reserved and the Linux boot partitions
    remain unencrypted and [this is a potential
    vulnerability](https://en.wikipedia.org/wiki/TrueCrypt#Physical_security).
    However, it should be sufficient to ensure my data is kept secure in
    the event of loss or theft.

All in all, not too bad.  
  

### SSD encryption?

After all that effort, software encryption might not even be the best
way to go. Instead, as SSDs have become more affordable, using
hardware-based SSD encryption might be simpler. With the drive handling
encryption, it should be completely transparent to the operating system,
meaning no hit on performance (this might be an issue if you want to use
encryption on an older PC), with the bonus of eradicating the
possibility of any install pain.  
  
Sounds great, doesn't it?  
  
Unfortunately, it's no panacea. The [implementation is not always
clear](http://vxlabs.com/2012/12/22/ssds-with-usable-built-in-hardware-based-full-disk-encryption/).
You are reliant on being able to use a strong ATA drive locking
password, rather than the eight character one that some BIOSes only
support. (Incidentally, this isn't information that's necessarily easy
to discover prior to buying new hardware).  
  
Additionally, note that some manufacturers might have vendor specific
workarounds, for example, [having a standard master password that should
be
changed](http://thaeial.blogspot.com/2013/01/locking-and-unlocking-hdd-with-dell.html).
This is all quite messy, but perhaps this will become more transparent
from an end user perspective in future.  
  

* * * * *

  
<span style="font-weight: normal;">Next time that I discuss encryption,
I'll be posting about external storage and backup encryption.
Thankfully, this is a far, far easier problem to solve than OS
encryption. If you've got any other approaches or tips for encrypting
dual boot systems, I'd be interested to hear them.</span>  
  
<span style="font-weight: normal;">^1^At the time of writing, [this is a
particularly relevant
concern](http://www.theguardian.com/world/2013/sep/05/nsa-gchq-encryption-codes-security).
</span>  
<span style="font-weight: normal;">^2^Edit November 2013: TrueCrypt's
source is going to be [security
audited](http://istruecryptauditedyet.com/).</span>

</p>

