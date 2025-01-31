rows_count = int(input())

matrix = []

for _ in range(rows_count):
    rows_data = [int(x) for x in input().split()]
    matrix.append(rows_data)

command = input().split()

while command[0] != 'END':
    row, col = int(command[1]), int(command[2])

    if row < 0 or row >= rows_count or col < 0 or col >= len(matrix[row]):
        print('Invalid coordinates')
    else:
        if command[0] == 'Add':
            matrix[row][col] += int(command[3])
        elif command[0] == 'Subtract':
            matrix[row][col] -= int(command[3])

    command = input().split()

for r in matrix:
    print(' '.join(map(str, r)))
