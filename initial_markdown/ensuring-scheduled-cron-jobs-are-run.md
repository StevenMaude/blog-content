Title: Ensuring scheduled cron jobs are run using anacron
Date: 2014-01-31 16:38
Author: Steven Maude
Tags: Raspbian, anacron, Pi, Linux, Raspberry, cron, schedule
Slug: ensuring-scheduled-cron-jobs-are-run

So, I was tinkering around with my [Raspberry
Pi](http://raspberrypi.org) (running Raspbian) over SSH and in doing so
found that when I was looking up info about commands using
<span style="font-family: Courier New, Courier, monospace;">man</span>
that although
<span style="font-family: Courier New, Courier, monospace;">man</span>
was still running perfectly fine, I was getting this
message:<a name="more"></a>

<div class="bgcode">
man: can't resolve /usr/share/man/man6/LS.6.gz: No such file or
directory

</div>
The fix is actually a [simple
one](http://ubuntuforums.org/showthread.php?t=1813609); just run
<span style="font-family: Courier New, Courier, monospace;">sudo
mandb</span> which updates
<span style="font-family: Courier New, Courier, monospace;">man</span>'s
database caches. Looking more closely, I found that a
<span style="font-family: Courier New, Courier, monospace;">mandb</span>
job was actually in cron.daily which means that it should run daily.
However, when I checked the syslog with:

<div class="bgcode">
grep cron.daily /var/log/syslog

</div>
there were no results indicating it hadn't actually run! **The reason
for this is that my Pi's not switched on long enough for the cron job to
run.** I usually leave it on for a couple of hours and then shutdown
once I've finished with it.

### Installing anacron is the solution!

If you install anacron:
<span style="font-family: Courier New, Courier, monospace;">sudo apt-get
install anacron</span>, you should find an
<span style="font-family: Courier New, Courier, monospace;">/etc/anacrontab</span>
containing lines like:

<div class="bgcode">
1 5 cron.daily run-parts --report /etc/cron.daily7 10 cron.weekly
run-parts --report /etc/cron.weekly@monthly 15 cron.monthly run-parts
--report /etc/cron.monthly

</div>
This means that anacron is going to run the jobs in
<span style="font-family: Courier New, Courier, monospace;">/etc/cron.daily</span>,
<span style="font-family: Courier New, Courier, monospace;">/etc/cron.weekly</span>
and
<span style="font-family: Courier New, Courier, monospace;">/etc/cron.monthly</span>.
It should do this at boot up by default (you can check
<span style="font-family: Courier New, Courier, monospace;">/etc/init.d/anacron</span>).
There's then a user-specified delay before anacron runs each task; here,
it's 5 minutes for
<span style="font-family: Courier New, Courier, monospace;">/etc/cron.daily</span>,
10 minutes for
<span style="font-family: Courier New, Courier, monospace;">/etc/cron.weekly</span>
and 15 minutes for
<span style="font-family: Courier New, Courier, monospace;">/etc/cron.monthly</span>.
If you then restart and wait five minutes or so, then do:

<div class="bgcode">
grep cron.daily /var/log/syslog

</div>
should show lines like:

<div class="bgcode">
Jan 31 10:28:02 raspberrypi anacron[2105]: Will run job \`cron.daily' in
5 min.Jan 31 10:33:21 raspberrypi anacron[2105]: Job \`cron.daily'
startedJan 31 10:33:21 raspberrypi anacron[2692]: Updated timestamp for
job \`cron.daily' to 2014-01-31Jan 31 10:33:29 raspberrypi
anacron[2105]: Job \`cron.daily' terminated

</div>
This shows that anacron is doing exactly what we want: running the
cron.daily job five minutes after we boot. It wasn't that obvious to me
how the existing cron scheduler interacts with anacron (nor that easy to
search for) but [this
site](http://www.tuxradar.com/content/automate-linux-cron-and-anacron)
gave a very clear and helpful explanation of how the two interoperate.

</p>

