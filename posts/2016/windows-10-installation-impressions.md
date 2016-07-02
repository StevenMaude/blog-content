Title: Windows 10 installation impressions
Date: 2016-07-02 23:35
Author: Steven Maude
Tags: Windows, installation
Summary: A late look at Windows 10, particularly installation improvements.

Windows 10 is only a free upgrade from Windows 7 or 8.1 until the end of
this month[^1]. If you've hesitated so far, you might be a bit unsure as
to whether you should switch a system you're satisfied with for a
potentially less satisfactory one. But, if you want a free upgrade, you
haven't got long left, so you need to decide whether to take it up very
soon.

Earlier this year, I installed it on one PC, partly to test Traktor out
on a clean install of Windows 10, and partly to claim the free upgrade
on that PC. That went OK. And, as I'm claiming free upgrades on other
PCs that I'm caring for, you might think that, at least, I don't loathe
the new version enough to not switch. From what I've seen, that's true,
though it has a few residual problems, even almost a year after release.

What I do know reasonably well is the installation process as I've been
through that a few times now, so I'll focus on how that compares with
previous versions.

Before you start, if you have an existing installation, it's worth
checking in the "Get Windows 10" app whether you have any compatibility
issues. As far as I can tell, there's no separate checker you can run.
If, like me, you disabled that annoying application, you'll want to
re-enable it and see if there are any potential issues from any
applications or hardware you have.

## Clean installation

Clean installation is a lot simpler than when Windows 10 was first
launched, if you're claiming a free upgrade. Since the Threshold release
last year, you can simply enter your existing Windows 7/8 product key,
and that will be activated. No need to do a upgrade over an existing
installation solely to claim a digital entitlement, and then reinstall.

The installation process is very similar to that of Windows 7 and 8, and
simple enough to navigate. Boot up the installer, select language
options, choose where you want to install the operating system, wait a
few minutes and you should soon have a working Windows install.

### Drivers

In the past, even as recently as Windows 7, installing hardware was a
mess in that you'd often have to trawl badly designed hardware
manufacturer websites for several drivers you'd need to make everything
work. Often, you'd be prompted to check online for drivers, only for
Windows to unhelpfully say "sorry, go and find them yourself"
(polite paraphrasing mine).

This seems particularly backwards compared to modern Linux installs
where, at least in my limited experience, most hardware works without
much user intervention. In this respect, Windows 10 has caught up[^2].
For the PCs I've tried Windows 10 on, almost all the hardware has been
correctly detected and the drivers installed.

Even on a PC near a decade old, long since abandoned by the
manufacturer, it was a particularly pleasant surprise to find that
almost everything had been correctly installed. The main exception I
found was a Native Instruments audio interface, but I realise that's not
common hardware.

## Updates 

One of *the* major drawbacks of Windows past is the update system. A
fresh install of Windows 7 now requires in excess of two hundred
updates, which greatly extends the time to complete the install. You'll
endure reboot on reboot, until it's done. *If* it's done. Unfortunately,
it's also possible to run into failures while installing such an
inordinate number of updates; trying to install as many updates in one
go to minimise rebooting sees some phenomenal memory usage.

That wasn't helped by there only being a single service pack for Windows
7, released several years ago, so you still need all updates released
since then.

(While you can slipstream updates into Windows installers, that's not
going to be something that many users bother with.)

Here, Windows 10 seems a big improvement. Installers available from
Microsoft's site are regularly updated: the one I've used recently is
from April of this year. This means that there shouldn't be many more
updates required for your newly installed system.

On top of that, they've made the updates cumulative, so you only need
the latest to get all fixes. Furthermore, they're all rolled into a
single update, which means there's very little that a new system needs. 

The downside of this, of course, is that you can't pick and choose what
applies. The past has seen cases where rogue Windows updates can
critically break systems: [recently, in my
experience]({filename}../2016/windows-7-secure-boot.md). With Windows
10, all you can do is not apply *any* subsequent updates whatsoever
until your issue with the updates gets resolved. Relying on the
stability of a house of cards doesn't seem that wise.
 
More positively, there is an upside of the cumulative update system.
Previously — and I've encountered this firsthand for XP and Windows 7 —
as a particular Windows version grows older, Windows Update becomes far
creakier. In recent months, Windows Update has taken the best part of an
hour to check for updates on relatively modern Core i5 machines, and
hours on my ancient Core2Duo PC. If this new method of rolling out
updates avoids this, it will prevent much user frustration as the
operating system gets older, particularly if, as Microsoft claim, this
is the "last version" of Windows.

## Upgrade install

I'm not a huge fan of upgrade installs with Windows. Usually, if a full
installation is warranted, enough time has passed that it's often
worthwhile to do a clean install. In one case I dealt with, I felt it
was worth a try first as reinstalling everything would be a lot of
work[^3]. If all else failed, a clean install was still an available
alternative.

In fact, the upgrade install went without a problem. Downloading the
installer for reuse is a smart idea if you have several PCs to upgrade.
You can download a USB creator or ISO from Microsoft's site, and run
`setup.exe` within your current install to upgrade.

The whole process didn't take too long either and didn't seem to cause
any problems following it. Microsoft do blatantly ignore your existing
choice of browser and select Edge as the default for you though...
thanks for that.

## And after installation?

Despite it being out almost a year, I'm only really now starting to use
Windows 10 on a regular basis. Where possible, I'd rather hold off if I
have systems that are working well and let others find and report bugs.

Even from the outset of installation, one noticeable difference to
previous versions of Windows is the number of privacy options there are.
Microsoft are intent on collecting much more data than in previous
versions of Windows. What you should be reading is this page on
[Microsoft's site that details
telemetry](https://technet.microsoft.com/en-us/itpro/windows/manage/configure-windows-telemetry-in-your-organization)
to tell you exactly what can be disabled.

### Other problems

Several other things I don't like have emerged over the few hours I've
used Windows 10.

1. Windows 10 sees the return of the Start menu on desktops, which was
   one of the big pain points of Windows 8. What still remains is a
   slightly uneasy mix of normal applications, and universal ones. This
   particularly affects settings. For example, there are two separate
   applications you can use to remove software: that as seen in the
   traditional Control Panel and another that's a universal looking app.
   That just feels indecisive. Likewise, prompts are a mixture of old
   and new. It's not enough to be too distracting, but does feel
   unpolished.

2. Speaking of the Start menu, there are lots of things that clutter it
   by default. There are more bundled apps (for instance, Twitter,
   Skype) too which some may find useful, but I'd prefer to not have
   them installed by default. OneDrive integration might be desirable
   for some people, but not for me, so it's disabled; the simplest way
   is to go to Group Policy and disable it there.

3. The default theme is ridiculously bright. When I used it earlier this
   year, I found it felt tiring to work with over long periods. The
   Anniversary Update to be released soon finally promises to
   reintroduce an Aero-like theme, which should address that complaint.
 
4. Another problem is that using BitLocker still requires a premium
   version of Windows. I have that, so it doesn't affect me, but I don't
   understand why Microsoft count what is nowadays a fundamental
   security feature as optional. Lots of consumer laptops will only have
   the Home version of Windows which doesn't feature BitLocker.

       Since Windows 8.1, there's another encryption option called
       "Device Encryption". It's also really difficult to find useful
       documentation about this option on Microsoft's site. I did find a
       couple of more informative links on Microsoft's site: ["What's
       New in
       BitLocker"](https://technet.microsoft.com/en-us/library/dn306081(v=ws.11).aspx#BKMK_Encryption)
       and the [Windows 10 Security
       Guide](https://technet.microsoft.com/itpro/windows/keep-secure/windows-10-security-guide#information).
       The requirements are declared in the [Windows 10
       Specifications](https://www.microsoft.com/en-us/windows/windows-10-specifications#sysreqs).
       Spoiler alert:
  
       > Device encryption requires a PC with InstantGo and TPM 2.0.

       But lots of budget hardware skips on the Trusted Platform Module.
       And, I might be mistaken, that still doesn't cover securing
       removable drives for non-Pro/Enterprise users.

5. The frequent notification to "install a language to enable typing
   features" gets tiring fast. As far as I can tell, the only way to
   disable it is bowing to its demands. If you just ignore it, it
   decides to reappear at regular intervals. That's a sloppy bit of user
   interface design.

6. The issue where you need to use [the `systempropertiesperformance`
   fix]({filename}../2014/making-aero-theme-settings-stick-in.md) to
   disable animations and other visual enhancements for non-admin users
   still remains. Otherwise, changes made disappear once you log out.

## But Windows 10 is worth a try

That's a long list of complaints, but actually I'm more positive about
Windows 10 than that might suggest. My near-decade old PC with an SSD
boots Windows 10 in around twenty seconds from power on, which feels
brisk. And there's nothing I've seen yet that seems particularly
detrimental in terms of major problems or compatibility issues. Lack of
BitLocker for home users aside, there's not much in the way of major
issues.

If you've been hesitating, it's worth taking a look. Especially given
that my understanding from reading elsewhere is that the digital
entitlement may well work as follows: once you've claimed the Windows 10
free upgrade entitlement for a PC **before** the deadline, even if you
revert to your previous version of Windows, the upgrade remains valid
even **after** the deadline.

[^1]: That month is July 2016. And it holds unless Microsoft decide that
they need a greater user uptake than they have now, and announce a
deadline extension.

[^2]: I never used Windows 8 enough to know if the improvements in
driver detection were there or not.

[^3]: There was a substantial customised game installation which would
have taken a long time to install the addons all over again. The
previous upgrade strategy from XP to 7 was to copy everything over, then
reinstall whichever extras for that game required it.
