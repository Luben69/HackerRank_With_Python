our_names = input().split(", ")

sorted_names = sorted(our_names, key=lambda x: (-len(x), x))
print(sorted_names)
