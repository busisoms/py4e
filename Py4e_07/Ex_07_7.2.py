# Write a program to prompt for a file name, and then read
# through the file and look for lines of the form: X-DSPAM-Confidence: 0.8475

count = 0
total = 0
n = input("enter a file name: ")
with open(n) as file:
    for line in file:
        if line.startswith("X-DSPAM-Confidence:"):
            number = float(line[19:])
            total += number
            count += 1
            average = total / count
    print(f"Average spam confidence: {round(average,12)}")
