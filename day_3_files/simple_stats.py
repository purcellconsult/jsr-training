###############################
#  Statistic Functions
# ---------------------
# Rewriting some formulas in
# python's standard module
#
# Helps use to develop algorithmic thinking
# Inspires you to create functions for your own workflow
# Helps you to create resharable code.
# Learn how to import your code.
# Good practice for coding interviews.
#################################

from math import sqrt


def mean(*args):
    """
    Computes the mean
    of an arbitrary list of
    numbers.
    """
    amount = 0
    for index, value in enumerate(args, start=1):
        amount += value
    return amount / index


def harmonic_mean(*args):
    """
    Computes the reciprocal 1/value for every value.
    Find the average of the reciprocals, and then divide
    the average by the total number of elements.
    """
    reciprocals = 0
    for index, value in enumerate(args, start=1):
        reciprocals += (1/value)
    return round(index / reciprocals, 3)


def variance(*args):
    """
    The average of the squared differences from
    the mean.
    Take the summation of the averages and divide by total items
    """
    amount = 0
    for index, value in enumerate(args, start=1):
        value = value ** 2
        amount += value
    return amount / index


def standard_deviation(*args):
    """
    Simply the square root of the variance.
    """
    amount = 0
    for index, value in enumerate(args, start=1):
        value = value ** 2
        amount += value
    return round(sqrt(amount / index), 3)


if __name__ == 'main':
    average = mean(1, 3, 5, 10, 20)
    print(average)
    harmonic = harmonic_mean(1, 2, 4)
    print(harmonic)
    variance1 = variance(206, 76, -224, 36, -94)
    print(variance1)
    st_dev = standard_deviation(206, 76, -224, 36, -94)
    print(st_dev)