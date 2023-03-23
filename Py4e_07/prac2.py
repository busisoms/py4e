# Seacrhing through a file

# with open('mbox-short.txt') as file:
#     for line in file:
#         line = line.rstrip()

#         if line.find('@uct.ac.za') == -1:
#             continue
#         print(line)
n = input
fhand = open(n("enter file path "))
for line in fhand:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print(line)
