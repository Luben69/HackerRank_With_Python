from collections import deque
from datetime import datetime, timedelta

robots_input = input()
robots_data = robots_input.split(";")


robots = []
for robot in robots_data:
    name, process_time = robot.split("-")
    robots.append({"name": name, "process_time": int(process_time), "available_at": None})

start_time = datetime.strptime(input(), "%H:%M:%S")

products = deque()
while True:
    product = input()
    if product == "End":
        break
    products.append(product)

current_time = start_time
while products:
    current_time += timedelta(seconds=1)
    product = products.popleft()

    for robot in robots:
        if robot["available_at"] is None or current_time >= robot["available_at"]:
            robot["available_at"] = current_time + timedelta(seconds=robot["process_time"])
            print(f"{robot['name']} - {product} [{current_time.strftime('%H:%M:%S')}]")
            break
    else:
        products.append(product)
