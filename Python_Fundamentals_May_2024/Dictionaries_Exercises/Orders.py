our_store = {}

while True:
    cmd = input()
    if cmd == "buy":
        break
    name, price, quantity = cmd.split()
    price = float(price)
    quantity = int(quantity)

    if name not in our_store:
        our_store[name] = [0, 0]
    our_store[name][0] = price
    our_store[name][1] += quantity


for k, v in our_store.items():
    total_price = v[0] * v[1]
    print(f"{k} -> {total_price:.2f}")
