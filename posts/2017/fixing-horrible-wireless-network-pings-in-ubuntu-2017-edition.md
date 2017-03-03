Title: Fixing horrible wireless network pings in Ubuntu (2017 edition)
Date: 2017-03-03 16:44
Author: Steven Maude
Tags: high, ping, latency, wireless, wifi, Ubuntu
Summary: How to disable wifi power management in Ubuntu. Again.

Today I was using my laptop on battery power and I remembered that I
hadn't disabled wifi power management since I reinstalled Ubuntu in
late 2016. With power management enabled for wifi, I find I get laggy
internet on battery power, and pings are noticeably higher.

If you suspect this is affecting you, it's easy to check:

```sh
$ iwconfig 2> /dev/null | grep "Power Management"
Power Management:on
```

Unfortunately, the [method I wrote about
previously to disable wifi power
management]({filename}../2013/horrible-wireless-network-pings-in.md) no
longer works. My guess is that this is due to Ubuntu switching to
systemd in 2015.

Instead, you need to use an alternative approach as [suggested in this
post](https://gist.github.com/jcberthon/ea8cfe278998968ba7c5a95344bc8b55).

First, look at your existing configuration:

```sh
$ cd /etc/NetworkManager/conf.d/
$ ls
default-wifi-powersave-on.conf
$ sudo cp default-wifi-powersave-on.conf wifi-powersave-off.conf
```

The new .conf filename must follow any other files alphabetically, in
this case the filename must be one that's alphabetically later than
`default-wifi-powersave-on`, so that it gets applied last, and your
modified setting overrides the default. If we named this file, e.g.
`a-wifi-powersave-off-config.conf`, our new settings wouldn't apply
since the filename would then be ahead of
`default-wifi-powersave-on.conf` alphabetically.

Now, edit the new file:

```sh
$ sudoedit wifi-powersave-off.conf
```

Change what is likely a 3 in the `wifi.powersave` line to 2. This
disables wireless power management.

It likely will look like this when you've edited it:

```text
[connection]
wifi.powersave = 2
```

Now, restart NetworkManager and you should see that this change is now
in effect. It should also persist across reboots. You can confirm this
again with `iwconfig`:

```sh
$ sudo systemctl restart NetworkManager
$ iwconfig 2> /dev/null | grep "Power Management"
Power Management:off
```
