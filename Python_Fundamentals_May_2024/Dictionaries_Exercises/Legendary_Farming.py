our_items = {'shards': 0, 'fragments': 0, 'motes': 0}
found = False

while not found:
    lines = input().split()
    for el in range(0, len(lines), 2):
        quantity = int(lines[el])
        material = lines[el + 1].lower()

        if material not in our_items:
            our_items[material] = 0
        our_items[material] += quantity

        if our_items["shards"] >= 250:
            our_items["shards"] -= 250
            print("Shadowmourne obtained!")
            found = True
            break
        elif our_items["fragments"] >= 250:
            our_items["fragments"] -= 250
            print("Valanyr obtained!")
            found = True
            break
        elif our_items["motes"] >= 250:
            our_items["motes"] -= 250
            print("Dragonwrath obtained!")
            found = True
            break

for k, v in our_items.items():
    print(f"{k}: {v}")
