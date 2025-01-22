factor = int(input())
count = int(input())

list_count = []

for mult in range(1, count + 1):
    list_count.append(factor * mult)

print(list_count)