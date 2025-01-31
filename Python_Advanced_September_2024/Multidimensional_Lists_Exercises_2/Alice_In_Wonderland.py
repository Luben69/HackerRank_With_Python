n = int(input())

matrix = []
alice_location = []

for row in range(n):
    matrix.append(input().split())
    for col in range(n):
        if matrix[row][col] == "A":
            matrix[row][col] = "*"
            alice_location = [row, col]

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

collected_teas = 0

while collected_teas < 10:
    command = input()

    # Determining the next move
    current_move = moves[command]
    row = alice_location[0] + current_move[0]
    col = alice_location[1] + current_move[1]

    if row < 0 or row >= n or col < 0 or col >= n:
        break

    if matrix[row][col] == "R":
        matrix[row][col] = "*"
        break

    if matrix[row][col] not in ['*', '.']:
        collected_teas += int(matrix[row][col])

    matrix[row][col] = "*"
    alice_location = [row, col]

if collected_teas >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(" ".join(row)) for row in matrix]