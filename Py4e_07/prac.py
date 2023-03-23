# Opening files in python

file = open("mbox-short.txt")
count = 0
for line in file:
    count += 1
print(count)
