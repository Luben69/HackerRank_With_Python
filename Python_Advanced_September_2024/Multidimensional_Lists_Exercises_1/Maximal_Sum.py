rows_count, cols_count = [int(x) for x in input().split()]

matrix = []

for _ in range(rows_count):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)

result = -181

for rows in range(rows_count-2):
    for cols in range(cols_count-2):
        sum_number = 0
        for i in range(rows, rows + 3):
            for j in range(cols, cols +3):
                sum_number += matrix[i][j]
        if sum_number > result:
            result = sum_number
            max_c = cols
            max_r = rows

print(f'Sum = {result}')
for rows in range(max_r, max_r + 3):
    for cols in range(max_c, max_c + 3):
        print(matrix[rows][cols], end=' ')
    print()
