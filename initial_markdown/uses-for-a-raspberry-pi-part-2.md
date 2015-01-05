Title: Uses for a Raspberry Pi (part 2)
Date: 2013-08-31 12:07
Author: Steven Maude
Tags: server, Samba, radio, Pi, tracklisting, Raspberry, iplayer, Python, get_iplayer
Slug: uses-for-a-raspberry-pi-part-2

<div class="separator" style="clear: both; text-align: center;">
[](https://www.blogger.com/blogger.g?blogID=2392456333762205400)[](https://www.blogger.com/blogger.g?blogID=2392456333762205400)[![A
Raspberry Pi working
hard!](http://4.bp.blogspot.com/-oMu1kEop_2c/UhE77Is0OAI/AAAAAAAAAEk/oDTZDZ_jIEw/s1600/Raspberry+Pi.jpg "Raspberry Pi")](http://4.bp.blogspot.com/-oMu1kEop_2c/UhE77Is0OAI/AAAAAAAAAEk/oDTZDZ_jIEw/s1600/Raspberry+Pi.jpg)

</div>
  
In my [last
post](http://www.stevenmaude.co.uk/2013/07/uses-for-a-raspberry-pi-part-1.html),
I described a few simple, but effective uses for a Raspberry Pi. Here
are two more!   
  

* * * * *

  

### **4. File server using Samba, and media server using MiniDLNA**

The Pi makes for a useful low cost file server. I used [this
guide](http://elinux.org/R-Pi_NAS) to install Samba which enables file
shares to be accessed via Windows (and also OS X). It's pretty easy to
follow step-by-step. Following that guide, you can also attach a USB
drive, making for a cheap [network-attached
storage](https://en.wikipedia.org/wiki/Network-attached_storage) (NAS)
solution.  
  
Furthermore, you can also [install
MiniDLNA](http://www.raspberrypi.org/phpBB3/viewtopic.php?t=16352) to
allow networked media devices to easily access video and audio on the
Pi, though I've not tested this personally.  
  

### **5. get\_iplayer: for UK users (or overseas users with e.g. VPN access)**

#### **  
**

#### **What's get\_iplayer?**

[](https://www.blogger.com/blogger.g?blogID=2392456333762205400)For the
benefit of those not in the UK,
[iPlayer](https://en.wikipedia.org/wiki/BBC_iPlayer) is a
[BBC](http://www.bbc.co.uk/) service that allows users to stream
television and radio programmes for a limited time after they are
broadcast. It also lets you download them for a limited time, although
they are then bogged down with
[DRM](https://en.wikipedia.org/wiki/Digital_rights_management),
restricting how you can watch or listen.  
  
[get\_iplayer](http://www.infradead.org/get_iplayer/html/get_iplayer.html)
is a great open source project that really enhances the usefulness of
iPlayer. First of all, it downloads TV and radio shows in DRM-free
formats, allowing you to play them back on any device capable of playing
those formats, without restriction. Second, it has a really useful PVR
feature: you can queue up future programmes that are already in the
BBC's current schedule, and you can easily setup PVR searches (e.g. to
look for a specific programme title) that can be configured to run
periodically and download on any suitable matches.  

#### **  
**

#### **Installation of get\_iplayer**

I installed get\_iplayer last year on my Pi running Rapsbian; I followed
[this
guide](http://raspi.tv/2012/get_iplayer-installation-on-raspberry-pi-with-raspbian).
Since then however, it's now much easier to install and maintain\*,
apparently you only need to enter this
<span style="font-size: small;">terminal command now:</span>  
<span>sudo apt-get install get-iplayer ffmpeg atomicparsley
libmp3-info-perl</span><span>  
</span>  
For convenience, I changed the default directory that get\_iplayer saves
in so that it was within a directory that was publically shared via
Samba, using a command like  
<span> ./get\_iplayer –-prefs-add
–output=/home/shares/public/iPlayer</span>  
(Note that for all these commands, I'm assuming that you have changed
directory to whichever one get\_iplayer is installed.)  
  
<span>--prefs-add</span>, unsurprisingly, adds settings to the
get\_iplayer defaults. I also used this command:  
<span>./get\_iplayer --prefs-add --modes=best -–subtitles
--subdir</span><span> --nopurge</span>  
  
<span>[--modes=best](https://github.com/dinkypumpkin/get_iplayer/wiki/modes)</span>
downloads the HD versions of a TV programme if it is available,
<span>[--subtitles](https://github.com/dinkypumpkin/get_iplayer/wiki/documentation#wiki-Subtitles)</span>
downloads subtitles if available,
<span>[--subdir](https://github.com/dinkypumpkin/get_iplayer/wiki/documentation#wiki-Filenames%20and%20Directories)</span>
sorts programmes into subdirectories based on their title, while
<span>--nopurge</span> prevents the deletion of programmes that were
recorded more than 30 days ago.  
  

#### **Basic use**

There are [plenty of usage
examples](https://github.com/dinkypumpkin/get_iplayer/wiki/documentation)
in the documentation which is definitely worth a read and explains all
the available options. A simple usage case would be to download all TV
programmes that have "Top Gear" in the title or episode info:  
<span>./get\_iplayer --get "Top Gear"</span>  
  
By default, the type of programme is set to TV. This is equivalent to
using the command line option <span>--type=tv</span>. If you are looking
for radio shows instead, you need to specify <span>--type=radio</span>.
Alternatively, you could use <span>--type=tv,radio</span> and
get\_iplayer will search both the TV and radio programme lists.  
  
If there are several programmes with the same title (e.g. Newsnight),
you can search for all programmes first by:  
<span>./get\_iplayer "Newsnight"</span>  
  
It shows a list of matching programmes and programme numbers. When I ran
this just now, it gave me several matches, but say that I wanted the
broadcast from 01/07/2013. Among the nine matches this command gave me,
it showed:  
<span>611: Newsnight - 01/07/2013, BBC Two, News,TV, default,</span>  
  
I can then get that specific programme by just <span>--get</span>ting a
programme number instead of a title:  
<span>./get\_iplayer --get 611</span>  
<span>  
</span>  

#### **Adding searches to the PVR**

Adding searches to the PVR is very similar to downloading available
shows. As the documentation shows, instead of the <span>--get</span>
option, you use <span>--pvr-add</span>:  
<span>./get\_iplayer --pvr-add=Top\_Gear "Top Gear" </span>  
  
This adds a search named Top\_Gear which looks for programmes with Top
Gear in the title or episode info. This doesn't actually do anything
until the PVR searches are executed by the command:  
<span> ./get\_iplayer --pvr</span>  
  
Supposing that we grew tired of Clarkson, Hammond and May's shenanigans,
we can remove the PVR search entirely by <span>--pvr-del</span>:  
<span>./get\_iplayer --pvr-del=Top\_Gear</span>  
or if we weren't so sure, we could use <span>--pvr-disable="Top
Gear"</span> to disable the search and <span>--pvr-enable="Top
Gear"</span> to re-enable it at a later date.  
  
Further PVR management options are listed in the
[documentation](https://github.com/dinkypumpkin/get_iplayer/wiki/documentation#wiki-PVR%20Usage).
Additionally, there is also a [web PVR
interface](https://github.com/dinkypumpkin/get_iplayer/wiki/webpvr), if
you prefer that to using the command line to manage the PVR, although
it's advised to have it running on trusted networks for security
reasons.  
  

#### [](https://www.blogger.com/blogger.g?blogID=2392456333762205400)**Scheduling the PVR to run**

<div>
**  
**

</div>
<div class="separator" style="clear: both; text-align: center;">
[![image](http://4.bp.blogspot.com/-XLadcq2QJCU/UhE8YuaARCI/AAAAAAAAAEo/VXNN_t7pfiI/s1600/get_iplayer_crontab.png)](http://4.bp.blogspot.com/-XLadcq2QJCU/UhE8YuaARCI/AAAAAAAAAEo/VXNN_t7pfiI/s1600/get_iplayer_crontab.png)

</div>
<div>
**  
**

</div>
<div class="separator" style="clear: both; text-align: center;">
[](https://www.blogger.com/blogger.g?blogID=2392456333762205400)

</div>
#### <span style="font-weight: normal;">However, it is more convenient to run the PVR regularly rather than have to run it manually. You can add the command to run the PVR to the [cron task scheduler](https://en.wikipedia.org/wiki/Cron). Scheduling tasks by cron is carried out by entering <span>crontab -e</span> and then editing the file to start the job.</span>

I had a problem where I could run the command <span>get\_iplayer --pvr
</span>and the PVR would work fine from a terminal window, but it failed
when running via cron. This was fixed by finding the contents of my
current PATH variable (by typing <span>echo $PATH</span> into the
terminal) and then copying this into a line in my crontab that started
<span>PATH=</span>.  
  

#### **Why I think the PVR is great**

What's awesome about the PVR function is that *the search terms are
persistent*. If the PVR is looking out for a particular show, you don't
even need to keep an eye out for when your favourite shows start a new
series, in case you forget to record it. The PVR feature will
automatically catch them for you, without you thinking about it.  
  

#### **Custom commands after downloading recordings**

This is another useful feature of get\_iplayer. <span>--command</span>
runs custom commands after downloading a recording and can pass various
bits of information to those commands as arguments. Because of this
feature, it's easy to *use your own scripts to process your
recordings*.  
  

#### **Example: automatic downloading of radio tracklistings**

Sometimes I'll hear a track that a DJ plays on a radio show and I'll
want to make a note of it to look it up later. It's not always that easy
to do, occasionally they neglect to mention the title and artist, which
can be frustrating when you've heard something amazing.   
  
At least these days tracklistings are usually posted online, but if I'm
listening on my iPod Nano (running [Rockbox](http://www.rockbox.org/)),
this means I still need to dig out my phone, fire up a web browser and
look it up. It's much easier if the tracklisting is stored together with
the radio show for quick reference.  
  
To automate this, I wrote [a Python script that downloads BBC
tracklistings](https://github.com/StevenMaude/bbc_radio_tracklisting_downloader/)
(bbc\_tracklist.py). Once a radio show has been downloaded using
get\_iplayer, the corresponding tracklisting is saved to a text file in
the same directory.  
  
All the bbc\_tracklist.py script needs to know is the programme id,
which get\_iplayer can pass through to it as <span><pid\></span>. For
example:  
./<span>get\_iplayer --get "Gilles Peterson" --type=radio --command
"/home/get\_iplayer/bbc\_tracklist.py <pid\> <dir\>
<fileprefix\>"</span>  
  
My script optionally takes arguments of the directory (to store the
tracklisting with the downloaded show) and a filename (to give the text
file the same base filename). These are provided by get\_iplayer via
<span><dir\></span> and <span><fileprefix\></span>.  
  
It also works in the same way with PVR searches.  
<span>./get\_iplayer --pvr-add=Benji\_B --type=radio "Benji B" --command
"/home/get\_iplayer/bbc\_tracklist.py <pid\> <dir\>
<fileprefix\>"</span>  
  
Once this has been setup in a radio PVR search, you can forget about the
script entirely. It should execute automatically everytime a show has
been downloaded.  
  

#### **<span style="font-weight: normal;">**Conclusion**</span>**

get\_iplayer does its job superbly well. It has many useful features and
seems very stable. Comparing get\_iplayer to the TV tuner my main PC has
installed, get\_iplayer has been used much more for "recording".  
  
Why should this be? It doesn't matter if you miss a show with
get\_iplayer since you can still download it several days after
broadcast and, with the PVR feature, you probably won't miss it. This
isn't possible with a TV card if you missed the only broadcast.
get\_iplayer also circumvents entirely the problems I occasionally have
with my TV signal. Combined with a Samba or miniDLNA setup described
above, you can leave the Pi running to periodically save programmes and
then either playback files across the network or copy them to another
device. Finally, shows downloaded by get\_iplayer are ready to playback
on many devices immediately; this isn't always the case with TV captures
which might require some post-record processing.  
  
Of course, I should mention that, since the video formats are
unencumbered with DRM, it's possible to play them with, of course,
[Raspbmc](http://www.raspbmc.com/). :)  
  
<span style="font-size: xx-small;">\*(That should also help keep it up
to date as it should be upgraded when you run a <span>sudo apt-get
upgrade</span>; my install is currently manually updated by running
<span>./get\_iplayer --update</span> in the install directory.)</span>  
  

* * * * *

  
So, there you have it. Five handy uses for a Raspberry Pi. If I find
further uses for my Pi, I'll definitely be writing about them. In the
meantime, feel free to let me know via a comment what you're using your
Pi for!

</p>

