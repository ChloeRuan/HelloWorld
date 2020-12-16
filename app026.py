def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')  # lots of text, low variable
    print('Welcome aboard')


print("Start")
greet_user(last_name="John",
           first_name="Smith")  # they are teh values for teh parameters we defined above, key-word argument
# keyword argument should be after teh postional argument
greet_user("A", last_name="Smith")
print("Finish")
