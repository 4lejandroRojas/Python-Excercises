# Create a program that calcules the total note. Given the grades, absences & total classes.
grade1 = float( input("Write the grade of the first test: "))
grade2 = float( input("Write the grade of the second test: "))
absences = int( input("Write the number of absences: "))
totalClasses = int ( input("Write the number of classes: "))

averageGrade = (grade1 + grade2) / 2
attendance = (totalClasses - absences) / totalClasses

# Print average grade and attendance
print("Average grade: ", averageGrade)
print("Attendance rate: ", str(round(attendance * 100, 2))+"%")


if (averageGrade >= 6):
    if(attendance >= 0.8):
        print("The student has been approved.")
    else:
        print("The student has been failed due to an attence rate lower than 80%.")
elif(attendance >= 0.8):
    print("The student has been failed due to an average grade lower than 6.")
else:
    print("The student has been failed due to an average grade lower than 6 and an attence rate lower than 80%.")

# Additional change with and and or operators
if (averageGrade >= 6 and attendance >= 0.8):
    print("The student has been approved.")
elif(averageGrade < 6 and attendance < 0.8):
    print("The student has been failed due to an average grade lower than 6 and an attence rate lower than 80%.")
elif(attendance < 0.8):
    print("The student has been failed due to an attence rate lower than 80%.")
else:
    print("The student has been failed due to an average grade lower than 6.")
