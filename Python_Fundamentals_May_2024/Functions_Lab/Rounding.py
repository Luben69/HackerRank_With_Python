numbers_as_string = input().split()

numbers_as_integers = []

for num in numbers_as_string:
    numbers_as_integers.append(round(float(num)))

print(numbers_as_integers)