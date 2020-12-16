#  comparison operator
temperature = 30

#  ==
if temperature >= 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#  exercise
name_character = 3
if name_character < 3:
    print("name must be at least 3 characters")
elif name_character > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")

# correction
name = "J"
print(len(name))
if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good!")
