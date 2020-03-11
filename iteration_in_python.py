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

for row in range(10):
    for col in range(10):
        print('*', end=' ')
    print()


pattern2 = """
*
* *
* * *
* * * *
"""

for row in range(6):
    for col in range(row):
        print('*', end=' ')
    print()

# while loop