def orders():
    total_price = 0
    command = input()
    count = int(input())

    if command == 'coffee':
        total_price = 1.50 * count
    elif command == 'water':
        total_price = 1.00 * count
    elif command == 'coke':
        total_price = 1.40 * count
    elif command == 'snacks':
        total_price = 2.00 * count

    print(f'{total_price:.2f}')


orders()
