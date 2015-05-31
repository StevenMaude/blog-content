Title: Hiding draft articles in Pelican
Date: 2015-05-31 20:16
Author: Steven Maude
Tags: draft,article,Pelican
Slug: hiding-draft-articles-in-pelican
Summary: How to hide articles you don't want to be published yet.

What I thought I'd get done in a week, actually took about four
months. But I'm finally free of Blogger and have moved to
[Pelican](http://docs.getpelican.com) for creating my blog. I'll be
writing more about how I migrated soon.

As I approached the end of that lengthy migration, I found myself
writing new draft articles that I wanted to ensure didn't actually make
their way into my publication directory.

## Writing blog posts

The way that I usually approach writing blog posts is that, as
I reach the end of writing them, I'll start reading in the final display
format, i.e. as a web page. This helps spot any mistakes that
I might miss from my eyes glazing over at a text editor, and helps me
spot formatting problems.

But, you might be working on multiple articles at once, so you want to
publish while you still have draft articles in your `content` directory.

Here's a few ways to prevent posts from being accidentally published,
without needing to do file juggling of your drafts in and out of the
`content` directory.

## Marking as draft and `.gitignore`

Any articles we stick in the `content` directory will end up in our
`output` directory, right? Not if we do like
[the documentation says](http://docs.getpelican.com/en/latest/content.html)
and add `Status: draft` to the metadata.

Building your site will then place draft articles in a `drafts`
directory, and the articles therein aren't linked from anywhere. This
might be useful if you want to share a link with someone to get feedback
on a post before you officially publish it.

Using a `.gitignore` file in your `output` directory is also an option
if you're using `git` to push new versions of your blog for publication.
Add `drafts/` to your `.gitignore` and you'd have to make a deliberate
effort to add them for publication.

## Using Pelican's `IGNORE_FILES`

Putting "draft" in the filename of any drafts is another option. Then,
you can use the `IGNORE_FILES` setting in `pelicanconf.py` to
specifically ignore the drafts.

Note that if you specify a setting in your Pelican configuration files,
the defaults get overridden. This means that you'll need to copy over
the existing settings from the defaults too. Otherwise, you'll
unintentionally change your configuration.

For instance, the [default](http://docs.getpelican.com/en/latest/settings.html)
`IGNORE_FILES` setting is `IGNORE_FILES = ['.#*']` so we'll need to
add `IGNORE_FILES = ['.#*', '*draft*']` to our Pelican settings.

## Hiding them completely (in Ubuntu, at least)

Another option is to just hide draft files from Pelican completely.

Under Linux, I thought that preceding the filename with a dot would hide
posts from Pelican, but it doesn't seem to. However, sticking a tilde on
the end of the filename does seem to prevent Pelican from seeing the
post.

One side-effect is that if you use a text editor that creates backup
files with a tilde on the end, your backup files will actually have
**another** tilde on the end (e.g. `my_draft_post.md~~`).

(Maybe marking files as hidden in Windows would have the same effect?
Haven't tried this.)
