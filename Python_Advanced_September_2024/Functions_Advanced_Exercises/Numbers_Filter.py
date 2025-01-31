def even_odd_filter(**kwargs):
    result = {}

    for k, v in kwargs.items():
        if k == 'even':
            result[k] = [num for num in v if num % 2 == 0]
        elif k == 'odd':
            result[k] = [num for num in v if num % 2 != 0]

    sorted_thing = dict(sorted(result.items(), key=lambda x: len(x[1]), reverse=True))

    return sorted_thing
