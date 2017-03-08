Title: If you want my money, please state your payment processor clearly
Date: 2017-03-06 23:30
Author: Steven Maude
Tags: security, UI, UX
Summary: Why don't websites always clarify who they're using to handle
         card payments?

Today I got a nice letter in the post informing me that my vehicle tax
was due. Wonderful news.

Maybe not.

Still, off I dutifully went to the appropriate [GOV.UK](https://gov.uk)
site to pay the tax: it's not like it's an option if you want to keep
your car on the road legally.

If you're not in the UK, or you are but haven't taxed a vehicle
recently, it's quite simple. They send you a paper reminder. This is
also a form that you can take into a Post Office and pay there.

Paying this online, you're asked for a reference number from the
reminder. There's a check made that your car has a valid [MOT
certificate](https://en.wikipedia.org/wiki/MOT_test) (which establishes
your vehicle's roadworthiness) and then asks you for payment.

Because I'm using
[uMatrix]({filename}../2014/taking-control-of-chromium-and-chrome.md) in
my browser, I can spot which sites other than the one I'm directly
visiting have content which is supposed to be loaded into the current
page. The payment form didn't initially load and I noticed a blocked
site: "ephapay.net".

OK, I've never heard of them: let's check them out and make sure they're
someone I can trust. I didn't anticipate that the UK government's
website would be using someone dodgy, but best to check anyway.

A few searches via web search engines didn't reveal anything about this
domain. Even weirder, the WHOIS information is all hidden by a privacy
service:

> Admin Name: PERFECT PRIVACY, LLC

Surely a legitimate payment processor wouldn't hide their details?

What did reveal who was operating the site was right at the end of the
WHOIS information, in the name server details:

> Name Server: NS1.THE-LOGIC-GROUP.COM

and turns out to be benign. They're a payment processor that got
acquired by Barclaycard in 2014. And I've heard of Barclaycard[^1]. And
the WHOIS information for the-logic-group.com actually points to their
business address. So, it seems that at least they're a established
company (since 1988, a Companies House search will tell you).

But I had to dig through to establish all that. It would have been much
easier if the GOV.UK vehicle tax site just stated clearly who the
payment processor is. I almost considered just reverting to paying the
tax in person when I first encountered the mysterious site.

What the UK government has going for them is that road users who want to
stay legal must pay this, so one way or another, online or offline,
they'll get your cash.

But there are other sites that have similar behaviour and don't have a
captive audience. There have been several cases where I'm interested in
paying for a product or service, and hit some anonymous looking page or
iframe pointing somewhere else, where it's down to my browser showing
details of blocked requests and content that reveal who's handling
payment (yes, of course, you could also search in the source too).

In my case, common culprits of having vague payment pages are sites that
handle ticket payments for small shows, or sites that let you book a
place at running events. I'm sure there are more. And it really does
deter me: if I'm not sure if my payment details are safe, I'd rather not
bother, especially if it's something I can live without.

If you're designing a website, bear this in mind: for the sake of
placing a small, clear explanation of how payment works, and why the
user should trust you and your payment processor, you can remove another
stumbling block that you're putting in the way of getting more paranoid
or technically savvy users to give you money.

[^1]: If nothing else, you have them to thank/blame for inspiring Rowan
Atkinson's Johnny English.
