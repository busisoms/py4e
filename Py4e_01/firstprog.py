#Python for Beginners - with Mosh
# excercise 1
# name = "John"
# age = 20
# is_patient_new = True
#
# print(f"Name: {name} \nAge: {age}  \n{name} is a new patient {is_patient_new}")

# #excercise 2
# no_1 = input('First> ')
# no_2 = input('second> ')
#
# sum = (float(no_1) + float(no_2))
#
# print("Sum: " + str(sum))

# excercise 3

w = float(input("Weight: "))
w_type = input("(K)g or (L)bs: ")
n = w * 0.45359237
l = w * 2.2046

if w_type.lower() == "l":
    print(f"Weight in Kg: {n:.2f}".format(n))

elif w_type.lower() == "k":
    print(f"Weight in lbs: {l:.2f}".format(l))

print("done")
