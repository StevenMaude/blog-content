Title: Managing a Bitbucket user's permissions when they've left your team
Date: 2016-04-16 01:54
Author: Steven Maude
Tags: Bitbucket
Summary: Removing users entirely from accessing your Bitbucket team's repositories.

## Kicking the Bitbucket

What I noticed this week is that users who'd left a Bitbucket team[^1]
that I'm currently a member of were still billed as having admin access
to several repositories. But, this wasn't by virtue of being a team
member, as we'd removed them.  Instead, this was via their own user
accounts. This seems like the intended behaviour. It's documented
[here](https://bitbucket.org/site/master/issues/5148/repos-transferred-to-a-team-retain-creator#comment-22446820):
a user gets admin access to the repository when they create it.

I tested this by just creating a new repository that was owned by the
team. Checking the access management settings showed that the team was
the owner of the repository, but I had separate admin permissions for
the repository.

If you've got the required permissions yourself, you can go and clean up
user access on a repository basis, via that same repository access
management settings. A short look around — though short does mean very
short, admittedly — for suitable bits of the API that would let me purge
old users without having to manually click through each repository
didn't reveal anything. Click, click, click seemed the only way to fix
it. And if you have a lot of repositories, that's a lot of clicking.

## Stop it (and tidy up)

Looking now at this late hour, it seems that I was looking in entirely
the wrong place previously. A much, much quicker route to cleaning up is
to browse to your team's page and select "Manage team". From there, look
at "Plan details". There you can see exactly who has access to your
team's repositories and what access type they have.

This might be "group". That is, because they're part of a user group in
your team — groups are another aspect of access management, you can be
in the team, but maybe you're in a group that maybe doesn't have access
to any team repositories at all.

A user's access type can also be "repository", i.e. they have access
because their user account has explicitly set permissions on that
repository.

Clicking "View access" shows you which team repositories they can
access. Next to "View access", there's a cross icon that you can click
to remove **all** the user's permissions from your team. In just one
click. What happens if you do that for a user that's still on the team?
I can't answer that; maybe it boots them out of the team too? (I wasn't
about to try it.)

## A potentially money saving tip

It's sensible to keep access permissions to your repositories to a
minimum to ensure that only users who need access have it. Of course, it
may be that you have equally sensible reasons to retain access for
ex-team members.

However, it's also worth considering how Bitbucket counts users in your
team's plan. The definition of users on the Bitbucket plan details page
is:

> The number of users (including you) with any level of access to one or
> more of your private repos.

**This is whether they are a formal team member or not**. (Team members
without repository access don't count here.) So, this spring cleaning
might allow you to switch to a cheaper Bitbucket plan for your team too.

[^1]: Organisation in GitHub parlance.
