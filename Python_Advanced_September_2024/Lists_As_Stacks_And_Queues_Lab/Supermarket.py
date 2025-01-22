from collections import deque

all_people = deque()
command = input()


while command != 'End':
    if command == 'Paid':
        while all_people:
            print(all_people.popleft())

    else:
        all_people.append(command)

    command = input()

print(f'{len(all_people)} people remaining.')
