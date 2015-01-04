Title: Working with multiple SSH keys: setting up git over SSH with GitHub and Bitbucket
Date: 2013-10-08 19:41
Author: Steven Maude (noreply@blogger.com)
Tags: GitHub, key, SSH, Bitbucket
Slug: working-with-multiple-ssh-keys-setting

My SSH key was setup for GitHub and working fine, but I wanted to add a
separate one for Bitbucket\*. It was daunting playing around with this
when everything was already working largely as I expected, but it was
simple to get this as I wanted.  
  
First, backup your existing keys first in case something goes wrong and
you accidentally overwrite them. (You're backing up your data anyway,
right?)  
  
[Create a new
key](https://help.github.com/articles/generating-ssh-keys). If you've
got an id\_rsa key already, you can name the new key e.g.
\~/.ssh/id\_rsa.1 (or 2, .3...). (Initially, I put the new key in a
separate Bitbucket directory and I don't think that the ssh-agent would
automatically pick it up there, so I moved it back to the .ssh
directory.)  
  
Add the following to \~/.ssh/config:  
  

<div class="bgcode">
<span style="color: black; font-family: Courier New, Courier, monospace;">Host
github.com  
User git  
IdentityFile \~/.ssh/id\_rsa  
IdentitiesOnly yes  
  
Host bitbucket.org  
User git  
IdentityFile \~/.ssh/id\_rsa.1  
IdentitiesOnly yes</span>

</div>
  
<span style="font-family: Courier New, Courier, monospace;">IdentitiesOnly</span>
ensures that only the specified key is used for that host; if you don't
have this, [you may end up failing to
authenticate](http://superuser.com/questions/187779/too-many-authentication-failures-for-username)
as too many incorrect keys have been passed to the server.  
  
If you're using the key in this session, you might need to ssh-add it.
In my case, on Ubuntu 12.04, on subsequent logins, the new key was made
available automatically.  
  
\*Unlike GitHub, Bitbucket only matches commits when the commit contains
an email address that has been confirmed on Bitbucket, so any commits
you make aren't matched to your user account.You can override this by
setting aliases, but this is on a per repository basis and you can't do
this unless you're an admin of the repository.  
  

</p>

