#############################
# Error handling in python
# ------------------------
# try/except statements
#
#
#############################

# syntax errors
# --------------
# Also known as parsing error.
# Below is an example of a syntax error
# x = 'hello world!"

# The other type of error are exceptions
# Can build them using try/except statements
# try/except statement

try:
    divide = 10 / 1
    print(divide)
except ZeroDivisionError:
    print('DivisionError: Can\'t divide by zero')

# try/except/finally

try:
    read_num = int(input("Read in a number "))
except ValueError:
    print("Not a valid number.")
finally:
    print("This always run regardless of what happens above")


# try/except/else
try:
    read = input('Enter in some text ')
except KeyboardInterrupt:
    print('Keyboard Interrupt Generated! ')
else:
    print('Nothing funny happened! ')

