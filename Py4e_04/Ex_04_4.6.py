#Rewrite your pay computation with time-and-a-half for over-time and create a function called computepay which takes two parameters
#(hours and rate).

# hours = float(input('Enter hours: '))
# rate = float(input('Enter rate: '))
# pay = hours * rate
# ot_rate = rate * 0.5
# over_time = (hours - 40) * ot_rate + pay
#
# if hours <= 40:
#     print(str(pay))
# elif hours > 40:
#     print(str(over_time))

def computepay(hours, rate):
    pay = hours * rate
    ot_rate = rate * 0.5
    over_time = (hours - 40) * ot_rate + pay
    if hours <= 40:
        return pay
    else:
        hours > 40
        return over_time

hours = float(input('Enter hours: '))
rate = float(input('Enter rate: '))
x = computepay(hours, rate)
print('Pay ' + str(x))
