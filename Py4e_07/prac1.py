# a program that opens any file given a path

file_path = input("enter file path: ")
try:
    with open(file_path) as file:
        n = file.read()
    print(f"\n{n}")
except FileNotFoundError:
    print("File not found")
