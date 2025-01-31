def grocery_store(**kwargs):
    new = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    return "\n".join(f"{product}: {quantity}" for product, quantity in new)
