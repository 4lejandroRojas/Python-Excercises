#Dictionary. They are mutable and it can store any kind of data. type= dict
person = { "firstName": "John",
          "lastName": "Green",
           "birthYear": 1980,
            "countryOfBirth": "Canada"
        }
print(person["firstName"])

#Update the birth year
person["birthYear"] = 1979

#Ad new keys/properties to the dictionary
person["maritalStatus"] = "Married"
person["children"] = ["Nathalie", "Ethan"]

#Update an existing property without deleting the previous value
person["children"].append("Ana")

#If the property does not exist, a KeyError appears.
#person["notExist"] -> KeyError
age = person.get("age", "Property does not exist")
print(age)

#It can useful to define keys as variables and use them to get or return the wanted data
keyFirstName = "firstName"
firstNameToShow = person[keyFirstName]
print(firstNameToShow)

firstNameToShow = person.get("firstName")
print(firstNameToShow)

#Delete all the properties of a dictionary
person.clear()
