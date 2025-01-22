n = int(input())

positive_numbs = []

negative_numbs = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        positive_numbs.append(number)
    else:
        negative_numbs.append(number)

print(positive_numbs)
print(negative_numbs)
print(f"Count of positives: {len(positive_numbs)}")
print(f"Sum of negatives: {sum(negative_numbs)}")
