# handle errors, define a "try" block
try:
    age = int(input('>age: '))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print('Age cannot be zero')
except ValueError:
    print('Invalid value')
# if you type a word, the terminal will say error as this cannotbe converted integer. in python 0 is correct, it means
# python is no crashed, anyting  above 0 is wrong
