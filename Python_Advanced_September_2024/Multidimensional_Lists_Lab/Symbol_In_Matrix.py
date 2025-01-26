n = int(input())

matrix = []

found = False

for _ in range(n):
    data = [x for x in input()]
    matrix.append(data)

symbol = input()

position = None

for row_index in range(n):
    for col_index in range(n):
        if matrix[row_index][col_index] == symbol:
            position = (row_index, col_index)
            print(position)
            exit()


print(f'{symbol} does not occur in the matrix')
