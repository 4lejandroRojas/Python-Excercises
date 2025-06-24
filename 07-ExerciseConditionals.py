# Create a program to calculate the BMI (body mass index) of a person.
#  Ask the user for his height in meters and his weight in kg.

weight = float(input ("Introduce your weight (kilograms): "))
height = float(input ("Introduce your height (meters): "))

bmi = weight / (height * height)
print("Your BMI is:", round(bmi, 2))

if(bmi <= 18.5): 
    result = "Underweight"
elif(bmi > 18.5 and bmi <= 24.9):
    result = "Normal weight"
elif(bmi > 24.9 and bmi <= 29.9):
    result = "Overweight"
else:
    result = "Obesity"

print("Your score is:", result)