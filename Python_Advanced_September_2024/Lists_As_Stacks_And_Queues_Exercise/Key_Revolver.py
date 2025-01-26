from collections import deque

price_of_each_bullet = int(input())
size_of_the_gun_barrel = int(input())
bullets = [int(x) for x in input().split()]
locks = deque(int(x) for x in input().split())
win_price = int(input())

count_of_shot_bullets = 0

while bullets and locks:
    current_bullet = bullets.pop()
    count_of_shot_bullets += 1

    if current_bullet > locks[0]:
        print("Ping!")
    else:
        locks.popleft()
        print("Bang!")

    if count_of_shot_bullets % size_of_the_gun_barrel == 0 and bullets:
        print("Reloading!")

if not locks:
    print(f"{len(bullets)} bullets left. "
          f"Earned ${win_price - (count_of_shot_bullets * price_of_each_bullet)}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")
