'''Coin Toss Game
User chooses heads or tails.
Computer randomly chooses one.
Print whether the user won or lost.'''

import random

select = ('heads','tails')
select = random.choice(select)

me = input("Enter = ")

computer = select
print("Computer Selected = ",computer)

if me == computer:
    print("You Won")
else:
    print("You Lost")