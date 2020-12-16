course = 'Python for Beginners'
print(len(course))  # count the number of characters, general purpose
print(course.upper())  # specific for string
print(course)
print(course.lower())

print(course.find('P'))  # help find the index of characters
print(course.find(
    'o'))  # sensitive to upper case and lower case if you type somehting it doesnt exist, it will show negative
print(course.find('Beginners'))  # shows the index starting teh word 'Beginners'
print(course.replace('Beginners', 'Absolute Beginners'))
print(course.replace('P', 'J'))

print('Python' in course)  # to see if 'Python' sits in teh string

"""
len()
course.find()
course.upper()
course.lower()
course.replace()
'' in course
"""
