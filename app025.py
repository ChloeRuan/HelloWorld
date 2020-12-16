# how to pass info to the function
def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')  # lots of text, low variable
    print('Welcome aboard')


"""
print("Hi" + name + "!")  # low text and low variables
print('Hi {}!'.format(name))  # low text, lots of variables
"""

print("Start")
greet_user("John", "Smith")
greet_user("Mary", "Dear")
print("Finish")

# parameters to receive info, argument is the actual info, name is parameter, "john" belongs to argument
