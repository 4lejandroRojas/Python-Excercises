#Create a program with a predefined dictionary for a person.
#Include the following informatio: name, gender, age, address, phone

person = {
    "name": "Alejandro Rojas",
    "gender": "M",
    "age": None,
    "address": "Mexico",
    "phone": "515555555555"
}
expectedKeyToShow = input("Which property would you like to see? ").lower()
print(person.get(expectedKeyToShow, "property is not valid"))
