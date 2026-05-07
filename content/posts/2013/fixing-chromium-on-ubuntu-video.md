---
title: Fixing Chromium on Ubuntu video playback issues (no video, black screen)
date: 2013-09-22T21:49:00+00:00
tags:
  - video
  - YouTube
  - screen
  - black
  - Chromium
  - Ubuntu
description: How to fix playback of online videos in Chromium on Ubuntu 12.04.
slug: fixing-chromium-on-ubuntu-video
aliases:
  - /2013/09/fixing-chromium-on-ubuntu-video.html
---
Had an issue where YouTube's HTML5 video wasn't working in Chromium on
Ubuntu 12.04 LTS, and didn't really want to install Flash Player if I
could avoid it. (HTML5 in Firefox was working fine.) All I got in
Chromium was a black screen with a spinner going endlessly,.

In the end, [the solution was as simple as missing
codecs](http://askubuntu.com/questions/331769/youtube-is-not-working):

```shell
sudo apt-get install chromium-codecs-ffmpeg-extra
```

It'll uninstall the currently installed chromium-codecs package and
replace it with this one. You might also have to restart Chromium if
it's running; it's a couple days back since I did this, so can't
remember.
