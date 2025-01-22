number_of_lines = int(input())
capacity = 0  # 255

for _ in range(number_of_lines):
    added_liters_of_water = int(input())
    capacity += added_liters_of_water

    if capacity > 255:
        print("Insufficient capacity!")
        capacity -= added_liters_of_water

print(capacity)
