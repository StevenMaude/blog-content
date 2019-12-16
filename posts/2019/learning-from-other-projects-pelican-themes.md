Title: Learning from other projects: pelican-themes 
Date: 2019-12-16 22:41
Author: Steven Maude
Tags: git, project management
Summary: Taking a look at pelican-themes — a project I currently use — to learn from it.

## Lack of updates

At the time of writing, this blog uses Pelican to convert the Markdown
blog content into publishable HTML. And, if you noticed from the dates
on my posts, there has been just over a year between the last post and
this one. This was mainly because there was considerable work needed to
get this blog setup up-to-date: both in upgrading Pelican to the latest
version, and pulling in updates to the theme.

Updating the theme was made slightly more complicated by the migration
of the theme from its [original
repository](https://github.com/DandyDev/pelican-bootstrap3). The new
home became the
[pelican-themes](https://github.com/getpelican/pelican-themes)
repository, not as a submodule but as the definitive repository for that
theme.

In the past, it was simpler for me to simply pull request changes from
the parent of my theme's fork directly into my fork. Instead, I had to
restructure my repository slightly and start to `git cherry-pick`
individual commits that were applied to the theme within the repository.

Anyway, I've caught up on the maintenance. Bootstrap 3 is now
[end-of-life](https://blog.getbootstrap.com/2019/07/24/lts-plan/) so
there is a longer term issue of this theme still being stuck on it. If I
end up migrating to a new theme, it might be worth investigating using
[Hugo](https://gohugo.io/) instead of Pelican at the same time. Hugo has
increased in popularity considerably since I started using Pelican.

## Learning from other projects

While spending a fair amount of time updating my theme and working with
the pelican-themes repository, I had chance to think about how the
pelican-themes repository is structured and lessons I've learned just
from having to work with it.

Reading and understanding — or at least attempting to understand —
other people's source code is a way of picking up new ideas or concepts.
What might also be useful for learning is looking at projects you use as
a whole. How are they organised? How does that makes them easy or
difficult to work with?

There is a caveat that even a public source code repository doesn't
necessarily yield all the decision making that went on to get it to such
a state. Some of that process may indeed be located with the source
repository, e.g. pull request comment threads or issues. Some of that
process may be separate to the source repository, but still public, e.g.
public mailing lists. Some of that process may be entirely private, e.g.
emails or private working documents. Some of it may be undocumented at
all and reside entirely within maintainers' heads.

## pelican-themes

### A note

The tone of this post shouldn't be considered as a ranting "why, oh why,
is this project not doing things the way I suggest?" post, but primarily
an exercise to just consider and note other ways it could have been
structured.

It's an actively maintained project, and the maintainers are
volunteering considerable amounts of their own time doing just that.

In many projects, whether by a single developer or a team, whether
commercial and proprietary or open source, it's also entirely believable
that there's no long-term maintenance plan from the outset. At the
start, it's not even known whether the project will have a long-term
future. The first commit of pelican-themes was in February 2011, making
it nine years old in 2020. Often, things do just get worked out along
the way.

### The current state

[pelican-themes](https://github.com/getpelican/pelican-themes/) is a
mixture of submodules and themes whose files exist entirely in the
repository. The included non-submodule themes sometimes (if not often or
even always) use the pelican-themes repository as their definitive home.
There are a few problems I've seen with this approach, exemplified by
the theme I am currently using my [own
fork](https://github.com/StevenMaude/pelican-bootstrap3-sm) of,
pelican-bootstrap3.

Back when pelican-bootstrap3 was still maintained by its original
developer, there were actually changes made to the version in
[pelican-themes](https://github.com/getpelican/pelican-themes/commit/c817f12a9f5034a05abec4d2515adabd003f9ac0#diff-32c97fb49ece91afc9f43c8405423109)
that diverged from pelican-bootstrap3. pelican-bootstrap3 within
[pelican-themes](https://github.com/getpelican/pelican-themes/commit/faa85d6112a759767a4f327e35a07fa55d9e747e#diff-0eb6cb930365747af1fe070650593b8e)
was then updated by simply a straight copy over of the then-current
version of the upstream theme, losing the changes made to the
pelican-themes version. Apart from losing work, this process can be
potentially confusing for users not directly following the development
process; you can have something that was fixed, then *unfixed*.

Later, the official home of pelican-bootstrap3 became the pelican-themes
repository as the original developer [no longer wanted to support
it](https://github.com/getpelican/pelican-themes/pull/383). This had a
couple of consequences.

First, it meant that the pelican-themes maintainers adopted the extra
maintenance work of a popular theme. Those maintainers may not even
*use* the theme. This means that pull requests can languish, perhaps
because the maintainers don't feel that comfortable merging substantial
changes or don't have strong opinions on whether the proposed changes
are worthwhile. For pelican-bootstrap3, at the time of writing in
December 2019, there are several unmerged pull requests on
pelican-themes right now, even as [far back as
2016](https://github.com/getpelican/pelican-themes/pull/414).  Pull
requests left unloved and unmerged are a deterrent to other developers
who may be considering contributing other changes.

Second, even if pull requests are regularly merged, there may be less of
a definitive direction taken than if maintainers have strong opinions
about where that subproject is headed. It can also lead to a lack of
quality assurance. For pelican-bootstrap3, an example is this
[translation
feature](https://github.com/getpelican/pelican-themes/pull/441). Such a
feature is one that's useful to lots of people, but unfortunately it
[broke things](https://github.com/getpelican/pelican-themes/issues/460)
for users who didn't have the same plugin configuration as the original
author, affecting those users who did not intend to use the new feature.

### How else might pelican-themes be managed?

That's how things are structured in pelican-themes now. I did think
about other ways the repository might have been structured taking the
above features of how it works right now into account.

* pelican-themes could simply have been a list of links to themes,
  solely a reference resource.
 
    The advantage of this is no management on the part of the
    pelican-themes maintainers is required except to add new themes or
    remove themes that are no longer supported or unavailable. In many
    cases, once a theme is added, that would be as much as is ever
    required to be done for that theme. The big disadvantage is that you
    can't just clone the entire repository and have all the themes ready
    to use. 

* There could be a "more strongly" monorepo version of what there is
  now, that is, pelican-themes could be a pure monorepo with no
  submodules.  This now means that *every theme* has to be
  hand-maintained by copying from the upstream version repository, if
  pelican-themes isn't the original repository for a theme. This
  doesn't, however, solve the problem of having a mixture of maintained
  and unmaintained themes.
* Going completely in the opposite direction is an option too: have
  every theme in pelican-themes included as a submodule. This has the
  advantage that pull requests into pelican-themes would be simple,
  simply reflecting a submodule update to the parent repository's
  current release.
  
    It would mean that every theme in pelican-themes where
    pelican-themes is the definitive repository for that theme would
    need to be moved to its own individual repository. However, breaking
    out the themes in this way might make it easier for those themes to
    be managed by specific maintainers for each theme only (provided
    volunteers could be found), as opposed to the current agglomerate
    repository maintained by developers who may not use most of the
    themes present.

Of course, the problems described above are easy to spot when using a
project that's been around a while, but perhaps subtle at a project's
inception. I think this is symptomatic of software development. It is
possible to build something that takes on a direction beyond that
originally envisaged, especially projects that have many contributors or
maintainers over time, each of which may have their own opinions as to
how such a project should be nurtured.
