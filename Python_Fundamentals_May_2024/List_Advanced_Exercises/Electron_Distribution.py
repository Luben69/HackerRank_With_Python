electrons = int(input())
distribution = []
shell = 1

while electrons > 0:
    capacity = 2 * shell**2
    if electrons >= capacity:
        distribution.append(capacity)
        electrons -= capacity
    else:
        distribution.append(electrons)
        electrons = 0
    shell += 1

print(distribution)
