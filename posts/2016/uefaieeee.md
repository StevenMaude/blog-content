Title: UEFaIeeee 
Date: 2016-12-16 00:11
Author: Steven Maude
Tags: EFI, UEFI, boot entry, efibootmgr 
Summary: Recovering a non-booting system when EFI boot entries are
         broken using efibootmgr.

In writing this, I checked the [valid spelling of
"aieeee"](https://en.oxforddictionaries.com/definition/aie) and it is
apparently with four e letters at the end.

If you're currently panicking how to fix a system where the UEFI boot
entry for your operating system has disappeared (i.e. from what you
might think of as the "BIOS" boot entries), you may be yelling a much
more extended form of that exclamation than that correct spelling could
ever suggest.

In that case, go straight to ["Fixing the problem"](#fixing-the-problem)
— go directly to that section and do not collect £200 — for advice.

## Background

Recently I've been undergoing the arduous process of getting a recent
version of Ubuntu on my laptop and dual booting with Windows. While I
was experimenting, I'd got everything working reasonably, when I'd
installed some updates and then, on shutting down that time, to let them
take effect, the laptop decide to lock up with the blinking
boot/shutdown dots illuminating but nothing happening.

I figured I'd check if everything was OK. I found that you can use
debsums to check if installed packages are as expected. Running it
(`sudo debsums -s` to ignore OK files) gave a few warnings. Since one of
them referred to a kernel image, it was a little concerning.

Since I hadn't done much with the laptop except install from a DVD for
which I'd verified the SHA256SUM (and verified the signature of the sum
file too), I didn't think anything untoward could have happened. And,
looking around, it seems that this has happened in previous releases
too: the mismatch was likely a genuine error in the release, not
indicative of anything wrong with my install. Of course, my rigorous
side stupidly got the better of me and I figured I might as well
investigate further.

Simple. I can just install Ubuntu again to a USB stick, not touching my
existing installation and then rerun debsums there. That thought there 
turned out to be anything but simple.

But I wasn't to know that at the time. An hour and a USB installation
later, yes, I'd demonstrated that the same warnings from running debsums
came up on this install too.

Satisfied with that explanation, I'd removed the USB stick, plugged my
hard disk back in and decided to boot, and saw:

> Boot failure

uh, OK.

## Installing Ubuntu to a USB stick broke my existing Ubuntu install

My guess as to what had happened is as follows. When I'd installed
Ubuntu to the USB stick, it installed to /dev/sdb, not /dev/sda. The
previous "ubuntu" boot entry that worked fine for my hard disk was
referencing /dev/sda and looked for a bootloader on the EFI partition of
my hard disk.

The USB install had been to /dev/sdb and the currently existing "ubuntu"
boot entry had been overwritten by one with the same name. Now that boot
entry was referencing /dev/sdb and looking for a bootloader on the EFI
partition of my USB install, couldn't find it, and therefore no longer
booted. The USB install could be booted without a hitch since the EFI
entry was pointing correctly to it.

Incidentally, the Windows install on the same hard disk was still
booting fine, again as expected, because the Windows EFI entry hadn't
changed.

## Fixing the problem

Some PCs give you UEFI setup options to add a boot entry, so you can
resolve the problem directly there. You'll need to know the path to the
bootloader for whatever operating system you want to boot, but that
should be relatively easy to locate.

However, my laptop is sparse in its configuration options and does not
offer this option. In that case — and even if your PC does have an
option to add boot entries directly) — you can use efibootmgr to add the
entry back. See [the answer here](https://superuser.com/a/697012)[^1] which
shows that you'll want something along the lines of:

```
efibootmgr -c -d /dev/sda -p 1 -l '\EFI\ubuntu\shimx64.efi' -L "Ubuntu"
```

As the post says, you can equally use Microsoft's `bcdedit` to do the
same, but that requires you to have Windows. You can always run
`efibootmgr` from a bootable Linux DVD or USB. And, you'll need to
change the disk (`/dev/sda`) and partition number (the `-p 1`) to
reflect which one is the EFI System Partition, which you can find by
doing `fdisk -l` in a terminal.

Then the entry will be readded and your install should be bootable
again.

That answer was exactly what I needed. Unfortunately, it took me far
longer to find than it should have, probably because it's talking about
"repairing GRUB". Hopefully, the keywords I've used here might help
others find this a bit more easily.

## What are the failures here?

This was unexpected. Yes, installing to a hard disk, then USB is
probably not a common use case, but you certainly wouldn't expect it to
break an existing installation. Maybe it's possible that it was because
I had a slightly unusual dual boot setup, but I don't see that should
make a difference. I'd expect this to happen even if you're single
booting. (Feel free to correct me if you've tested and found otherwise.)

### Hardware side

For my laptop in particular, you can't add EFI boot entries at all.
Auto detection would be ideal, but you can't even add entries manually.

### Ubuntu

Why does the installer not check for or warn of the possible issue of
clobbering an existing valid boot entry? Wouldn't it be preferable for
this to be far more explicit, check for an existing boot entry and ask
the user whether they want to leave the boot entries intact (and abandon
the install), add a new entry or replace the existing entry (with the
warning that this will probably break the existing installation)?

[^1]: The author of the answer maintains [an EFI boot
manager](https://en.wikipedia.org/wiki/REFInd), so he definitely knows
his stuff here.
