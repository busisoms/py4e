def count(string, x):
    count = 0
    for b in string:
        if b == x:
            count = count + 1
    return count


n = count("Good boy", "o")
print(n)
