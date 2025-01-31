def kwargs_length(**kwargs):
    count = 0
    mutable = sorted(kwargs.items(), key=lambda x: (len(x[0])))

    for el in mutable:
        count += 1

    return count


dictionary = {}

print(kwargs_length(**dictionary))
