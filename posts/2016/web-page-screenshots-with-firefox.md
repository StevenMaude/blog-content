Title: Taking web page screenshots smartly with Firefox's Developer Tools
Date: 2016-04-20 20:30
Author: Steven Maude
Tags: Firefox, screenshot 
Summary: Using Firefox's Developer Tools to take full page web screenshots without stitching by hand.

## Snap happy

Firefox has a buried feature in its Developer Tools, which is potentially
useful even if you're not a developer. If you've never used the Developer
Tools, just press F12 and you'll see the tools.

You should see a cog icon towards the upper right of the pane that's just
displayed. The cog is on the same row as the Inspector, Console etc. buttons.

Clicking this displays a page of options that you can use to customise the
Developer Tools. By ticking "Take a fullpage screenshot" under "Available
Toolbox Buttons", you should see a camera icon appear near the cog icon you
previously clicked. Selecting this gives you a screenshot of the page where you
opened the Developer Tools. The resulting PNG file can be found in your Firefox
Downloads.

This is a really handy feature. It means that you can take an image of a
scrollable page that's **larger** than your current window. No need for
screenshotting parts of the page then joining them together by hand.

## Solving bigger problems

But what if you want to enlarge the visible area beyond the size of your
current window, and then take a screenshot?

Why would this be even useful?

Let's say that you want a screenshot of a web page displaying a map, where the
map expands to fill your browser window. And let's say that you want the
screenshot to cover a larger area than fits into the largest browser window you
can have on your desktop. Just expanding the window isn't going to give you the
size that you need.  

How can you do this? If you hover over the toolbox icons in the Developer Tools
panel, near to the cog, you should be able to find the Responsive Design mode.
(It's a very small, dotted rectangle inside a larger, thicker rectangle.) Click
this. Your display will change to have a border and extra options appear. The
selected resolution is shown above the display. Clicking on the resolution
dropdown menu, you can directly type the resolution you want this preview
display to have and press Enter to have it take effect.

All that's left is to take a screenshot again using the "Take a fullpage
screenshot" option in the Developer Tools toolbox. (Note that Responsive
Design mode has its own screenshot tool, near to the resolution menu,
but this only takes an image of the page visible within the display
window you've just set, i.e.  it's not necessarily the full page if
there would still be scroll bars at that actual display resolution
you've selected.)
