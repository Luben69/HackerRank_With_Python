n_of_guests = int(input())

invited = []

for _ in range(n_of_guests):
    codes = input()
    invited.append(codes)


cmd = input()

while cmd != 'END':
    if cmd in invited:
        invited.remove(cmd)

    cmd = input()

print(len(invited))
for el in sorted(invited):
    print(el)
