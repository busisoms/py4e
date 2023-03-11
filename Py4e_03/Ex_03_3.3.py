# Write a program to prompt for a score between 0.0 and 1.0.
# If the score is out of range, print an error message.
# If the score is between 0.0 and 1.0, print a grade
try:
    sc = float(input('Enter score: '))
except:
    print('Bad score ')
    quit()
if sc < 0.6:
    print('F')
elif sc <= 0.7:
    print('D')
elif sc <= 0.8:
    print('C')
elif sc <= 0.9:
    print('B')
elif sc <= 1.0:
    print('A')
else:
    print('Bad score')
