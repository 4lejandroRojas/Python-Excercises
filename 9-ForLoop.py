# Generate a program with a list that is iterated over by a for loop and filters out the empty elements.

blogPosts = ["", "The most powerful tools in Javascript", "", "Python and its advanteges", "empty"]

for post in blogPosts:
    if (post == "" or post == "empty"):
        continue
    
    print(post)

print("----------------------")
# -------
#It is also possible use a range to iterate
for x in range(0, 10):
    print(x)

print("----------------------")
# -------
#It is also possible use a dictionary to iterate
person = {
    'name': 'Alejandro',
    'lastName': 'Rojas',
    'Gender': 'Male'
}

for key in person:
    print(key, ":", person[key])

print("----------------------")
# -------
#Iterate a list inside a dictionary
blogPosts = {   
             "Javascript": ["The most powerful tools in Javascript", "Promises and its advantages"],
             "Python":["Python and its advanteges", "Machine Learning + Python"],
             "Java": ["New Java 21 Features", "Java and its power in enterprise companies"]
            }

for language in blogPosts:
    print("-> Posts for language", language, ": ")
    for post in blogPosts[language]:
        print(post)
print("----------------------")