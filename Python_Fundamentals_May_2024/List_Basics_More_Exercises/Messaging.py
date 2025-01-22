numbers = input().split()
the_string = list(input())

message = ""

for num in numbers:

    index = sum(int(digit) for digit in num)

    index %= len(the_string)

    message += the_string[index]

    the_string.pop(index)

print(message)
