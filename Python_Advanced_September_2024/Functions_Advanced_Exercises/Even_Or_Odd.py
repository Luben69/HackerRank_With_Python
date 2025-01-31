def even_odd(*args):
    the_numbers = []
    if args[-1] == 'even':
        for i in args:
            if isinstance(i, int):
                if i % 2 == 0:
                    the_numbers.append(i)

    elif args[-1] == 'odd':
        for i in args:
            if isinstance(i, int):
                if i % 2 != 0:
                    the_numbers.append(i)

    return the_numbers

