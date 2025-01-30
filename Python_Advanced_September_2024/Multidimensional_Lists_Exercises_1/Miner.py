from collections import deque

field_size = int(input())
commands = deque(input().split())
matrix = []
miner_position = []
coals_count = 0

for row in range(field_size):
    matrix.append(input().split())
    for col in range(field_size):
        if matrix[row][col] == 's':
            miner_position = [row, col]
        elif matrix[row][col] == 'c':
            coals_count += 1

moves = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

while coals_count > 0 and commands:

    if commands[0] in moves:
        current_move = moves[commands.popleft()]
        new_row = miner_position[0] + current_move[0]
        new_col = miner_position[1] + current_move[1]

        if 0 <= new_row < field_size and 0 <= new_col < field_size:
            if matrix[new_row][new_col] == 'c':
                coals_count -= 1
                matrix[new_row][new_col] = '*'

            elif matrix[new_row][new_col] == 'e':
                print(f"Game over! ({new_row}, {new_col})")
                exit()

            matrix[miner_position[0]][miner_position[1]] = '*'
            miner_position = [new_row, new_col]
            matrix[new_row][new_col] = 's'

if coals_count == 0:
    print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
else:
    print(f"{coals_count} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
