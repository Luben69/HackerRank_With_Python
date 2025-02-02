our_string = input("String to repeat:\n")

while True:
    try:
        x = int(input())
        print(our_string * x)
        break
    except ValueError:
        print("Variable times must be an integer")
