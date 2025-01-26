rows_count = int(input())

matrix = []
left = []
right = []

for _ in range(rows_count):
    row_data = [int(x) for x in input().split()]
    matrix.append(row_data)


for i, j in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    left.append(a)
    right.append(b)

print(f'{abs(sum(left)- sum(right))}')
