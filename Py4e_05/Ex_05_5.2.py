#Exercise 2: Write another program that prompts for a list of numbers
#and at the end prints out both the maximum and minimum

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print("invalid entry")
        continue
        print(n)
    if largest is None or  n > largest:
        largest = n
    if smallest is None or n < smallest:
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
