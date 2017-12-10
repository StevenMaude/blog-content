Title: Upgrading Raspbian and <code>rc.local</code> failures
Date: 2017-12-10 20:13
Author: Steven Maude
Tags: Raspberry Pi, Raspbian, Linux
Summary: Using a Raspberry Pi as a wireless bridge, in-place upgrading Raspbian
         and dealing with `rc.local` not running tasks as planned.

## A Raspberry Pi as a wireless bridge for old hardware

This is something I did a couple of months back, but figure it's worth
documenting, to maybe help anyone with a similar problem search for it.

One use for my Raspberry Pi is as a wireless bridge, and this is mainly
for a now ancient Xbox 360. Yes, the one without built-in wifi, it just
has an Ethernet port for networking; not much good when your router is
nowhere near a TV.

Originally, and as is often customary when solving technology problems,
I used [instructions that I cobbled
together](https://unix.stackexchange.com/a/64353/32125) from various
places.

I'd been slack on upgrading my Raspberry Pi's Raspbian. It was working
perfectly fine for what it was doing, so there was no immediate need to
touch it. Because of this, it has languished on a distribution based on
the now aging Debian Wheezy.

More recently, with the [recent WPA2
exploit](https://www.ncsc.gov.uk/krack) in October, and the then lack of
any as-yet patch even for Debian Wheezy (which has since been patched,
not sure about Raspbian itself), I thought I should finally upgrade, so
the Pi was patched against this and any other future security issues.

I didn't particularly want to go to the trouble of doing a fresh
install, so I tried an in-place operating system upgrade, deciding that
the worst that could happen is the upgrade fails and I'd have to do a
fresh install anyway.

## The upgrade process

I actually upgraded in two stages. First from Wheezy to Jessie, and then
I figured if that went OK, I could try upgrading again, from Jessie to
Stretch too.

Upgrading the distribution actually worked well. With my Raspbian Wheezy
install, I upgraded to Jessie as described on the [Raspberry Pi
forum](https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=121880).
Everything seemed to work, including the Xbox's internet connection.

Since I was feeling brave, I decided to upgrade again. However, I didn't
feel so brave that I would do that without first backing up the working
system, so I [backed up the SD card with
`dd`](https://raspberrypi.stackexchange.com/a/312/12370) to a gzipped
image in case something went wrong and I could recover a working system
quickly.

Next, I upgraded from Jessie to Stretch. This is the same process as for
Wheezy to Jessie, just with [different repository sources
used](https://www.raspberrypi.org/blog/raspbian-stretch/).

Once again, the upgrade worked fine, the Pi booted up, and I could
connect to it wirelessly.

## A stretch too far

But, the Xbox's internet connection no longer worked. Checking the Pi, I
spotted what looked like error messages appearing at boot time.

The first problem is checking the boot log messages that quickly
disappear from the screen. Since Debian now uses systemd, you need `sudo
systemctl` to review those messages.

What I spotted there is that there was an error that indicated that
commands I had in `rc.local` were not running correctly. As mentioned,
in my [description of my Xbox and Pi
configuration](https://unix.stackexchange.com/a/64353/32125), I was
using `rc.local` to run the commands on boot that ensured the bridge
worked, instead of having to run anything by hand every boot.

That seemed strange. More so when running the script by hand caused it
to work as normal, which allowed the Xbox to once again connect to the
internet as it did on Raspbian Jessie.

Why did this script fail on boot via `rc.local`? As [mentioned on the
Raspberry Pi
forums](https://www.raspberrypi.org/forums/viewtopic.php?f=66&t=122207),
the difference presumably is that the Pi's networking isn't configured
at the time of the script trying to run. Trying to then change this
configuration when it's not ready will then fail.

So there are no guarantees about when `rc.local` is run. If you have
dependencies on other things, the moral of this longish story is that
you should create a systemd service and have systemd launch it after
everything else; this fixed the problem and everything finally was
working again.

## Configuration

For reference, here's what I have configured:

`wireless_bridge.sh` is saved in `/usr/local/sbin`, with 755 file
permissions, root as owner and group, and contains:

```sh
#!/bin/sh -e
/usr/sbin/ifplugd eth0 --kill
/sbin/sysctl -w net.ipv4.ip_forward=1
/sbin/ifconfig eth0 192.168.1.1
/sbin/iptables -t nat -A POSTROUTING -o wlan0 -s 192.168.1.0/24 -j MASQUERADE
```

`wireless-bridge.service` is saved in `/etc/systemd/system`, with 644
file permissions, root as owner and group, and contains:

```
[Unit]
Description=Wireless Bridge Service
After=multi-user.target

[Service]
Type=idle
ExecStart=/usr/local/sbin/wireless_bridge.sh

[Install]
WantedBy=multi-user.target
```

You could possibly change `multi-user.target` to one of systemd's
[network
targets](https://www.freedesktop.org/wiki/Software/systemd/NetworkTarget/),
but I didn't bother testing this out, as the configuration above just
seemed to work (with, I suppose, the possible cost of the bridged
connection not being available until slightly later).

I also have the Xbox network settings as:

IP address: 192.168.1.2  
Subnet mask: 255.255.255.0  
Gateway: 192.168.1.1  

and the primary DNS server set to my router's IP address.
