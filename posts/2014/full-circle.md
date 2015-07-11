Title: Full circle
Date: 2014-03-22 14:55
Modified: 2014-03-22 14:59
Author: Steven Maude
Tags: Wordpress, blog, static, Jekyll, blogging, site, Pelican
Slug: full-circle
Summary: Thoughts on moving away from Blogger to a static site.
Alias: /2014/03/full-circle.html

## Blogger and blogging

To me, it doesn't seem that long ago, but I wrote the first post on this
blog ten months ago. Funnily enough, [it
discussed](http://www.stevenmaude.co.uk/2013/05/blogger-versus-wordpress)
what I'm thinking about right now: how best to blog.

Writing using the Blogger editor is not a great experience. Not great,
but adequate. It removes that the need for the user to know HTML. With
that, it also removes the possibility to do anything beyond the limited
formatting you get with that. (Some of my use cases, for instance,
include highlighting code/command lines to offset them from text, and
using footnotes.)

I've had a couple of instances where, largely through my own fault, I've
been switching between posts, hitting back and ended up wiping out my
work. After those experiences, I decided to just draft posts in a text
editor, then paste in and markup the HTML.

I find it quite clunky to mark up text posts as HTML, even basic things
like paragraphs need tagging, and having to open and close tags
constantly starts getting distracting. After speaking with drj this week
about him considering migrating his [Wordpress
blog](http://drj11.wordpress.com/) to [Jekyll](http://jekyllrb.com), I
had the inspiration of starting to write blog posts in Markdown and then
converting them to HTML.

## What's Markdown?

You might be asking that if you're not a developer. I hadn't heard of it
at all before I started using GitHub, but I'm a convert now. It's a
no-nonsense tool that converts plain text to HTML. Grab your drink of
choice and spend the whole five minutes you'll need to learn to use it.
There are several online editors [like this one](http://dillinger.io/)
that you can test out.

Adding formatting is really simple, for instance, \*putting text between
asterisks\* in Markdown would make it *italic*. It means you can focus
on writing, instead of getting distracted fiddling around with HTML
tags.

Furthermore, there are fantastic tools such as
[pandoc](http://johnmacfarlane.net/pandoc/) that will convert Markdown
to a host of other outputs too, e.g. PDF via LaTeX, Word docx,
LibreOffice, even the epub ebook format.

## What next?

After finding that I prefer writing posts in Markdown, my next thought
was: why not remove the middleman and use a system, like Jekyll, that
directly uses Markdown?

I'm feeling this particularly so now, given that I'm starting to feel
like Blogger is limiting. By default, the provided Blogger templates
look dated. (And feature some odd design choices too: why is text in a
h2 tag smaller than that in a h3 tag?) I've not had time to start trying
to modify it or look for a better one. When I see my posts look
beautiful in an online Markdown preview, and then sending them to the
horrors of my (pretty much stock) Blogger template where they are
rendered so unappealing is always going to make me sigh.

**The content is the most important thing, of course, but a poorly
designed website is always going to distract.**

It's also clunky to try to customise certain aspects of Blogger, and
having my own blog setup might simplify this. Being completely in
control of my blog, rather than having parts of it in hidden black boxes
appeals too. One example is that someone reading an article commented
that the mobile version of the blog was irritating because it disabled
zooming; nothing that I could do really do about that.

*This isn't to take away from Blogger being an easy way to get started.*
It's simple to use and definitely helped me share my writing. Without
having to worry about choosing a host and managing some blogging system,
it was easy to get going. Login to your Google account and a few clicks
will get your first post published. It being free of charge helps too.

So, I now have a project whenever I have a free weekend next: look into
static site blogging with Jekyll/Octopress (Ruby based) or perhaps
[Pelican](http://blog.getpelican.com) (Python based) and hosting on
[GitHub Pages](http://pages.github.com). I'll definitely write up what I
find.

Finally, why consider these static site generators, and not my
originally suggested move to WordPress? WordPress itself is free to use,
but hosting WordPress somewhere costs money. It also gets me into the
quagmire of shopping around for a host and hosting plan, and managing
security updates. Once the static page generator is initially setup, I
can deploy the site to GitHub Pages, then focus on writing again.
