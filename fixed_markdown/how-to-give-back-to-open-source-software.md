Title: How to give back to open source software
Date: 2014-03-21 22:53
Modified: 2014-03-22 17:58
Author: Steven Maude
Tags: documentation, open, software, source, coding
Slug: how-to-give-back-to-open-source-software
Summary: Ways for developers and non-coders alike to contribute to open source software.
Alias: /2014/03/how-to-give-back-to-open-source-software.html

Even if you have no idea what open source software is, it's likely
you've either used some or, at the least, had some indirect experience
with it.

Maybe you're using a Linux desktop to read this. Even if not, Linux is
present in various embedded devices particularly Android. Maybe you've
read books or documents that have been written in LaTeX, or maybe you've
used [LibreOffice](http://www.libreoffice.org) (a cost-free alternative
to Microsoft Office). Maybe you've watched videos with [VLC media
player](http://www.videolan.org) and maybe someone's used tools like
[Blender](http://www.blender.org) or [VirtualDub](http://virtualdub.org)
in making that video, or [Audacity](http://audacity.sourceforge.net/) to
edit the audio. And what web browser are you running there? If it's
[Firefox](http://www.mozilla.org/firefox), that's open source, and
Chrome is based on an [open source browser](http://www.chromium.org/).

The most important thing about open source software is not that *it's
free* of cost (closed source software can be freeware too, of course),
but that the software's source code is available. Assuming the licence
is amenable to it, this often means that *you're free* to modify it and
even redistribute your changes.

As I'd personally benefited from using so much open source software in
the past, I felt that I'd like to start making contributions back if I
could. However, it may not be immediately obvious how you can get
started, particularly if you're not a developer. Here are a few
suggestions.

## If you can code:

### Share your own projects

GitHub and Bitbucket both allow you to publish your own code as Git
repositories, making them available to anyone. The sharing aspect aside,
it also provides you with a public backup (incidentally, Bitbucket
offers free private repositories too), and means that you can access
your code from any computer with an internet connection.

### Add features or fix bugs in other open source projects

[GitHub
suggest](https://help.github.com/articles/where-can-i-find-open-source-projects-to-work-on)
that you look at popular or trending repositories which I guess may
alert you to something that you didn't know about. Each repository will
probably have several open issues that you could consider working on.
Another resource is [openhatch](http://openhatch.org) which lists
projects in need of fixes, though if the Python projects are anything to
go by, the number of projects covered on there seemed to be fairly
small.

If you're using existing software, you may well encounter issues
yourself that you want to fix for your own use case. I think I'd find
this more motivating than just trying to pick out some project

## If you're not a developer:

From the outside looking in, it's easy to think along the lines of,
"software is code, so if I can't code, I can't contribute". That
couldn't be more wrong. There's much more to software projects than just
the code, and there are still valuable ways for you to contribute that
would be no less appreciated by the owners of a project.

### Write or translate

At a very basic level, submitting documentation fixes or improvements is
a great help as it helps other users get started. If no documentation,
start writing some! If you speak other languages, the developers may
want documentation or strings in the software to be translated.

The fact projects are on GitHub and Bitbucket can look intimidating for
you to make a contribution. But, on GitHub, it's a particularly simple
process to submit changes to text. If you're logged in, click on a text
file you want to edit, click Edit and it will create a separate copy of
the project's repository under your account.

All you need to do is to make your changes, click "Propose file change",
then click "Send pull request" on the next page. The owner of the
project will be notified that you've suggested some changes, which they
can easily pull back into their project from their copy.

### Raise issues

While you're using an open source project, you might spot a bug or think
of something which would make a neat feature. If you check the available
issue trackers for anyone mentioning something similar and don't find
anything, it's probably worth highlighting.

From my own experience, I wrote a script that [grabs tracklistings for
BBC radio
shows](https://github.com/StevenMaude/bbc_radio_tracklisting_downloader)
that I'd downloaded using get\_iplayer. Someone used it, a user
contacted me via GitHub's issue tracker to say that it shouldn't just
save them to text files, but it should also tag the audio file too. This
was something I hadn't thought of, but it seemed a nifty feature so I
was happy to work on adding it as I felt it improved the software.

### Design

Maybe a project is looking for designers, for assets in the software
(e.g. icons) or for their website?

### Contribute to the community

Is there a piece of open source software that you know a lot about? Can
you help out other users questions on an official forum, user group or
mailing list, or somewhere on the Stack Exchange sites?

Tell others about cool projects you've found, without marketing budgets,
much open source software relies on word of mouth. For example, this
week, I discovered [waveshop](http://waveshop.sourceforge.net/) which is
a lightweight audio editor (more so than Audacity) thanks to this post
on
[kvraudio](http://www.kvraudio.com/forum/viewtopic.php?f=7&t=405650&sid=290141ba72f888578036b63bf6bd3981)

### Donate

Some open source projects have contributions made by paid employees, but
many projects are developed by enthusiasts without any funding and in
their free time, so money must be a good thing, right?

Jeff Atwood's experience of [making a sizable donation to an open source
project](http://blog.codinghorror.com/is-money-useless-to-open-source-projects/)
suggests that it might not be so straightforward. Unfortunately, small
donations don't buy the developers more time which is one of the most
important things they need to continue developing software. (Though
sufficient money may be enough to hire developers or allow people to
quit their day jobs to work on projects.)

In some cases, certainly, developers may well [welcome donations to
acquire hardware for testing](http://www.rockbox.org/wiki/DonatedMoney).

## Conclusion

There are plenty of ways to get involved. The next time you're
downloading an open source project, maybe consider taking a look around
their web pages or their repositories to see if there's anything you can
help with.
