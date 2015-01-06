Title: Ensuring scheduled cron jobs are run using anacron
Date: 2014-01-31 12:59
Modified: 2014-01-31 16:38
Author: Steven Maude
Tags: Raspbian, anacron, Pi, Linux, Raspberry, cron, schedule
Slug: ensuring-scheduled-cron-jobs-are-run
Summary: Using anacron to make sure that cron jobs are actually executed for Linux installs where the machine is not running 24/7.

So, I was tinkering around with my [Raspberry
Pi](http://raspberrypi.org) (running Raspbian) over SSH and in doing so
found that when I was looking up info about commands using
`man`
that although
`man`
was still running perfectly fine, I was getting this
message:

```text
man: can't resolve /usr/share/man/man6/LS.6.gz: No such file or
directory
```

The fix is actually a [simple
one](http://ubuntuforums.org/showthread.php?t=1813609); just run
`sudo mandb` which updates `man`'s
database caches. Looking more closely, I found that a `mandb`
job was actually in cron.daily which means that it should run daily.
However, when I checked the syslog with:

```
grep cron.daily /var/log/syslog
```

there were no results indicating it hadn't actually run! **The reason
for this is that my Pi's not switched on long enough for the cron job to
run.** I usually leave it on for a couple of hours and then shutdown
once I've finished with it.

## Installing anacron is the solution!

If you install anacron:
`sudo apt-get
install anacron`, you should find an
`/etc/anacrontab`
containing lines like:

```shell
1 5 cron.daily run-parts --report /etc/cron.daily
7 10 cron.weekly run-parts --report /etc/cron.weekly
@monthly 15 cron.monthly run-parts --report /etc/cron.monthly
```

This means that anacron is going to run the jobs in
`/etc/cron.daily`, `/etc/cron.weekly` and `/etc/cron.monthly`.
It should do this at boot up by default (you can check `/etc/init.d/anacron`).
There's then a user-specified delay before anacron runs each task; here,
it's 5 minutes for `/etc/cron.daily`, 10 minutes for `/etc/cron.weekly`
and 15 minutes for `/etc/cron.monthly`.
If you then restart and wait five minutes or so, then do:

```shell
grep cron.daily /var/log/syslog
```

should show lines like:

```text
Jan 31 10:28:02 raspberrypi anacron[2105]: Will run job `cron.daily' in
5 min.
Jan 31 10:33:21 raspberrypi anacron[2105]: Job `cron.daily' started
Jan 31 10:33:21 raspberrypi anacron[2692]: Updated timestamp for
job `cron.daily' to 2014-01-31
Jan 31 10:33:29 raspberrypi anacron[2105]: Job `cron.daily' terminated
```

This shows that anacron is doing exactly what we want: running the
cron.daily job five minutes after we boot. It wasn't that obvious to me
how the existing cron scheduler interacts with anacron (nor that easy to
search for) but [this
site](http://www.tuxradar.com/content/automate-linux-cron-and-anacron)
gave a very clear and helpful explanation of how the two interoperate.
