Title: Windows Update locking up on XP when checking for updates: fixing the svchost.exe CPU usage problem
Date: 2014-01-04 11:27
Author: Steven Maude (noreply@blogger.com)
Tags: hog, 100%, XP, Windows, freeze, CPU, update, security, fix
Slug: windows-update-locking-up-on-xp-when

It does seem ridiculous that Windows XP has been around for quite so
long. Of course, you should be thinking about moving away from Windows
XP as soon as possible since the extended support period is ending in
April 2014, but there are still a huge number of XP machines around.
(I'm really keen to migrate the remaining machines in my care sometime
this month.)  
  
In the meantime, there's a problem with Windows Update on XP machines
which means that just *checking for updates* takes an incredibly long
time to run (if it actually completes, I've never waited that long to
see...) and causes svchost.exe to peg the CPU core it's running on at
100% usage.  
  
This is actually reminiscent of a [problem from a few years
back](http://support.microsoft.com/kb/932494), although I'm not
particularly nostalgic about it. As a result, it's a little more
difficult to find relevant search results for, unless you restrict your
searches to within the past month or year.  
  
[From the sounds of
it](http://www.infoworld.com/t/microsoft-windows/microsoft-fix-windows-xp-update-svchost-redline-issue-soon-230940),
there's something rather horrible going on behind the scenes with how
the Windows Update client actually determines which patches are
required.  
  
Microsoft have been looking into it, but not actually resolved it yet.
In the meantime, **a fix is to manually install the latest Cumulative
Security Update for whichever version of Internet Explorer is
installed.** Providing this is installed before the check for updates
happens, it removes the need for the checks that are hogging the CPU and
everything works well again. Someone's been helpfully posting links to
the latest updates in this [forum
thread](http://www.bleepingcomputer.com/forums/t/514140/svchostexe-using-100-cpu/),
otherwise you can just visit [Microsoft's TechNet
site](http://technet.microsoft.com/en-us/security/default) directly and
find the updates in the latest Security Bulletin.  
  
This will have to be carried out every month until Microsoft actually
deploy a working fix. On the other hand, at most, there will only be
another four sets of monthly updates to do this for, since April will be
the last [Patch Tuesday](https://en.wikipedia.org/wiki/Patch_Tuesday)
for XP.  
  
Just another reason (as if you needed one) to be upgrading from XP
though...
