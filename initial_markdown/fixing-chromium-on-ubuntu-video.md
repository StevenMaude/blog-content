Title: Fixing Chromium on Ubuntu video playback issues (no video, black screen)
Date: 2013-09-22 21:49
Author: Steven Maude
Tags: video, YouTube, screen, black, Chromium, Ubuntu
Slug: fixing-chromium-on-ubuntu-video

Had an issue where YouTube's HTML5 video wasn't working in Chromium on
Ubuntu 12.04 LTS, and didn't really want to install Flash Player if I
could avoid it. (HTML5 in Firefox was working fine.) All I got in
Chromium was a black screen with a spinner going endlessly,.  
[  
](http://askubuntu.com/questions/331769/youtube-is-not-working)In the
end, [the solution was as simple as missing
codecs](http://askubuntu.com/questions/331769/youtube-is-not-working):  
<span style="background-color: #f3f3f3;"><span>sudo apt-get install
chromium-codecs-ffmpeg-extra</span></span>  
  
It'll uninstall the currently installed chromium-codecs package and
replace it with this one. You might also have to restart Chromium if
it's running; it's a couple days back since I did this, so can't
remember.
