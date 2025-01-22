n = int(input())
total_sum = 0

for character in range(n):
    current_str = input()
    total_sum += ord(current_str)

print(f"The sum equals: {total_sum}")