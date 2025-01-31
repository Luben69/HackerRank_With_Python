presents_max = int(input())
n = int(input())
matrix = []
santa_positions = []
nice_kids_count = 0
good_kids_who_got = 0

for rows in range(n):
    matrix.append(input().split())
    for cols in range(n):
        if matrix[rows][cols] == "S":
            santa_positions = [rows, cols]
        if matrix[rows][cols] == "V":
            nice_kids_count += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while presents_max > 0:
    command = input()
    if command == "Christmas morning":
        break
    row = santa_positions[0] + directions[command][0]
    col = santa_positions[1] + directions[command][1]

    if 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == "V":
            matrix[row][col] = "-"
            good_kids_who_got += 1
            nice_kids_count -= 1
            presents_max -= 1
        elif matrix[row][col] == "X":
            matrix[row][col] = "-"
        elif matrix[row][col] == "C":
            for move in directions.values():
                next_r = row + move[0]
                next_c = col + move[1]
                if matrix[next_r][next_c] in "VX" and presents_max > 0:
                    presents_max -= 1
                    if matrix[next_r][next_c] == "V":
                        nice_kids_count -= 1
                        good_kids_who_got += 1
                    matrix[next_r][next_c] = "-"

        matrix[santa_positions[0]][santa_positions[1]] = "-"
        santa_positions = [row, col]
        matrix[row][col] = "S"

if presents_max <= 0 < nice_kids_count:
    print("Santa ran out of presents!")

for r in matrix:
    print(*r)

if nice_kids_count == 0:
    print(f"Good job, Santa! {good_kids_who_got} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")
