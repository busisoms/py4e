# Modifythe program that prompts the user for the file name so that it prints a
# funny message when the user types in the exact file name “na na boo boo”.


count = 0
total = 0
n = input("enter a file name: ")

try:
    with open(n) as file:
        for line in file:
            if line.startswith("X-DSPAM-Confidence:"):
                number = float(line[19:])
                total += number
                count += 1
                average = total / count
    print(f"Average spam confidence: {round(average,12)}")
except:
    if n == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print(f"File cannot be opened: {n}")
