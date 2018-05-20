Title: Solve your problem with sloppy Python
Date: 2018-05-20 17:24
Author: Steven Maude
Tags: PyCon, Python
Summary: A summary of a talk by Larry Hastings at PyCon 2018.

## PyCon 2018: A quick note

As PyCon 2018 happened last week, I've been watching a few talks. It's
sometimes difficult to keep up with changes to technology if you're not
paying constant attention. These kinds of talks are a useful way of
trying to catch up a little. With that in mind, I'm writing up summaries
of a few talks here.

## Solve your problem with sloppy Python

The talk is available to [watch
here](https://www.youtube.com/watch?v=Jd8ulMb6_ls), and an easy watch.
This was a pragmatic and enjoyable talk that would be easy for beginners
in Python to follow.

It's a nice contrast from other programming talks too. Often,
presenters, quite reasonably, focus on telling or teaching an audience
what they believe to be best practice on a topic. Concentrating on a
more practical side made for a light and refreshing approach.

### Code being discussed is for personal automation

Writing code to solve your problem.

* Not writing code in a professional context.
* These are throwaway scripts.
* You're the only person writing it and likely to see it.

#### Rules

* Fail early and noisily.
* Use Python instead of shell scripts.
* Have fun!

#### Guidelines

* Use latest Python version to take advantage of new features.
* Try automating even more, push as far as you can go, but may have some
  human intervention too.
* These projects are an excuse to try or learn new libraries/technologies.

It doesn't matter if the code's hacky; you may not bother with tests.
Quick and dirty code to get a job done. A couple of examples of this
from the renaming files problem in the talk:

* using `ls` to generate a list of filenames in Python; add triple
  quotes around string, `strip()` and `split()` on newlines gives a
  list.
* using exceptions lists in renaming files (e.g. to add apostrophes to
  words), run through each check for each filename. Most won't trigger,
  so you're doing lots of unnecessary checks, and could refine that, but
  performance unlikely to be an issue for these kinds of tasks.

Cutting corners is OK in this context, if it gets the job done.

### Example uses

* Renaming files. A general tip for file renaming tasks — in this case,
  downloaded radio shows — back these up via creating hard links with
  the same filenames in a backup directory. That way you can always
  revert to the original names, without having to backup the files.
  Could use Python's `os.link()` but also possible via a simple shell
  loop: `mkdir backup && for a in * ; do ln $a backup/$a ; done`.
* Provisioning new machines, e.g. running `apt install` and configuring
  programs, e.g. copying license keys.
* Tidying audio files, creating playlists etc.; possibly with human
  intervention here.
* Ripping CDs, using simple metadata format that can be parsed easily.

### A final note

* Sometimes Python was used to call out to the shell. `subprocess.run(s,
  check=True, shell=True)` is better than `os.system()` because
  `os.system()` does not fail noisily, but `subprocess.run()` does.

### A thought

One thing that didn't get asked in the Q&A at the end: how should you
estimate whether the automation is actually costing you time? xkcd
has covered this well in these [two](https://xkcd.com/1205/)
[comics](https://xkcd.com/1319/).

In some cases, it can be reasonably predicted that, if the process is
either time consuming or will be repeated often, it's worthwhile to
spend the time to write code as a solution to the problem.

But, the "Rogue's Gallery" radio show renaming given as the main example
presumably took a few minutes to write, find the exceptions (by hand)
and verify (probably also by hand) the code is doing what it should.
There are only actually a few shows to rename, and these themselves
could be done by hand, as a one-off task.
