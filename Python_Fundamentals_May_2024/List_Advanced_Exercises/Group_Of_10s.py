sequence_of_numbers = [int(x) for x in input().split(", ")]
target = 10
result = []
while sequence_of_numbers:
    group = [n for n in sequence_of_numbers if n <= target]
    sequence_of_numbers = [i for i in sequence_of_numbers if i > target]
    result.append(f"Group of {target}'s: {group}")

    target += 10

for el in result:
    print(el)
