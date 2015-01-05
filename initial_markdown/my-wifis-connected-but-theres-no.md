Title: My wifi's connected, but there's no internet...? (Intel Centrino versus Ubuntu)
Date: 2014-07-29 23:15
Author: Steven Maude
Tags: connection, Centrino, wifi, Ubuntu, Intel, fix
Slug: my-wifis-connected-but-theres-no

### Intel Outside (of my own office)

One thing I've never had too much of a problem with on my Ubuntu 12.04
LTS install is networking. There's been the odd time when it's refused
to connect to the network, despite everything else being fine. This has
always been fixed with a reboot, though.

The problem I experienced today was a lot more serious. I'd travelled to
another office to work and tried to connect to their wifi. I knew the
network should have been OK as no-one else seemed to be having an issue,
and I'd entered the WPA password correctly.

<a name="more"></a>

What I saw was that the wifi showed as connected, but I couldn't connect
to anything. Occasionally, I could try and ping a server, and when I
bothered to wait long enough to see anything, what I saw was connection
timeouts, horrible packet loss, and ping times of several **seconds**.
(Pings are normally measured in milliseconds; I was seeing results of
**thousands** of milliseconds.)

I'd never seen this problem before. It quickly became apparent that this
was specific to my hardware and my Ubuntu install. When I booted into
Windows, it connected immediately without any problem, and a colleague
was using a later version of Ubuntu on different hardware without a
problem at all.

It's certainly difficult to try to fix such a vague problem. Running
searches like "wifi not connecting on Ubuntu" inevitably brings up much
noise relating to every wireless problem out there and not anything much
of relevance, but I didn't have a lot more to go on. Having to do lots
of searching and skimming through web pages using a phone to search
isn't ideal either, but it did eventually lead me to the right answer.

### Fun with `iwlwifi`

What worked was searching for issues relating to the wifi driver
(`iwlwifi`). A common theme that came up was `11n_disable=1` which is a
modprobe option that disables the wireless N feature of the Intel
wireless adapter. (`lshw -C network` states the model is "Centrino
Wireless-N 2230".)

By running the commands

<div class="bgcode">
`sudo rmmod iwldvm`

`sudo rmmod iwlwifi`

`sudo modprobe iwlwifi 11n_disable=1`

`sudo modprobe iwldvm`

</div>
I got normal wireless access back (minus wireless N speeds, but the
choice between fast, but no wifi and slow wifi is not a difficult one to
make).

The `rmmod` commands remove the modules from the kernel, while
`modprobe` adds them. We need to readd the wifi module with wireless N
disabled. (The offending module is `iwlwifi` but I couldn't `rmmod` it
until I'd removed `iwldvm` as trying to do so showed that `iwldvm` was
using `iwlwifi`. There is a force option for `rmmod` but it didn't seem
sensible to use it when there was an alternative.)

### Making this fix stick

If you want this fix to apply every time you boot, you can just create a
new `.conf` file:

`/etc/modprobe.d/wireless-n-fix-iwlwifi.conf`, adding just this line to
the file:

<div class="bgcode">
<p>
`options iwlwifi 11n_disable=1`

</div>
</p>
(Thanks to this [nice
summary](http://askubuntu.com/questions/119578/how-to-fix-slow-wireless-on-machines-with-intel-wireless-cards).)

You can choose any valid filename you like, provided it ends in `.conf`;
you'll also need to edit this using `sudo` and your favourite text
editor.

### Why hadn't I seen this problem before?

What seems to be the issue is that I think that the office was using a
wireless N router, and there's some kind of issue with this for the
Intel Centrino wireless network adapter on my laptop under Ubuntu.

Nowhere else I've been with this laptop seems to be using wireless N, so
that explains why it was an issue for the first time today. It's pretty
poor that this seems to have been a [long-running
problem](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/1034740)and
yet it's still present... but at least there's a workaround.

</p>

