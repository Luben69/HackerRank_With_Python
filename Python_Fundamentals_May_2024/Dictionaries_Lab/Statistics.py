command = input()
bakery = {}

while command != 'statistics':
    name, quantity = command.split(": ")
    if name not in bakery:
        bakery[name] = 0
    bakery[name] += int(quantity)
    command = input()

print("Products in stock:")
for k, v in bakery.items():
    print(f"- {k}: {v}")

print(f"Total Products: {len(bakery.keys())}")
print(f"Total Quantity: {sum(bakery.values())}")