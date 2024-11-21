command = input()
coffee = 0

while command != "END":
    if command == command.lower():
        if command == "dog":
            coffee += 1
        elif command == "cat":
            coffee += 1
        elif command == "movie":
            coffee += 1
        elif command == "coding":
            coffee += 1
        else:
            print()

    elif command == command.upper():
        if command == "DOG":
            coffee += 2
        elif command == "CAT":
            coffee += 2
        elif command == "MOVIE":
            coffee += 2
        elif command == "CODING":
            coffee += 2
        else:
            print()

    command = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)
