Title: How to use mock in Python to mock methods on objects
Date: 2014-05-10 11:05
Modified: 2014-05-10 11:05
Author: Steven Maude
Tags: mock, testing, test, unit, Python
Slug: how-to-use-mock-in-python-to-mock
Summary: Using mocks in Python to mock methods on objects.

## Testing

Testing is a useful programming practice which, in all honesty, I'm
still learning much about. Tests can give you some reassurance as to the
behaviour of your code, providing you've written your tests such that
they're testing appropriate things. They can also help you think about
how you write your code, in a positive way: the process of making unit
tests can require you to rethink how your code operates in order to make
it testable.

If you're unfamiliar and want to know more, probably the single most
useful resources I've found are two of Ned Batchelder's PyCon talks, one
from [Pycon 2010](http://nedbatchelder.com/text/testability.html), and
one he [recently](http://nedbatchelder.com/text/st.html) gave. In the
latter, he covers testing from the ground up. The former is a little
less introductory, but is a good complimentary talk; he works through a
few examples where writing tests can give a better organisation to code.

## Testing and me

My problems in creating tests are often two-fold. First, I'm not always
sure what are good tests to write - for instance, unit tests should be
isolated, but how much should I be mocking out in unit tests? For some
functions, if you mock out all other function calls, you may have very
little left to actually test there.

Spotting which paths through the code you want to prioritise for
integration tests is another issue. Ideally, you'd either work bottom
up, starting with tests that mock out everything, then slowly adding in
real code, or maybe top down, progressively mocking out units. However
you approach it, the number of combinations of tests you could write
will increase rapidly: even for moderately small programs, the number of
possible combinations of mocked out functions and objects can be huge.
For example, if A calls B and B calls C, I could write tests that use
all three actual functions, two of them or just one (and perhaps even
none of them). To exhaustively test every combination becomes
unmanageable.

I'm hoping the more I write tests, the more confident I'll be at
evaluating whether the tests I'm thinking of aren't going to be that
useful to implement. Where I know I should improve is the second problem
I often encounter: how to actually implement tests. Often, I'll find I
know what I want to achieve but find difficulty in actually articulating
this in code, usually because I've not found the functions I want in
`mock`.

## Mocking a method of an object with Python `mock`

Anyway, here's an example of this which might be useful if you're trying
to do something similar. In this case, I wanted to test a method of an
object, but wasn't sure how to do that using a mock.

This is a really cut-down version of what my code was doing, but
features the main thing I was testing:

```python
import sqlite3


def main():
    table_name = 'some_table'
    sqlite_db = sqlite3.connect('database.sqlite')
    sqlite_db.execute("drop table if exists {};".format(table_name))
    # next, get some data and then save to db

if __name__ == '__main__':
    main()
```

As what the database saves depends on some input that the user supplies
(fixed here), I wanted to ensure that the table is wiped before we add
anything to it. Otherwise repeated runs would cause the table to become
cluttered with data the user no longer wants.)

What I specifically wanted to check was whether the database was getting
the correct table name to drop. One way of checking this is using
Python's `mock`(a `pip`-installable package if you're on Python 2, part of
the standard library from Python 3.3).

By replacing objects with mocks as stand-ins, we can avoid the need for
actually connecting to a database in our test (which may be slow or
unreliable, if it's remote). Mocks aren't just dummy objects though;
it's possible to inspect them after we execute some statements, allowing
us to see, for instance, if the mock was called, and what arguments it
was called with.

In my case, I got particularly confused with the mocking out of the
`.execute method` of the `sqlite_db` object. I'd tried all combinations
of accessing the call via the `mock_sqlite3_connect`. What it took me
ages to realise is that I had to mock out what `sqlite3.connect()`
returns; you can't (unless I'm mistaken) access calls on the object it
returns otherwise.

```python
import unittest
import code_to_test
import mock

class CodeToTestTestCase(unittest.TestCase):
    @mock.patch('code_to_test.sqlite3.connect')
    def test_database_drop_table_call(self, mock_sqlite3_connect):
        sqlite_execute_mock = mock.Mock()
        mock_sqlite3_connect.return_value = sqlite_execute_mock
        code_to_test.main()
        call = 'drop table if exists some_table;'
        sqlite_execute_mock.execute.assert_called_with(call)
```

What's happening here? First, we're using a decorator, `@mock.patch`
which replaces `sqlite3.connect()` in `code_to_test` with a mock,
`mock_sqlite3_connect`. We can then make the return value of the
`mock_sqlite3_connect` *a mock itself*. After that, all we have to do is
actually call the main function which now will run with our mocks
inside. Now, we can check that `sqlite3.execute()` was called correctly.
If we save this as `tests.py` and run `nosetests`
(`pip install python-nose mock` if you haven't already), the test will
pass.

(What I think happens is that without us supplying a return value, the
sqlite database is mocked, but there's no easy way to access it within the
test to check the method's called. If you know I'm wrong and have an
explanation, I'd love to hear it.)

Given the solution, you might wonder why I'd been bashing my head
against the keyboard for an hour or two to figure it out. It's just
knowing the vocabulary of what you need to do with mocks, whereas I'd
got sidetracked thinking there **must** be a way to implicitly access
methods of the object with the initial mock. Seeing and using patterns
is definitely a good way to develop; next time I do something similar,
I'll be much quicker to get something going.
