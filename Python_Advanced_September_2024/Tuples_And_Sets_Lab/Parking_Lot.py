n_of_commands = int(input())

parking_lot = set()

for _ in range(n_of_commands):
    direction, car_number = input().split(", ")

    if direction == 'IN':
        parking_lot.add(car_number)
    elif direction == 'OUT':
        parking_lot.remove(car_number)

if not parking_lot:
    print('Parking Lot is Empty')
else:
    print(*parking_lot, sep="\n")
