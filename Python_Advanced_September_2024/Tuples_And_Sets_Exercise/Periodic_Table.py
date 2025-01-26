count = int(input())

chemicals = set()

for _ in range(count):
    for el in input().split():
        chemicals.add(el)

print(*chemicals, sep='\n')
