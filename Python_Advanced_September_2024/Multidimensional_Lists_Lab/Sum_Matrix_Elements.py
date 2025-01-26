rows, columns = [int(x) for x in input().split(", ")]

matrix = []

summon = 0

for r in range(rows):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)
    summon += sum(row_data)

print(summon)
print(matrix)
