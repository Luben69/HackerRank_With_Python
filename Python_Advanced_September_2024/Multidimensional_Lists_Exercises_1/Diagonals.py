rows_count = int(input())

matrix = []
left = []
right = []

for _ in range(rows_count):
    row_data = [int(x) for x in input().split(", ")]
    matrix.append(row_data)


for i, j in zip(range(0, len(matrix)), range(len(matrix) - 1, -1, -1)):
    a = matrix[i][i]
    b = matrix[i][j]
    left.append(a)
    right.append(b)

print(f"Primary diagonal: {', '.join(str(num) for num in left)}. Sum: {sum(left)}")
print(f"Secondary diagonal: {', '.join(str(num) for num in right)}. Sum: {sum(right)}")
