Title: git: nice and lease-y
Date: 2018-11-10 13:23
Author: Steven Maude
Tags: git 
Summary: Why generally using `git push --force-with-lease` over `git push --force` seems sensible.

## Can you feel the `--force`?

Force pushing to a remote repository that others may be using should
always be done with care. Even if it's a completely private repository
that only you use, you maybe should double check your thinking before
going ahead.

The double edged sword of a force push is that you're changing the state
of the remote repository history irrevocably.

This can be good, for instance, if you're working on a non-master
repository branch that you "own" and have perhaps cleaned it up:
rebasing it, removing or squashing unneeded separate commits.

It can be bad if you force push to master on a repository, and cause, at
minimum, considerable inconvenience for other developers. Those
developesr may now face working out what exactly has happened to the
repository, when they try and integrate their future changes, or may be
baffled that a previously existing commit has now mysteriously
disappeared.

If you're working on a non-master development branch, you may be a
little bit more lax in how you force push. Certainly, the way I've used
branches with other people is that generally a branch is owned by one
particular person, and those are free to be amended by that branch owner
(usually the creator of that branch, although ownership may be passed
from person to person). Then, as the agreed owner of such a branch,
provided I know that I'm happy with the local changes, I can just force
push to that development branch.

However, that's not always the case. Perhaps two people are working on
the same branch, maybe working on slightly different things, e.g. one
could be working on frontend changes for the site, while another works
on backend changes, but these changes are part of the same feature, and
therefore need to be part of the same branch. 

## What `--force-with-lease` offers over vanilla `--force`

What I discovered recently, although it's been around for ages, is that
git has another option for forcing push: `--force-with-lease`. What this
option does is checks that the remote branch is still in the same state
it was when you last pulled it, and refuses to force push if not, i.e.
there have been no other changes to the branch in the intervening time.

Of course, you can always still override this check by just using plain
old `--force`. But `--force-with-lease` at least gives you another
safety check before force pushing, just in case someone else has altered
the remote branch (giving you chance, for example, to pull that branch,
and rebase your changes on it), and avoiding any confusion between
developers, and potentially loss of work.

Note though, [as this answer
highlights](https://stackoverflow.com/a/43726130), if you have an editor
or other scheduled task running `git fetch` in the background,
`--force-with-lease` won't offer any protection as the remote tracking
branches that would be stored locally are being periodically updated.
