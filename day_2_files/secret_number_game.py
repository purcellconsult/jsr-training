# Secret Number Game
# -------------------
# A text based game written in python.
# The user gets to take an arbitrary number of guesse.
# They will be provided feedback on if their guess
# is less than, greater than, or equal to the secret num.
# If equal, the secret number should be revealed, and
# then the loop terminates.
#
###########################################

from random import randint

secret_number = randint(1, 100)
print("The secret is {}. Don't tell anyone!".format(secret_number))
while True:
    user_guess = int(input("Enter in your guess "))
    if user_guess < 0 or user_guess > 100:
        print("Enter in a number within the range of 1-100")
    elif user_guess == secret_number:
        print("{} is the secret number. You win!".format(secret_number))
        break
    elif user_guess > secret_number:
        print("{} is greater than the secret number".format(user_guess))
    else:
        print("{} is less than the secret number".format(user_guess))

