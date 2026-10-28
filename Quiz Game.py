'''Simple Quiz Game
Ask 5 questions.
Check each answer.
Keep a score.
At the end: You scored 4/5.'''

correct = 0
wrong = 0
q1 = int(input("what is 2+3 = "))
if q1 == 5:
    correct += 1
else:
    wrong += 1

q2 = int(input("what is 20+350 = "))
if q2 == 370:
    correct += 1
else:
    wrong += 1

q3 = int(input("what is 350-450 = "))
if q3 == -100:
    correct += 1
else:
    wrong += 1

q4 = int(input("what is 5*4 = "))
if q4 == 20:
    correct += 1
else:
    wrong += 1

q5 = int(input("what is 10/5 = "))
if q5 == 2:
    correct += 1
else:
    wrong += 1

print("You Scored = ",correct)