# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = input('Enter Hours: ')
rate = input('Enter rate: ')
pay = round(float(hours) * float(rate))
print('Total pay: ' + str(pay))      # had to the float "pay" into a str for concatenation.

