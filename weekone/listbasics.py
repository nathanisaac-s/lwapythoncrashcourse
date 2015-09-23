#! /usr/bin/env python3
# ^ this line is a 'shebang' or 'hashbang' or 'crunchbang'. it tells a
# unix-like system what program to run a script through so that you can
# set the file to an executable and call it by itself. It's like how 
# windows guesses the program via the filename extention.

# python has imports. they're usually less-namespaced than java.
# module names should not have uppercase, spaces, dashes, underscores, etc.
import random

#
# Lists
#
# lists are dynamic structures that permit mixed types and have both
# array and list-like interfaces available.

# prefer underscores for variable names
# python is fluent and flexible.
my_first_words = "hai u guise lets go and learn us a new python for an such a great goods!"
hello = "hello"
world = "world"
hello_world = hello + " " + world
print(hello_world)
my_first_list = my_first_words.split()  # unlike java < 1.7, python ships with useful stdlib methods.

# you might want to loop over a list...
i = 0
while (i < len(my_first_list)):
    print(my_first_list[i])
    i = i + 1

# ...except it's not 1970 anymore, so don't do that again.
# we can iterate over the list:
for word in my_first_list:
    print(word)  # you will see `print word` in python 2. print is now just a function in python 3.

# maybe you want to index the list. you might be tempted to do this:
i = 1
for word in my_first_list:
    print("{}: {}".format(i, word))
    i += 1  # since it's not pretending to be a 1970s language, python has no `++` operator.

# Remember how I said not to do that and that python ships with features? The saner way is simple:
for index, word in enumerate(my_first_list):
    print((word + " ") * index)  # I thought you said python was type safe! how can you multiply a string?

# because string implemetns __mul__, which exposes the `*` syntax to the user.
# start with 1, because we don't want to `* 0` against the first word and disappear it.
for index, word in enumerate(my_first_list, 1):
    print((word + " ").__mul__(index))  # I thought you said python was type safe! how can you multiply a string?

# maybe we need more words.
my_first_list.append("i'm")
my_first_list.append([ "not", "finished", "yet!" ])

print(my_first_list)
# we can index and slice into lists.
print(type(my_first_list[0]))
print(type(my_first_list[-1]))
# see how that last one  is a different type? let's fix it.
# first, pop the last value off and grab it.
whoops = my_first_list.pop()
my_first_list += whoops  # `+=` calls __iadd__ for 'iterable add'
# that's better.
print(my_first_list)

# let's noisy up our list some.
orig_list_len = len(my_first_list)
for _ in range(0, 1000):
    rand_draw = random.randint(0, orig_list_len - 1)  # list slicing can get fencepost errors
    my_first_list.append(my_first_list[rand_draw])

# let's get back to slicing. like any real langauge python is zero-indexed.
print(len(my_first_list))
print(my_first_list[0:3])
print(my_first_list[:3])
print(my_first_list[1018:])
print(my_first_list[-3:])

# here's the fencepost error.
try:
    print(my_first_list[len(my_first_list)])
except IndexError as e:
    print("Ruhroh! Got an IndexError: " + str(e))

print(my_first_list[len(my_first_list) - 1])
print(my_first_list[-1])
