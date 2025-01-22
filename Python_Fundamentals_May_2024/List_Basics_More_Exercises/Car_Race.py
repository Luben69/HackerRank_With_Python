times = list(map(int, input().split()))

middle_index = len(times) // 2
left_car = times[:middle_index]
right_car = times[middle_index + 1:][::-1]


def calculate_time(car):
    total_time = 0
    for time in car:
        if time == 0:
            total_time *= 0.8
        else:
            total_time += time
    return total_time


left_time = calculate_time(left_car)
right_time = calculate_time(right_car)

if left_time < right_time:
    winner = "left"
    total_time = left_time
else:
    winner = "right"
    total_time = right_time

print(f"The winner is {winner} with total time: {total_time:.1f}")
