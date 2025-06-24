people = []

#It will compare the lenght of the list people and it won't allow more than 5
while( len(people) < 5):
    person = input("Introduce the person's name: ")
    people.append(person)

print(people)