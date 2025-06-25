# Create a program that asks the user for 8 names of people and store them in a list.
# When all the names have been givem pick a random one and print it.

import random

people = []
while(len(people) < 3):
    person = input("Write the person's name: "+(len(people)))
    people.append(person)

print("The randon name is: ", people[random.randint(0, len(people))])