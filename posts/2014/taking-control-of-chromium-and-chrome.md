Title: Taking control of Chromium (and Chrome) with µblock and HTTP Switchboard
Date: 2014-09-28 00:02
Modified: 2015-07-24 11:37
Author: Steven Maude
Tags: ad, µblock, HTTP Switchboard, blocking, privacy, adblock
Slug: taking-control-of-chromium-and-chrome
Summary: How you can use µblock and HTTP Switchboard to take control of what your browser loads.
Alias: /2014/09/taking-control-of-chromium-and-chrome.html

!!! article-edit ""
    Edit 2015-07-24: Slightly involved story aside, the version of
    µBlock linked here, by the original developer, is now µBlock Origin.
    I'd recommend searching for that version if installing as an
    extension.

    It's available for both Firefox and Chrome/Chromium.

!!! article-edit ""
    Edit 2015-05-18: The Chromium bug is fixed which should fix the µMatrix
    UI sluggishness, and µMatrix is finally available as a Firefox addon.

!!! article-edit ""
    Edit 2015-01-09: HTTP Switchboard development is discontinued and has been
    replaced with [µMatrix](https://github.com/gorhill/uMatrix). The
    interface is largely unchanged. One problem at the time of writing is a
    [Chromium bug](https://github.com/gorhill/uBlock/issues/419) which I
    think is the cause of the UI being really laggy to appear. Hopefully,
    this should be fixed soon.

After tinkering around with Adblock's filters to block some ads, I
remembered that I'd read about an alternative to Adblock for
Chromium-based browsers called [HTTP
Switchboard](https://github.com/gorhill/httpswitchboard) a few months ago
and figured I should actually give it a try.

One of the reasons that HTTP Switchboard was notable is that it promised
to be much more CPU and memory friendly than [Adblock Plus](https://blog.mozilla.org/nnethercote/2014/05/14/adblock-pluss-effect-on-firefoxs-memory-usage/)
currently is.

In fact, the adblocking part of HTTP Switchboard has now been separated
out into another project, µblock. Both are still useful. I'll explain
why below.

## Why are you blocking content at all?

Many content-driven websites use advertising as their business model. My
feeling is that, while sites are welcome to try and send content to my
browser, I should have the freedom to choose what my browser actually
loads.

There's no contract I've signed that states I must load and display the
page as the site owner intends. (What if I'm using a text browser like
links?) And there's no obligation on my part to make their business
model sustainable.

Maybe you still think this seems selfish. Well, to some extent it is.
But, my privacy and computer security are more important to me than the
financial success or failure of an external organisation. That I put my
priorities in this order is kind of obvious though, right?

## Why shouldn't sites and advertisers worry so much?

Even with "despicable" users like me, there are two reasons I can think
of as to why advertisers and sites dependent on them shouldn't feel so
glum:

1.  Adblocking users have made an active choice to block ads. Those
    users have done you a favour in removing themselves from your
    viewership as you don't waste time targeting them; why chase
    "customers" running in the opposite direction from you?

2.  Browsing is increasingly done from mobile browsers. How many users
    are going to bother to root their devices or install alternative
    browsers just for adblocking?

## But why worry about where displayed web content originates from?

### Privacy

One contentious issue with ads and cookies is privacy.

As [this Economist
article](http://www.economist.com/news/special-report/21615871-everything-people-do-online-avidly-followed-advertisers-and-third-party)
highlights,
the depth of what advertisers collect about your browsing habits is
extensive, and it's handled and passed around by many organisations.
Unless you're all for being advertised at, this isn't for your benefit.

Maybe advertisers are really all benign and just interested in deciding
who's best to try to sell to. Perhaps just as the executive in that
article quoted claims, it really is just that,

> "We are not trolling for personal information. We are trying to figure
> out if you are a high-value customer and are in the market for a car."

But, the sheer amount of information being collected is worrying,
especially when, as a user, I've no idea of what's actually being
tracked and what the intended end use is.

### Malware

As well as that, web advertising has been a conduit for the deployment
of malware previously and will no doubt continue to be. (It's a nice way
of distributing it to users who are visiting, what to them, might seem
like a trustworthy site. If they can get the malicious ad past the
company providing the advertising, they don't need to go to the trouble
of hacking the site directly.)

There have been
[one](http://arstechnica.com/security/2014/09/google-stops-malicious-advertising-campaign-that-could-have-reached-millions/)
or [two](http://www.washingtonpost.com/blogs/the-switch/wp/2014/01/04/thousands-of-visitors-to-yahoo-com-hit-with-malware-attack-researchers-say/)
high-profile incidents this year too.

In terms of potentially malicious content, it's not only just ad
providers that I'm concerned with, but allowing large numbers of
arbitrary sites to run their scripts on your machine unchecked.

Look at the recent [JQuery
compromise](http://www.zdnet.com/was-jquery-hacked-7000034009/), for
instance. Fortunately, only the site itself was affected and **not** the
hosted libraries that many sites. It's not inconceivable that an
attacker may well deliberately go after to poison hosted libraries. It's
just way too big a jackpot for malware distributors to ignore.

Even if such an attack might be spotted quite quickly, how many users
could be affected in the interim? (I'm not even sure what the solution
is here; often JQuery's needed for sites to function as intended...)

Minimising the number of third-party sites that you allow content to
load from can't be a bad thing. (There's some risk wherever you go, but
in some cases, I've seen sites loading in content from more sites than I
can count on both hands.)

## Controlling what your browser displays

So, what can you do? There are browser extensions for Firefox and Chrome
that give you more control over what your browser loads.

Lots of sites are perfectly readable without them storing tracking
information about you, without arbitrary JavaScript running. For those
that don't, it's quite simple to whitelist them.

The downside of this is that it can be a chore. In Firefox, I need a
slew of extensions to do this: which sites are allowed to run scripts
(NoScript), which cross-site requests are allowed (RequestPolicy), and
which sites can store cookies (CookieMonster).

Managing each one in turn, allowing permissions for cookies, scripts and
third-party scripts, can be tedious. I've run NoScript for a long time,
but these days with sites often hosting content and scripts somewhere
other than on the domain you're visiting, it's much more work than it
was.

HTTP Switchboard was a big, all encompassing project for Chromium-based
browsers that had features comparable to Adblock Plus, and the Firefox
extensions, NoScript, RequestPolicy. Recently, the [adblocking,
pattern-based filtering](https://github.com/gorhill/httpswitchboard/issues/378)
has been split out into another project,
[µblock](https://github.com/gorhill/ublock).

## µblock

By virtue of what HTTP Switchboard aims to do — give you full control of
what is allowed by your browser — this makes its user interface slightly
more complex, which I'll soon get onto.

<img class="article-image" src="{filename}/images/2014/ublock.png" alt="The µblock enable/disable icon." width="174">

Stripping out this sophistication seems like a smart move, since
µblock's incredibly easy to use. Really, it requires the same amount of
setup as Adblock Plus does: not much at all.

It comes with the most popular Adblock Plus filters accessible on
install, and you can easily choose which of those filter lists are
applied.

Disabling µblock for a site is also straightforward. Click the red µ
icon next to the address bar and then click the power icon.

It does the same job as Adblock Plus, but with lower CPU and memory
usage. If you've ditched an ad blocker for this reason, it's worth
looking at. Even if you're still happy using Adblock Plus (or one of its
forks), µblock is definitely worth spending the couple of minutes to try
it out.

## HTTP Switchboard

On to HTTP Switchboard, which allows fine grained control of the types
and locations of content that Chromium-based browser can access.

Note that with the current version of HTTP Switchboard, there's a little
[initial setup](https://github.com/gorhill/httpswitchboard/issues/378) to
disable the adblocking filtering that µBlock covers.

HTTP Switchboard's interface can feel initially overwhelming; more so
than perhaps the likes of NoScript, RequestPolicy and CookieMonster that
I use which all have similar menus to allow or deny permission for a
site to run scripts or store cookies. These have a text explanation of
what the option does.

<figure class="article-figure">
  <img src="{filename}/images/2014/Firefox_menus.png" alt="Examples of NoScript, CookieMonster and RequestPolicy permission menus.">
  <figcaption>From left to right, examples of NoScript, CookieMonster and RequestPolicy permission menus when accessing Google Books.</figcaption>
</figure>

The problem with this menu format is, though it's explicit and clear,
it's cumbersome when you're dealing with several extensions. For each
extension, you need to repeat the process of whitelisting every site
that you're allowing.

When you've actually used HTTP Switchboard for a few minutes, its
simplicity clicks. HTTP Switchboard opts for a table-like interface.
Each site is represented as a row, and each type of content is shown as
a column.

<figure class="article-figure">
  <img src="{filename}/images/2014/HTTP_Switchboard.png" alt="Example of HTTP Switchboard's table interface.">
  <figcaption>Example of HTTP Switchboard's interface when accessing Google Books.</figcaption>
</figure>

This lets the user approve different permissions for different sites
quickly. Just read down the list of sites, click on those you want to
whitelist completely, and for those you don't you can allow specific
features only (e.g. loading images only). Likewise, if you want to
enable one type of content for all sites, just click the appropriate
column. If you want to save the permissions in future, click the padlock
icon, and you're done.

It helps a lot that you can see **all** the sites that are trying to
load content or save cookies in one glance, rather than consulting
separate menus.

There's an autoreload option that refreshes the page when you change
permissions, so once you've approved everything needed, the page should
then work as expected.

Out of the box, (I think) HTTP Switchboard was configured to allow most
requests through, apart from those blacklisted by filters. What
initially confused me was at what level the filters apply. (Do they
apply to this site? To this domain? globally?).

What I'd recommend is, like the extension developer, is to
[block everything](https://github.com/gorhill/httpswitchboard/wiki/How-to-use-HTTP-Switchboard:-Two-opposing-views)
by default and then whitelist only what you want to allow.

There's an option in the HTTP Switchboard settings under "more security"
to create a new site-specific scope for every site you visit which is
really useful. This creates a set of rules for each site you visit.
Furthermore, the drop down (click the blue top-left box with the site
name in) lets you select where the rule applies (to the site, to the
domain or globally).

This lets you block content from, say, a site like twitter.com when
you're visiting a third-party site, but allow it when you're directly
visiting Twitter.

It also has some nice bonus privacy features, like removing HTTP
referers when visiting non-whitelisted sites and a user-agent
randomiser.

The only thing that's missing for me is guidance on what the sites
likely are. If you're happy to spend a few seconds researching, it's not
hard to figure this out. It might save a bit of time if there was a
database of sites telling you "hey, you might need this, it's a content
delivery network" or "this is tracking how you're using the site; you
probably don't need it for the site to function properly". Yes, I can
search, but it's a bit clunky to do that.

## A summary

These are really great browser extensions, and credit to Raymond Hill
for an awesome job on them. Every time I'm managing permissions with
multiple extensions in Firefox now, I sigh a little. (Firefox's awesome
bar is far more useful to me than Chrome/ium's omnibox though, so I tend
to stick with Firefox.)

Longer term, I'd really hope that a Firefox add-on developer [picks up
the baton to port these](https://github.com/gorhill/uBlock/issues/27).

(As a postscript, I should point out that as well as adblocking and
control over requests, [HTTPS Everywhere](https://www.eff.org/https-everywhere)
is another useful privacy-enhancing extension for Firefox and Chromium
browsers. Where HTTPS browsing is available on sites but not always used,
HTTPS Everywhere enables it for you.)
