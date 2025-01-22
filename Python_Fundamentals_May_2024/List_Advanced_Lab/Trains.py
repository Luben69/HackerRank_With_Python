n = int(input())
train_list = [0] * n
while True:
    command = input()
    if command == "End":
        break

    command = command.split()

    if command[0] == "add":
        people = int(command[1])
        train_list[-1] += people

    elif command[0] == "insert":
        index = int(command[1])
        people = int(command[2])
        train_list[index] += people

    elif command[0] == "leave":
        index = int(command[1])
        people = int(command[2])
        train_list[index] -= people

print(train_list)
