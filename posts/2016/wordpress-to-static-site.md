Title: Archiving a WordPress site with <code>wget</code> and hosting for free
Date: 2016-09-21 23:54
Author: Steven Maude
Tags: WordPress
Summary: Migrating WordPress to a static GitHub Pages site.

After what seems quite a long time from when the idea was first mentioned to
change the name of my employer, it's finally happened, and they've got a [new
website](http://sensiblecode.io) and everything. We still have the old company
mugs, sadly.

I'd been helping out in renaming things. It's surprising just how deep
the hooks of a name go: email addresses, documentation, licences, even
mentions in code too. A more startlingly obvious case is that of a
website. And as there's now a new website, we don't really need to
maintain the old one anymore. Just taking everything down would be a
shame as there's lots of content on there that people have found
useful in the past.

## WordPress migration

Like many sites, it used WordPress. One option for migration away from
WordPress is to export the content as an XML file, which either various
other hosts may be able to import for you directly, or you can try
converting into a useful format yourself, e.g. if you're using a static
site generator to build a new site.

We just wanted to archive the site, rather than move to a new site and
reuse the old content, which is a different task.

There are several WordPress plugins that are supposed to convert your site into
a static one. However, none of the two I tried were successful; one just froze
without seemingly doing anything, while the other only pulled a couple of pages
from the site.

## Gathering the site content with `wget`

In the end, I resorted to [`wget`](https://www.gnu.org/software/wget/) which
did an admirably good job after a few attempts.

`wget` is more often known as a command-line download tool, but is much more
powerful than a simple downloader. The downside with this is that there are
options present that you might not even know about until you try this kind of
site archiving, hit a problem and then discover which `wget` option you should
have used to fix it. The upside is that `wget` probably does feature the option
you require.

After lots of trial and error, what I ended up with was (deep breath):

```sh
wget --page-requisites --convert-links --adjust-extension --mirror --span-hosts --domains=blog.scraperwiki.com,scraperwiki.com --exclude-domains beta.scraperwiki.com,classic.scraperwiki.com,media.scraperwiki.com,mot.scraperwiki.com,newsreader.scraperwiki.com,premium.scraperwiki.com,status.scraperwiki.com,x.scraperwiki.com scraperwiki.com
```

Let's look at what each option does:

* `--page-requisites` collects other files need to render a HTML page,
  e.g.  images and CSS.

* `--convert-links` converts links in the retrieved document to one that
  will correctly display in the local mirror; this all happens at the
  end of a collection; if you check files while the collection is in
  progress, the links won't yet have changed.

* `--adjust-extension` gives HTML files an `.html` file extension if
  they don't have one (`--convert-links` adheres to these modified
  filenames too, so if a HTML file has a modified name, then the link to
  will be correct).

* `--mirror` is an alias for a series of options that facilitate
  mirroring a site.

* `--span-hosts` enables wget to move across different hostnames.

* `--domains` and `--exclude-domains` list domains that `wget` should or
  shouldn't retrieve content from.

Later the files from our multiple domains got moved into one directory for
simplicity. I think you could have done this using `--no-host-directories`.

Running this command will then proceed to collect the content from the sites
you've allowed it to crawl.

## Hosting for free

If you have a free GitHub account and are competent enough with the
basics of `git`, note that you can host static sites, also for free, on
GitHub Pages.  Introducing `git` version control is an entirely other
post, but there are plenty of online tutorials. To do something like
this, don't feel overwhelmed by the different commands. You only really
need the basics, i.e. knowing how to create a new repository, add files
to it, make commits and push them to a remote repository.

Another nice feature of preparing your static site in a version
controlled repository is that when you encounter things that need
fixing, you can try them and always be able to restore to an earlier
version, should you need to.

## Problems I had to solve

### Broken links

Initially, the links to images or other pages were broken, the
`--convert-links` option fixed that.

### Unrestricted crawling

`wget` was crawling other scraperwiki.com domains than the ones we wanted and
collecting a lot of unnecessary content. All I needed was the main site, so I
specified the domains to exclude.

### Removing dynamic features in the static site version

Some features of the site, as expected, no longer functioned after collecting
the pages. For example, the comment and contact forms we had involve some
processing on the WordPress server, and therefore were displayed on the static
site, but didn't work.

Removing this content is possible in a couple of ways. Either you could process
the HTML, using blunt instruments of find/replace, or the finer tools of
reprocessing the HTML with a proper parser, and remove the unwanted elements,
for instance using Python and [`lxml`](http://lxml.de).

Easier still is just hiding the broken elements. Finding an appropriate
selector for those elements, and then adding a CSS rule for that
selector containing `display: none;` (perhaps with `!important` if
required) will hide them. This also preserves the HTML as it was without
mangling it.

It probably won't affect you, but it's worth noting that automated bots
may well still be trying to trigger elements "hidden" in this way.
They're still on the page, just not displayed to normal users of the
site (unless they tweak the CSS). We had an odd issue possibly caused by
a redirect from the old site: bots were presumably attempting to submit
to a form on our new site, even though they were visiting the archive of
the old site. (It was flagged by the form provider asking us to approve
submissions from that URL.)

### Query strings in filenames

This was caused by WordPress hosting resources with version query
strings in the URL, e.g.  CSS and JS. 

When `wget` retrieved the files initially, it retained the `?` and the
trailing part of the name, e.g. `jetpack.css?ver=4.1.1`. The problem is
that the links also look like this too.  The "`?`" gets interpreted by
clients as a query string, and not part of a static filename. In a
static version of the site, the query string won't work: the browser
requests the file without the `?` and passes a (now) useless query
string. Our copy of the file actually has a filename of
`jetpack.css?ver=4.1.1`, not `jetpack.css`. We don't want the client to
request `jetpack.css` with a query string of `?ver=4.1.1`, but to
actually request a static file with the question mark in its name.

I'm not entirely sure what fixed this; I didn't notice at first. From
some point onwards, the `?` ended up getting encoded as `%3F` which then
gets correctly requested as a filename with a question mark in it. Not
particularly clean, but it worked. It may have just been using a recent
version of `wget` that solved this. This was nice as the alternative was
a horrendous find/replace task using commands like:

```sh
find . -type f -exec grep -Iq . {} \; -and -exec sed -i
's!wp-content/plugins/jetpack/css/jetpack.css?ver=4.1.1!wp-content/plugins/jetpack/css/jetpack.css!g'
{} \;
```

to fix up the content by hand for every CSS and JS file. (You could optimise by
having `sed` perform all the replacements in one command, rather than executing
the same find repeatedly, but I was verifying the changes by eye after
processing each filename; `git diff` is useful here.) That equally worked, but
was much more work to check.

Searching now, by far the simplest fix would be use a Wordpress plugin
to remove the query strings before archiving. There are a couple out
there.

### `srcset` images

Some of our images were responsive `srcset` images listed in `img`
attributes.  Until recently, `wget` didn't handle this, but from `wget`
1.18, it supports `srcset` images just as it does images in `src`
attributes of `img` elements. To clarify, it both correctly retrieves
the images *and* updates the links. (I assume only when using
`--convert-links`.)

### Links in option values

As part of the site archive navigation, there were links to option
values.  These weren't updated. I just hid those elements as it didn't
seem a critical part of the site.

### WordPress emoji code

Recent versions of WordPress feature code to add emoji support for certain
browsers. This embedded JavaScript is in the HTML and was still pulling from
the old WordPress site because it contains an absolute URL within it. Saving
the file locally and correcting the URL is non-trivial as a relative URL
depends on how deep in the local mirror you are. The simplest solution was
disabling this feature, by adding the ["Disable
Emojis"](https://wordpress.org/plugins/disable-emojis/) plugin to the
site, then recrawling.

It's not essential to fix this, but means the static site is not making
requests for files that don't exist when you move from WordPress.

### Fixing up incorrect `index.html` URLs

Lots of URLs on the original site ended with `/`, rather than
`/some_page.html`. `wget` instead saved these pages with a filename of
`index.html`. Fixing these up was a pain. In terms of making the site
work, this strictly wasn't necessary. GitHub Pages will respond with a
request to `foo/` as the `index.html` in the `foo` directory, so any
existing links to the site would still work. However, fixing this does
ensure anyone sharing links to our pages uses the same URL as the pages
always had.

I'm not even completely sure that this was entirely fixed correctly; there are
just too many URLs to verify, but it appeared to have the desired behaviour.
You can see the [commit
message](https://github.com/scraperwiki/scraperwiki-site-archive/commit/73881788c40a427068e6af415a3a16399bdecffa)
for the code I used.

Essentially, it used lots of regular expressions to substitute:

* `foo/index.html` to `foo/`;

* `foo/index.html#bar` to `foo#bar`;

* `foo/baz.html` to `foo/baz`;

* `foo/baz.html#foobar` to `foo/baz#foobar`.

There are a few other tweaks I did to clean up URL links too. They are
detailed in the other [commit messages in the
repository](https://github.com/scraperwiki/scraperwiki-site-archive/commits/master).

### Some other redirect problems

For us, some redirects we had set up on the old site caused a couple of cases
where files ended up in the wrong place or with the wrong name compared with
the original site. We had to be careful to fix up relative URLs here. We also
had multiple copies of certain files. These weren't difficult to fix by
hand as there were only a few to modify.

Finally, we had to correctly set up redirects to the new site in our server
configuration, and everything was finally done.

## Moving on

After much work, the static version's now working well. Everything's
pretty much the same on [the site](https://scraperwiki.com/) aside from
the interactive forms. It was much more of a task to get done than I'd
imagined. I think it was around half a day spent trying out `wget`
options and another couple of days spent on resolving all the other
issues.

The advantages are that we don't need to maintain a WordPress
installation to run the site and the site's getting hosted
for free.

Good luck if you're tackling the same problem! Hopefully some of the
tips here might help you with your migration.
