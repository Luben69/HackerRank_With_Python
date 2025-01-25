from collections import deque

number_of_petrol_pumps = int(input())
pumps = deque()


for _ in range(number_of_petrol_pumps):
    added_amount_of_petrol, distance = input().split()
    pumps.append([int(added_amount_of_petrol), int(distance)])

start_positions = 0
stops = 0

while stops < number_of_petrol_pumps:
    fuel = 0
    for i in range(number_of_petrol_pumps):
        fuel += pumps[i][0]
        destination = pumps[i][1]
        if fuel < destination:
            pumps.rotate(-1)
            start_positions += 1
            stops = 0
            break
        fuel -= destination
        stops += 1

print(start_positions)
