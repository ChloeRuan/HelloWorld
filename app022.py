# dictionnary, store info
customers = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}  # {} c an define dictionary, each key should be unique
print(customers["name"])
print(customers.get("birthday"))  # for info that is not in the dictionary
# we can supple the value for "birthday" too
print(customers.get("birthday", "Jan 1 1982"))
# update info
customers["name"] = "Jack Smith"
print(customers["name"])
customers["birthday"] = "Jan 1 1982"
print(customers["birthday"])

# exercise
phone = input("Phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch,
                                 "!") + " "  # "!" is a default value, it means that if we dont have a value in phone, like 5,if  we type out phone number is 555, it appears !!!1
print(output)
