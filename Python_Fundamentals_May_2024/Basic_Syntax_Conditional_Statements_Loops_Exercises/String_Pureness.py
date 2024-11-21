n = int(input())

for word in range(n):
    string = input()
    if "." in string or "_" in string or "," in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")