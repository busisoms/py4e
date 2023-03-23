# Write a program to read through a file and print the contents
# of the file (line by line) all in upper case.

file_name = input("Enter a file_name name: ")
with open(file_name) as file:
    for line in file:
        line = line.strip()
        if line.endswith("Sat, 05 Jan 2008 09:14:16 -0500"):
            break
        line = line.upper()
        print(line)
