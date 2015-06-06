Title: Blogger versus Wordpress revisited
Date: 2015-06-06 14:46
Author: Steven Maude
Tags: Blogger,Wordpress
Summary: Pros and cons of Blogger and Wordpress, and why neither of these was a good fit for my blog.

If you look back, the [first post]({filename}../2013/blogger-versus-wordpress.md)
on this blog was agonising over what blogging system to use. At the
time, my reasoning for choosing Blogger was that it was quick to get
started with.

And that was true. Provided you already have a Google account, you can
make a blog in a few clicks. There's a simple interface for entering
posts: you can enter raw HTML or use something that looks more like a
word processor. Even if you know very little about how the web works, it
makes publishing straightforward. It's cost-free to use too, even if
you're using your own domain name.

However, the limitations of Blogger soon became apparent:

* The default templates available look dated. (Though you could well
  modify them or install one from elsewhere). Furthermore, for the
  default template I used, which was fairly plain, it wasn't even
  possible to read the site properly without JavaScript: half of the
  page content would not be displayed. Code snippets, which I've often
  used in posts, are also hard to read because there's no syntax
  highlighting.

* The mobile template for Blogger interprets swiping left or right
  across the screen as meaning that you want to move to a different
  article. This is frustrating enough even when you know about it as
  it's easy to trigger unintentionally. It's more confusing for someone
  visiting your site for the first time. As mobile internet browsing
  increases, the needs of viewers on those devices becomes more
  important.

* Personally, I found writing posts on Blogger to be clumsy. The WYSIWYG
  editor is quite limited. If you want anything outside of the fairly
  limited feature set (for example, footnotes, or more control over
  images), you need to edit the HTML directly. The HTML that the editor
  creates seems to get polluted with unnecessary tags quite often,
  especially if you're switching fonts (e.g. between code and non-code
  sections).
     
    I've also accidentally lost work due to having two copies
    of the post creator open, with one overwriting the contents of the
    other unintentionally on save.
  
    To work around this, towards the end of my Blogger use, I was
    writing posts in Markdown[^1] completely separately, converting them
    from Markdown to HTML, then pasting the HTML into Blogger, fixing
    up things and adding images. Writing posts in Markdown was
    convenient, the subsequent wrangling of the HTML output to Blogger
    was not.

* The current, published form of the blog posts is that which is
  stored in Google's servers. Keeping a local copy and
  tracking any changes made in posts was a chore, so I never bothered.

* Blogger isn't software available for you to run on your own computer,
  so you're at
  Google's mercy. If Google change something that you find particularly
  detrimental, or if they ever decided to drop it completely, you'll be
  forced elsewhere.

So, what are the alternatives?

The main off the shelf solutions seem to be Wordpress or static site
generators. Wordpress is **very** popular for building blogs, and
actually resolves many of my Blogger complaints.

One big plus is that it's open source (see [wordpress.org](https://wordpress.org)).
This means you can run it anywhere you like, though you'll have to pay
to host it somewhere. Alternatively, you can host your blog at
[wordpress.com](https://wordpress.com) for free, albeit with possible
ads and without the use of your own domain name. Resolving these
problems is simple: just give them money!

Wordpress is also a step up from Blogger in terms of customisability,
with a much larger user community around it. Because of this, there's
far more in the way of themes and plugins to tweak your blog how you
want it. Researching just now, I discovered 
[Markdown](https://en.support.wordpress.com/markdown/) is supported
for writing posts, which is great. And some previous history of your
posts are saved (25 revisions at the time of writing), with the
ability to [revert and compare
them](https://en.support.wordpress.com/posts/post-revisions/).

But, having used Wordpress at work, there were still three big reasons
why Wordpress didn't seem a suitable replacement:

* **Cost of hosting.** This isn't particularly high, but my blog is just
  a side project, so I'd rather keep the costs minimal. Blogger is
  free: any other possible solution is competing with that.

* **Wordpress uses PHP, which I know nothing about.** It's unlikely, but
  if I ever did want to do any low-level customisation, I'd need to
  learn it.

* Wordpress seems too heavy-handed for what I need: a simple way of
  presenting text-based articles on the web. This is reflected both in
  its frequent security updates (though an [automatic update option](https://codex.wordpress.org/Configuring_Automatic_Background_Updates)
  is available) and its byzantine menus which ordinarily see me
  clicking every option exhaustively until I find the setting I want to
  change.

That's not to say Wordpress is a bad option — lots of sites do use it
— just that it wasn't the right option for me. For my use case, which is
sharing things I've written, static site generators seemed a better fit.
I'll describe the advantages of those in a later post.

[^1]: Markdown is a simple way to mark up plain text with your intended
      formatting using annotations that you might already be accustomed
      to. For example, to indicate bold text you would type
      `**important point**` to give the output **important point**. Its
      original use was to create HTML simply, but it can also be
      converted into many other formats using tools like
      [pandoc](http://pandoc.org/).
