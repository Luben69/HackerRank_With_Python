people = list(map(int, input().split()))
k = int(input())

execution_order = []

index = 0

while people:
    index = (index + k - 1) % len(people)

    execution_order.append(people.pop(index))

print(f"[{','.join(map(str, execution_order))}]")
