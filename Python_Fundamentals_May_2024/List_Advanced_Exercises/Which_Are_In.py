first_string = input().split(", ")
second_string = input().split(", ")
found_elements = []

for target in first_string:
    for el in second_string:
        if target in el:
            found_elements.append(target)
            break

print(found_elements)
