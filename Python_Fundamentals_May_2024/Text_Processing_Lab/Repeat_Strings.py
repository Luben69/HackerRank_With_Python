sequence_of_string = input().split()
result = ""
for el in sequence_of_string:
    result += el * len(el)

print(result)