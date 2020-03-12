# Coin Simulator
# ---------------
# Models the flipping of a coin in python
# A coin has two sides. Heads and tails.
# We keep track of how many times the coin
# landed on heads and how many times it
# landed on tails.
######################################

from random import choice
from time import sleep
from random import randint

flips = randint(1, 300)
coin = ('heads', 'tails')

h, t = 0, 0     # h represents heads and t represents tails

for x in range(flips):
    toss = choice(coin)  # selects 'heads' or 'tails' from coin
    if toss == "heads":
        h += 1
    else:
        t += 1

print('Coin landed on heads {} times! '.format(h))
print('...')
sleep(5)
print('Coin landed on tails {} times! '.format(t))
if h == t:
    print('TIE!')
elif h > t:
    print('Heads appeared the most!')
else:
    print('Tails appeared the most!')