#To create a list with strings -> Check the use of []
students = ["John", "Mary", "Steve"]
students2 = ["Bety", "Pietro", "Jay"]

#To get the last student (Steve)
print(students[-1])

#To get the first two students (John & Mary)
print(students[:2])

#To add elements
#At first -> Using the index number
students.insert(0, "George")
#At final
students.append("Kate")

print(students)
#Delete the last element -> Without index number
students.pop()

#Delete the element at specific position -> Using an index number
students.pop(1)

#Delete a specific 
students.remove("Mary")
print(students)

#Concat two lists
allStudents = students + students2
print(allStudents)

#Tuple is an inmmutable -> Check the use of {}
months = ("Junuary", "February", "March")
daysOfWeek = ("Monday", "Friday", "Saturday")

#Concat two tuples
monthsAndDaysWeek = months + daysOfWeek
print(monthsAndDaysWeek)
