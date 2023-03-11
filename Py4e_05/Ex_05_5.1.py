# Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done” then adds all numbers entered.
# largest_so_far = -1
# print('Before', largest_so_far)
# for num in [9,41,12,3,74,15]:
#     if num > largest_so_far:
#         largest_so_far = num
#     print(largest_so_far, num)
# print('After', largest_so_far)

# found = False
# print('Before', found)
# for value in [9,41,12,3,74,15]:
#     if value == 3:
#         found = True
#         break
#     print(found, value)
# print('after', value, found)

###############################################################################

i = 0
count = 0
while True:
    n = input("Enter a number ")
    if n == "done":
        break
    try:
        b = float(n)
    except:
        print("invalid entry")
        continue
    count = count + 1
    i = i + b
    avr = i/count
print(f"number count: {count}, total: {i}, average: {avr}")

################################################################################
