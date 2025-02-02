import re

with open("./words.txt") as file:
    words = file.read().split()

with open("./all_words.txt") as bigger_file:
    all_words = bigger_file.read()

occ = {}

for word in words:
    pattern = rf"\b{word}\b"
    founded = re.findall(pattern, all_words, flags=re.IGNORECASE)
    occ[word] = len(founded)

sorted_occ = sorted(occ.items(), key=lambda x: x[1], reverse=True)
for k, v in sorted_occ:
    print(f"{k} - {v}")