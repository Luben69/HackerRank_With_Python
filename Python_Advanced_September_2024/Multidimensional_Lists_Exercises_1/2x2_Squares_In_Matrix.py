rows_count, cols_count = [int(x) for x in input().split()]

matrix = []

points_found = 0

for _ in range(rows_count):
    row_data = [x for x in input().split()]
    matrix.append(row_data)

for rows in range(rows_count-1):
    for cols in range(cols_count-1):
        element = matrix[rows][cols]
        if element == matrix[rows][cols + 1]:
            if element == matrix[rows + 1][cols]:
                if element == matrix[rows + 1][cols + 1]:
                    points_found += 1

print(points_found)
