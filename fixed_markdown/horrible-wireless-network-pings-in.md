Title: Horrible wireless network pings in Ubuntu and how to fix them
Date: 2013-11-20 18:51
Modified: 2013-11-20 18:53
Author: Steven Maude
Tags: high, ping, latency, wireless, wifi, Ubuntu
Slug: horrible-wireless-network-pings-in
Summary: A quick guide on how to fix high and variable pings when connecting to wireless networks using Ubuntu Linux.

Yesterday I had an important video call that I needed to carry out under
Ubuntu as I need to demo some of my work. About two minutes before it
was due to begin, I noticed that my pings to the home network router
were ridiculously variable and high:

```text
PING 192.168.0.1 (192.168.0.1) 56(84) bytes of data.
64 bytes from 192.168.0.1: icmp_req=1 ttl=64 time=60.3 ms
64 bytes from 192.168.0.1: icmp_req=2 ttl=64 time=82.9 ms
64 bytes from 192.168.0.1: icmp_req=3 ttl=64 time=105 ms
```

Awful.

Unfortunately, two minutes before an important call is not the time to
be tinkering with network settings, so I left it at the time.
Fortunately, it didn't seem to adversely affect the call.

Later, I booted into Windows to find my pings were perfectly normal (1
ms)[^1]. So, what's the issue under Linux?

What it turns out to be is wireless power management. You can easily
test this by trying:

```shell
sudo iwconfig wlan0 power off
```

and remeasuring the pings:

```text
64 bytes from 192.168.0.1: icmp_req=1 ttl=64 time=0.970 ms
64 bytes from 192.168.0.1: icmp_req=2 ttl=64 time=1.04 ms
64 bytes from 192.168.0.1: icmp_req=3 ttl=64 time=0.994 ms
```

Much better!

[Thanks to this forum
thread](http://ubuntuforums.org/showthread.php?t=1686641), I found an
easy way to make this fix permanent, you need to do something like:

```shell
sudo nano /etc/pm/power.d/wireless
```

and add the following lines to the newly created file:


```shell
\#!/bin/sh

/sbin/iwconfig wlan0 power off
```

Next, do:

```shell
sudo chmod +x /etc/pm/power.d/wireless
```

so that this script is executable.

Next time you reboot, the fix should still be in place.

[^1]: I have a feeling that I disabled any wireless power management on
Windows when I first installed it a few months back; it may be that
you'd suffer a similar problem in Windows too otherwise.
