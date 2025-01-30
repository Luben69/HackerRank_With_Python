from collections import deque

rows, cols = map(int, input().split())
lair = [list(input()) for _ in range(rows)]
commands = input()

bunnies = deque()
player_row, player_col = None, None

for r in range(rows):
    for c in range(cols):
        if lair[r][c] == "P":
            player_row, player_col = r, c
        elif lair[r][c] == "B":
            bunnies.append((r, c))

moves = {
    "L": (0, -1),
    "R": (0, 1),
    "U": (-1, 0),
    "D": (1, 0),
}


def spread_bunnies():
    new_bunnies = deque()
    for r, c in bunnies:
        for dr, dc in moves.values():
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < rows and 0 <= new_c < cols and lair[new_r][new_c] != "B":
                lair[new_r][new_c] = "B"
                new_bunnies.append((new_r, new_c))
    return new_bunnies


for move in commands:
    new_row, new_col = player_row + moves[move][0], player_col + moves[move][1]

    lair[player_row][player_col] = "."

    if not (0 <= new_row < rows and 0 <= new_col < cols):
        bunnies = spread_bunnies()
        for row in lair:
            print("".join(row))
        print(f"won: {player_row} {player_col}")
        exit()

    player_row, player_col = new_row, new_col

    if lair[player_row][player_col] == "B":
        bunnies = spread_bunnies()
        for row in lair:
            print("".join(row))
        print(f"dead: {player_row} {player_col}")
        exit()

    lair[player_row][player_col] = "P"

    bunnies = spread_bunnies()

    if lair[player_row][player_col] == "B":
        for row in lair:
            print("".join(row))
        print(f"dead: {player_row} {player_col}")
        exit()
