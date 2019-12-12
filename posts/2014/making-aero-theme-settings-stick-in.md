Title: Making Aero theme settings stick in Windows (resetting on log off)
Date: 2014-01-12 15:11
Modified: 2014-01-12 15:12
Author: Steven Maude
Tags: theme, Aero, Windows, lag, delay
Slug: making-aero-theme-settings-stick-in
Summary: How to fix Aero visual effects settings that keep resetting to default in Windows.
Alias: /2014/01/making-aero-theme-settings-stick-in.html

If you've used any recent version of Windows which is running an [Aero
theme](https://en.wikipedia.org/wiki/Windows_Aero), you've probably
noticed that it doesn't feel that responsive by default. For instance,
when minimising or maximising a window, you get an animation that
someone must have worked really hard on to get look nice. Unfortunately,
this adds some (admittedly short) delay in responsiveness.

My preference is for a PC to feel as swift as possible to use over fancy
graphical decorations. If you go to the Start Menu, right click on
Computer and click Properties, you can access the "Advanced system
settings" which lets you access the Aero theme settings to disable these
features.

<img class="article-image" src="{static}/images/2014/SystemPropertiesPerformance2.png" alt="The Windows System Properties and Performance Options (visual effects) menus.">

However, on changing these settings, you might find that, although they
work, they don't actually stick. When you next log on, the settings have
been restored to the defaults. It may be an issue with running accounts
as standard users, rather than administrators.

<img class="article-image" src="{static}/images/2014/SystemPropertiesPerformance.png" alt="The Windows Start Menu with SystemPropertiesPerformance typed to display the settings menu that lets users change the Aero theme settings.">

To ensure the settings are kept, access this settings panel instead by
typing
[**`systempropertiesperformance`**](http://hardforum.com/archive/index.php/t-1431776.html)
into the Start Menu search. The same panel appears, but the settings
will actually be retained when you next log on.
