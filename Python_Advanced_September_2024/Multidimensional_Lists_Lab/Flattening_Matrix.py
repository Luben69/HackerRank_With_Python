rows_count = int(input())

matrix = []

for _ in range(rows_count):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)


new_matrix = []

for data in matrix:
    for el in data:
        new_matrix.append(el)

print(new_matrix)
