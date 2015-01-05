Title: Migrating email from POP to IMAP in Thunderbird
Date: 2014-05-06 18:50
Author: Steven Maude
Tags: Thunderbird, migration, POP, IMAP, Gmail
Slug: migrating-email-from-pop-to-imap

I had my Gmail account setup to be accessed via
[POP](https://en.wikipedia.org/wiki/Post_Office_Protocol) in [Mozilla
Thunderbird](http://www.mozilla.org/en-GB/thunderbird/) and thought it
was about time to shift to using
[IMAP](https://en.wikipedia.org/wiki/Internet_Message_Access_Protocol)
instead. In fact, it's that long ago that I can't actually remember why
I didn't just use IMAP in the first place.  
  
Why should you be bothered about how your email is accessed? As long as
you can read it, what's the difference?  
  
As explained in this [Gmail blog
post](http://gmailblog.blogspot.com/2008/05/getting-gmail-anywhere-imap-versus-pop.html),
when using POP, changes made on a local device (e.g. marking mail as
read or sorting mail into folders) aren't reflected on the mail server.
When you access your mail from a different device (or client), you'll
find your mail organised as if you hadn't made any of those changes at
all. IMAP, on the other hand, synchronises any changes you make locally
to the mail server, so your mail will be organised in the same way when
using IMAP, no matter which device or client you use. The changes will
propagate to the next device you use.  
  
With the prevalence of smartphones and mobile data connections becoming
more usable, it's increasingly the case that multiple devices, rather
than a single PC, are used to access mail. So, it seemed a good move to
make the switch now.  
  
The approach I used was the [accepted answer
here](http://superuser.com/questions/317274/convert-a-gmail-account-from-pop-to-imap-and-keep-folder-structure):
setup the IMAP account in Thunderbird so that you have both the old POP
account alongside a new IMAP account, and then just drag folders from
the POP to the IMAP. It's not much more complicated than that, but these
are the specific steps I used for migration:  
  
1. [Enabled IMAP access on
Gmail](https://support.google.com/mail/answer/77695).   
2. Moved everything in the current Gmail inbox — all this mail was
already on my PC via the POP account — into the bin. (I actually did
this after I migrated all my folders, but you could do it here while
logged into Gmail via the web.)   
3. [Backed up my current Thunderbird
profile](http://kb.mozillazine.org/Profile_backup), in case anything
goes wrong or you want to quickly revert back to using POP for some
reason.  
4. [Setup the Gmail IMAP account in
Thunderbird](https://support.mozillamessaging.com/en-US/kb/thunderbird-and-gmail).  
5. Stopped the POP account from checking for new messages, to avoid the
possibility of the POP account redownloading all the sorted mail that
was currently being copied from the local POP folders back to Gmail.
(Untick the two boxes in *Tools menu \> Account Settings \> Server
Settings \> Check for new messages...*)  
6. Dragged each folder from the POP account to the IMAP account. This
will probably be by far the slowest step if you have plenty of mail.
Don't forget your Sent Mail folder.  
7. Once I was happy that everything had migrated across, I emptied the
Gmail bin, and then removed the POP account from Thunderbird (*Tools
menu \> Account Settings \> Account Actions \> Remove Account*).  
  
Overall, it was simple. The only time consuming part was actually moving
the messages from the copies I had in the Thunderbird POP account to the
IMAP account.  
  
The only other (optional) thing I did was keep a local copy of all my
previous mail for [quicker message loading and
searching](https://support.mozillamessaging.com/en-US/kb/imap-synchronization#w_benefits-of-imap),
and as a backup. Make sure that the appropriate account setting is
ticked (*Tools menu \> Account Settings \> Synchronisation & Storage \>
"Keep messages for this account on this computer"*). Next, right click
on a mail folder, go to the Synchronisation tab and click Download Now.
Repeat for each mail folder.
