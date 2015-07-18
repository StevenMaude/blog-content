Title: Thinking of using a static site generator for your blog?
Date: 2015-07-18 23:54
Author: Steven Maude
Tags: Blogger, Pelican, Wordpress, static site
Summary: The (many) good and the (few) bad aspects of static site
         generators.

When I first thought about moving from Blogger to Pelican, it was
because I'd had more than enough of Blogger's drawbacks. What hadn't
crossed my mind, because I had no experience of using them, were the
problems that static site generators could have. At the time, my hunch
was that it wasn't possible for them to be worse than Blogger.

As it turns out, that was the case. But, they are not entirely perfect
and, going through this migration, I better understood what what the
good and the bad of static site generators are. If you're thinking of
making a similar migration, these points might give you an idea of what
you might deal with in shifting.

While I'm familiar with Pelican and Blogger, most of the points apply
generally so could still be informative for you if you're considering a
move from, say, Wordpress to Jekyll.

## Converting and writing content (Markdown)

### Bad

*   Depending on what you used to create a blog previously, and how much
    content you had on your old blog, it may be time consuming to move
    content. Even armed with a [fork of Pelican](
    https://github.com/getpelican/pelican/pull/1390) where
    someone helpful had added Blogger conversion, the output
    wasn't perfect and still had plenty of residual cruft that had to be
    fixed up by hand.[^1]

*   Markdown's quick to write with, but only gives you a small subset of
    HTML and so doesn't handle every eventuality. There are dialects of
    Markdown which expand this with more layout options that may be
    available in your blog software of choice.

    With Pelican at least, it's possible to use
    [Pandoc](http://pandoc.org/) via a
    [plugin](https://github.com/liob/pandoc_reader). Pandoc is one of
    the more versatile Markdown converters, but does introduces another
    dependency. Pelican also offers reStructuredText support which has
    support for more formatting options than vanilla Markdown, but just
    isn't as nimble to write.
    
    Instead, I opted to occasionally allow fall back to raw HTML in
    posts, mainly for handling images. This isn't ideal, but is a decent
    compromise that's at least compatible with different Markdown
    implementations.

### Good

*   All my content is in fairly plain Markdown which I love writing in.
    It also means that I'm far less locked into Pelican than I was ever
    tied into Blogger. Should I wish to switch to another static site
    generator, only the metadata and Python-Markdown specific tweaks may
    need adjusting.

## Adding content to the site and hosting

### Bad

*   My git repositories are structured in a way that I like: blog HTML,
    the theme I use, my Pelican configuration, my Markdown posts, and
    the post images are all separate. However, for making small
    adjustments to posts, this is a nuisance: you need to edit the post
    and remember to push that, *then* generate the HTML, *then* move
    that into the HTML repository and finally push that to GitHub. I
    usually do this via branches too, which is more work too (though
    this is my choice). Improving this workflow is on my to-do list.

### Good

*   My blog's not trapped within Google's servers. Certainly, I'm wary
    of how much Google's hands are present in much of what I do on the
    web, whether through hardware devices I use, their search tools or
    through websites that use features like Google Analytics and Fonts
    (including mine). At least the blog's now hosted elsewhere and
    Analytics and Fonts that the site's using could, in the worst case,
    be removed entirely, or replaced with alternatives.

*   In fact, the blog's not really dependent on the whims of any service
    owner at all. If GitHub stop hosting, I can take the HTML and host
    it elsewhere. With Blogger, you're at Google's mercy: if they ever
    decided to drop Blogger, then you'd be forced to switch to a new
    blog platform.

*   All the content is tracked within a git repository. This means it's
    version controlled, and there's no easy way to obliterate posts.
    With Blogger, at least once, I foolishly attempted to edit multiple
    posts in separate browser tabs and subsequently lost the content of
    one of them. Luckily, I had a window open with the web version of
    the post to recover it. Having only a single canonical copy of
    posts stored in Google's servers was clearly not a good thing.
    (Wordpress is better in that it's possible to store multiple
    revisions of posts.)

*   You have much more control of the post URLs; Blogger posts always
    have the year and date in them.

*   Blog hosting using my own domain name on GitHub is free of charge.
    This is also free on Blogger. If you use wordpress.com, you'll need
    to pay; if you're using your own Wordpress installation, using your
    own domain is free, but it's likely you'll need to pay for hosting.

## Appearance and viewer experience

### Bad

*   With Pelican (probably much less so for Jekyll), there's not a huge
    range of themes. If you're fussy like me, you may need to spend some
    time tweaking, or creating your own. 

### Good

*   My site now functions without the viewer needing JavaScript. With
    Blogger, you used to only see half the page content. If JavaScript
    is disabled now, the only issue is that the mobile menu doesn't
    open, which is far less of a problem.

*   There's no awful separate mobile version of the site. On Blogger,
    the template I used had an unfriendly feature where swiping would
    navigate away from the page to the previous or next article. This
    could be triggered quite unintentionally by trying to pinch to zoom.

*   Often my posts are on programming. Having code snippets that look
    nice without me having to do anything is a great bonus. In Blogger,
    you'd need a JavaScript plugin for syntax highlighting.

## Running the generator

### Bad

*   Static site generators are not for the impatient. For Pelican, being
    comfortable with Python is a big help, though not essential.
    Pelican — and I imagine this applies to Jekyll too — isn't difficult
    to get a basic blog up and running, but to get the result you want
    may take you considerable work.

*   If you have a very large number of posts, the time it takes to build
    your site may become an issue. With 61 posts and 1 page, my site
    takes 2 to 3 seconds on my Core i5 PC. If the site starts taking
    minutes to build, that may become a chore. This would be
    particularly frustrating if editing posts and wanting to quickly
    preview how the changes look since, with Pelican, the entire site is
    rebuilt when running the development server.

### Good

*   Pelican is nice to use, and I had very few problems in doing so.
    Most of my effort was spent on converting content and amending the
    theme to my liking. Though the community's relatively small, it does
    seem like there are more blog posts and activity compared with when
    I first looked into it last year.

*   Pelican, and many other static site generators, are [open source](
    http://opensource.org/) software. This means they are free
    to use, and free to modify (and share those modifications). The
    implication is that, as long as there are developers interested in
    it, it's likely that it will continue to be supported and developed.
    Even in the unlikely event that everyone else abandons it and you're
    the only user, you can still continue modifying it. (This also
    applies to Wordpress' source too incidentally.)

## Living with a static site

When worrying about the limitations that static sites may have, think
about the actual minimum you need on a web site to share and present
written ideas and thoughts you have. It's really not very much; do you
*really* need everything that Wordpress offers?

Overall, I'm pleased with the result. When I'd started thinking about
moving, I'd got fed up of using clunky old Blogger, which feels
distinctly unloved by Google.

Being able to write directly in the format (Markdown) that the blog
actually uses is a real convenience. (Note that Wordpress offers this
option too.) Along with that, the blog looking fresher than it did is a
bonus. These features, more than perhaps anything else, actually makes
me want to add new content to my blog, which is more than I could say
that Blogger ever did for my inspiration.

[^1]: You can see exactly how much work in the early commits
[here](https://github.com/StevenMaude/blog-content/commits/master).
