n = int(input())
our_list = set()

for _ in range(n):
    name = input()
    our_list.add(name)

print(*our_list, sep='\n')
