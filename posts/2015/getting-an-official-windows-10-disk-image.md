Title: Getting an official Windows 10 disk image
Date: 2015-10-26 17:00
Author: Steven Maude
Tags: Windows, ISO, disk
Summary: How to get a Windows 10 ISO directly from Microsoft. No install required.

## Getting an official Windows 10 disk image, without a Windows install

Currently looking to test out installing Windows 10 and one stumbling block was
just getting hold of an official disk image. (I'm cautious these days and want
to see how setting up a dual boot encrypted Windows 10/Ubuntu goes on a spare
drive prior to actually committing to an upgrade.)

### Start me up

The obvious searches for installing Windows 10 inevitably lead you to [this
page](https://www.microsoft.com/en-gb/software-download/windows10) where it
tells you to install the Media Creation tool and use that.

Critically, that's not an option if you don't have access to a current Windows
install. (Yes, it should be easy enough to find a Windows PC *somewhere*
around, but there might not be one to hand.) The other drawback is that, as far
as I can see without testing, is that it only creates media for one particular
version of Windows, so you'd have to run through the process twice for Home and
Pro.  The actual ISO disk image is buried on the site under ["Tech
Bench"](https://www.microsoft.com/en-us/software-download/techbench).

Though the filename differed, the 64-bit download from that page *did* match
the SHA1 as listed on the MSDN site as of 2015-10-23:

```
File Name: en_windows_10_multiple_editions_x64_dvd_6846432.iso
Languages: English
SHA1: 60CCE9E9C6557335B4F7B18D02CFE2B438A8B3E2
```

Note that there's a 90-day Win10 Enterprise
[trial](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-10-enterprise),
but there was no checksum at all to verify that download, and you need a
Microsoft account just to get to the download. It also had the following
ambiguous information:

> In order to use Windows 10 Enterprise, you must sign in to your PC with a
> Microsoft account. The option to create a local account will be made available
> at the time of the final release.

which was unclear as to whether this still applies or not.

### Clean installing Windows 10

The other question I had was which version, Home or Pro, gets installed from
this single ISO. If it's a clean install, how is the version to install (Home
or Pro) determined? From what I remember reading, the answer should be that if
you skip entering a product key on request by the installer (which would
automatically install the appropriate version if you provide a key), the
installer prompts you to choose the version to install.
