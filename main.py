# Task - 1 - Guess the number

import random

number= random.randint(1,6)
attempts = 0
print("guess the number")

while True:

    guess=int(input("enter the number = "))
    attempts +=1
    if (guess > number):
        print("too heigh try again")
    elif (guess < number):
        print("too low")
    else:
        print("correct number")


# -------------------------------------------------------------------------------------------

# Task-2 - word scramble

import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

selection = random.choice(words)
scrambled_word=''.join(random.sample(selection, len(selection)))

print(scrambled_word)

attempts = 0

while True:
    answer=input("answer the original word")
    attempts +=1
    if (answer.lower()==selection.lower()):
        print("right answer")
    else:
        print("wrong answer try again")

