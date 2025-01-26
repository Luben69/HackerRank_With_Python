n = int(input())

occ = set()

for _ in range(n):
    names = input()
    occ.add(names)

print(*occ, sep="\n")
