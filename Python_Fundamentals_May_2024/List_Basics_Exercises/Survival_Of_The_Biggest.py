list_of_strings = input().split()
n = int(input())

list_of_integers = []

for char in list_of_strings:
    list_of_integers.append(int(char))

for _ in range(n):
    list_of_integers.remove(min(list_of_integers))

print(", ".join(map(str, list_of_integers)))
