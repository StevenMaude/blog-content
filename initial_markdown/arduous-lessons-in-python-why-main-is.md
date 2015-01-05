Title: Arduous lessons in Python: why main() is useful
Date: 2014-07-05 11:42
Author: Steven Maude
Tags: foolishness, name, main, Python, fix
Slug: arduous-lessons-in-python-why-main-is

<div class="separator" style="clear: both; text-align: center;">
[![Python
logo](http://1.bp.blogspot.com/-H-pwiTI3Mss/U7fgl39aaTI/AAAAAAAAAO0/hQH96CfEwmY/s320/python-logo-master-v3-TM.png)](http://1.bp.blogspot.com/-H-pwiTI3Mss/U7fgl39aaTI/AAAAAAAAAO0/hQH96CfEwmY/s1600/python-logo-master-v3-TM.png)

</div>
An ordinary afternoon and I'd wanted to work on some code locally on my
machine. I knew the tests previously ran without any issue. So, after
I'd cloned the repository locally, I ran `nosetests` to make sure
everything was OK with my setup before I started.

What I expected is the tests to run pretty quickly as before.

What happened instead is that Python started hogging a CPU and I saw a
lonely blinking cursor where I expected my test results.

Something was happening, but none of the tests were seemingly running.
That is, I wasn't seeing any pass/fail indicators, which was strange.

### What actually happened

Something was running that evidently wasn't what I intended.

On inspection, one of the import statements in the test code had a
structure somewhat like:

<div class="bgcode">
    def some_function():    do some thingsdef another_function():    do some other thingsdef really_long_winded_scraping_function():    do lots of thingsreally_long_winded_scraping_function()

</div>
</p>
Bear in mind that when you import a module, the statements are actually
executed. If you've just got function and class definitions in there,
then this means that they get defined, but they aren't executed until
you call them.

However, if functions are called in the module's flow of execution, then
they'll be called when you import it too.

So, when this module was being imported by the test module, the
`really_long_winded_scraping_function()` was being called. So, yes,
eventually, the tests would have run, but they'd run *after* the code in
the `import` had finished, which would have taken **hours**.

### Fixing the problem

Normally, I routinely use:

<div class="bgcode">
    if __name__ == '__main__':    main()

</div>
</p>
in Python code that I start writing.

From the [official
documentation](https://docs.python.org/2/tutorial/modules.html):

> "Within a module, the module’s name (as a string) is available as the
> value of the global variable `__name__`."

What it also does is assigns `'__main__'` to `__name__` if the module is
being executed directly. This gives you a way to specify different
behaviour depending on whether the module itself is run or just
imported.

If you're importing the module to reuse the code elsewhere, you can then
just access the relevant functions and classes that you need, rather
than running code that actually starts doing things.

In this case, for some reason, we'd just quickly thrown some functions
together, then found that the function that actually initiates all of
the scraping wasn't being called. So, we'd just quickly added a call to
what was our at the bottom of the module, set the code going to do the
scraping and not run the tests again.

This was fine, until I forgot about this and came to run the tests again
later! It's a good case for running your tests regularly; the reason it
took me so long was that we hadn't run the tests since getting the main
code working. If we had, I think I'd have been more likely to spot the
connection between our fix to the code and the tests taking an age.

(This isn't a test specific problem. You'd notice it whenever you
imported the code into another module. It just happened to be that the
tests were the only other module that we'd imported the code into.)

</p>

