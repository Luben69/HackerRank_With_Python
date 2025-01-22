from collections import deque

kids_name = deque(input().split())
tosses = int(input()) - 1

while len(kids_name) > 1:
    for i in range(tosses):
        kid = kids_name.popleft()
        kids_name.append(kid)

    print(f'Removed {kids_name.popleft()}')
print(f'Last is {kids_name.popleft()}')
