def calculator():
    command = input()
    n1 = int(input())
    n2 = int(input())

    if command == 'add':
        print(n1 + n2)
    elif command == 'subtract':
        print(n1 - n2)
    elif command == 'multiply':
        print(n1 * n2)
    elif command == 'divide':
        print(int(n1 / n2))


calculator()
