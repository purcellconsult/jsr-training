###############################
# Strings in python
# -----------------
# Learn how to create them,
# manipulate them, and use
# common string functions
# and methods.
#
##################################

city = 'San Francisco'
city1 = 'SanFrancisco'

# indexing
print(city[0])  # S
print(city[5])  # r
print(city[3])  #
print(ord(city[0]))  # 83
print(ord(city[3]))  # 32
print(len(city))     # 13
print(len(city1))   # 12
print(city[12])     # o
print(city[len(city)-1])  # o
print(city1[len(city1)-1])  # o

# negative indexes
print(city[-1])     # maps to last character
print(city[-2])     # maps to second to last char

# slicing
print(city[0:3])    # returns values from index 0-2
print(city[::2])    # returns every 2 indexes in a string
print(city[::-1])   # reverses the string

# string methods
m1 = 'hello world everyone!'

print(type(m1))     # <class 'str'>
print("This is an int type", type(10))  # This is an int type <class 'int'>
print(city.upper())  # SAN FRANCISCO
m1 = m1.split('-')  # splits a string around the sep
print(type(m1))     # <class 'list'>


stringy1 = 'hello-world'
stringy1 = stringy1.replace('-', '*')
print('This =', stringy1)  # This = hello*world
x1 = stringy1.find('e')
x2 = stringy1.find('l')
print(x1)  # 1
print(x2)  # 2

# 3 ways to format strings in python
# ----------------------------------

print('hello', 10)  # format strings using commas
print("{} {}{}".format(10, 100, 'star'))    # format using format() method
print('%d %d %s' % (10, 100, 'hello!'))     # format using c-style technique

