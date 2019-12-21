Title: A ULPS take: Windows 10 black screens and slow boot
Date: 2019-12-21 12:29
Author: Steven Maude
Tags: Windows
Summary: Disabling ULPS on laptops that Windows 10 doesn't play nicely with.

# A slow boot problem

Recently I was helping a friend with an older laptop running Windows 10
that seemed unusually slow to start.

Though Windows seemed nimble once it started, the boot and shutdown
times felt excessively slow: minutes instead of the seconds it should
take. And it wasn't like Windows itself was doing anything in this state
either: the machine was silent, instead of the fans powering up, and
there was just a black screen following the Windows logo.

Fortunately, with some frantic searching, I stumbled on a potential
solution: the cause might be a particular AMD graphics problem,
especially with two graphics cards, integrated and discrete. And the
laptop I was looking at did indeed have AMD Radeon hardware.

# ULPS

ULPS is an initialism used by AMD to refer to Ultra Low Power State, and
is the feature that can lead to this slow boot problem. As the name
suggests, this is a power saving feature.

With the particular Windows install I was looking at, I didn't try
updating drivers beyond those that were automatically found by Windows
itself. However, reading around, the drivers may never have been fixed
for legacy hardware anyway.

# The fix

The fix I found was to disable this ULPS feature in the registry.

First, open the Windows Registry Editor. (In the Windows 10 search box,
search for "regedit" and then run "Registry Editor"; I can't remember,
but these edits may require you to be running the Registry Editor as
administrator, so you may need to right-click on "Registry Editor" and
then choose to run it as administrator.)

Search for `EnableULPS`, set any `1` values to `0`. There are also
`EnableULPS_NA` settings but I read conflicting reports of whether to
set these to `0` or not; in the end, only changing the `EnableULPS`
settings was sufficient to resolve this issue for the laptop I was
working with.

Hopefully, that should cure the problem. It's certainly a possibility
that subsequently installed graphics drivers could reset these overrides
and cause the symptom to recur, but, if that's the case, the problem is
easy to spot.

After disabling ULPS, both booting and shutdown were much, *much*
faster. The downside is that disabling ULPS may make the battery deplete
more rapidly than if it were enabled. But the boot up and shutdown times
were so slow without this fix that I think it's a necessary trade-off
to make your PC usable day-to-day, should you require it.

There are other causes of a slow booting Windows installation, but if
you are dealing with a slow starting PC with Radeon graphics,
particularly with two display adapters, it's worth trying to update the
drivers and, failing that, seeing if this fix works.
