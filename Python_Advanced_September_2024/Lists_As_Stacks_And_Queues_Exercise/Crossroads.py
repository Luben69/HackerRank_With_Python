from collections import deque

def main():
    green_light = int(input())
    window = int(input())
    cars = deque()
    car_counter = 0
    car_crash = False

    while True:
        command = input()

        if command.upper() == "END":
            break

        if command.lower() == "green":
            current_light = green_light

            while current_light > 0:
                if cars:
                    current_car = cars.popleft()

                    if current_light - len(current_car) < 0:
                        # Check if the car can pass during the free window
                        if current_light - len(current_car) + window >= 0:
                            car_counter += 1
                            break
                        else:
                            # Crash occurred
                            hit_character = current_car[current_light + window]
                            print("A crash happened!")
                            print(f"{current_car} was hit at {hit_character}.")
                            car_crash = True
                            break

                    current_light -= len(current_car)
                    car_counter += 1
                else:
                    break
        else:
            # Add car to the queue
            cars.append(command)

        if car_crash:
            break

    if not car_crash:
        print("Everyone is safe.")
        print(f"{car_counter} total cars passed the crossroads.")

if __name__ == "__main__":
    main()
