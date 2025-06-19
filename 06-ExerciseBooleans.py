# Create a program and store your age in a variable. Then, ask the user for his age and print whether:
# He's older than you
# He's  younger than you
# You two have the same age

myAge = 32
userAge = int(input("Write your age: "))

if(myAge < userAge):
    print("User is older")
elif(myAge == userAge):
    print("User has the same age")
else:
    print("User is younger")