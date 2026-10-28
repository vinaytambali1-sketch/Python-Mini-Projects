import random
select = ('rock','paper','scissor')
select = random.choice(select)
me = input("Enter = ")
computer = select
print("Computer selected = ",computer)
if me == computer:
        print("Tie")
else :
    if me == 'rock' and computer == 'paper':
        print("Computer Wins")
    elif me == 'paper' and computer == 'scissor':
        print("Computer Wins")
    elif me == 'rock' and computer == 'scissor':
        print("You Wins")
    elif me == 'paper' and computer == 'rock':
        print("You Wins")
    elif me == 'scissor' and computer == 'rock':
        print("Computer Wins")
    elif me == 'scissor' and computer == 'paper':
        print("You Wins")