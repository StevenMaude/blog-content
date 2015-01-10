Title: Leaky phone apps
Date: 2013-06-28 21:03
Modified: 2013-07-14 13:13
Author: Steven Maude
Tags: data, app, leaky, Android, Juniper, privacy, PDroid
Slug: leaky-phone-apps
Summary: My view on third party phone apps that leak data.
Alias: /2013/06/leaky-phone-apps.html

My phone doesn't have a huge number of third party apps installed, but
saw this chart today and it's a little worrying nonetheless:

![Chart showing a substantial proportion of free apps collect data
such as location]({filename}/images/Free_apps_chart.jpg)

[//]: # (Below line needs to be a caption.)

Chart courtesy of
[Statista](http://www.statista.com/topics/876/android/chart/1228/free-apps-are-hungry-for-user-data/).

I'm not sure exactly what "account info" describes. I did check the
[original
report](http://www.juniper.net/us/en/forms/mobile-threats-report/) but
it's not defined there either. Also, I'm not sure whether the authors
corrected for the fact that some apps might require some information —
e.g. location access for some kind of mapping app — to actually be
useful. As a result, these numbers could be an overestimate of the
actual number of apps that are doing something unexpected with your
data. Furthermore, it might explain why even a substantial proportion of
paid apps require these permissions. (For ad-supported apps, location
information might be requested for some [targeted advertising
component](https://en.wikipedia.org/wiki/Location-based_advertising) of
the app.)

It's unlikely that Google will ever allow fine control of app
permissions to enable the user to install an app without necessarily
giving it access to e.g. your address book. The only options on stock
Android are to take the app, warts and all, or do without. So,
definitely worth considering installing
[PDroid](http://www.stevenmaude.co.uk/2013/05/patching-android-roms-for-pdroid-using.html)
to help deal with this issue.
