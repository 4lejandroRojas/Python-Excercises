# Boolean type should be defined with capitalize 'T' or 'F'
myBoolean = True
myBoolean = False

# Comparison operators
#   >   Greather than
#   <   Less than
#   ==  Equal to
#   !=  Not equal to
#   >=  Greather than or equal to
#   <= Less than or equal to

#A program that ask two numbers and compare them.
num1 = float(input("Write the first number: "))
num2 = float(input("Write the second number: "))

if(num1 > num2) :
    print(num1, "is greather than", num2)
elif(num1 == num2):
    print(num1, "is equal to", num2)
else:
    print(num1, "is less than", num2)
