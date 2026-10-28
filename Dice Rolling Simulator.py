'''Dice Rolling Simulator
User enters roll.
Computer randomly generates a dice number from 1–6.
Ask whether they want to roll again.'''

import random
select = random.randint(1,6)
me = int(input("Enter = "))
computer = select
print("Computer Selected = ",computer)
me1 = input("Want to roll again? = ")
while True:
    if me1 == "yes":
        print(int(input("Enter = ")))
        select = random.randint(1,6)
        computer = select
        print("Computer Selected = ",computer)
        me1 = input("What to roll again = ")
    if me1 == "no":
        break