Title: Things I have learned from rebuilding a PC in 2021
Date: 2021-02-26 14:02
Author: Steven Maude
Tags: PC, build
Summary: What are you buying? What are you selling?

Despite working with computers (supposedly) professionally, I don't
often build PCs or upgrade PC hardware. A few years ago, I learned a few
lessons from [building a PC]({filename}../2013/things-ive-learned-from-building-and.md).

Over the 2020 Christmas holidays, I was upgrading someone's PC for them,
so here are my lessons I've thought about in 2021.

## Buying PC parts is *not* easy

In the UK at least, the latest processors (CPUs) and graphics cards
(GPUs) were out of stock at the time of buying. That is probably due to
some or all of:

* COVID-19 related supply chain issues;
* releases of hardware in the run up to the holiday period;
* the current trend for people to buy coveted, in-demand trinkets
  (fashion, new generation video game consoles, hand sanitiser) and
  resell at higher than retail price;
* demand from people stuck at home and spending money on PC hardware
  instead of other things.

Adding to all that, the 2021 changes in UK trade due to Brexit may not
help either. However, the fundamental issue of shortages applies
globally from what I've read.

Pent-up demand then drove up prices of older kit. By chance, I managed
to spot AMD's new Ryzen 5 5600x CPUs available just before Christmas
from a retailer at slightly higher than the billed retail price. Somehow
I also managed to order while holding my nose at the inflated cost. I
wasn't actually intending to buy the latest CPU, but the previous
generation Ryzen 5 3600x was being priced at around 75-80% of the cost
of the newer kit anyway.

This might all resolve itself in time. I could do with a new desktop
build myself, but not really inclined to do so right now. Reading
around, it seems like stock shortages, particularly for GPUs, will
continuing well into 2021.

## Buying from a retailer with good returns policies can save time

Here's a long and dull story; feel free to skip to the lessons below.
As part of the same build, and after a lot of research, I ordered a
mainboard that was on offer, as researching it showed it to be a good
buy. As lots of mainboards are, it seemed to be one with lots of RGB
LEDs — nice if you want that, but unnecessary to me — and I figured you
could disable the LEDs easily.

Shortly after ordering, I discovered that you couldn't simply toggle the
LEDs off in the BIOS. Instead, you had to have the mainboard's
manufacturer's clunky software — nice if you want that, but unnecessary
to me — running constantly on Windows to control the LEDs.

I tried to cancel the board order. The order hadn't yet moved to the
stage of being prepared for shipping and was temporarily out of stock
anyway. So I sent a message via the website and hoped they would cancel
on the next working day. This was almost out of office hours, and I
figured that everything would be OK.

About an hour later, I got another email saying the order was
dispatched. From there, things became more of a mess. The next morning,
the courier shipping the order sent me a message with delivery options
including delaying the delivery. I delayed it, the courier still arrived
with the parcel and I explained that I'd deferred delivery.

After a phone call to the company I ordered from, confirming I could
refuse delivery and they would create an returns number, I waited a
week, and heard nothing at all. There was no repeat delivery and I
assumed the parcel was in limbo somewhere.

In the end, it took over a week for the company to get the parcel back
from the courier, it then took a further two written requests to
customer support to finally receive my money back.

I told you it was a long and dull story. No refunds.

### A long and dull story with two lessons learned

* Ordering from a company that has an automated online system for
  cancelling orders is useful for sudden onset of buyer's remorse.
* Ordering from a company that has a good and simple returns process is
  useful if you find the hardware isn't right after you've received it.

There is one obvious market-leading online retailer that has these
attributes, but may not be everyone's first choice for various reasons.
Nonetheless, on customer service, these attributes are fantastic from a
buyer's perspective.

I don't frequently make regrettable purchases. But you can do all the
reading of specifications, manuals, reviews and opinions that you like,
and still find two PC components just will not get along for whatever
reason.

Having no-fuss returns can save you a lot of time and frustration
chasing up customer support. In the UK, there is [substantial current
legislation regarding consumer
rights](https://www.legislation.gov.uk/ukpga/2015/15/contents). However,
it's far simpler as a customer if the vendor already provides better
than the minimum customer service.

## Selling PC parts *is* easy…

After the upgrade, we advertised the old removed parts online. They all
sold within a week, and the proceeds could be spent on a new graphics
card, if you could buy one (see above). I was surprised at both how
quickly these old components sold and for what we sold them for. Some
parts sold for not much less than they cost at retail. It's possible
that people are looking for budget builds, or upgrading/repairing
existing builds.

### …but make sure you upgrade any firmware before selling

After the mainboard sold, the buyer asked about what CPU was used with
it; it wasn't working for them and they were trying to diagnose it. When
they booted up the PC, nothing happened.

Between the details the buyer gave and reading around the BIOS release
notes for the mainboard, we concluded that it was probably a combination
of the mainboard BIOS never being updated, and the buyer using a newer
CPU than had previously been installed.

It was lucky that there was a route to flashing the BIOS without a CPU
via one of the USB ports. Decent mainboards often feature this recovery
option. That meant the buyer could solve this problem without borrowing
or buying another CPU to upgrade the BIOS, or, worse for us, returning
the item.

The wise thing to do is to upgrade the firmware, if there is any, before
removing components.

## What tedious CPU cooler installations should tell hardware manufacturers about marketing 

Two very disparate ideas in the heading there; let's see if there's
anything like a cohesive argument here.

Last time I wrote about [building a
PC]({filename}../2013/things-ive-learned-from-building-and.md), I had
lots of fun installing Intel's push pins. This time I had fun with
fitting a cooler to an AMD setup. It didn't use screws. Instead the
cooler used long metal tweezer-like clips to fit over the tabs on the
AM4 socket on the mainboard.

How this all was assembled to secure the cooler was not obvious at all.
The lack of clear instructions did not help one bit. The text basically
said "build the thing and look at the diagram". The diagram wasn't
clear.

Nor were there many decent YouTube tutorials on this. Eventually I
managed to piece together what to do from looking collectively at
several installation videos in several different languages. Even then,
it was a delicate task to keep the assembly together, while placing the
cooler contact directly on the CPU package and not smudging thermal
paste everywhere.

As an esteemed non-influencer, hardware manufacturers are doing whatever
the opposite is of queuing up to ask me what I think. But if there ever
did suddenly appear an itinerant queue of manufacturers on my doorstep,
what I'd advise them is:

* Instead of relying on buyers of the hardware to provide tutorials,
  manufacturers should create or commission their own videos.
* Make sure these videos have appropriate metadata (title and
  description) to make them easy to find by those who need them.
* Provide videos in multiple languages, whether by audio, subtitles or
  both.
* Show less obvious steps from multiple angles.

It's probably justifiable to spend a relatively small portion of a
marketing and/or support budget to ensure that there is a decent
installation video available. This is marketing and brand awareness:
you're demonstrating, hopefully, that your kit is easy to use, and,
importantly, providing support for users.

I think it's a wider lesson for anyone selling anything — whether
hardware or software — that might require some tricky user installation.
Whether a prospective buyer seeing how to install something and deciding
to buy based on that, or an actual buyer not complaining online or
requesting a refund, there's a benefit for the vendor too.
