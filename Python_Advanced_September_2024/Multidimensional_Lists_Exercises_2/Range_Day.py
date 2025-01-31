matrix = []

your_position = []

targets = 0

for rows in range(5):
    matrix.append(input().split())
    for cols in range(5):
        if matrix[rows][cols] == "A":
            your_position = [rows, cols]
        if matrix[rows][cols] == "x":
            targets += 1

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

n = int(input())
targets_down = []

for _ in range(n):
    command = input().split()

    if command[0] == "shoot":
        row = your_position[0] + directions[command[1]][0]
        col = your_position[1] + directions[command[1]][1]

        while 0 <= row < 5 and 0 <= col < 5:
            if matrix[row][col] == "x":
                matrix[row][col] = "."
                targets -= 1
                targets_down.append([row, col])
                break
            row += directions[command[1]][0]
            col += directions[command[1]][1]

        if targets == 0:
            print(f"Training completed! All {len(targets_down)} targets hit.")
            break

    elif command[0] == "move":
        row = your_position[0] + directions[command[1]][0] * int(command[2])
        col = your_position[1] + directions[command[1]][1] * int(command[2])

        if 0 <= row < 5 and 0 <= col < 5 and matrix[row][col] == ".":
            matrix[row][col] = "A"
            matrix[your_position[0]][your_position[1]] = "."
            your_position = [row, col]

if targets > 0:
    print(f"Training not completed! {targets} targets left.")

[print(r) for r in targets_down]