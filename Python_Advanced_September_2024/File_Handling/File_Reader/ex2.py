file = open("numbers.txt")

contents = file.read().split("\n")

total_sum = 0

for el in contents:
    try:
        total_sum += int(el)
    except ValueError:
        continue

print(total_sum)
