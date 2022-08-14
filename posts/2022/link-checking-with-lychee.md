Title: Link checking with lychee
Date: 2022-09-07 21:11
Author: Steven Maude
Tags: blog, documentation, documentation as code, link, lychee, URL, research software engineering, writing
Summary: A rundown of validating URLs with lychee

## The use of URLs in writing

Lots of information these days is on the web. Here, you're looking at
some.[^1]

And with that, this means that URLs, often in the form of links to web
content, are also heavily used in all kinds of writing: other web pages,
reports, papers, books.

In some of those cases, writing is published and then largely "done",
unless there's a revised edition. Writing on the web is, ideally for the
reader, maintained, if that's appropriate. Even if you're not
maintaining the links after you've published something, you might want,
if you're writing over a long period of time, to at least assert that
the links you may have added sometime ago are still valid at
publication. Electronic formats at least offer this possibility, even if
that possibility is often unfulfilled.

Writing often becomes less relevant with time — particularly in the
current climate of "content creation" (and it is difficult to see right
now how this might ever slow down). But some ideas do have a more
enduring relevance. Although, even if the ideas endure, the URLs linked
as part of that work may not. Often, an author may link to sources they
did not create and do not have any control over. If a resource you don't
control disappears, then, well, it disappears.

## Validating links

So, let's assume what you've written is useful or relevant, at least, to
readers present and future. How can you validate that the links you have
in whatever documents you're dealing with are still functioning?

You could hack together a shell script or similar that will do this and
give you a good idea of which links are broken. It's often less work to
choose existing software, should something suitable exist, for fairly
common tasks. The authors have then done the work for you, including
thinking about handling any awkward cases or behaviour.

[lychee](https://github.com/lycheeverse/lychee) is one such program
designed to check URLs in collections of text-based source files. You
can also run it against a website, but I've found it most useful for
"local"[^2] files.

A lychee link check runs *very* quickly. Each run gives you a summary of
how many links were checked, how many were successful and reasons for
failures. As a guide, the link checking step in a GitHub Actions lychee
run takes about 10 seconds for a site with about 450 URLs.

### What's nice about lychee

lychee is particularly useful in that it can check various plain text
formats: whether HTML, Markdown, reStructuredText, or other text files.
You can also point to an existing website and check the links there.

On top of that, lychee is cross-platform. Since I have always run it via
GitHub's hosted virtual machine runners, it's perhaps less important how
it runs.

As a quick summary, it's nice that it worked well from the start,
without spending lots of times debugging. The results I initially got
from it were, on the the whole, useful.

## Possible applications

There are more uses than you might first think of:

* web content (the obvious use)
* "formal" documentation sources
* collections of less formal READMEs that act as documentation within a
  coding project
* a research paper or thesis, to check the links before submission
* anywhere else you have a collection of text files (applied to
  collections of notes, or digital
  [Zettelkästen](https://en.wikipedia.org/wiki/Zettelkasten) or similar)

And checking links has the auxiliary benefit of checking your own
content: if the links that relate to a particular point are defunct, it
may be that the underlying information or situation has changed. That's
particularly the case with computing where information can date rapidly,
due to software or hardware developments or changes in best
practice.[^3]

## Some usage notes

### Within GitHub

It is possible to run lychee within a GitHub Actions runner. There is an
existing [action](https://github.com/lycheeverse/lychee-action) or you
could write your own workflow to download and run the latest version.

This way, you can run lychee automatically, either on a schedule or on a
pull request. This works relatively well, with the additional benefit
that the link checking isn't being done using your own internet
connection.

Other tips for running in GitHub Actions:

* For checking GitHub links, you may want to use `GITHUB_TOKEN` with
  lychee or the action which avoids rate limiting. You may want to
  restrict that token, to, for example, just *read* the contents of the
  repository with the `permissions` key.
* GitHub Actions runners get blocked by various sites, so you may have
  to exclude a few links. You can add a `.lycheeignore` file which
  allows you to specify links via regular expressions.
* You cannot check email addresses within a GitHub-hosted runner, so you
  need to use the `--exclude-mail` option.

### Outside of GitHub

Restrictions outside of GitHub might be less onerous, but at the risk of
getting your IP address rate limited or even temporarily blocked. So I'd
be very wary of running something like lychee using a personal internet
connection.

If you have access to cloud virtual machines, that might be another
option. However, the IP address ranges that such a virtual machine might
have could already be blocked by the sites (or their hosting providers)
that you're trying to check.

There are two things you could do to be careful:

* Set a maximum number of concurrent connections.
* Run the `--dump` option just to see which links would be checked; if
  there are any in there which are important for you to access for and
  might rate limit or block you, maybe consider adding them to the
  `.lycheeignore`

### Wherever you're running

Basic authentication is supported for logging into sites, but links that
require some kind of two-factor authentication can't be checked. Whether
you want to go to the trouble of creating an account, particularly if
that account's credentials are solely for GitHub use, just for checking
a few links is another question.

### Integrating into a document's build process

#### A rough strategy

Initially, particularly for a collection of files that may have not been
written or reviewed recently, it's likely that there are several broken
links.

This is the approach I've taken:

1. Run lychee.
2. Review the error log.
3. Check and classify the failures.
4. Decide whether to fix up links, or ignore them by adding to a
   `.lycheeignore` file.
5. Repeat the previous steps until you have no errors.

You can see a real-world example of this [that I used at
work](https://github.com/opensafely/documentation/issues/642).

#### Resolving failures

Failures tended to fall into one of these categories:

* Genuinely broken links.
* Links to resources that are restricted to authorised users: you need
  to login first.
* Links that were inaccessible from within the GitHub Actions runner
  virtual machines.
* Internal Markdown or HTML template links that were not getting
  interpreted correctly, and, in some cases, could be corrected.

My approach has been to skim through the errors by hand and classify
them. You can also get JSON output if it's useful to have a directly
machine-readable format.

From the errors and your investigation, you can create a `.lycheeignore`
file: an exclusion list of links. That file is used if it is in the
working directory, or you can specify its path explicitly via lychee's
options. Adding a `.lycheeignore` file at the top-level of your source
repository, if you are using a version control repository, works well.

You can specify exclusions by regular expressions: excluding subdomains
works quite well when there are multiple links to that subdomain. You
can just include the direct URL if there's just one specific URL for a
specific domain you want to exclude. It's worth generalising the
exclusion once you get more variations of a single URL or domain.

For fixing up broken links, then either you need to find where the
relevant URL has moved to, if it is still available, or review whether
the [Internet Archive](https://web.archive.org) has a copy saved. If
it's for a blog post, you might want to pick a version that's close in
date to when you added the link to that post: that version is possibly
what you'll have been reading. Alternatively, you could review the most
recent available version and use that version if suitable.

For the couple of projects I've tried lychee with, it's able to check
something like 80-90% of URLs. The checks have been useful and have
flagged URLs and surrounding text that require updating. This will vary
depending on where the URLs you are checking point to though.

### Miscellaneous tips

* If you are particularly finicky, it is possible to flag redirects by
  setting the number of maximum redirects to 0. And it is possible to
  check for non-HTTPS web URLs: these days most URLs should be available
  via HTTPS.
* You can set another User-Agent. I've not tried this to see if it
  improves the accessibility of some URLs.
* Excluding directories is, at time of writing, clunky; see the
  [associated GitHub
  issue](https://github.com/lycheeverse/lychee/issues/470). This is the
  only finicky usability hurdle I've encountered.
* If your documents are not in a supported format, lychee is still
  potentially useful. You would need to export your document to a plain
  text format, either in whatever authoring tool you are using, or with
  something like [pandoc](https://pandoc.org).
* There are lots of other options that you can use with lychee: take a
  look at the documentation.

## Persistence of web content

So, you can probably tell: I think lychee is a really useful tool.

However, its usefulness comes with a caveat: **all lychee can do is tell
you whether a link is accessible or not**. But, wait, you might argue:
that's the whole point of this post that I'm reading — we *want* to
check links, right?

In a way, yes.

All a valid link tells you is that the relevant resource provider has
some resource available and accessible at that URL.

It **doesn't** assure you that whatever you've linked to is in anything
like the state it was when you read it. There are no guarantees that
typical web URLs point to static or immutable content. They work more
like pointers: it's up to the relevant server hosting the URL's domain
and the people who put content on that server that decide what the
content is.

In many cases, this could be fine. In others, maybe less so:

* The original author may have updated their content in a way that might
  change the relevance to whatever argument or citation you intended to
  make.
* Another organisation could have taken over (perhaps legitimately,
  perhaps not) the site and decided to post a contrary view, or
  something entirely different at the same URL.

Making HTTP requests and checking for a non-error response codes only
tells you that a resource is available at that URL, whether directly or
with redirection somewhere else. It doesn't guarantee that a resource is
actually as you read it, when you read it.

### Preservation

You may now be thinking: well, I could just take a copy and link to
that, providing my own cache of the resource as it was when I reviewed
it. That would work, but hosting that copy is probably a bad idea:

* There are potential copyright issues.
* If you're intending to host this copy on the web, then, if it is
  public and discoverable, it's possible that search engine providers
  think you're up to some kind of nefarious search engine optimisation
  shenanigans.[^4]

Much simpler is linking to the [Internet
Archive](https://web.archive.org): either finding a "good" copy there
already, or using their page save feature to archive a copy of the page
there and then.

Wait, so why wouldn't we just always link to the Internet Archive?

In some limited cases, this might be useful, where you want readers to
have the information as you accessed it at the time. That is
particularly useful if you are specifically citing a work and the
version available at a given time. In many other cases, it is still
useful to link to the "live" resource because:

* You may be pointing to an interactive service, and the Internet
  Archive's more static version may not function correctly, without
  access to the original host's backend servers.
* You may want your readers to always access the latest published
  version of the information that you link.

If we link to the original host instead of a third-party preservation
service, this does pose the future risk of the resource being
unavailable in future. But tools like lychee can definitely help with
maintaining working URLs.

And, finally, if you're now asking: "what guarantees are there on
availability and integrity of the content the Internet Archive hosts".
Or maybe more succinctly: "who archives the archivers?" Let's say that
those are also good questions, but there are already enough words here
not to worry about this here and now.

[^1]: Unless you've tried to subvert that by printing this out. You
  rascal.
[^2]: The quote marks are because all my running of lychee has been via
  GitHub Actions: a "local" checkout of my source files on a remote
  virtual machine.
[^3]: Indeed, Stack Overflow are finding this a problem. It turns out
  that sifting through years of accumulated answers, some now
  deprecated, is a [big spring cleaning
  task](https://meta.stackoverflow.com/questions/405302/introducing-outdated-answers-project).
[^4]: That said, there is less evidence from Google's search results
  that this rule is actually *enforced*. Sites that are obviously
  cloning contents from other sites do sometimes rank quite highly.
