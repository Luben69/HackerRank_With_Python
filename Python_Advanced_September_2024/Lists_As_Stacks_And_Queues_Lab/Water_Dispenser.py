from collections import deque

line_of_people = deque()
starting_quantity = int(input())

names = input()

while names != 'Start':

    line_of_people.append(names)
    names = input()


command = input()

while command != 'End':

    if command.isdigit():

        if starting_quantity >= int(command):
            starting_quantity = starting_quantity - int(command)
            print(f'{line_of_people.popleft()} got water')

        elif int(command) > starting_quantity:
            print(f'{line_of_people.popleft()} must wait')

    else:
        refill_command, new_liters = command.split()
        new_liters = int(new_liters)
        starting_quantity += new_liters

    command = input()

print(f'{starting_quantity} liters left')
