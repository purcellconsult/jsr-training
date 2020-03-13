############################
# How to create your own
# python modules
# -------------------------
# Learn how to create our
# own modules in python.
#
#
#
#############################


def double(x):
    """
    Takes x and doubles it
    """
    return x * 2


def triple(x):
    """
    Takes x and triples it
    """
    return x * 3


def multiply(x, y):
    """
    Multiplies x by y
    """
    return x * y


def demo():
    """
    Create a function that demos
    the functions in this module.
    """
    double_input = float(input("Enter in a number to double "))
    d1 = double(double_input)
    triple_input = float(input("Enter in a number to triple "))
    t1 = triple(triple_input)
    multiple_num1 = float(input("Enter a number 'a' "))
    multiple_num2 = float(input("Enter a number 'b' "))
    m1 = multiply(multiple_num1, multiple_num2)
    print(d1)
    print(t1)
    print(m1)

