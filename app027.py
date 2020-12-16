# create functions that return
def square(number):
    return number * number


"""
result = square(3)
print(result)
"""

"""
def square(number):
    print(number * number)
print(square(3))  # if you doesnt have "return", teh timinal will say "none" after 9 because none represents teh absence of teh valu
"""


def square(number):
    print(number * number)
    return


# all function will say none if without the return statement


# exercise
"""
message = input(">")
words = message.split(' ')  
print(words)  # get a seperated words of the msg
emojis = {
    ":)": "😄",
    ":(": "😟"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)
"""


def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😄",
        ":(": "😟"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
