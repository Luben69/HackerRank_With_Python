n = int(input())
total_free_chairs = 0
count_visitors = 0
problem = False

for rooms in range(n):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])

    if visitors > chairs:
        print(f"{visitors - chairs} more chairs needed in room {rooms + 1}")
        problem = True
    else:
        total_free_chairs += chairs - visitors

if not problem:
    print(f"Game On, {total_free_chairs} free chairs left")
