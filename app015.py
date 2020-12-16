for item in 'python':  # see each character in this string
    print(item)

    for item in ['Mosh', 'Josh', 'Sarah']:  # for a list o
        # f things
        print(item)
for item in [1, 2, 3, 4]:
    print(item)
# range function
for item in range(10):
    print(item)
for item in range(5, 10):
    print(item)
for item in range(5, 10, 2):  # two steps forward，间隔为2
    print(item)

# exerccise
prices = [10, 20, 30]
total_cost = 0
for price in prices:
    total_cost += price
print(f'Total: {total_cost}')
