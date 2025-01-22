n1, n2, n3 = [int(x) for x in input().split(".")]

n3 += 1

if n3 == 10:
    n3 = 0
    n2 += 1
    if n2 == 10:
        n2 = 0
        n1 += 1
        if n1 == 10:
            n1 = 0
print(f"{n1}.{n2}.{n3}")