train_ticket = 150
collection_of_items = input().split("|")
budget = float(input())
for_profit = []

wardrobe = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

for x in collection_of_items:
    type_of_cloth, price = x.split("->")
    price = float(price)

    if price <= wardrobe.get(type_of_cloth) and budget >= price:
        budget -= price
        for_profit.append(price)

new_prices = [el * 1.4 for el in for_profit]

print(' '.join([f"{el:.2f}" for el in new_prices]))
print(f"Profit: {sum(new_prices) - sum(for_profit):.2f}")
budget += sum(new_prices)

if budget >= train_ticket:
    print('Hello, France!')
else:
    print('Not enough money.')
