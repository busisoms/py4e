"""Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit\
and print out the converted temperature."""

temp_in_C = float(input("What's the temperature in Celsius? "))
convert = (temp_in_C * 9/5) + 32
print(f'The weather in Fahrenheit ' + str(convert))
