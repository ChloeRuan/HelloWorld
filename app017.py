names = ['John', 'Bob', 'Mosh', 'Sarah', 'Mary']
names[0] = 'Jon'
print(names[0])  # 0, again, is a index, stands for John
print(names[2:])
print(names[2:4])

# Exercises
list = (1, 9)
print(list[-1])

numbers = [3, 6, 2, 8, 4, 10, 5]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)
