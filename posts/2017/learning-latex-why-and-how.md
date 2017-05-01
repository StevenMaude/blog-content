Title: Learning LaTeX: why and how 
Date: 2017-05-01 15:02
Author: Steven Maude
Tags: LaTeX, document preparation, word processor
Summary: The pros and cons of LaTeX and Word; why you might want to learn
         LaTeX, and how you might do that.

## ShareLaTeX

Today I saw [this
documentation](https://www.sharelatex.com/learn/Learn_LaTeX_in_30_minutes)
from ShareLaTeX linked on Hacker News and, as I haven't used LaTeX in a
while, thought I'd quickly skim through to see what I remembered. And I
started reminiscing about LaTeX which I'd been using semi-regularly
around a decade ago, eventually writing a circa 300 page thesis with it.

If you've never encountered it before, LaTeX is a free software project
that is described by the [project's site](https://www.latex-project.org)
as:

> a high-quality typesetting system; it includes features designed for
> the production of technical and scientific documentation.

There's nothing to stop you using it for other types of documents too;
those are just the areas where it's traditionally used, particularly in
academic circles.

Back to ShareLaTeX. First, the ShareLaTeX documentation looks pretty
good if you need something to get you started.

I haven't used ShareLaTeX recently although I think I tried it out a few
years back and it seemed fine enough. It's a web app that lets you
prepare LaTeX documents and, if you pay, collaborate on them. One big
advantage I can see of using a web app for LaTeX beginners is that it
removes one of the barriers of starting with LaTeX: installing
everything.

## Installing LaTeX on Windows

I've not had cause to use LaTeX much recently, so haven't tried
installing on Ubuntu; a lot of my writing is done via Markdown, whether
technical documentation or words like the ones you're reading now on my
blog.

On Windows, it used to be reasonably simple to get a working system with
[TeXnicCenter](http://www.texniccenter.org) and
[MikTeX](https://miktex.org), but you'd still have to get a PDF viewer,
like [SumatraPDF](https://www.sumatrapdfreader.org) integrated into that
for previewing. This [Stack Exchange
answer](https://tex.stackexchange.com/questions/116981/how-to-configure-texniccenter-2-0-with-sumatra-2013-2016-version)
may help with integrating the PDF preview.

Though that's still three different bits of software you have to get
working together, so not a trivial task by any means. From memory,
install MikTeX first, as TeXnicCenter can detect it during install and
configure its own settings to use your MikTeX installation without you
needing to set things up by hand.

## Starting out

The ShareLaTeX documentation just starts out with creating a basic
document and has you working through following their example. That's
fine to see things piece by piece. Beyond that the single suggestion I'd
have for a new user to learn effectively is to take a completed document
you have written, representative of what you'd like to create using
LaTeX, and then **struggle through recreating that existing document in
LaTeX**.

And it may well be a struggle, but this has a few benefits:

* It's presumably a finished work, so you don't have any time pressure
  for completion. With a deadline to meet, as soon as you encounter
  issues with LaTeX, you'll likely fall back to whatever word processor
  or document creator you're comfortable with to get the job done, and
  then give up on learning LaTeX.

* Using a document similar to that you'd usually be writing, you'll
  encounter many of the issues in LaTeX that you'd hit doing so, and can
  solve these without the aforementioned time pressure.
  
    In my experience, it was graphics and, especially, table layouts
    that caused the most problems, but you may have particular
    typography requirements that require some package to be installed,
    or some subtle override of the LaTeX defaults to change.

    Finding these solutions is not always quick, but I imagine there are
    more forum posts, [Stack Exchange](https://tex.stackexchange.com/)
    questions and blog posts around than there were when I started, so
    it's likely someone's encountered and asked about the same issue
    you're dealing with. The LaTeX Community forum was also a good
    source of helpful solutions from knowledgable people even in its
    early days ten years ago, and [still lives on
    today](http://latex.org/forum/).

* A completed document gives you a reference for getting started in
  future.  You can use it as the basis for a new document, instead of
  starting from nothing, or you can just refer back to it and copy and
  paste appropriate bits of formatting markup you need.

## LaTeX versus Word

### LaTeX installation

As I saw it when learning back in 2007ish, LaTeX was more difficult to
get started with than the likes of conventional word processors: the
installation isn't trivial, and you need several things other than your
desired text in a LaTeX document before you can get that text to
display. In a word processor, you can just start typing. So there's some
level of competence you need just to make *any* old document, let alone
the one you actually want to make.

### Word woes

Word is easy to get started with, but Word had, and maybe still has, its
own problems: again, going back to 2007, to when Word 2003 was still
popular, referencing support was limited, that you'd use external tools
for (e.g. EndNote or [Zotero](https://www.zotero.org/)).  I'm not sure
how Word looks with respect to that now.

Back then, Word seemed to struggle and be sluggish with large documents
with lots of images, which was always fun. Again, maybe that's improved
in recent versions? When editing LaTeX, you're only editing the source
markup in whatever text editor you choose to use, and this source, even
for a lengthy document, will be relatively small; images for LaTeX are
stored entirely separately from the source. 

Another issue with Word is ensuring formatting styles are correctly and
consistently applied to text. You can create styles, but you then have
to apply them by hand, selecting the text. Sometimes you may delete
spacing between words and suddenly you have to reapply a styling, as the
text has changed to the style of its neighbours. In LaTeX, anything to
do with formatting is specified explicitly in the markup, making it easy
to see that the correct styling is applied to the text.  Furthermore,
the LaTeX defaults are usually decent, not always perfect, but decent.

### The good and bad of LaTeX

This explicitness and strictness of LaTeX is good and bad. It means that
you know what is intended for your text, but it also means that it's
possible for you to break your document sufficiently such that it cannot
be rendered correctly, or sometimes even at all, by LaTeX.

If you've done programming and are used to finding and correcting your
inevitable mistakes, this isn't unusual. But the idea of having written
a document that you can't then display in the intended output format may
be an intimidating concept to new users. Likewise, the error messages
can be numerous and formal, and not much help to novice users.

Tricks known to programmers like a regular edit-compile cycle to ensure
you find issues as you create them, or commenting out markup to isolate
the specific parts of markup that are the cause of difficult to
understand problems are useful skills. (These ways of working are
perhaps a result of the creators of LaTeX — and TeX, which LaTeX is
built on — being computer scientists.) However, these concepts may not
be immediately obvious by users with little experience of coding who
just want to get on with writing, and don't want tools getting in the
way.

On the other hand, working just with the LaTeX source and focusing on
the text alone seems much more productive to me. You can concentrate on
content first, and fix up the presentation at the end. Otherwise, I find
that working alongside the printed document layout presents me with the
continuous distraction of making things look "right", fixing incorrect
formatting or alignments, even though the content in question could be
modified or removed entirely during later editing. This time might be
better spent just writing.

Talking of layout, in my opinion, a LaTeX document using defaults will
be much more pleasant to read than a Word document using defaults. To
some extent, in both cases, this can somewhat depend on templates that
you may choose to create your document, but a default LaTeX document has
more of the look of a professionally typeset book.

Finally, many useful additions to LaTeX come in the form of a huge range
of additional packages you can install to add new commands and features.
Again, this is a mixed blessing. First, you need to be aware that they
even exist — [lists like
this](https://tex.stackexchange.com/questions/553/what-packages-do-people-load-by-default-in-latex)
can help: there may be a package perfect for what you're trying to do,
but you just haven't discovered it yet. Another hassle is that you can
have incompatibility issues between certain packages, or they may
require to be loaded in a certain order. Fixing problems like these is
time, again, spent on tools, not on writing.

You do need to be careful of package updates. Mostly these should be
benign, but in one case I experienced, a package update suddenly broke
my document, and I had to spend time discovering the problem and
reverting the package version.  (My memory's hazy, but I think this was
complicated by MikTeX only having the latest package versions, so in the
end I think that I had to download from elsewhere and install by hand.)
This may be an issue for compiling documents if you return to them much
later in the future: if any of the packages have broken their backwards
compatibility, you may be stuck. There's also no easy way that I was
aware of to pin package versions, like you might in a [Python
setup.py](https://packaging.python.org/requirements/) file.

## Do you still need to learn LaTeX these days?

Since I learned LaTeX, software like [pandoc](http://pandoc.org/) has
appeared and made it simple to write in other formats — for instance,
Markdown, reStructuredText, or HTML — and convert that to LaTeX.
[Markdown](https://en.wikipedia.org/wiki/Markdown) in particular is very
simple, and easy to learn.

For relatively straightforward documents, that's an alternative to give
you the benefit of nicely typeset output, without having to bother
writing LaTeX directly. This can give you a handy subset of LaTeX in
potentially a simpler markup, especially with Markdown.

However, LaTeX remains flexible and powerful and, especially for
creating more complicated documents, it still retains popularity more
than thirty years after its first development. Furthermore, it's also
released under an open source license (the LaTeX Project Public License)
so these professional-level tools are available to everyone at no cost.
If you have the likes of long reports or a thesis to write, it's
certainly still worth a look.
