string = input()
while string != "End":
    if string != "SoftUni":
        for character in string:
            print(character * 2, end="")
        print()
    string = input()