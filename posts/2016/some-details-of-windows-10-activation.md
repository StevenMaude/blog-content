Title: Answers to some Windows 10 activation questions
Date: 2016-01-12 22:23
Author: Steven Maude
Tags: Windows, activation
Summary: Some details of Windows 10 activation post-Threshold 2 release.

With a Windows 10 1511 Threshold 2 ISO that I downloaded (using the
[source I've previously
described]({filename}../2015/getting-an-official-windows-10-disk-image.md)),
I was recently testing out Windows 10.

The Threshold 2 release was the first major release of Windows 10 since
launch and was made available in November 2015. Previously, the route to
claiming the free Windows 10 upgrade from an existing version of Windows
was to do an in-place upgrade from a current install. The Threshold 2
release changes this so that you can enter a Windows 7 or 8 product key
on a clean install of Windows 10 and successfully activate it.

But I still had a lot of questions about how the activation process
worked and, probably because Threshold 2 is still fairly new, I couldn't
find much to tell me how this was actually going to work out. Here's
what I learned.

## What happens if you clean install Windows 10 on a PC with an embedded Windows licence?

These days, Windows licences for mass produced consumer systems are
usually included in the BIOS itself, rather than printed on a sticker.

What the Windows 10 install does is automatically installs and activates
the corresponding Windows 10 version if your hardware has an embedded
licence. (Pro if your laptop had a Win 7 Pro/Ultimate or Win 8 Pro
licence, or Home if you had a Win 7/8 Home licence.)

I suspect that this is still counted as part of the free upgrade
entitlement rather than offered in perpetuity, so won't be an option
once Microsoft's free upgrade offer expires in July 2016. You'll
probably have to pay for an upgrade then.

## Can you use a Windows 8/8.1 Pro Pack key to claim a Windows 10 Pro upgrade?

Yes. You can go to "change product key" and try entering your key, but
you'll probably see the error `0xc004f210`.

This is because you're on Home, not Pro, so the key's not valid for that
version of Windows.

What works instead is to use the [generic Pro
key](https://answers.microsoft.com/en-us/windows/forum/windows_10-windows_install/windows-10-pro-becomes-home-after-reinstallation/f1d7d4e5-cdf6-4fd7-b0e7-f87084b73df8)
which will then install the Pro upgrade. Your Windows install will then
show as not being activated as it only had a Home licence.

Now, entering that Pro Pack key should activate without any problem, I
think, provided that it was previously used on the same hardware.

Clarifying this with how this worked for me might help explain this
process if it's still somewhat unclear. My laptop had a Windows 8 Home
licence which got upgraded to Windows 10 Home automatically on install.
Then, I changed the product key to the generic Pro key. Following the
Pro upgrade, the Windows 8 Pro Pack key that I'd previously used on the
same laptop activated Windows 10 Pro.

## Can you clean install Windows 10 Pro on a laptop which has an embedded Home licence?

Once you've activated Windows 10, you get a digital entitlement. Any
product key you first used to activate is no longer needed: in future,
the Windows activation servers just check your hardware and see that you
have a valid licence.

The issue here is that — **even if your hardware has a entitlement for
the Pro version** — if the hardware has a key for a Home version, that
will be recognised on install and you'll end up with a Home version
install.  You'd then have to enter the generic Pro key and hopefully
your PC should activate without a problem then, since it should have the
digital entitlement.

This is inconvenient: it does mean you don't get a clean Pro install,
but one that's upgraded from Home to Pro (though in practice there's
probably little difference between these two routes).

I haven't tested this, but as far as I can tell, the solution is to
[modify the installer disk
image](https://technet.microsoft.com/en-us/library/hh824952.aspx) with a
text file that contains a product key. If you use the generic Pro key,
you should get the Pro version installed.

From there, you could enter your Windows 7/8 product key as described
above or, if reinstalling, the digital entitlement should allow you to
activate without entering any product key.

## First impressions of Windows 10

So far, I've noticed that the start menu is an improvement on Windows 8,
but not as good as the one in Windows 7, the default theme is awful to
look at compared with Windows 7's Aero — it's far too white and bright,
with very little contrast in Explorer and Control Panel windows — and
that there are lots of telemetry tracking and unwanted bundled software
(e.g. OneDrive) to remove. There is a [Microsoft guide on how to do
so](https://technet.microsoft.com/en-us/library/mt577208%28v=vs.85%29.aspx).
Set aside some time. It's a lengthy read.

Activation confusion aside, Windows 10 installed without a problem. The
installation process has been streamlined to require very little
interaction beyond picking install language. Another pleasant surprise
was that every piece of built-in laptop hardware had drivers installed
automatically which saves a lot of delving into badly designed
manufacturer websites to retrieve them. Even on Windows 7, a clean
install would usually result in a lot of small pieces of hardware having
missing drivers. And, in the brief testing I've done running Traktor,
Windows 10 seemed stable enough.
