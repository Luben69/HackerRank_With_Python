numbers = input().split()

filtered_list = []

for num in numbers:
    filtered_list.append(abs(float(num)))

print(filtered_list)