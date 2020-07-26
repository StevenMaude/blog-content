Title: Continuous integration with GitHub Actions
Date: 2020-08-02 14:38
Author: Steven Maude
Tags: automation, continuous delivery, continuous integration, GitHub, GitHub Actions
Summary: A look at GitHub Actions, and the good and bad of coupling automation
         to a remote repository provider

## A quick review of GitHub Actions

I've been using [GitHub Actions](https://github.com/features/actions) a
lot recently. It's a continuous integration and continuous
delivery/deployment (CI/CD) tool that's, unsurprisingly, part of GitHub.

As the vagueness of the "D" in "CD" might indicate, different people
have different interpretations of how you actually define these terms.
For this discussion, let's just take it that these tools encourage
developers to automate many software development processes that don't
involve writing code. There's an aim of frequently getting changes into
the main development branch, with minimal manual labour and aiming for a
good level of quality control, trying to avoid broken code getting
deployed.

So, I've been using GitHub Actions a lot, both for personal projects and
at work. And I've enjoyed using it. It's reasonably easy to use, and
there's a quick feedback loop from you pushing a workflow to seeing it
run. This in turn makes it fun to work with; it puts you in a frame of
mind where you ponder what development tasks you could automate.

Where GitHub Actions lacks is often for want of a little polish and
refinement are needed. I'll mention three examples. First, the
[documentation](https://docs.github.com/en/actions) occasionally lacks
simple concrete examples for some of the features. The early parts of
the documentation are actually example-focused. But then many of the
features are simply all piled into a reference section at the end.
Additionally, I don't know what exactly it is about the page design or
the structuring of the documentation, but I did find it difficult to
find precisely what I was looking for. That was the case even when I'd
actually read some information before and knew it was hidden there,
somewhere.

Often I've found more useful information elsewhere. Other helpful places
I've found have included: GitHub's Architecture Decision Records in the
[GitHub Actions Runner](https://github.com/actions/runner) repository,
Stack Overflow, other people's GitHub Actions workflows, and
documentation for third-party actions.

Second, at time of writing, there is no simple way to remove repetition
within workflows and between workflows. For instance, you might want to
run tests before you merge pull requests, and might want to do the same
when you build and publish a new release. At the moment, this means
duplicating part of one workflow in another, or creating a custom
action. GitHub are planning to add ["composite"
actions](https://github.com/actions/runner/issues/438) soon which should
help simplify this type of common reuse.

Finally, workflow steps do not have a non-failing "neutral" outcome.
(Apparently, this did use to be a feature during the GitHub Actions
beta.) You might design a workflow with a step that could determine
whether subsequent steps should run or not. Without a neutral outcome,
there is no easy way to indicate "no error, but we have stopped the
workflow early". The only way to directly exit the workflow at that
point is to fail. But this isn't semantically what is intended: this
type of exit may be an expected valid state and not a workflow failure.

Alternatively, you can continue without failing by specifying
`continue-on-error: true` for a step. But now all subsequent steps will
run, which we don't want: maybe those steps will waste a sizable chunk
of our Actions minutes quota and/or maybe those steps will fail too. To
skip the rest of the steps when they're not needed, conditional checks
on "success" of steps can be threaded through the subsequent steps of
your workflow. But this complicates the workflow, a "neutral" outcome
would simplify this entirely by allowing us to exit, without failure, at
the point where we really do want the workflow to stop.

### Competitive pricing and features

GitHub Actions does well on bundling free usage minutes, even for
private projects. For something like, say [Travis
CI](https://travis-ci.com/), you have to pay a hefty fixed price per
month to get that option. Though it should be noted that Travis CI
pricing includes unlimited minutes, whereas you have to pay if you
exceed your GitHub Actions monthly quota.

However, at current pricing, you could get almost 10,000 monthly minutes
on GitHub Actions using a Linux runner — $0.008 per minute, with 2000
included in a GitHub Free plan — for the cost of the cheapest Travis
plan ($63). So, unless you're using a lot of minutes, when comparing on
price alone, there's no contest.

The other big advantage of GitHub Actions is that it permits far more
concurrent jobs than Travis CI: at the time of writing, a GitHub Free
account has twenty concurrent (non-macOS) jobs. Travis CI offers only
ten concurrent jobs even at the highest "Premium" plan, and just one on
their lowest priced plan. This is important as, particularly if you're
collaborating in a team, your request for a CI job may be blocked by
other outstanding jobs, possibly delaying the completion of your
requested job.

Both Travis CI and GitHub Actions offer free usage in some cases. GitHub
Actions pricing refers to "free for public repositories". Travis CI's
own site mentions "free for open source". I suspect by that this Travis
CI really just mean "your code must be public". And not that anyone
actually checks that your code is published under some kind of valid
open source license.

### Coupling automation to the remote repository host

Price and concurrency aside, what might be consequences of using the
same service — here GitHub — for hosting the repository's code and that
repository's automation?

From a quick search around, there doesn't appear any standard format for
specifying these types of automation workflows. That's not too
surprising. One reason might be that every provider implements their own
features and therefore wants to be able to flexibly specify the
configuration to incorporate those features. There aren't any
transpilers for different formats: I can't take an existing
`.travis.yml` and automatically convert it to a GitHub Actions
`workflow.yml`. (However, there is [an R
project](https://github.com/ropensci/tic) that aims to specify workflow
configurations for R packages agnostically, outputting configuration for
different providers.)

The consequence is that using GitHub Actions means that you now have a
coupling of your code's organisation to GitHub, and adds work should you
migrate to another Git repository host. To be fair, this is likely true
already, even without using GitHub Actions. If you move to a different
host, say GitLab, at the least, you'll also probably want to move the
existing issues from GitHub to the new host. In mitigation of this,
there are often tools or automatic imports for migrating these other
non-code features, like issues.

But, as we've seen, any GitHub Actions workflows will probably need a
manual rewrite to use a similar process elsewhere. This, then, is
probably where using an external automation tool like Travis CI offers a
benefit. If you migrate to a new remote repository host, to get your
automation running, you just need to connect your new host to your
existing automation system. No rewrite required.

On the other hand, it's reasonable to think that external tools are more
awkward to configure and monitor as opposed to comparable tooling that
is a key part of your existing repository host. With an external
service, there will also be some requirement for developers to create an
account there, and then allow the external application to access their
GitHub account. With GitHub Actions, it's just another tab on your
GitHub repository. (Travis CI certainly didn't help themselves here by
previously having [*two* separate
domains](https://blog.travis-ci.com/2018-05-02-open-source-projects-on-travis-ci-com-with-github-apps),
to independently handle free and paid services.)

And an external tool is an additional point of failure. It's possible
GitHub is up and running, while Travis CI is unavailable, or vice versa.
Either service failing can block active development.

## So what's best?

Like many choices, there's no definitive answer. If the CI services have
roughly equivalent features, then it comes down to what other aspects
you prioritise. Is tight integration of your software development
processes a positive — making for potentially easier configuration — or
a hindrance to migration? Is pricing the most critical aspect?

For funded development teams, the pricing issue is perhaps less
important since it will likely still be a small part of an
organisation's budget. Where GitHub Actions is particularly well placed
is in the giving of individual developers an allocation of free
automation job time for their private projects. Together with that
allocation being easily used as part of the service developers are
already likely using, it is challenging for external automation services
to compete.

And that's where my personal view is. I'm still sticking with GitHub
Actions, notwithstanding the slight risk of getting too tied into
GitHub. GitHub is incredibly popular right now, it's where open source
projects are developed, and that network effect is an important one.
