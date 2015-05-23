Title: Book review: "Data Science for Business"
Date: 2014-01-14 18:35
Modified: 2014-01-16 18:30
Author: Steven Maude
Tags: data, review, science, business, book
Slug: book-review-data-science-for-business
Summary: A review of Foster Provost and Tom Fawcett's introductory data science book: "Data Science for Business".
Alias: /2014/01/book-review-data-science-for-business.html

<img class="article-image" src="{filename}/images/2014/Data_Science_for_Business.jpg" alt="Cover of &quot;Data Science for Business&quot; book." width="300">

I recently read "Data Science for Business" by Foster Provost and Tom
Fawcett for the upcoming [Data Science Book
Club](http://growthhackers.com/ask-gh-anyone-else-want-to-join-the-data-science-book-club/)
that [Nichole Elizabeth DeMeré](https://twitter.com/nikkielizdemere) is
putting together. As the title suggests, it's pitched primarily at
business people involved in data science projects.

For me, it covered some familiar territory I've encountered either via
introductory courses or through work (e.g. hierarchical and k-means
clustering, text processing, [classifiers and lift
curves](https://blog.scraperwiki.com/2013/12/machine-learning-about-scraperwikis-twitter-followers/)),
and some I hadn't (ROC curves, expected value in decision analysis; the
latter of which I found really interesting in how it can help give a
framework to problems).

With it being business-oriented, the emphasis
throughout is definitely on how the data science process both relates to
(the focus is on marketing and churn) and fits into business (for
example, if you don't already have the right data to answer your
question, is it worth you investing in doing so?)

The authors made a smart choice in starting from absolute basics,
avoiding a lot of complexity in the algorithms and sticking to giving as
simplified a view as possible of things while still retaining the core
ideas. The coverage was enough that someone knowing nothing about data
science could come away thinking of how they could start to consider
applying it.

Even the sections marked as more complicated mathematically were usually
a fairly straightforward read: you shouldn't struggle to get by even
with very little maths training. I read it sequentially, but — final few
chapters aside which pull together some of the ideas discussed — they're
largely self-contained enough that it's easy to dive into selected
parts.

A slight criticism that could have made the book feel more rounded for
the non-developer or business reader was to show *how data is actually
processed*. This was left a little abstract in the book. Results were
shown, the process of how the algorithms give rise to the results was
discussed, but what the user would do to actually get those results was
skipped over. (They do include some interesting walkthroughs of the
process of solving data science problems, just without the gritty
details.)

I've a little experience of using `scikit-learn` and didn't find it hard
to imagine how I could go about using the ideas that were being
discussed. Without that, I might have found it a little more difficult
to relate to otherwise.

A few mentions of [Weka](http://www.cs.waikato.ac.nz/~ml/weka/) are made
throughout the book: with it being open source and GUI-driven, it would
have been ideal for a worked example of how to load and process data.
However, it's a minor oversight; there are plenty of [online
tutorials](https://www.youtube.com/watch?v=m7kpIBGEdkI) for the
interested and the authors have done a great job in communicating
several, potentially intimidating, ideas with clarity.

It's pitched as a "broad, deep, but not-too-technical guide" which is a
fair description. **I'd definitely recommend it as an introductory
book**. A big chunk of it is available to preview on [Google
Books](http://books.google.com/books?id=4ZctAAAAQBAJ&printsec=frontcover),
if you want to check it out before buying.
