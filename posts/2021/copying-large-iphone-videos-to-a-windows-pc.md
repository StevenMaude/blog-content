Title: Copying large iPhone videos to a Windows PC
Date: 2021-01-25 20:50
Author: Steven Maude
Tags: iOS, iPad, iPadOS, iPhone, Windows
Summary: How to copy iPhone videos that don't appear in Windows File Explorer

## A simple task made complicated

This isn't a particularly interesting post. That is, unless you reading
this now, like me at the time of writing this, have spent the best part
of an hour trying to solve the same issue. Like a few other posts I've
made in the past, the purpose is really to make this easier to search
for, if others encounter the same problem.

Someone had recorded a video on an iPhone that they wanted to transfer
to a Windows PC. Naturally, they connected the phone via a USB cable to
the computer, navigated through the existing `DCIM` directories to copy
the files across and found, well, nothing. So they asked me about it.

What was going on? They used the same process before and it worked fine.
And the videos were definitely still on the phone: you could play them
there. As these videos had large file sizes, I suspected there was some
limit being encountered.

## No easy answers

Many of the workarounds posted online seem to fit one of the following
categories:

* Moving the video via iCloud, or some other uploading route. (Too slow
  and too tedious.)
* Using some other app to get the video to a PC. (May involve spending
  money and requires auditing the app to ensure it and the developers
  are reputable.)
* Re-encoding the video on the phone to a smaller size somehow, possibly
  via iMovie? (Didn't try this and may have been slow. This would have
  been the next thing I suggested if the solution below had not worked.)

The Apple documentation itself suggests making sure iTunes is installed,
using the Windows Photos app and then importing from there. This didn't
work.

### The fix

I found someone posted a fix on a forum. On the iPhone's Settings,
select Photos, and then under "Transfer to Mac or PC" setting for the
Photos app, change "Automatic" to "Keep Originals". That was it. Much
simpler than any of the other suggestions.

The import actually worked through the Photos app then. In fact, you did
not need Photos at all: checking the `DCIM` directory listed the file.

What "Keep Originals" does is take a direct copy of the photos and
videos, instead of doing some unspecified magic and converting them on
copy.

(Though not tested, iPadOS has the same setting and presumably behaves
in the same way.)

As someone unfamiliar with iOS, I'm not entirely sure how you would
connect the setting to the behaviour. But the main thing is that it
resolved a very frustrating and very badly documented issue very, very
quickly.
