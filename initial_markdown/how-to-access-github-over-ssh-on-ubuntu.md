Title: How to access GitHub over SSH on Ubuntu
Date: 2013-09-07 12:07
Author: Steven Maude (noreply@blogger.com)
Tags: GitHub, SSH, remote, shell, Ubuntu
Slug: how-to-access-github-over-ssh-on-ubuntu

<div class="separator" style="clear: both; text-align: center;">
[![GitHub
logo](http://4.bp.blogspot.com/-r9qn9TMJR_M/UisRWapGv1I/AAAAAAAAAFM/1yF2Eh1lyDc/s1600/GitHub_Logo.png "GitHub logo")](http://4.bp.blogspot.com/-r9qn9TMJR_M/UisRWapGv1I/AAAAAAAAAFM/1yF2Eh1lyDc/s1600/GitHub_Logo.png)

</div>
  
[Since starting working at
ScraperWiki](http://blog.scraperwiki.com/2013/09/02/hi-im-steve/), I've
been using [Git version control](http://git-scm.com/) and
[GitHub](https://github.com/) a lot to collaborate on projects I'm
working on. Out of the box, connecting to GitHub via HTTPS is simple to
get going and works perfectly fine. One problem is that you have to
enter a username and password every time you do anything with the remote
repository, such as pushing code to it.  
  
For me, this gets in the way of workflow. It's a small, but distracting,
obstacle that snaps me out of whatever thought process I was in. Over a
full day's work, this can happen several times.  
  
Instead, I prefer to connect to GitHub using an
[SSH](https://en.wikipedia.org/wiki/Secure_Shell) connection. All I do
now is enter a passphrase once per login session and then forget about
it^1^. Another advantage is that you can [forward access to your local
SSH
credentials](http://www.unixwiz.net/techtips/ssh-agent-forwarding.html)
even when developing in remote shell accounts.  
  
GitHub's help section has several well written pages that detail clearly
how to get this setup running. The only issue with those guides is that
the individual steps are actually split over a few individual help
pages. Here's a combined summary of what you need to do.  
  
1. [Generate an SSH key locally (not on a remote shell account), with a
passphrase, add it to your GitHub account and test
it.](https://help.github.com/articles/generating-ssh-keys)  
  
You should now change the clone URLs GitHub displays to SSH (see right
image; where it says clone with HTTPS, SSH..., click on SSH).  
  

<div class="separator" style="clear: both; text-align: center;">
[![GitHub sidebar showing the position of the clone URL
display](http://3.bp.blogspot.com/-TGMUacXRCXU/UisP7tB4afI/AAAAAAAAAFA/2qjKu2SdYIM/s1600/GitHub+clone.png "GitHub sidebar")](http://3.bp.blogspot.com/-TGMUacXRCXU/UisP7tB4afI/AAAAAAAAAFA/2qjKu2SdYIM/s1600/GitHub+clone.png)

</div>
Now, the first time you try to perform some action on GitHub via ssh
(e.g. <span style="font-family: Courier New, Courier, monospace;">git
clone</span>), you should only get asked for the passphrase once and
subsequent connections will proceed without prompting. This worked out
of the box for me on Ubuntu 12.04 LTS. If you have issues, you'll need
to look into how to configure
[ssh-agent](http://mah.everybody.org/docs/ssh) on your system.  
  
Bear in mind that if you already have repositories that you have cloned
via HTTPS using GitHub, [you'll likely want to update the git remotes to
use the appropriate SSH URLs
instead](https://help.github.com/articles/changing-a-remote-s-url).
These won't be automatically changed. Otherwise you'll still get asked
for your username and password credentials: these local repositories
will still be connecting via HTTPS URLs!  
  
2. (Optional; handy if you're developing or git cloning on remote boxes)
[With everything now working locally, you need to setup ssh-agent so
that your remote account can access your SSH
key](https://help.github.com/articles/using-ssh-agent-forwarding).  
  
When you now carry out an operation with GitHub on the remote machine
you connected to via SSH, **you shouldn't get asked for your password on
that machine either^2^**.  
  
<span style="font-size: x-small;">^1^I am aware that you do have the
option of using credential helper to [cache your HTTPS
password](https://help.github.com/articles/set-up-git#password-caching),
but you would need to do this both locally and remotely if you are
working on different machines. Also, the default setting, though it can
be changed, is to cache the password for just 15 minutes.</span>  
<span style="font-size: x-small;">^2^Again, the caveat regarding
changing repository remote settings from HTTPS to SSH applies on remote
machines too.</span>

</p>

