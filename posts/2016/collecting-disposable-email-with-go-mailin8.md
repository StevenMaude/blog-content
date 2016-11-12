Title: Collecting disposable email with go-mailin8
Date: 2016-11-12 21:47
Author: Steven Maude
Tags: golang, Mailinator, email
Summary: go-mailin8 lets you read the latest message from disposable Mailinator inboxes.

[go-mailin8](https://github.com/StevenMaude/go-mailin8) is a command
line utility I've created to get the most recent message from a
Mailinator email inbox.

# What's Mailinator?

[Mailinator](https://mailinator.com) is one of a number of free services
that allows you to use a disposable email address. This is handy when
you're signing up for something but when you know that the account or
email is only needed ephemerally, as a one-off. My frequent use case is
for free Bandcamp downloads that require an email address. It can also
be useful for testing on the web, if you're developing something that
sends email.

What using a disposable email address offers is not having to hand out
your real email address when that's not needed, with the advantage of
reducing the number of unwanted messages you receive. Yes, of course,
you can usually unsubscribe from mailing lists, but that's extra work.
Better to just not let the unwanted messages anywhere near your real
inbox, where possible.

# Can't you just visit the site?

Yes, you can. But I'm lazy, and this means switching to a new tab,
visiting the URL and loading their home page, then entering the inbox
address, loading the inbox page, and clicking the mail to display it and
then finally copying the activation or download URL I'm looking for.

Much easier if I can just run a command line program that just takes the
local-part of the mailbox name (the part before the @):

```sh
./go-mailin8 <local-part>
```

and gives me back the most recent message. Copy-pasting the URL directly
from the terminal is then simple.

# Why Go and not Python?

It would be probably have been easier to write in Python as I know that
better than I do Go. But I'm conscious that I spent some time over the
summer reading up on Go; the more chance to practise, the better.

In this case, features Go offers like being faster, and easier to write
concurrent code aren't really important. You could equally well write
this code in Python and it would be just as useful.

Where Go excels is that the code has no dependencies to install once it
is compiled. Much simpler than telling someone to first install Python
and then the packages that they need. (I realise that the target
audience of such a tool are probably more than capable of doing so, but
this reduces the barrier for someone to get the program running on their
computer nonetheless.)
