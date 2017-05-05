Title: Trying to trim down static GTFS feeds 
Date: 2017-05-05 11:15
Author: Steven Maude
Tags: GTFS, open data, transit, public transport
Summary: Some tools to perhaps pare down ponderous static GTFS feeds.

## What's a GTFS feed?

This week I've been attempting to reduce the size of a static GTFS feed.

For the uninitiated, GTFS is the [General Transit Feed
Specification](https://developers.google.com/transit/gtfs/), a format
for public transport providers to distribute details of their services.
For example, a bus operator might want to share which routes they run
on, and the times at which they arrive at certain stops. It's not
restricted to buses. You might find GTFS feeds published for trains,
underground services, ferries and [even
gondolas](https://developers.google.com/transit/gtfs/reference/routes-file).

The "static" distinguishes those feeds from realtime[^1] feeds. Static
feeds are just zip files that contain a number of text files in a
comma-separated values (CSV) format, with a .txt filename extension.
These CSVs detail regular timetables that should remain valid for some
reasonable length of time, i.e. they change infrequently.

Realtime feeds (GTFS-RT) report, for example, live trip updates (e.g.
when a bus gets behind the published ideal schedule) or vehicle
locations. Realtime feeds are in Google's Protocol Buffers format, not
CSV. It's useful to be aware of the difference, but, beyond that, I
won't discuss GTFS-RT feeds further in this post.

## The problem

Colleagues on a project were attempt to load the data we'd found for a
particular country, and they were finding it far too large to be usable.
GTFS files come zipped, and the total unzipped content of this file
wasn't far off a gigabyte, and the import into their software was taking
too long.

They were only interested in one geographic region, so maybe most
content can be filtered out either by location, or by transport agency.
Here's a rundown of what I found with the existing tools.

## onebusaway GTFS transformer

Oh, on seeing the [onebusaway GTFS
transformer](http://developer.onebusaway.org/modules/onebusaway-gtfs-modules/1.3.3/onebusaway-gtfs-transformer-cli.html),
it seemed like a dream.

It's a Java program that lets you simply specify the agencies to retain
from the feed in a simple JSON format, and it's fairly comprehensive in
how you can do that. So, hey, let's write a simple transform JSON that
keeps the bus and train agency for the region of interest, and drop the
rest. Exactly what's needed, and a job well done, so now I can relax, and
take a well-earned rest.

Oh, *opens eyes to the smell of a burning PC*, it's time to wake up.

The documentation does provide a warning that this transformation may be
memory and CPU hungry with large GTFS feeds, and that's what I found.

Unfortunately, the transformer seemed to choke on this large GTFS file.
It ran for a long time (hours, across multiple CPUs), got stuck spinning
its wheels on the huge stop_times.txt file (millions of lines) and never
managed to escape that mud. As well as that, out of memory errors were a
problem. In the software's defence, the free memory on the instance I
was running on was fairly limited.

If you've simpler GTFS feeds to work with, it may do the trick, but, for
large ones, you'll need a beefy PC to possibly get anywhere with it.
That said, there's little status output while it's running, meaning it
was unclear whether the transformer was ever doing any useful work or
just getting stuck in some loop.

## gtfstidy

Next, [gtfstidy](https://github.com/patrickbr/gtfstidy/). It can reduce
the size of static GTFS feeds by removing redundant content, simplifying
identifiers and doing clever things to optimise shape data.

It's written in Go, although there are no builds provided, so you'll
have to have Go to install or compile it yourself, which is easy enough.

Once again, it took a long time to process; here, about five hours on my
2013 Core i5 laptop. Then, gtfstidy crashed right at the end of
processing the data [because as I later discovered, it expected the
output directory to
exist](https://github.com/patrickbr/gtfstidy/issues/1) and just failed
to write the output otherwise.

And then it took *another* few hours after I created said output
directory to run again and actually get the cleaned feed data.

In the end, gtfstidy reduced the total size of the GTFS files by about
150 MB, which is a considerable saving. My initial idea was maybe it
might clean the data up enough to make running the onebusaway
transformer a little bit quicker, but it didn't seem worth bothering
trying that again, as the data files overall were still large.

## gtfssplit

Finally, [gtfssplit](https://github.com/samuelmr/gtfssplit) is a PHP
tool that breaks apart a static GTFS feed into trips, shapes and stops.
Unlike the other two projects, this one hasn't been touched for a
while.[^2]

This took a fair time to run, although you can see it's at least doing
something some of the time, because, contrary to the relatively shy and
subdued onebusaway transformer, it displays a lot of warnings while
running.

Once these files are all on disk, maybe it's possible to write code to
recombine these back together into a GTFS feed, filtering out for
agencies that you're not interested in?

I'm not sure.

What I observed is that the dates.txt files that the gtfssplit documentation
refers to in the output (that should be for a given service, i.e. to
tell you which dates the service applies) didn't seem to be present, so
it might be possible that it's losing data somewhere. Maybe that's
because the feed I was looking at has a [calendar_dates.txt and no
calendar.txt
file](https://developers.google.com/transit/gtfs/reference/calendar_dates-file),
and this case isn't handled. (It's valid, just not the recommended way
of putting together a feed.)

Again, I'm not sure, and didn't spend any more time investigating.

## Journey's end?

And that's as far I got to, which is a little anticlimactic. That is, I
haven't found a good existing solution for solving this for large feeds,
outside of the prospect of attempting to write code to do this myself.
However, the fact that all the existing software runs slowly, doesn't
exactly instil me with much hope of doing a better job.

A big difference is that what's actually needed here to solve the
problem is something relatively simple by comparison. The core issue is
that the stop_times.txt is too large. Maybe it's possible to filter that
down based on working through the various files, which is a much more
specific kind of tool than the generic transformer. Perhaps this could
work along the lines of:

1. Keep rows from routes.txt that match the relatively few transport
   `agency_id`s of interest giving a set of `route_id`s.

2. Keep rows from trips.txt that match those `route_id`s from 1 in
   trips.txt, so now these give `trip_id`s of interest.

3. Keep rows in stop_times.txt if they match a `trip_id` retained from
   2, meaning most of the rows disappear, assuming the agencies that are
   of interest make up only a small proportion of the total rows.

You could go further and then fix up the other files too to purge
anything that's now no longer relevant: for example, cleaning agency.txt
to remove agencies that are no longer present. But perhaps gtfstidy
might be enough to tidy up the remaining files and allow us to construct
a clean and valid feed from the files we've mangled.

There are also ways of wrangling GTFS feeds into SQL databases — haven't
linked any as I haven't tried any and can't vouch for them, but they're
easy to find by searching "GTFS to SQL" — so importing and writing
queries to do this filtering, then exporting the result as CSV might be
an alternative option instead of coding something.

This is all speculation for now; I haven't attempted any of this yet. If
I do and it's useful, I'll share what I learn.

What would be nice is if feed providers offered feeds in smaller
regional chunks. Often, transport companies are providing GTFS feeds at
an agency level, so these should be relatively small. I suspect that the
sources of countrywide feeds are usually efforts of communities or
companies to compile the data, which is sometimes originally in a format
other than GTFS, into a standard feed. So it feels ungrateful to comment
that it would be nicer if they broke these feeds into smaller chunks for
data consumers to import into software without further work because
they're providing a free service and their efforts are appreciated.

At the same time, those making efforts to share this data may find more
users for their data if it's ready for import into other software
without needing fast PCs with lots of RAM, or without consumers having
to find ways to divide up the provided feed. For instance, applications
like OpenTripPlanner can, at time of writing, [still struggle with large
GTFS
files](https://github.com/opentripplanner/OpenTripPlanner/issues/2063).

[^1]: The single word "realtime" is how the specification writes it.

[^2]: This isn't always the case, but looking at the activity of an open
      source project can be a portent of how useful it might be, if
      there are several competing bits of software that do the same
      thing and you're trying to narrow down to a few candidates to try
      out.

      How popular a project is, e.g. the number of GitHub stars, might
      be one indicator, although all projects will start out at zero on
      this, so it could well be a good project you've stumbled across
      that's just relatively new, or in a particular niche that means it
      will never become extremely popular. If there are multiple
      competing projects, you can compare them relatively, as opposed to
      comparing their number of stars to [something like
      Bootstrap](https://github.com/twbs/bootstrap).

      The age of the last commit is another. If a project has not been
      touched in a very long time, it could be so good that it hasn't
      needed any maintenance, or just be abandoned because it no longer
      works, or it never did.

      A project with comprehensive documentation, particularly if the
      documentation is good and still valid is another positive sign.
      Especially if you can get a software package or program to install
      and runs an example as described in the docs. There have been
      times I've found that this isn't the case; not a good start and
      I'm likely to give up at this point, if there are alternatives to
      still try.

      These aren't definite rules. And if projects are open source, then
      the only cost in trying them out is time, but these are some of
      the rules of thumb that I'd use when looking out for software I'm
      unfamiliar with.
      
      Asking for recommendations from others is another valuable
      resource that might speed up your search, instead of solely
      relying on your own judgement and web searching skills too.

      This footnote definitely turned out much longer than planned.
