initial_energy = 100
current_energy = 100
initial_coins = 100
closed = False
string_representation = input().split("|")

for x in string_representation:
    if closed:
        break
    event_or_ing, value = x.split("-")
    value = int(value)

    if event_or_ing == "rest":
        gained_energy = min(100 - current_energy, value)
        current_energy += gained_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {current_energy}.")

    elif event_or_ing == 'order':
        if current_energy >= 30:
            current_energy -= 30
            initial_coins += value
            print(f'You earned {value} coins.')
        else:
            current_energy += 50
            print('You had to rest!')
    else:
        if initial_coins >= value:
            initial_coins -= value
            print(f'You bought {event_or_ing}.')
        else:
            closed = True
            print(f"Closed! Cannot afford {event_or_ing}.")

if not closed:
    print("Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {current_energy}")