try:
    file = open("text.txt")
    print("---FILE FOUND---\n")
    print(file.read())
except FileNotFoundError:
    print("---FILE NOT FOUND---")
