Title: US PyCon 2014 talks
Date: 2014-04-19 15:57
Modified: 2014-04-19 16:31
Author: Steven Maude
Tags: scraping, lxml, BeautifulSoup, regular, testing, Python, expressions
Slug: us-pycon-2014-talks
Summary: Rundown of some great US PyCon talks I recently watched.
Alias: /2014/04/us-pycon-2014-talks.html

<img class="article-image" src="{filename}/images/2014/python_logo.png" alt="The Python logo.">

The US PyCon took place over the last week or so and there are a huge
selection of videos of the talks up at
[pyvideo.org](http://pyvideo.org/category/50/pycon-us-2014). Still
haven't got through all of the ones I want to take a look at, but the
ones I've checked already were pretty good.

## Regular expressions and testing

Out of those I saw, I can definitely recommend two great mini tutorial
talks; one on testing and one on regular expressions. What I loved about
both is that they started from pretty much zero knowledge and built up
on that, without seeming overwhelming.

Luke Sneeringer's [talk on regular
expressions](https://www.youtube.com/watch?v=jKfkLVDAwRQ) was really
helpful consolidation for me. Occasionally I've used regular expressions
before, but I tend to play around with them in an online debugger like
[Regex101](http://regex101.com) until they work. I usually learn enough
at the time to get the job done, then promptly forget everything until
the next time. Hopefully, some of this talk will stick (and at least
it's on YouTube to refer back to, if not).

Here, the start of the talk threw down what looked like intimidating
expressions, then, over the course of a brisk twenty-five minute talk,
gave the viewer the tools to go back and understand it. It was also a
decent reference if you aren't even using Python: there are a few bits
of Python-specifics, but the focus was on the expressions, not so much
code.

Ned Batchelder's talk on [how to start with
testing](http://nedbatchelder.com/text/test0.html) was great too. When I
first was trying to start testing my code last year, I knew this was
important but I never found a good step-by-step guide of how to get
started from scratch. The talk starts with showing that automated tests
are better than a coder manually running statements to check their code
is working as it should (less work!).

It then leads into showing why test runners are better than you just
writing your own code to run tests. For instance, they help you to
isolate individual tests, ensuring that each starts from a clean state
and have failure and error handling built-in already. Finally, test
doubles are covered. At first, painstakingly hand-crafted doubles are
used, then this is simplified using the
[mock](http://www.voidspace.org.uk/python/mock/) library.

Doubles are particularly handy when your code is using external
resources, for instance accessing a database or a web site; in these
cases, your tests may run slowly, and you may not be able to guarantee
the result (e.g. if a web page changes).

Again, I'd seen, and have used, several of these ideas before, but to
see them all presented in one place, and explained so well, makes it a
good resource.

## Scraping

Since I do a bit of web scraping, I also skimmed a couple of
presentations given by Katharine Jarmul. [Her
tutorial](https://www.youtube.com/watch?v=p1iX0uxM1w8) looked pretty
good from what I saw, covering the basics of using BeautifulSoup, lxml
and Selenium for basic scraping. If you're wondering where to start with
scraping in Python, it's worth a look. She also gave [a
talk](http://www.youtube.com/watch?v=dWlhrL1l3QU&t=4m50s) comparing the
performance of these scraping tools; lxml using XPath was much faster in
her tests than both lxml using CSS selectors and BeautifulSoup.

That said, even BeautifulSoup was still only taking a fraction of a
second in the cases she looked at. Incidentally, a quick glance at the
[code](https://github.com/kjam/web-scraping-speed-comparison) shows that
the HTML was being read locally (and I understand why given the
variability inherent in accessing this information over networks and
from a remote server).

So I don't think that this should have much of an influence on your
choice of Python scraping library; use whatever you're comfortable with
to get the job done. The slow part is still likely to be accessing the
content from the site. Especially if you're being considerate and
throttling your requests to a site.

Finally, I'm guessing that
[this](https://www.youtube.com/watch?v=FQuIqtx1Z24) talk delving into
rap lyrics is probably one of the few given at a coding conference where
you can hear a snippet of N.W.A.'s "Straight Outta Compton".

If you watch any particularly thought-provoking or useful talks, please
let me know! There's way too many to practically sit through.
