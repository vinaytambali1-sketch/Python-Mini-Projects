'''Number Guessing Game
Computer randomly selects a number from 1–100.
User keeps guessing.
Print:=== "Too High"  ,  "Too Low"  , "Correct!"'''


import random
select = random.randint(1 , 100)
computer = select
me = int(input("Enter number = "))
print("Computer Selected = ",computer)

if me == computer:
    print("Correct!")

else : 
    if me > computer:
        print("Too high")
    elif me < computer:
        print("Too low")
    else:
        print("Correct!")