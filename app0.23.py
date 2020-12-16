# dictionary, emoji convertion, split method
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
