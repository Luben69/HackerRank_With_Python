n = int(input())

odd_set = set()
even_set = set()

for i in range(1, n+1):
    points = 0
    name = input()
    for el in name:
        points += ord(el)
    final_points = points // i

    if final_points % 2 == 0:
        even_set.add(final_points)
    else:
        odd_set.add(final_points)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=', ')

elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')

elif sum(odd_set) < sum(even_set):
    print(*odd_set.symmetric_difference(even_set), sep=', ')
