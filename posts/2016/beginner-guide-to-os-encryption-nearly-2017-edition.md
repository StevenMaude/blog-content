Title: A beginner's guide to OS encryption: (almost) 2017 edition
Date: 2016-11-28 00:26
Author: Steven Maude
Tags: BitLocker, encryption, LUKS, Ubuntu, Windows
Summary: How to dual boot Windows with Ubuntu and encrypt them both.

Previously I wrote about setting up my laptop to [dual boot Windows and
Ubuntu]({filename}../2013/a-beginners-guide-to-os-encryption-dual.md).
As the Ubuntu LTS I had installed was now aging badly[^1], it really,
really, *really* needed upgrading.

I'd been hesitant to upgrade. The last time I installed this way, it
took a week of following several guides, many of them out of date or not
working, and several failed installs.

## A quick guide

Fortunately, thanks to someone really helpful on the internet, I don't
have to write much this time:

1. Follow this [guide](https://askubuntu.com/a/293029/623909).

2. That's pretty much it.

## Installing Windows

Seeing as I have my text editor open, I'll clarify a little more.

To start with, I booted Windows 10 with my computer set to boot in UEFI
mode and with Secure Boot enabled. Starting from a clean hard disk, when
the Windows installer booted, I was using a clean drive, and instructed
the installer to create a new partition using a certain proportion of
space on my drive, leaving the rest of the disk as unformatted space.

You'll find you don't get one partition but four: a recovery partition,
the system (or EFI partition), a reserved space partition and the
primary partition where Windows will actually be installed.

Another hour or so later, and following running Windows Update,
hopefully you have a working and updated Windows machine. One big plus
of the Windows 10 installer versus what I've experienced previously is
that most computer hardware tends to get detected and installed
automatically, without you needing to find drivers buried away on a
manufacturer's website. Another is that, although Windows 10's
cumulative updates can be problematic if there's an issue with one part
of them, they do mean that you have only one big update to install, not
several hundred, as is seriously the case with Windows 7.

At this point, you can go ahead and encrypt the Windows operating system
drive with BitLocker, provided you have a version of Windows that offers
it. If you don't have a Trusted Platform Module in your PC, it's still
possible to use BitLocker, but you'll need to override this using [Group
Policy](https://technet.microsoft.com/en-us/library/jj679890(v=ws.11).aspx)
(search for `gpedit.msc` in the Windows search bar and run it). 

You can find the options in Group Policy under (breathe in): Computer
Configuration\Administrative Templates\Windows Components\BitLocker
Drive Encryption\Operating System Drives. The specific option you need
to change is "Require additional authentication at startup" and you can
then tick "Allow BitLocker without a compatible TPM".

You should probably consider enabling "Allow enhanced PINs for startup"
which is in the same Group Policy section while in there, seeing as this
lets you use characters, not just numbers.[^2]

Right clicking on the drive in Windows Explorer and selecting "Turn on
BitLocker" should let you then go through the process of encrypting the
drive.

Although I'm discussing Windows and Ubuntu here, note that the guide
I've linked to may well work for two Linux installations too.

## Installing Ubuntu

The usual advice is to install Linux *after* Windows, since Windows
doesn't necessarily play as nicely with Linux. I'm not sure if that
still holds in the days of UEFI booting, but it seemed sensible to do.

Going back to the [excellent
guide](https://askubuntu.com/a/293029/623909) that was posted, it's not
difficult to follow. Pay attention to the comments, as there were three
steps that were unnecessary in the process, which were pointed out
there.

The process has quite a few steps, but even if you don't understand
fully what's going on, it should Just Work™. Here's an overview of
what's involved once you've loaded Ubuntu from a DVD or USB:

1.  Use your unpartitioned disk space to create two partitions. One will
    be the unencrypted /boot partition and the other will be a LUKS
    container that contains an LVM physical volume. This is then
    subdivided into two logical volumes, one for the root partition, /,
    and the other for /swap.

2.  Install Ubuntu to the root partition you created with the installer,
    as normal, although make sure that you choose "Something else" when
    asked how to install.

3.  Don't immediately reboot after installing. Access your new
    installation by using a
    [chroot](https://en.wikipedia.org/wiki/Chroot). This gives a
    convenient way of modifying a configuration file in the new install
    (crypttab) to add details of your drive which need to be available at
    boot, and updating its
    [initramfs](https://en.wikipedia.org/wiki/Initramfs) with that
    configuration.

After that, booting up into Ubuntu should work and prompt you to unlock
the LUKS container. Depending on your UEFI setup and your preference,
you may need to go into your PC's boot menu at startup and select Ubuntu
directly (or reorder the default boot order so that it boots by
default). 

### Some more tips

The guide's pretty good, and my install was successful first time with
no real hiccups, which was a pleasant surprise. There are, however, a
few points which aren't mentioned:

1.  When you're using GParted to partition your drive, you may wish to
    use the "cleared" option instead of "unformatted" to avoid any
    confusion. Otherwise, if your drive has previous partitions present,
    you may see GParted inform you that the type of partition is
    whatever used to be there. It shouldn't make a difference however,
    as you later should format the partitions anyway. 

2.  Make sure you read what the terminal's telling you. I was really
    confused when the `luksOpen` command didn't work as I'd run the
    `luksFormat` command before. Where I'd gone wrong is that
    `luksFormat` asks you to confirm you want to format the drive.
    Instead of typing uppercase "YES" as it instructs, I'd typed "yes",
    and the program just exited instead, without warning it hadn't done
    anything.

3.  When creating the logical volumes where / and /swap will live, you
    use the `lvcreate` command. With the `-L` flag as used in the guide,
    you directly specify the size it should take. If you want to ensure
    that the second partition uses the rest of the space, you can use the
    `-l` flag as in `-l 100%FREE` instead of e.g. `-L 7.5g`.
    
    You can also check the status of the volumes you've created using
    `pvs` and `lvs` to ensure everything is as you like, before
    proceeding.

4.  When installing the GRUB bootloader, it belongs in the EFI
    partition.  If you select the disk where you're installling the
    operating system, the Ubuntu installer should automatically detect
    the partition and install GRUB there. It's likely that it's /dev/sda
    if the only hard disk that's plugged in. Alternatively, you can
    identify the EFI partition directly and choose that, e.g. /dev/sda2.

5.  The guide suggests using `mount` and `swapon` to check which volumes
    are being used in the new installation. Running `lsblk` in the
    terminal can do this in a single command. It will show you which
    block devices are mounted and where: you should see the / and /swap
    inside your encrypted LUKS container.

## Reinstalling

How would reinstalling one of the operating systems work? I haven't
tried it yet, so can't say for certain. Below is a thought experiment,
although please heed the warning that it is only a thought experiment.

My hunch is that an Ubuntu reinstall should be fairly straightforward:
delete the two partitions you created (/boot and the LUKS/LVM
partition), create new ones and follow the whole process again. It
shouldn't impact the Windows installation, as the Windows bootloader
should still exist in the EFI partition. And reinstalling Ubuntu should
just overwrite the existing Ubuntu bootloaders.

Reinstalling Windows might be trickier. If you retain the existing EFI
partition and install Windows to the same operating system partition
(i.e. without wiping all four partitions and telling Windows to install
to the unpartitioned space), that shouldn't break Ubuntu as I'd guess
that Windows just uses the existing EFI partition, and therefore would
leave GRUB in place. Otherwise, if you do decide to wipe out all four
partitions that Windows created, you'll need to reinstall the GRUB
bootloader to the new EFI partition; see [Debian's
wiki](https://wiki.debian.org/GrubEFIReinstall) and [this
guide](https://superuser.com/a/376471).
It still shouldn't otherwise break your Linux installation, apart from
this though.

Again, I've not tested any of this has been tested yet. If I ever try
reinstalling one operating system and not both, I'll no doubt edit this
post or add a new one describing that process.

[^1]: A subject for another post. My brief advice if you're intending to
use Ubuntu LTS releases is to upgrade every time, and not skip any,
especially if you're running it as a desktop.

[^2]: Yes, in this case "PIN" does then become a misnomer.
