Title: Firefox keyword searches, and how to fix adding them
Date: 2016-04-03 17:00
Author: Steven Maude
Tags: Firefox, keyword search, quick search
Summary: How Firefox keyword searches speed up web searching, and how to resolve the situation when you can't add new ones.

## What are keyword searches?

Keyword searches, or quick searches, are really handy when browsing. If
you think of something that you want to search for, they remove the
extra step of first navigating to the site and selecting the search box. 

Instead, you can just directly enter your query into your address bar,
preceded by some keyword. For instance, if I look up "Ubuntu" on
[DuckDuckGo](https://duckduckgo.com), I can just hit Ctrl+L to access
the address bar, type `d Ubuntu` and hit enter, to directly access the
page of search results.

## How keyword searches save time

This might not seem like a big time saving, but when you consider that
you have to repeat the same process for every site you search on, it
soon adds up. It's a feature you can use not only with traditional
search engines, but with most sites that have a search box. One example
is YouTube, I'll often — maybe **too** often — type `yt Yet another timewasting
distraction`.

## Creating and using custom keyword searches in Firefox

This is really simple to do. You're really just adding a bookmark, but
one that refers to whatever URL the search box will send you to, not the
page itself.

1. Right click a search box on a webpage.
2. Select "Add a Keyword for this Search…"
3. In the dialogue that opens, enter a keyword and the search URL is
   then added to your bookmarks with a placeholder for a query.
4. When you next type that keyword followed by a search query into the
   address bar, the bookmark gets loaded with your query automatically inserted
   into the URL.

These keyword searches are normal bookmarks; you can edit them like any
other bookmark. The only difference is that they contain the `%s`
[placeholder](https://en.wikipedia.org/wiki/Printf_format_string) in the
URL. When you carry out a keyword search, the term following the keyword
replaces the `%s` in the bookmark.

If you're browsing through your bookmarks in the Library, you'll only
see "Name", "Location" and "Tags", but if you click "More", you'll see
(and can change) the keyword you've set too. 

(This all works because, as you've probably noticed, using a search
option on a site usually sends you to a URL that contains the search
term. Hopefully you can see that if you construct the URL without even
visiting the site first, that this should still work. That said, this
assumes that the site uses GET requests where the query is contained in
the URL itself.)

## But my keyword searches aren't being added?

As I find them so useful, I sorely missed it when recently, for whatever
reason, Firefox decided that it wouldn't add them any more.

The bookmark would get created, but the keyword I added didn't get
saved. Even if I manually edited the bookmark, I could enter a keyword
but on navigating away to another bookmark and back again, the keyword
would be lost again.

The simple fix was just to exit Firefox, locate `places.sqlite` inside
the Firefox profile directory,[^1] rename `places.sqlite`, and let the
file be rebuilt on the next restart (as documented in [Mozilla's support
pages](https://support.mozilla.org/en-US/kb/cant-add-change-or-save-bookmarks)).

The documentation states that you lose history, but any bookmarks are
rebuilt from a backup. Once you're happy everything's OK, you can delete
the old `places.sqlite`. After that, new keyword searches were added
without a problem.

[^1]: Its location depends on [your operating system](https://support.mozilla.org/en-US/kb/profiles-where-firefox-stores-user-data).
For me, on Linux, it was in the hidden `~/.mozilla/firefox`. On
Windows, it'll be in `%APPDATA%\Mozilla\Firefox\Profiles\`. Make sure
that you're in the correct profile directory, if you have multiple
Firefox profiles.
