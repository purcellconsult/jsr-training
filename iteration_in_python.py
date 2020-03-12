# LOOPS: 03/10/2020
# -----------------
# Example for loops for python training
# Example while loops for python training
# Haven't covered while loops
# Or iterating over strings and data structures

# for loop
for x in range(10):
    print(x)

# even numbers in range of 1...10000
# use % operator to test if number is even

for x in range(1, 10001):
    if x % 2 == 0:
        print('x =', x)

print('----------')

# prints odd numbers from 1 ... 10000
for x in range(1, 10001):
    if x % 2 == 1:
        print(x)
print('-----')

# inner loops:
# the outer controls the inner loop
# therefore, the inner loop must complete
for x in range(5):  # outer
    for y in range(3):  # inner
        print('x = {}, y={}'.format(x, y))

pattern1 = """
* * * *
* * * *
* * * *
"""

print(pattern1)
"""
* * * *
* * * *
* * * *
"""


pattern2 = """
*
* *
* * *
* * * *
"""

pattern3 = """
$
* $
* * $
* * * $
"""
print()
for row in range(1, 5):
    for col in range(row):
        if col + 1 == row:
            print('$', end=' ')
        else:
            print('*', end=' ')
    print()


# Sum all the numbers from 1-100
count = 0
for nums in range(1, 101):
    count += nums
print('The sum of 1-100 = {}'.format(count))


# create the multiplication tables from 1 ... 5

for x in range(1, 6):
    for y in range(1, 6):
        print('{} x {} = {}'.format(x, y, x * y))
    print('----------')

# Can you combine else statement with for loop?
for x in range(5):
    print(x)
else:
    print('nada')

# triple nested loop?
# -------------------
# quick 5 minute QUIZ in PPT


# while loop
i = 0
while i < 10:
    print("i = {}".format(i))
    i += 1

# break statement
# ---------------
# causes the loop to exit

i = 0
while True:
    i += 1
    print('i = {}'.format(i))
    if i == 20:
        break
print()

# continue statement
# -------------------
# forces a skip in the cycle

x = 0
while True:
    x += 1
    if x == 5:
        continue
    elif x == 10:
        continue
    elif x == 25:
        print('{}!'.format(x))
        break
    else:
        print(x, end=' ')

i = 0
while i < 10:
    if i % 2 == 0:
        print("{} is even".format(i))
    i += 1
else:
    print('Nice while loop!')


# using while loop to read infinite input
# while True:
#     user_input = input("Enter in some input. Type 'remove' to terminate ")
#     if user_input == 'remove':
#         break
#     else:
#         print(user_input)

# timeit module
# --------------
# ? from yesterday
# docs: https://docs.python.org/3/library/timeit.html
# one way to test the performance of implementations
# this is suitable for small snippets of code

import timeit

nested_loops = """
for x in range(100):
    for y in range(100):
        print(x, y)
"""
# commented out as it takes a good 8-10 seconds to run on my machine
print(timeit.timeit(stmt=nested_loops, number=50))

docstring = """
This is an example of a docstring.
It's typically used to help describe
functions, methods, and classes you create.
"""
print(type(docstring))
print(docstring.__str__())


# Iterating over strings
# ----------------------
# can use either the 'for' or 'while' loop

drink = 'double shot espresso'
# using a for loop
for cup in drink:
    print(cup)
print('-----')

# one way to get the index of each character using a for loop
for cup in range(len(drink)):
    print(drink[cup])

print('--------------------')

# Using enumerate to keep track of index in for loop
for index, char in enumerate(drink):
    print('index = {}, char = {}'.format(index, char))
print()

# Iterating over strings using a while loop
# Notice the string in print statement. It includes, single & double quotes

i = 0
while i < len(drink):
    print("'{}' at index {} = {}".format(drink, i, drink[i]))
    i += 1