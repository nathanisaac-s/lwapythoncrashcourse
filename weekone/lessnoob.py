#! /usr/bin/env python3
"""
This is the module-level docstring, like a class-level Javadoc. It is
actually just a multi-line string: that's what the three quotes are for.

What a Real Programmer makes a Python.
"""
# import some things.
import sys
import time

# define a constant--this is only enforced by convention, you can change it later.
HELLO = "O HAI!"


# let's write our first method!
def say_something(name):
    """
    Let's say hello!
    """
    # python is whitespace sensitive. you must use tabs or spaces consistently.
    print("{} Today is {}".format(HELLO, time.strftime("%Y-%m-%d",
                                                       time.localtime())))
    # except when you're inside parens and in some other circumstances,
    # which makes mandatory whitespace less obnoxious. Set up your editor
    # properly and this cease to be an issue.
    print("Hello {person}".format(person=name))


# use of `main` is entirely optional and follows no enforced standard.
# but let's use a `main` function to make the program more recognizable.
def main(your_name):
    """
    Wow you follow conventions too!
    """
    # call our method
    say_something(your_name)

# now, let's actually run a program!
#
# in reality, there actually is a main called "__main__".
#
# We can worry about this in a later module, but the way it works is that
# double-double-underscores are "magic" methods provided by the interpreter
# under certain circumstances, like if you're running at the top-level or if
# a class implements specific __interface__. This is called the "data model".
#
# this is actually how infix operators work: a class implements __add__.
# see https://docs.python.org/3/reference/datamodel.html
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("sorry you need an arg.")
        # non-zero exit if improper use
        sys.exit(1)
    # wrap the whole program up in sys.exit() so that if it exists sucessfully
    # the OS and shell or other calling program are aware.
    sys.exit(main(sys.argv[1]))
