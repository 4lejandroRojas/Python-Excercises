#Create a program that asks the user for their birthday in the format "DD-MM-YYYY".
# Then print: "You were born in [month]"

birthdate = input("Introduce your birthday in format DD-MM-YYYY: ")
#Tuple of months
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

#Convert String to list. One possible but implies the creation of a list
birthdateList = birthdate.split("-")
monthNumber = int(birthdateList[1])
#Create an index using the conversion of the String based on the position of the Month
monthIndex = int(birthdate[3:5]) -1

print("You were born in ", months[monthNumber-1])
print("You were born in ", months[monthIndex])


# Create a program with a predefined list of people. Ask the user for their name, add it to the end of list and print the updated list
names = ["Juan", "Maria", "Carlos", "Sofia", "Luis"]
nameofUser = input("Introduce your name: ")
names.append(nameofUser)
print(names)
