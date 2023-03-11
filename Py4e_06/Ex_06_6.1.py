""" Write a while loop that starts at the last character in the
string and works its way backwards to the first character in the string,
printing each letter on a separate line, except backwards."""

fruit = "banana"
index = 5
while True:
    letter = fruit[index]
    index -= 1
    print(letter)
    if index == -1:
        break

print("done")
