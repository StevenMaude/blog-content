Title: Still rocking Rockbox
Date: 2016-12-10 23:06
Author: Steven Maude
Tags: open source, Rockbox
Summary: Explaining why Rockbox is my portable audio player software of choice, and how you can try it out.

In the days of the iPod, when travelling on public transport, in the UK
at least, those trademark white earphones were everywhere. But it seems
that portable audio players have become a thing of history; with the
advent of phones as all-in-one devices, these have pretty much replaced
audio players (and cameras too). Why carry extra devices when the one
you've already got in your pocket will do?

Returning back to those past days, I'd put up with a couple of very
cheap MP3 players, which would often glitch in all kinds of infuriating
ways. That ranged from failing to read certain MP3s, going further in
their obstinance and just locking up entirely, or further still and
actively protesting noisily. I'm not sure that "randomly firing a loud
burst of white noise into my ears until power off" is a particular
bullet point to stick on the box blurb.

Fortunately, it didn't take long before I'd spotted Rockbox, a open
source replacement firmware for audio players. Since then, Rockbox has
become one of the open source projects that I use most. I've used it
near daily on some device or other for probably around a decade, and I
don't see that changing anytime soon.

## Easy listening

As an audio player is one of the things I'm using all the time, I like
having a separate device with its own, usually lengthy, battery life.
With that in mind, I'm probably a little ignorant if there's phone audio
player software that's as competent and fully featured as Rockbox. It's
certainly possible there's a suitable competitor. But I'd be surprised.

In terms of the range of audio formats supported and the number of
features Rockbox offers, it seems difficult to match. There's gapless
playback, bookmarking, equalizer, compressor, crossfeed, control of
pitch and speed, and ReplayGain support. On top of that, adjusting many
aspects of a Rockbox-enabled device is possible. Even the display theme
is fully customisable should you wish to create your own.  Furthermore,
if a device has the option of adding external media card storage, such
as microSD, Rockbox sometimes goes beyond a device's official support,
enabling the use of larger memory cards.

## Installing Rockbox

If you want to give it a try, the first step is to take a look at the
[official site](https://rockbox.org) and see what devices are currently
supported. It's also worth checking around the forums there too,
particularly under "New Ports" as there may be newer devices where less
stable ports-in-progress are available, but not listed on the main site.

Devices that run Rockbox are commonly fairly cheap as it's usually
older, out of demand hardware that's supported. It does mean getting
hold of one in good condition might not be necessarily easy. I've used
Rockbox on several different devices, first and second generation iPod
Nanos, and the Sansa Fuze and Fuze+. There have been devices I have
preferred, but most devices are quite usable since once you've selected
what to play, there's little more to do. The main differences really
come down to screen size, ease of accessing the user interface (for
instance, the Fuze+ has a touch sensitive pad which isn't ideal compared
with the definite precision of the iPod Nano or Fuze wheels), and
whether a device supports storage expansion.

When you've got a compatible device, it's relatively straightforward to
get things going. The Rockbox Utility is a program that you can use to
install Rockbox directly to hardware that's plugged into your PC, or you
can install manually if you prefer, although it may involve using a
compiler. The actual installation process varies depending on hardware,
for instance, you may also have to download some official firmware file
for your hardware first so that it can be patched to add Rockbox. After
that, you should be ready to copy files onto your player's storage and
start using it.

On a security point: when I last used the Rockbox Utility, only a few
weeks back, it was using insecure HTTP URLs for downloading from the
site. This is despite the download servers the Utility downloads files
from during installation actually supporting HTTPS. I don't have the
changes I made to hand, but it's possible to use your favourite
find-replace tool to patch the source to replace URLs that match, for
example (but not limited to) http://download.rockbox.org to use HTTPS. I
really should have submitted a patch but I couldn't face the hassle of
creating a account to access Rockbox's Gerrit instance at the time.

## The future?

What's the long, long term future of the project? If you've hardware for
which Rockbox is claimed to be stable, you'll probably find that's the
case. I've had devices occasionally lock up, but these haven't happened
frequently enough to be frustrating. As mentioned above, it's as
feature-filled as you'd likely require too, so even if development
stopped on it entirely it would still continue to be usable too.
Nonetheless, it's still actively maintained with a steady run of code
changes being made.

You're limited to what devices you can install Rockbox on, but these
were often produced in large quantities (e.g. iPods) so there should be
an abundance of them on the market. All this makes it relatively simple
to pick up a working used one to install Rockbox. For now. Getting hold
of one of these is unlikely to be a problem as there are so many out
there, but getting one in good working order may prove increasingly
difficult as time goes on. If it's a failed battery that's a problem,
it's probably easy to get a replacement, although replacing the battery
may prove trickier: these devices weren't often designed to be
user-serviceable.

There has been work on making Rockbox an Android app. Ultimately, that's
likely the way things will go in the far distant future as old audio
hardware becomes scarce and fewer new devices are designed and
manufactured. In the meantime, it's nice to have software that does one
thing and does it particularly well. As nothing better seems to have
come along to usurp Rockbox's place, it's quite possible that I'll be
using it over the next ten years as I have for the last ten.
