# Exercise 1
"""
patient_name = "John Smith"
age = 20
new_patient = True
print(patient_name)
print(age)
print(new_patient)
"""
# Exercise 2
"""
num1 = float(input("first "))
num2 = float(input("second "))
sum = num1 + num2
print("Sum: " + str(sum))

"""
# Exercise 3

# Weight = input("weight ")
# Kg_or_lbs = input("(k)g or (L)bs ")
# if Kg_or_lbs == "l":
#     print(float(Weight) * 0.453592)
# elif Kg_or_lbs == "k":
#     print(float(Weight) * 2.20462)
# this is my solution

# mosh Solution
"""
weight = float(input("weight "))
Unit = input("(k)g or (L)bs ")
if Unit.upper() == "K":
    converted = weight / 0.45
    print("weight in lbs: " + str(converted))
else:
    converted = weight * 0.45
    print("weight in kg: " + str(converted))
"""






