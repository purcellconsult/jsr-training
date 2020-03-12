# Crafting our own functions in python
# -------------------------------------
# We've used builtin functions like print(),
# input(), and int(), but now it's time to start
# crafting our own.
# creating your own module of functions
#
#######################################


def double(x):
    """
    Takes in an argument and then
    doubles it's value.
    """
    return x * 2

# f is the name of the function
# x is the parameter, or the value that gets passed


def f(x):
    """
    Currently a blank function
    """
    return x * 5


def g(x):
    pass


def h(x):
    pass


def i(x):
    pass

# how to call or execute a function


f1 = f(10)
print(f1)
f2 = double(20)
print(f2)
print(double.__doc__)