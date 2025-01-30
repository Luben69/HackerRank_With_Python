n = int(input())
matrix = []

for _ in range(n):
    rows_data = [int(x) for x in input().split()]
    matrix.append(rows_data)

indices_of_bombs = input().split()


def get_cells(x, y, s):
    cells = []

    if x - 1 in range(s) and y - 1 in range(s):
        cells.append((x - 1, y - 1))
    if x in range(s) and y - 1 in range(s):
        cells.append((x, y - 1))
    if x + 1 in range(s) and y - 1 in range(s):
        cells.append((x + 1, y - 1))
    if x - 1 in range(s) and y in range(s):
        cells.append((x - 1, y))
    if x + 1 in range(s) and y in range(s):
        cells.append((x + 1, y))
    if x - 1 in range(s) and y + 1 in range(s):
        cells.append((x - 1, y + 1))
    if x in range(s) and y + 1 in range(s):
        cells.append((x, y + 1))
    if x + 1 in range(s) and y + 1 in range(s):
        cells.append((x + 1, y + 1))

    return cells


for bomb in indices_of_bombs:
    row, col = [int(x) for x in bomb.split(',')]
    current_bomb = matrix[row][col]
    if current_bomb > 0:
        neighbour_cells = get_cells(row, col, n)
        for r, c in neighbour_cells:
            if matrix[r][c] > 0:
                matrix[r][c] -= current_bomb
        matrix[row][col] = 0

result_count = 0
result_sum = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            result_count += 1
            result_sum += matrix[row][col]

print(f"Alive cells: {result_count}")
print(f"Sum: {result_sum}")

for row in range(n):
    print(*matrix[row])
