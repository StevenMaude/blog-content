Title: Stopping Fujitsu's Battery Charging Control Update Tool from crashing Windows 10
Date: 2018-12-10 21:16
Author: Steven Maude
Tags: fix, Windows
Summary: Preventing Fujitsu's Battery Charging Control Update from
         making Windows 10 crash with a blue screen error caused by
         tdklib64.sys.

(NB: There's some background here just by way of introduction. If you encounter
this problem and don't want to endure my waffling, check the setting I [mention
below](#the-fix).)

My Fujitsu laptop currently dual boots Windows and Ubuntu, but it's rare that I
boot into Windows. Nonetheless, I had a little time spare last week, I figured
I might as well catch up on things everywhere and update the Windows install.

Dropping into that did update Windows, and all well and good. Or so I thought.

# The problem

On restarting, I noticed there was a Fujitsu prompt that appeared, and was a
little unexpected. What I was being asked to install was the very precisely
named "Battery Charging Control Update Tool". It seems [Fujitsu have had some
issues with battery
quality](https://www.fujitsu.com/global/about/resources/news/notices/2018/1031-01.html),
leading to a potential fire risk; this tool is supposed to mitigate that.

It seems that, at least for my model of laptop, the tool was attempting to
update the BIOS. And you can see how the [tool *should* work on Fujitsu's Hong
Kong site](https://www.fujitsu.com/hk/support/products/computing/pc/ap/announcements/battery-control-update-tool.html)
(and that page I could only find on the Hong Kong site for some reason).

In the previous paragraph, I say *attempting* to update the BIOS, because what
happened, after the initial preparation stage occurred with the "Continue to
update BIOS?" prompt, was that shortly after I clicked "Yes", I saw a lovely
Windows 10 blue screen which I think mentioned tdklib64.sys as the cause.

There's nothing I could find relating to this failed BIOS update and these blue
screens — although there were mentions of BIOS update failures and tdklib64.sys
relating to other manufacturers machines. Finding nothing struck me as strange:
it's a fair bet that you'll find at least one person's already complained
loudly somewhere about a problem you've encountered too. 

Anyway, I rebooted and tried the update again. Same result. Blue screen.

OK then. Third time lucky, maybe? No. Just the same (reliably) unreliable
result.

# The fix

In a moment of fortunate (and rare) inspiration, I remembered that I'd turned on a
relatively new security feature — [Memory
Integrity](https://support.microsoft.com/en-us/help/4096339/windows-10-device-protection-in-windows-defender-security-center)
— in Windows Defender Security Center as I'd spotted it as a setting I'd not
enabled already. Perhaps that was the culprit, especially as no-one else seemed
to have encounter this failure yet?

Yes. Yes, it was.

Disabling that again meant the update proceeded without a problem, and then I
just re-enabled the Memory Integrity setting once again after the BIOS update
completed. If you're having a similar problem, check this setting before
attempting to update. Maybe this tip helps you avoid the hour I spent figuring
this out.
