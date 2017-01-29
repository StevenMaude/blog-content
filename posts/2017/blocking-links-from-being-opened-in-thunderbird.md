Title: Blocking URLs in emails from being opened in Thunderbird 
Date: 2017-01-29 14:40
Author: Steven Maude
Tags: Thunderbird
Summary: Preventing links from emails displayed in Thunderbird from
         being opened in a browser.

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
