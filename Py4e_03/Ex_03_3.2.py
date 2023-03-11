# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully\
# by printing a message and exiting the program.

# hours = input('Enter Hours: ')
# rate = input('Enter rate: ')
# try:
#     pay = float(hours) * float(rate)
#     print('pay: ' + str(pay))
# except:
#     print('Error, please enter numeric input')
try:
    hours = float(input('Enter hours: '))
    rate = float(input('Enter rate: '))
except:
    print('Error, please enter numeric input')
    quit()
pay = hours * rate
ot_rate = rate * 0.5
over_time = (round(float(hours) - 40) * ot_rate) + pay

if hours <= 40:
    print('Total pay: '+ str(pay))
elif hours > 40:
    print('Total Pay + over time: ' + str(over_time))


