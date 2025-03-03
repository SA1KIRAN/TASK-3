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


