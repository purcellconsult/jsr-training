###############################
# The four core data structures in python
# Lists, tuples, sets, and dictionaries.
#
#
################################

# list
# -----
# A mutable data structure in python
# Similar to arrays in other languages

evens = [2, 4, 6, 8, 10]

# indexes
print(evens[0])  # 2
print(evens[2])  # 6
print(evens[-1])  # 10
print(evens[len(evens)-1])  # 10

# slicing lists

print(evens[0:3])   # [2, 4, 6]. The first index is inclusive and the second index is exclusive
print(evens[1:4])   # [4, 6, 8]
print(evens[::])    # returns the whole list
print(evens[::2])   # [2, 6, 10]
print(evens[::-1])  # reverse elements in a list

# how to modify?
# --------------
# a list is called mutable
# all the items in a list are known as elements

odds = [1, 3, 5, 3, 7, 9]
print(odds)          # [1, 3, 5, 3, 7, 9]
odds.append(11)      # adds 11 to the end
print(odds)          # [1, 3, 5, 7, 9, 11]
print(odds.count(3)) # 1

# getting the size with len()

size = len(odds)
print('size of odds is {}'.format(size))

# nested lists

x = [1, 2, 3, [4, 8, 2, 7], [1, 2, 3, 3]]  # can put lists inside lists

print(x[0])  # 1
print(x[1])  # 2
print(x[2])  # 3
print(x[3])  # [4, 8, 2, 7]
print(x[4])  # [1, 2, 3, 3]
print(x[4][1])  # 2

# iterate over a list

electronics = ['mp3', 'laptop', 'smartphone', 'lcd tv', 'tablet', 'pager' ]

# let's compare the size of two items in a list

if len(electronics[0]) < len(electronics[1]):
    print('Size of {} < {}'.format(electronics[0], electronics[1]))
else:
    print('Size of {} > {}'.format(electronics[0], electronics[1]))

# iterate over list using for loop
for x in electronics:
    print(x)

# iterating over list using enumerate function
for index, item in enumerate(electronics):
    print(index, '-->', item)


# while loops
size = len(electronics)  # size of list is 6
count = 0
while count < size:
    print(electronics[count])
    count += 1

# tuple
# ------
# how to declare

x = (1, 3, 1, 7, 6, 5)
# keep note of the hash address
print("The address of x = {}".format(hash(x)))

# can we index a tuple?
print(x[0])  # 1
print(x[-1])  # 5
print(x[3])  # 7

# keep note of how the hash address change. Why is that?
x = (1, 2)
print(x)
print("The address of x = {}".format(hash(x)))

del x  # deletes the tuple

# tuple does not allow item reassignment
# the following will cause an error
# x[0] = 10

# list allows item reassignment
i = [2, 3]
i[0] = 10
print(i)

# set
# -----
# this is a data structure
# sets allow only unique items
# the order of the items are not saved

a = {1, 1, 1, 2, 5, 10}
print(a)
print('set {} sorted is {}'.format(a, sorted((a))))

x = [1, 2, 1, 4, 6, 10, 3, 2]
print('{} sorted is {}'.format(x, sorted(x)))

# builtin methods for a set

a.update([110, 95])
print(a) # {1, 2, 5, 10, 110, 95}
x = a.intersection([3, 4])
print(x) # set()
x = a.union([1, 3, 7, 9, 23])
print(x) # {1, 2, 3, 5, 7, 9, 10, 23, 95, 110}

# simple for loop to iterate over a set

for x in a:
    print(x)

# dictionaries
# -------------
# a dictionary stores key/value pairs
# the keys are the first items in the pair
# hash tables are extremely popular data structures
# they are very efficient. The implementation is used for databases

lang = {'a': 'algol', 'c': 'cobalt', 'e': 'erlang', 'j': 'javascript'}
print(lang.keys())  # [a, c, e, j]
print(lang.values())  # [algol, cobalt, erlang, javascript]
print(lang.items()) # returns everything from dictionary

#  iterating over a dictionary and getting key/value pairs
for key, value in lang.items():
    print(key, '-->', value)

# iterating over a dictionary and getting values only
for value in lang.values():
    print(value)

# another way to format dictionaries in python
{  'key1': 1,
   'key2': 2,
   'key3': 3
}

print()
print(lang.get('a'))  # algol
print(lang.get('apple'))  # None
print(lang['a'])  # algol

