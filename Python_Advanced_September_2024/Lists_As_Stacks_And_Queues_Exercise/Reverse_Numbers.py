n = list(map(int, input().split()))
stack = []

while n:
    stack.append(n.pop())

print(*stack)