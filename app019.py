# list of functions
numbers = [5, 2, 1, 7, 4]
"""
numbers.append(20)
print(numbers)
"""

numbers.insert(0, 10)  # 0 stands for index, before '0', 10 is teh actually number we want to insert
print(numbers)
numbers.remove(5)
print(numbers)
numbers.clear()
numbers = [12, 1, 5, 9, 7, 9]
numbers.pop()  # remove teh last number
print(numbers)
print(numbers.index(7))
print(50 in numbers)  # in check checks the existence or sequence of the character
print(numbers.count(5))
print(numbers.sort())  # it appears "none", none is an object in python that represents the absence of a value
numbers.sort()  # sort teh items in descending order
numbers.reverse()  # daoxu
print(numbers)
numbers2 = numbers.copy()
numbers2.append(10)
print(numbers2)

#  exercises, remove teh duplicates
numbers3 = [1, 1, 3, 5, 3, 9]
uniques = [5, 9]
for number in numbers3:
    if number not in uniques:
        uniques.append((number))
    print(uniques)
