size = int(input())

matrix = []

diagonal = 0

for _ in range(size):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

for row_index in range(size):
    for col_index in range(size):
        if row_index == col_index:
            diagonal += matrix[row_index][col_index]

print(diagonal)