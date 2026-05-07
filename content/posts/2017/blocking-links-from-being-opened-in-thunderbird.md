+++
title = "Blocking URLs in emails from being opened in Thunderbird"
date = 2017-01-29T14:40
author = "Steven Maude"
summary = "Preventing links from emails displayed in Thunderbird from"
slug = "blocking-links-from-being-opened-in-thunderbird"
url = "/posts/blocking-links-from-being-opened-in-thunderbird/"
tags = ["Thunderbird"]
+++

I'd got some unwanted spam message and wondered if it was possible to
stop accidental clicking on any URLs that are displayed in those cases.

Turns out you can easily.

Go to the Edit menu > Preferences > Advanced > Config Editor. Skip past
the warning about changing advanced settings if it's displayed (you must
have already disabled it previously, if you don't see this).

Search for network.protocol-handler.external-default, right click the
option of that name that appears under Preference Name and select Toggle
to change it from the default (true) to false.

Now, if you try to click on a URL now that's displayed in an email,
nothing will happen; your web browser won't open. However, you can
always copy the URL and paste into a browser yourself.
