# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# hours = input('Enter hours: ')
# rate = input('Enter rate: ')
# pay = round(float(hours) * float(rate))
# ot_rate = round(float(rate) * 0.5)
# over_time = (round(float(hours) - 40) * ot_rate) + pay
#
# if hours <= '40':
#     print(str(pay))
# elif hours > '40':
#     print(str(over_time))

# if hours is not converted to float in the beginning it will return a str
hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
pay = hours * rate
ot_rate = rate * 0.5
over_time = (hours - 40) * ot_rate + pay

if hours <= 40:
    print(str(pay))
elif hours > 40:
    print(str(over_time))
