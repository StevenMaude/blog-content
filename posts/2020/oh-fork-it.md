Title: Oh, fork it
Date: 2020-06-19 12:35
Modified: 2020-06-19 20:39
Author: Steven Maude
Tags: GitHub
Summary: Why you should fork obscure, interesting repositories

## Lost…

At work recently, I was trying to find a GitHub repository that I knew I
had previously seen a while back.

But I couldn't find it.

Normally, I would "star" possibly useful repositories: it wasn't in that
starred list. After spending a fair length of time trying to rediscover
the repository by many searches on GitHub and on search engines, I
concluded that maybe the author had simply deleted the repository or
their account.

And so I gave up.

## …and found

Sometime later, while reading a related GitHub issue, I spotted I had
written a comment linking to the repository. It was still there, just
not easily discoverable.[^1]

## Lessons

Things shared on the internet have no guarantee of longevity. You are
subject to the whims either of service providers either disappearing
entirely, or [removing a user and all their
content]({filename}../2017/rinse-fms-soundcloud-takedown.md).

Users themselves may also delete things they've previously shared.
Especially in a post-GDPR world, where people are likely far aware of
their ability and rights to do just that.

Even if I had starred the elusive repository, that would not have helped
if the user deleted the repository or the user's account disappeared.
For popular repositories, there is no likely threat of them vanishing
entirely overnight, because there are probably several existing forks.
And users may well restore a copy of such a deleted repository from
local clones.

But if a repository is obscure, then that published version may be the
only source readily available.

So, if there is some GitHub — or other online Git remote — repository
that looks interesting or useful, but is relatively obscure, then
forking it is prudent, and a one click operation without requiring you
to store a copy locally.[^2]

It may not be that often when people or organisations decide to delete
all their code, but it [does
happen](https://www.theregister.com/2016/03/23/npm_left_pad_chaos/).
Even if you may not necessarily have the final version before deletion,
something may be better than a distant memory.

[^1]: After all that effort, I actually decided to use a different
      approach anyway.
[^2]: Of course, cloning locally is another valid approach, but requires
      you to store content that may just be clutter on your local storage.
      I'd wager if GitHub was to end their service, then there would be
      more than a day's notice.
