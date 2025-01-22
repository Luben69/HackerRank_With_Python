n = int(input())
total_price = 0

for order in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_needed_per_day not in range(1, 2000 + 1):
        continue

    price = price_per_capsule * days * capsules_needed_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")
