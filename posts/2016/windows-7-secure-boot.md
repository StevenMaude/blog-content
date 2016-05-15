Title: The case of a Windows 7 update, Secure Boot and a suspect motherboard 
Date: 2016-04-12 00:33
Author: Steven Maude
Tags: Windows, Secure Boot
Summary: Fixing Secure Boot related issues on Windows 7 following the KB3133977 update.

Because, obviously, I have nothing I'd rather do than try to fathom how Secure
Boot works on a Monday evening, I'm writing this up. 

Maybe you're experiencing this problem right now. Maybe you're not, but you're
intrigued as to how I go about diagnosing computer problems.

## A stubborn PC

I maintain a PC that has Windows 7 installed (due to be upgraded to Windows 10)
and, yesterday evening, installed several optional updates.[^1] Nothing unusual
there.

A day later, an owner of the machine restarted it. Except, well, the PC
refused.

Instead it said this:

> The system found unauthorized changes on the firmware, operating system or
> UEFI drivers.

Hmm. That's certainly not good since it's related to [Secure
Boot](https://technet.microsoft.com/en-GB/library/hh824987.aspx)'s check of
boot integrity. Warily, I disabled Secure Boot in the BIOS to get the machine
to boot Windows, and checked the System Event Log.

Looking around the log, it turns out that the last time that the machine had
previously successfully started was just before I installed the updates, which
is consistent with what had happened. As the PC was fine until that point, it
ruled out anything malicious, and pointed to the update as being a likely
candidate.

Having looked through the list of recently installed updates, most of them
seemed fairly routine, except [the KB3133977 update for a Bitlocker
issue](https://support.microsoft.com/en-gb/kb/3133977). What stood out were the
changes to Windows Boot Manager files `Bootmgr.efi` and `Bootmgfw.efi`, which
also suggested the update was at fault.

## ASUSpect?

Searching around led me to several recent links, as I mentioned in comments on
this [SuperUser
question](https://superuser.com/questions/1054790/system-found-unauthorized-changes-on-the-firmware).

In those posts, Windows users were reporting the same issue: the BIOS
complaining that there was an unauthorised change. This being a relatively new
issue isn't surprising as the update was only released on March 14th, 2016.

ASUS being the motherboard manufacturer seems to be common to those
experiencing the problem. It seems to affect different models; here it's a
H87-PRO. Even then it's unclear what the root cause is:

* maybe ASUS motherboards are the only ones that allow you to enable Secure
Boot with Windows 7?

* maybe there's something unusual with the signing process of this update that
only affected ASUS motherboards?

* or maybe it's just a coincidence? (But, it's odd that it's a common link in
several cases. You'd think if users with other motherboards would have been
affected, they'd have mentioned it too.)

As linked above, Microsoft's site suggests Secure Boot is supported on Windows
8 and up, and I can't find any documentation to suggest Secure Boot should work
on Windows 7. It's possible that this is just behaviour out of specification
that didn't cause any problem until now.

!!! article-edit ""
    Edit 2016-05-15: It turns out that it was a bad configuration on the
    part of ASUS as documented by their
    [FAQ](https://www.asus.com/support/faq/1016356/). Judging from the
    news stories published around 4th May 2016 and onwards, that note
    has only been released by ASUS this month. Pretty slow response,
    really, seeing as this problem's been known for several weeks. Their
    fix is one of those already suggested here: disable Secure Boot.

(It's a while ago since I installed the PC, but I guess that I originally must
have tried turning on Secure Boot during installation and, since the PC booted
without a problem, left it enabled.)
 
## What to do?

Other posts I'd read indicated that removing KB3133977 didn't solve this.
Perhaps there are EFI changes that don't get reverted when you uninstall the
update? Who knows?

However, restoring a previous system backup fixes the issue. You could then
leave everything as is, but have to make sure that you don't install this
update (hiding it would work). This is inconvenient then, but fine provided you
have regular backups.

Oh, but the update might actually fix a problem you're experiencing with
Bitlocker. In which case, you're going to have to install it regardless then,
aren't you?

Another solution is to disable Secure Boot in the BIOS. That's not a perfect
solution though, especially if you're booting other operating systems that work
with Secure Boot.

It's always possible, but unlikely, that Microsoft could reissue the update and
enabling the Secure Boot option might be possible again.

None of that explains completely what happened, but that's at least enough to
hopefully stop you panicking and make your Windows install accessible, if
you've been affected.

What fun will today's later batch of updates brings, I wonder?

## One more thing

Incidentally, I wondered what happens if you disable Secure Boot, then do an
in-place upgrade of Windows in this situation, where we can't enable Secure
Boot? Can you later enable it?

My hunch is that you should be able to, provided your operating system was
installed when your BIOS was in UEFI mode. With the ASUS motherboard I was
looking at, if you were doing an in-place upgrade in this particularly strange
case, I think you'd need to clear the Secure Boot keys to disable Secure Boot
while allowing UEFI (otherwise you wouldn't be able to boot Windows 7).

Once the upgrade's complete, I'd then expect I could go back to the BIOS and
install the default Secure Boot keys, which should let you set Secure Boot
again.

[^1]: Previously, I had recommended updates set to automatically install, but
unfortunately it's now necessary to make sure you don't [inadvertently install
Windows 10](https://blogs.windows.com/windowsexperience/2015/10/29/making-it-easier-to-upgrade-to-windows-10/).
