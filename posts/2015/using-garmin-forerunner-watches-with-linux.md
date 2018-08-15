Title: Using Garmin Forerunner watches with Linux
Date: 2015-12-30 23:30
Modified: 2016-09-16 23:40
Author: Steven Maude
Tags: Garmin, Forerunner, Linux, GPS, running
Summary: A quick look at Garmin's Forerunner 15 watch and using it with Linux.

!!! article-edit ""
    Edit September 2016: What I didn't mention here was how you could
    get EPO data when on Linux. This can help reduce the time it takes
    for your watch to get a GPS signal lock. There's a helpful
    [blog post](https://www.kluenter.de/2014/03/23/garmin-ephemeris-files-and-linux.html)
    that gives a lot of the details. There's a
    [Ruby utility](https://github.com/scrapper/postrunner/) that manages
    FIT files and features an option to collect the EPO data from
    Garmin's servers. Alternatively, I also wrote a [Go
    program](https://github.com/StevenMaude/armstrong) (which
    just compiles to a single binary rather than needing lots of
    dependencies) to collect this data which I've been using on Linux;
    you should be able to compile it easily to work on OS X or Windows.

I'm now the owner of a Garmin GPS watch. When I was looking at GPS
watches, I couldn't find a huge amount of information on using them with
Linux. This post concerns the Forerunner 15 (FR15) particularly, but
think may well apply to several others in that range that function as
USB storage devices, with the usual "your mileage may vary" caveats.

## Can you use it with Linux?

Yes, to some extent. Though you won't be able to use all the fancy
display features on Garmin's site. That said, I'm not bothered about
that and would actually prefer to keep my data offline, especially with
the number of website data breaches there have been recently.

The FR15 shows up as a normal USB storage device so you can copy over
.FIT files from the watch directly and work with them on your computer.
My run data was stored in `GARMIN/ACTIVITY`.

Note that, when researching this, you may read older posts about the
unofficial Garmin Communication web browser plugin that was capable of
uploading data to Garmin's servers.  This no longer functions and [this
GitHub issue](https://github.com/adiesner/GarminPlugin/issues/14)
suggests it won't be fixed anytime soon.

### Installing GPSBabel

The next job is to get the FIT files into a format that's more widely
usable.

[GPSBabel](https://www.gpsbabel.org/) is a application for Windows, OS X
and Linux that lets you convert between GPS data formats, including
converting Garmin's FIT (Flexible and Interoperable Data Transfer)
format into .GPX (GPS Exchange Format) which is well supported by
various free, open source applications.

Support for FIT was added to GPSBabel in versions 1.4.3 and later,
judging from the [GPSBabel
changelog](https://www.gpsbabel.org/changes.html).

If your distribution's repositories have an older version, you'll need
to compile it from source. In Ubuntu, it was reasonably straightforward
to clone it from [GitHub](https://github.com/gpsbabel/gpsbabel) and then
do the following:

```sh
./configure --prefix=$HOME/.local
make
make install
```

Using `prefix` in `configure` allows you to [install to a local
directory](https://unix.stackexchange.com/a/42569) and avoids the need
for `sudo` in `make install`.

The only hiccup was that the `configure` step gave the error message:

```console
configure: error: Qt4 or Qt5 is required, but neither was found
```

[The fix](https://stackoverflow.com/questions/16607003/qmake-could-not-find-a-qt-installation-of)
was to do the following:

```sh
sudo apt-get install qtcreator
```

which was probably overkill as it installed a lot of packages, but
compiling then worked. (I then removed `qtcreator` via `apt-get
remove`.)

### Converting Garmin's FIT data to GPX

An example use of GPSBabel is:

```sh
gpsbabel -i garmin_fit -f input.FIT -o gpx -F output.gpx
```

This gives you a GPX file which can be loaded into far more software. 

As a quick test, I loaded the output GPX file into
[Viking](https://github.com/viking-gps/viking) which seems a
little bit limited, but at least let me visualise speed against time,
and see where I've been.

There are web apps out there that will save you this hassle and do the
conversion for you, but, again, I'd rather keep my location data to
myself.

(Some of the high-end watches also have the ability to send the data to
Garmin via Bluetooth to mobile apps that collect the data, so that's
another way you could avoid the requirement for Windows or OS X.)

### Upgrading the watch's firmware

My watch came with the latest firmware installed and the watch has been
out a while, so I doubt there are any major issues remaining. But, there
may still be further updates as it's still a supported product.

The official update method is via Garmin's Windows or OS X software. If
you search their site, you can find that updates exist, but you're told
to use Garmin Express to install them.

However, it is possible to find download URLs for firmware updates, if
you look in the HTML source. For instance, the [current FR15
firmware](http://download.garmin.com/software/Forerunner15_270.rgn) is
available via direct download using any client you like, albeit via
insecure http. (I haven't tested the official software, it may well use
the same links.)

I haven't needed this information yet, but there are [more details
regarding a different
model](https://forums.garmin.com/archive/index.php/t-103787.html) on the
Garmin forums, but may well be relevant here. As a post there states,
you may need to remove 60 bytes of an extraneous header using `tail`:

> To verify that an original file needs this header-removing, open it
> with `hexdump -C [Download FileName] | head`. You should see it
> starting with the string KpGrd The main watch firmware has two of
> those KpGrd headers, but we only remove the first one.

Also bear in mind that there may be multiple firmware files to update,
e.g. the watch firmware itself, as well as language files and the ANT
firmware. And apparently *all* these need the header removing. Anyway,
you can search Garmin's site for e.g. "Forerunner 15 update" and see
what you find.
 
## What's the watch actually like?

I've only started using it today, but it seems good at what it does. I
tracked a run and, at a glance, the data looked consistent with where
I'd been and how I'd run.

It's a basic model, but capable. It's got what seems like a decent
battery, apparently eight hours in active GPS use. Anecdotally, I headed
out taking it straight from the box without charging and it was flashing
an empty battery warning for most of the run (an hour or so), but still
managed to record the entire distance.

It's also waterproof which was handy since I was caught up in a heavy
downpour while out. And it didn't feel noticeably less comfortable or
more cumbersome than the (near-weightless) Casio digital watch that I'm
usually wearing.

There are also activity tracker features available to count steps and
calories, though I'm less concerned about those. Recording a run for
later inspection, tracking my heart rate, distance travelled and time
elapsed while running, and keeping my best times are the features I
really want. And the FR15 does all of these things.

The FR15 was on offer when I bought it. Would I have paid the full
retail price? I don't know. At that price and adding on an optional
heart rate monitor bundled, it's very similar in price to higher-end
watches like Garmin's 225.

On the other hand, I did look into more expensive watches and all of
them, at least the Garmin watches, seemed to have drawbacks. There
wasn't an obvious candidate that stood out as the one to get.

As a starter watch, the FR15 seems like a good deal, especially as it
seems we're in a time where the technology's still improving. (Perhaps
indicative of that, Garmin, much to the chagrin of unlucky purchasers,
released a newer version of their FR225 only a few months after they
launched it.) There's also competition from the likes of Fitbit and
Jawbone which will probably push improvements to these devices in
future. Newer, more expensive watches are already switching over to
wrist monitoring of heart rate instead of using more traditional heart
rate bands.

So, if this is technology that I use long term, then the next step would
be to a watch featuring wrist heart rate monitoring and cadence
measurement. Nonetheless, the expandability of the FR15 is a bonus: you
can use a separate ANT heart rate monitor (it optionally is bundled with
one), as well as a footpod. Excluding these extras keeps the price down,
but it's still possible to augment the device with these features in
future; I've already ordered a heart rate monitor.

The one downside of the design I've seen so far is that I think the
battery will be a chore to replace when it expires. It's not officially
user-replaceable. That drawback aside, it seems a decent choice.
