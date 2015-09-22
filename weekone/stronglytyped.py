#! /usr/bin/env python3
# https://i.imgur.com/6aclmM6.png
import time
# imports can pull in individual parts of a module
from datetime import datetime
from collections import namedtuple

# you'll see this later.
# it's effectively a lightweight class.
CallArgPair = namedtuple("CallArgPair", ["arg", "method"])


# python has classes--unlike Java, they aren't the unit of project structure
# so they can be named anything and multiple classes can live in one file.
#
# worry about this later.
class CallArg(object):  # inherit from object import for 'New-Style' classes.
    # you probably want to define a constructor.
    def __init__(self, arg, call):
        self.arg = arg
        self.call = call

    # here's a magic method to get more sugar.
    def __str__(self):
        return "CallArg(call={}, arg={})".format(self.call, self.arg)

    # python is unconcerned with method privacy.
    def run(self):
        self.call(self.arg)


def run_safely(potentially_broken_function):
    # python is newer than 1980 so it has exceptions. syntax is, of course,
    # whitespace sensitive
    try:
        # Java may be the industry leader getting books about OOP printing,
        # but Python (and lots of other langs) have a stronger object model.
        #
        # in Python, almost everything is an object (and the things that
        # aren't, like infix operators, are usually sugar around the object
        # data model.
        #
        # This means that methods and functions are also objects, allowing
        # them first-class status: anything you do with an object can be
        # done with a function. Cf. with Java prior to 1.8
        #
        # tl;dr: we can pass a method as a function.
        return potentially_broken_function()
    # like with all exception-based languages it's bad practice to 
    # catch all exceptions. But let's do that here for sake of demonstration.
    except BaseException as e:
        print("caught exception: {exc}\n  {msg}".format(exc=type(e), msg=e))
    # while not often used, python try-catch features an `else` that runs
    # prior to `finally` if the block doesn't throw an error.
    else:
        print("you ran a function ({}) successfully. programming is hard.".format(potentially_broken_function))
    finally:
        print("ran {}.".format(potentially_broken_function))


def run_an_eval(eval_str):
    try:
        # lol code injection on purpose
        return eval(eval_str)
    except Exception as e:
        print("caught exception: {exc}\n  {msg}".format(exc=type(e), msg=e))
    else:
        print("you did stupid shit and evaled `{}` successfully. programming is hard.".format(eval_str))
    finally:
        print("ran {}.".format(eval_str))


def run_arg_call_pair(arg_with_call):
    try:
        # mass assignment is possible.
        arg, method = arg_with_call[0], arg_with_call[1]
        # this isn't ideal since you could easily hit a type error here.
        return method(arg)
    except Exception as e:
        print("caught exception: {exc}\n  {msg}".format(exc=type(e), msg=e))
    else:
        print("you ran `{}({})` successfully. programming is hard.".format(method, arg))
    finally:
        print("ran {}.".format(method))


def run_typesafe_arg_call_pair(arg_with_call):
    try:
        # isinstance checks an object against a type.
        # the `assert` keyword checks something is true.
        assert isinstance(arg_with_call, CallArgPair)
        arg_with_call.method(arg_with_call.arg)
    except Exception as e:
        print("caught exception on arg: {arg} {exc}\n  {msg}".format(arg=arg_with_call,
                                                                     exc=type(e),
                                                                     msg=e))
    else:
        print("you ran `{}({})` successfully. programming is hard.".format(arg_with_call.method,
                                                                           arg_with_call.arg))
    finally:
        print("ran arg-call-pair: {}.".format(arg_with_call))


def run_class_based(call_arg):
    # python is dynamically typed AKA "duck typed" AKA late-bound, meaning
    # you can get away with something like this.
    try:
        # because of late-binding, you don't know if the code will run until
        # an object gets to the call site, so generally speaking some checking
        # is a good thing.
        #
        # you could just asert, but let's try to be clever.
        if not isinstance(call_arg, CallArg):
            # try to instantiate on-demand from args
            call_arg = CallArg(call_arg[0], call_arg[1])
        call_arg.run()
    except Exception as e:
        print("caught exception: {exc}\n  {msg}".format(exc=type(e), msg=e))
    else:
        print("you ran `{}` successfully. programming is hard.".format(call_arg))


def main():
    # python has had lambdas since about 2003 or so, which means that at least
    # it caught up with 1950s comp sci.
    #
    # in reality it's just interpreted to an anonymous `def` by the VM, and
    # because passing named functions is okay, use of lambda tends to be
    # limited...
    print("\n\n[+]    let's run some simple calls.\n")
    simple_calls = [lambda: "5" - 3,
                    lambda: "5" + 3,
                    lambda: "5" - "4",
                    lambda: "5" + str(4),  # this one works.
                    lambda: "foo" + None]

    for each in simple_calls:
        run_safely(each)
    # this looks like a type error, but it's not: str class implements __mul__
    # it implements __add__, too, but doesn't cast implicitly.
    print(79 * "-")

    print("\n\n[+]    let's run some calls that take args.\n")
    # ...for example, you can name lambdas...
    times_three = lambda x: x * 3
    five_plus_minus = lambda x: "5" + x - x
    five_minus_plus = lambda x: "5" - x + x

    # ...or just inline it explicitly...
    def times_three_again(arg):
        return arg * 3

    # ...you can also do that on one line:
    def times_four(x): return x * 4

    # functions defined inline in another function only exist in that scope.
    #
    # if you haven't seen a tuple before, you have now.
    # a tuple is an immutable array-like structure that is preeminantly useful.
    calls_with_args = [(1, times_three),
                       (1, five_minus_plus),
                       (1, five_plus_minus),
                       (1, times_three_again),
                       (1, times_four)]

    # this doesn't work, but why?
    for every in calls_with_args:
        run_safely(every)
    print("??? let's try again\n")
    for _, every in calls_with_args:
        run_safely(every)
    print("??? and one more time.\n")
    for call_with_arg in calls_with_args:
        run_arg_call_pair(call_with_arg)
    print(79 * "-")

    # what if you want more type safety?
    print("Let's run this with some type checking.")
    namedtup_calls_with_args = [CallArgPair(1, times_three),
                                CallArgPair(1, times_three_again),
                                datetime.now(),
                                "blow up"]
    for call_with_arg in namedtup_calls_with_args:
        run_typesafe_arg_call_pair(call_with_arg)
    print(79 * "-")

    print("Maybe you like using classes though.")
    #what if you <3 classes?
    class_calls = [ CallArg(1, times_three),
                    CallArg(1, times_three_again),
                    (1, times_four),
                    (0, 1),
                    "not a class" ]
    for each in class_calls:
        run_class_based(each)

    print("\n\n[+]    now let's do it Biznez Rewls style\n")
    # don't use evals.
    calls_to_eval = ['x * 3',
                     '"5" + + "5"',
                     '"foo" + + "foo"',
                     '"5" + - "2"',
                     '"5 - 2"']

    for each in calls_to_eval:
        run_an_eval(each)
    print(79 * "-")


if __name__ == "__main__":
    # because everything is an object, we can import inline and conditionally.
    if time.time() > 0:
        import sys
    sys.exit(main())
