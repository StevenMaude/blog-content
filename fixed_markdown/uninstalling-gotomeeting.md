Title: Uninstalling the Windows GoToMeeting client
Date: 2013-05-14 19:35
Modified: 2013-07-14 13:08
Author: Steven Maude
Tags: uninstall, GoToMeeting, Citrix
Slug: uninstalling-gotomeeting
Summary: How to uninstall the Windows GoToMeeting client.
Alias: /2013/05/uninstalling-gotomeeting.html

I like to uninstall software that I don't really anticipate using on my
PC in the near future. This is partly just to keep my PC free from
clutter, but it also reduces the number of packages that I need to watch
for security updates. [Secunia](http://secunia.com/)'s software helps a
lot with this, and there's always [Ninite](http://ninite.com/) and
[Chocolately](http://chocolatey.org/) too, but limiting the programs
installed to those I actively use helps a lot.

So, when I'd finish using GoToMeeting's client for a one-off meeting, I
was looking to uninstall it. However, there wasn't an entry in the list
of installed programs in the Windows Control Panel, contrary to Citrix's
[FAQ](http://support.citrixonline.com/en_us/gotomeeting/all_files/gtm130001):
"If desired, an attendee may uninstall all GoToMeeting files using the
Add/Remove Programs feature in the Windows control panel."

Fortunately, this issue has already been
[documented](http://www.islandearth.com/articles/2010/9/2/uninstalling-gotomeeting.html)
and the command to use is `g2muninstall.exe /uninstall`

My install was actually located in Program Files (x86), rather than a
user folder. (I'd assumed it needed administrative privileges when
running the installer, so that might be why it placed it there.) Because
of this, I needed to execute this command as an admin, although running
this with a standard user account, the uninstaller was still happy to
cheerily tell me that "GoToMeeting has been uninstalled", even though it
hadn't done a thing.
