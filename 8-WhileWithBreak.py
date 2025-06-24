#Create a program that ask a number to guess a number between zero and ten.

import random

number = random.randint(0, 10)

guess = int(input("I'm thinking in a number between zero and then. Can you guess it?: "))
while True:
    if ( number == guess):
        break
    else:
        guess = int(input("Nope. Try it again: "))

print("You're right. I was thinking in the number: ", number)