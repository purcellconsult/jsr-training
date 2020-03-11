# Boolean datatype exercises
# ---------------------------
# Learn about the boolean data type
# Learn about relational and logical operators
# Learn how to craft if/else/elif statements
# write code to check the proper letter grade a student received
# -------------------------------

# Expressions evaluates to True or False
x1 = True
x2 = False
print(type(x1))

# relational operators
# >, <, ==, >=, <=

# if statement
if 5 > 2:
    print('A!')

if 5 == 5:
    print("5 is equal to 5")

# if/else statements
y = 3
if y <= 3:
    print('abc')
else:
    print('def')

# Can optionally use parentheses to separate expressions
x, y = 2, 4
if (x < y) and (y > x):
    print('111')

# logical operators
# -----------------
# and
# or
# negation
# can combine multiple expressions

a1 = 5
if a1 >= 5 and a1 % 2 == 0:
    print('good')
else:
    print('not good')

if a1 >= 0 and a1 >= 3 and a1 >= 5:
    print("All True")

# 'or' operator
b1 = 10
if b1 < 5 or b1 >= 9:
    print("b1 works")
else:
    print("b1 does not work")

x, y = 2, 4
if x > y and y < x:
    print('111')


# combining and/or operators

b1, b2, b3 = 5, 10, 15
if (b1 > b2) and (b2 > b3) or (b3 > b2):
    print('101')
else:
    print('010')


# nested if statements
# an if statement inside an if statement
# nested if statements

x, y = 2, 3
if x >= 2:
    print('level one')
    if y < 5:
        print('level two')
    else:
        print('level two is not here')
else:
    print('level one is false')

# triple nested if statements
# an if statement, inside an if statement, inside an if statement

x, y = 2, 3
if x >= 2:
    print('level one')
    if y <= 3:
        print('level three')
        if x + y == 5:
            print('level three')
else:
    print("nothing happens")

# what's printed?
# why?

a = 2
if a:
    print('a = {}'.format(a))

# ALWAYS evaluates to True
if True:
    print('True is cool')

# ALWAYS evaluates to TRUE too
if not False:
    print("I'm not sure it will be printed??")

# negation example
# what's printed?
# happy
if not(not True and not False):
    print('happy')
else:
    print('sad')


# nested if statements

if a > 1:
    print('This is good')
    if a >= 2:
        print('This will work')
    else:
        print("Too bad")
    print("Does this execute?")

# elif statements
# ---------------
# allows for the checking of multiple 'if' statements
# if expression is true it evaluates expresion and ignores remaining checks

x, y, z = 2, 3, 4
if x > y:
    print('a')
elif y < z:
    print('b')
else:
    print('c')


# nested if statement?
# ----------------------
# Can you have an elif statement inside an nested if statement?
# YES

x, y, z = 2, 3, 4
if x == 2:
    print(x) # printed
    if y == 3:
        print(y) # printed  # not printed
    elif z == 4:
        print(x)
if y == 3:  # printed
    print(y)
if z == 4:
    print(z) # printed

# multiple if statements
# -----------------------
# If I want to just check the letter grade for 'grade' what's wrong with the following?
# B C and D are printed!

grade = 80
if grade < 0 or grade > 100:    # eliminates variables less than 0 or greater than 100
    print('Invalid Input. Try again')
if grade >= 90:
    print('A')
if grade >= 80:
    print('B')
if grade >= 70:     # will this block execute?
    print('C')
if grade >= 60: # what about this?
    print('D')
else:
    print(':(')


# Here's a better way to do the above
# Use elif statements
# This prevents all the other if statements from running

letter_grade = 75.98

if letter_grade >= 90 and letter_grade <= 100:
    print('A')
elif letter_grade >= 80 and letter_grade < 90:
    print('B')
elif letter_grade >= 70 and letter_grade < 80:
    print('C')
elif letter_grade >= 60 and letter_grade < 70:
    print('D')
else:
    print(':( :(')