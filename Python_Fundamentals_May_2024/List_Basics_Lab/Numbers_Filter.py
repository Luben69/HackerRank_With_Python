n = int(input())
numbs = []
filtered_list = []


for _ in range(n):
    numbers = int(input())
    numbs.append(numbers)

command = input()

if command == 'even':
    for number in numbs:
        if number % 2 == 0:
            filtered_list.append(number)
elif command == 'odd':
    for number in numbs:
        if number % 2 != 0:
            filtered_list.append(number)
elif command == 'negative':
    for number in numbs:
        if number < 0:
            filtered_list.append(number)
elif command == 'positive':
    for number in numbs:
        if number >= 0:
            filtered_list.append(number)

print(filtered_list)