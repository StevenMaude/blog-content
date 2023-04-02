Title: "Docs Like Code": a book review 
Date: 2023-04-02 14:23
Author: Steven Maude
Tags: documentation, docs as code
Summary: A review of "Docs Like Code" by Anne Gentle, and some thoughts on docs as code

## What is "docs as code" anyway?

The book "Docs Like Code" covers the approach of treating software
documentation just as the code that it documents. This approach to often
referred to as "documentation as code" or "docs as code".

It seems that "docs as code" is the more common description. But,
whether intentional or not, the "like" in "docs like code" could also be
considered a pun. That is, not just treating your documentation like
code, but your documentation "liking" code, being handled in the same
way and sometimes in the same repository.

What is meant by treating software documentation as code is that you use
the same kinds of tools, processes and workflows to work on your
documentation, as software developers do when working on code.

This might include some or all of:

* use of a version control system
* collaboration via an online code hosting service
* writing documentation in a markup language
* using a static site generator to build the documentation
* automated checks on the documentation before changes are included to
  the main documentation version
* manual review on changes proposed for inclusion in the main
  documentation version
* automatic documentation build and deployment once new changes are made
  to the main documentation version

Sometimes approaches to solving technical problems can be pushed with a
very prescriptive, dogmatic approaches: do this, use that, do not do
this, why are you using *that*? From what I have seen, one refreshing,
feature of docs as code is that it is not particularly prescriptive
about the *specific* tools that you use. Nor does docs as code say how
much of the tooling you need to adopt.

In some cases, tooling choices might be almost predetermined by
overwhelming popularity: for instance, you can use any version control
system for docs as code, but it is likely that people right now will
choose Git. But this is still left to you to decide for your own case.

Even if you do not intend to adopt a full docs as code approach for
writing documentation, you might benefit adopting some of the closely
associated tooling. For example, you could still run tools like link,
style and spell checkers against your documentation source, even outside
of using version control or automated checks.

## Edition recognition

I actually bought the second edition of this book to read through prior
to giving a talk in 2022 on documentation. I skimmed it, realised that
some of it was understandably outdated seeing given it was published
five years before. On looking again very recently, I found the third
edition, and decided to revisit the book. As it turns out, *obviously*,
the third edition of course got published about a week after I bought
the second edition.

Having just bought and read the third edition, it does generally seem
up-to-date. There was nothing I read that felt like it was giving advice
that was once appropriate, but no longer.

Skimming through the second edition for comparison, it seems like the
main differences are:

* the book has generally been expanded a little; particularly on
  building and testing documentation
* there was a tutorial in the second edition that has been perhaps
  sensibly removed for the third edition, given that tutorials can date
  quite quickly

## What the book covers

The book has three core chapters and a final chapter summary. The first
chapter describes the benefits of adopting a docs as code approach,
summarising why the kinds of tools I listed above are useful.

The second chapter details what you might consider when deciding to
apply docs as code to a project: from requirements, to thinking about
the tools you might use, and how you might organise repositories.

The final core chapter describes some of the features of working on docs
as code projects. You need to think about how to make it easy for
contributors to work on the documentation, how changes are incorporated
into the repository, how to review and approve those changes, how you
will publish and release, and how you use automated tooling to help with
tasks.

Although the book is written from the perspective of practitioners who
have applied docs as code in enterprise projects, the book is not overly
sanguine. Some of the challenges of docs as code are also described:
getting adoption from a wider team, that is both from developers who may
not feel like documentation is their responsibility, and writers who may
be less comfortable using a different, and perhaps more complicated, set
of authoring tools than they are used to.

Quite rightly, the authors highlight that working with Git and online
code hosting platforms like GitHub has a considerable learning barrier
to overcome for new users. Certainly, once you *do* feel a little bit
more comfortable with Git, it is easy to forget how much of a struggle
it is when you start out, with several opaque and mysterious commands
that you need to know.[^1]

## A few small criticisms

While I did not generally disagree with anything I was reading, I did
feel like the book could have done with another proofread. I probably
would not be so picky, but the authors[^2] are technical writers by
trade.

Some presentational examples:

* there is one particularly horrendous bit of word spacing over a couple
  of sentences where all the words just run into each other
* there are a few footnotes that are then immediately and pointlessly
  duplicated

There were also a couple of small technical points that I queried as
reading: for example, the claim that Ruby:

> predates Python by about four years

Perhaps the authors just got the two mixed up. From reading around, it
seems that this is the other way around, as I instinctively thought,
with Python being older.

Finally, glossaries are included as part of the main text and this feel
incongruous, particularly early on in the text. In the second edition,
the glossary was included at the end, which feels less daunting than
throwing lots of Git jargon at the reader, when the reader probably does
not really need it to understand most of the book. The authors do remark
that the book is not intended to teach the reader about Git or GitHub.

These are all relatively small complaints, however, and do not really
detract from the book itself.

## Origins of docs as code

As mentioned, the authors seem to have a technical writing background.
Without researching it, my hunch would be that some of where the push
for docs as code has come from is more from technically skilled writers,
more so than for developers, and some of those realising that they could
use the same tools as developers. That is my personal guess: the book
does not actually give much of a history of who actually originated the
idea of docs as code. Instead, a timeline of major organisations
proclaiming public support for the docs as code approach is given.

These origins might also explain the lack of dogmatism around what you
should and should not do that I alluded to above.

Even without knowing that docs as code is a described concept, I suspect
that developers would naturally favour a docs as code approach for
documentation, if developers were given a choice in the isolation of any
external considerations or requirements. It is a natural extension of
how developers often work: developers routinely work in a repository,
collaborate on code hosting platforms, and often implement automation of
checks, builds and releases.

Personally, I even write collections of notes and writing in plain text
markup and store in Git repositories, even when the intent is to just
collate that text, without any further publication. Creating and working
on Git repositories is a quick and powerful process, once you are
accustomed to it.

## Where next?

The authors do also quite rightly point out that docs as code is an
approach that can be at least considered at all scales. It is as valid
to consider for single developers maintaining their own software, as it
is for much larger organisations working on bigger collaborative
projects. Because this is a flexible approach, and one that can gel well
with developers working on code, it does seem likely that it will
continue to persist and gain increased adoption and recognition.

Though I did not learn much new from the book, I am perhaps not the most
appropriate audience — the authors recommend it for technical writers
and ther managers. My reading was still useful to be reassured that lots
of ideas that I have learned from various places, without much formal
training, are not incongruent with those of people who do primarily work
on documentation.

Though the book seems a good summary of where docs as code is right now,
what is not mentioned is much of where the authors anticipate future
trends. They do allude to artificial intelligence and machine learning
tools being used as auxiliary supporting helpers when writing. With the
rate that large language models are developing, and finding application,
it does not seem unreasonable that this might be a considerable shift in
the near future.

One of the barriers for the uses of large language models is that what
they output does not always necessarily make sense, or may be
inaccurate. But writing usually involves editing as a central part of
the process. Adoption of automated tools here, when you anticipate
editing regardless of where the author's material originate, seems a
natural fit. One of the interesting conclusions from Hannah Fry's "Hello
World" is that automated tools may be particularly valuable to do
tedious work or heavy lifting, but are likely to be particularly useful
when used in partnership with humans. This seems like it could be the
case for future writing.

What that means for docs as code is that the integration of code with
documentation — where code is actually aiding a considerable part of the
authoring of documentation — may become even closer.

[^1]: I think the Git developers have made some efforts to make its
  interface more consistent, but I suspect the initial barrier to
  learning is still there. Whether tools like GitHub Desktop can help
  here, I am not sure. Really, the problem is that having an
  understanding of how Git functions is helpful to be able to use it,
  and there are several concepts you need to learn at once.
[^2]: Why "authors"? Strangely, there are three listed authors in the
  third edition, including the named author. In the second edition, two
  of the third edition's authors are listed as contributors. In any
  case, I have used the plural.
