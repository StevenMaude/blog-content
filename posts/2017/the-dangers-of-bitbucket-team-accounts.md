Title: The dangers of long forgotten Bitbucket team accounts
Date: 2017-02-04 21:30
Author: Steven Maude
Tags: Bitbucket, security
Summary: The security issues of having a legacy Bitbucket team account
         still active.

Last month, I'd been reviewing some of the shared accounts for online
services we have at work. Often, users have an individual login for
online services. Some services don't offer that feature and there's a
single account that's shared by everyone. While digging around, I found
details for a shared Bitbucket account. If everyone has their own
Bitbucket account, then what's this one?

Logging in worked, and allowed me access to an account for the team
itself; there was no user, as such. Not only could this team account
access the team, but with full permissions. Furthermore, this account
had no settings of its own. If you accessed the settings page, you got
the team's settings, not that of this team account, so it wasn't
possible to change any security settings for the account.

With one of these "legacy" accounts lying around, it's possible that it
is sat there with only password authentication — Bitbucket [introduced
two-factor
authentication](https://blog.bitbucket.org/2015/09/10/two-step-verification-is-here/)
late, in 2015 — an unchangeable (and maybe weak, depending on your
policies) password, and with full team access.[^1]

What makes this particularly insidious is that if you're not aware of
this account, you'll be blissfully unaware if you look at the list of
users on your team. Even if you manage the team as an administrator,
**this team account didn't appear as an admin user**. I don't even think
it counts as a billed user. Someone who gains access presumably could
maintain that silently without you being able to do anything about it,
at least if they just sat there cloning your code. Mitigating that is
the audit log which would be a giveaway if anything noisy happened. By
that point though, someone malicious could still cause a lot of problems
for you by, let's say, booting out all other team members, or deleting
all your repositories.

In the end, I had to contact support and request them to remove this
account, since there was no way I could fix this as a team
administrator. Therefore, this is definitely something worth auditing if
you think you might have such dormant accounts, even though, according
to Atlassian, this shouldn't be the case at all. They [earlier
stated](https://blog.bitbucket.org/2014/01/14/important-changes-are-coming-to-teams/):

> Starting February 18, 2014, Bitbucket will remove the ability for
> individuals to log into a team with a username/email and password.

Insert your own [Unicode shrug
character](http://www.unicode.org/emoji/charts/emoji-list.html#1f937)
here.

[^1]: Creating new repositories failed, but, for instance, creating a
repo using my account (as a team administrator), then logging in as the
"team account" and using the team account to delete the test repo was
successful. I didn't test removing team members, but don't see why this
would have failed.
