course = 'Python for Beginners'
print(len(course)) #len is a general purpose function
print(course.upper())
print(course) #.upper does not modify the core variable
print(course.lower())

print(course.find('P'))
print(course.find('Beginners')) #will show the starting index of the substring
print(course.replace('Beginners','Absolute Beginners')) #case sensitive
print('Python' in course) # will give a boolean solution