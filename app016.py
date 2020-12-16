"""
#  nested loop in python
#  what coordinates? (x, y). (0.0)
for x in range (4):
   for y in range (3):
       print(f'({x}, {y})')
"""
# exercise,, print a 'F'
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
