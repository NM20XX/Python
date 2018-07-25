# Python program to shuffle a deck of card
# Draw n number of cards

import random
from itertools import product

# make a deck of cards using itertools module
# product() function in itertools module does the Cartesian product.
deck = list(product(range(1,14),['Heart','Spade','Club','Diamond']))

# shuffle
random.shuffle(deck)

# draw cards
while True:
  players = int(input("\nHow many players: "))
  num = int(input("\nHow many cards to draw: "))
  if players * num > 52:
    print("\nwrong input")
  else:
    break

# print cards
for i in range(players):
  print("\nplayer "+ str(i+1) + " You got below cards:\n")
  for i in range(num):
    print(deck.pop())
   

