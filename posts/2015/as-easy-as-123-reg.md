Title: As easy as 123(-reg) 
Date: 2015-12-11 17:04
Author: Steven Maude
Tags: domain, Namecheap, registrar, transfer 
Summary: Transferring a .co.uk domain from 123-reg to Namecheap with no downtime.

## Two factor or not two factor

We're living in the future right now: it's almost 2016. Almost as unbelievably,
123-reg *still* haven't implemented any kind of two factor authentication for
their site.

From their own [blog](https://www.123-reg.co.uk/blog/security-issues/how-to-create-a-strong-password-and-protect-your-online-life/):

> Two-factor authentication adds another layer of protection and you should use
> it where it is available.

Well, yeah, I would. If I could.

It's stupid for me to not be using a registrar that provides two factor
authentication. Get control of the domain and you could hijack my website or my
email.

It's also stupid on their part not to implement this. It's a security feature I
expect as standard on important web services these days. And I'm sure that I'm
not the only person who's decided to leave or not use their service as a
result. Moreover, the implication of no two factor support does have me
questioning what else they can't be bothered to do security-wise.

Apart from this issue, I wouldn't say I'd be exactly content, but I'd have the
apathy towards transferring my domain out that many people have towards
switching bank accounts, rather than any more urgent impetus to leave.

As I don't ever really use the 123-reg site itself, I don't really have a
problem with them not redesigning it in years. The only major outage I've
knowingly experienced in over 12 years(!) of being with them is that email was
[hideously delayed](http://www.theregister.co.uk/2006/12/18/123_says_sorry/) a
few years back. However, when reading about domain transfer, I also learned of
some recent [moneygrabbing
tricks](http://www.mayne.net/123reg-domain-name-hostage) they've
tried.[^1]

Searching around for other domain registrars, it seems there is no single
standout provider. You can find complaints about every one, so it's a bit of a
crapshoot in choosing one. Namecheap were, true to their branding, a name that
was reasonably cheap. And, they appeared to have no more complaints than any
other provider.

But as a prelude to committing to moving, I figured I'd buy some other domain
names with Namecheap and see what I made of the site. My first impressions were
that the initial signup and buying services from Namecheap was pretty easy.
Their dashboard also simple to navigate and fairly fresh looking. This is a
marked improvement on the 123-reg control panel that is well overdue for a
modern, clean redesign.

The final thing to give me the confidence to start looking into domain transfer
was the quick response I received from Namecheap in resolving an issue when
extending my domain name expiry. So, I started delving into the murky waters of
domain transfers.

## 12(free)-reg

When you dive in, you find the depths are actually not as bad as they first
look. Certainly, the process isn't actually that complicated. The confusing
part is navigating around help pages that usually tell an incomplete story of
what you need to do to move your domain. Neither 123-reg nor Namecheap did a
great job here: I ended up reading several different pages to do something
that's, I imagine, a reasonably common procedure for their customers.

To give you an idea, I probably spent about five to ten minutes actually making
changes on the old and new domain registrar's sites, and probably spent ten
times that time reading around, and double and triple checking what I was
doing. I didn't want to bungle the whole thing and spend hours in dialogue with
support to resolve it.

## Migrating .uk domains

One important note is that .uk domains are handled a bit differently to others.
The stages you need to carry out and avoid downtime aren't much more than:

1. set up new name servers on your new registrar, and copy over whichever
   existing DNS settings are needed from your current registrar to the new one;

2. change name servers on your current registrar to those of the new registrar
   and wait for this to be updated everywhere;

3. *maybe* you need to make WHOIS data public (not sure if this is absolutely
   necessary for UK domains);

4. change the Internet Provider Security (IPS) tag on your current registrar to
   that of the new registrar;

5. request a transfer in at your new registrar.

Again, all that matters for .uk domains is the IPS tag. Anything you read about
EPP authorisation code or lock status just doesn't apply at all for them.

Also note by .uk domains, this is *any* .uk domain, i.e. this applies for
stevenmaude.co.uk, not just stevenmaude.uk.

## How to move from 123-reg to Namecheap 

1. First, set up FreeDNS on Namecheap. Add your existing domain as detailed
   [here](https://www.namecheap.com/support/knowledgebase/article.aspx/536/51/how-do-i-set-my-domain-to-use-namecheaps-freedns-service).
   If you want to potentially activate that more quickly, note that you can
   prompt for an activation email. This also means you don't need to change
   name servers before you activate should you wish. You'll receive a link to
   activate the FreeDNS service in that case.

2. Go to Advanced DNS on Namecheap's dashboard and copy over entries from the
   123-reg Advanced DNS settings. There were a couple of 123-reg IP addresses
   in there which I didn't move as they were no longer needed. Everything else
   I just copied over by hand. MX records are added in Namecheap by selecting
   "Custom MX" in "Mail Settings" which is in the Advanced DNS dashboard.

3. **Optional**: if you were using web forwarding and want to preserve it, you
   can set this up on Namecheap's Manage options for the domain ("Redirect
   Domain") or go to Advanced DNS and add entries manually. See their
   [help pages](https://www.namecheap.com/support/knowledgebase/article.aspx/385/77/how-do-i-setup-url-forwarding-for-a-domain)
   for more.

4. Go to 123-reg's control panel and select the option to add name servers to
   your domain. I added two of Namecheap's FreeDNS servers.

5. **Possibly optional**: you may need to make the WHOIS contact details public
   for the domain if they're not already. Go to 123-reg's control panel and do
   this. You may wish to change the address first to one which you're happy
   with making publically accessible.

6. Check the new name servers have been added and that they work. Windows, Linux
   and OS X all have a `whois` command you can use to see if the name servers
   are at least visible on the DNS server you're accessing. You may see this
   change fairly quickly e.g. within a few seconds or minutes.
   
    My way of testing that the name servers were working as expected was to add
    a temporary web forwarding rule on the new registrar which didn't exist on
    the old one. Once I could confirm that redirect worked, I could remove the
    rule. As I was confident things were working OK, I then removed the 123-reg
    name servers from my domain, leaving only the FreeDNS ones there.

    If you can verify that everything is working OK, you should now wait
    sometime for the settings to propagate everywhere. 123-reg currently
    recommend [48 hours](https://www.123-reg.co.uk/support/answers/Domains-Archive/Domain-Configuration/why-do-people-always-tell-me-that-my-dns-changes-take-24-48-hours-to-propagate-2653/).

7. As mentioned, make sure you've waited for the name server changes to
   propagate before continuing. Do something exciting in the meantime.
   Or just sleep.

8. Change the IPS tag on 123-reg to Namecheap's IPS tag as detailed in the
   [123-reg help](https://www.123-reg.co.uk/support/answers/Domain-Transfers/Transfers-Out/how-do-i-change-the-ips-tag-on-my-domain-name-1264/).
   Enter Namecheap's IPS tag which you can find
   [here](https://www.namecheap.com/support/knowledgebase/article.aspx/260/8/what-is-an-ips-tag).
   If they've changed the link, a search for "IPS tag site:namecheap.com" will
   probably get you to the right place to find it.

9. Go through the Namecheap transfer, select your domain in the dashboard and
   select "Transfer in". You'll probably have to pay them some money. The
   process should hopefully begin and be complete within an hour or two.[^2] My
   transfer only took maybe half an hour or even less. You can see the status
   of your transfer in the Namecheap dashboard.

10. Finally, check that the FreeDNS has changed to the normal DNS, and that
    all of your DNS records are still present.

    For some reason, in the advanced DNS, the mail settings had changed from
    "Custom MX" to "No Email Service". Email still appeared to work in the
    meantime, and the records were all still there when I reselected "Custom
    MX" which was odd.

    While here, you may also wish to set the public WHOIS to private if you're
    domain is for use by a "UK Individual".

And that's it!

[^1]: I wasn't charged for changing IPS tag; no idea if 123-reg changed their
      policy for everyone or it's because the domain was registered long ago.

[^2]: It's a little disconcerting that all this happens without receiving any
      email to the domain contact to confirm the move. I'm not sure what
      procedure's in place to prevent someone else transferring your domain to
      the same registrar but under their control, once you've changed the IPS
      tag...
