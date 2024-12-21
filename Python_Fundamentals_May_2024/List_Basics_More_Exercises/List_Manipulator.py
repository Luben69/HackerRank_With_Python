def exchange(lst, index):
    if 0 <= index < len(lst):
        return lst[index + 1:] + lst[:index + 1]
    else:
        print("Invalid index")
        return lst


def find_max(lst, parity):
    filtered = [i for i, x in enumerate(lst) if x % 2 == (0 if parity == "even" else 1)]
    if not filtered:
        print("No matches")
        return None
    return max(filtered, key=lambda i: (lst[i], i))


def find_min(lst, parity):
    filtered = [i for i, x in enumerate(lst) if x % 2 == (0 if parity == "even" else 1)]
    if not filtered:
        print("No matches")
        return None
    return min(filtered, key=lambda i: (lst[i], -i))


def first(lst, count, parity):
    if count > len(lst):
        print("Invalid count")
        return
    filtered = [x for x in lst if x % 2 == (0 if parity == "even" else 1)]
    print(filtered[:count])


def last(lst, count, parity):
    if count > len(lst):
        print("Invalid count")
        return
    filtered = [x for x in lst if x % 2 == (0 if parity == "even" else 1)]
    print(filtered[-count:])

nums = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break
    parts = command.split()
    cmd = parts[0]

    if cmd == "exchange":
        index = int(parts[1])
        nums = exchange(nums, index)
    elif cmd in ("max", "min"):
        parity = parts[1]
        if cmd == "max":
            result = find_max(nums, parity)
        else:
            result = find_min(nums, parity)
        if result is not None:
            print(result)
    elif cmd in ("first", "last"):
        count = int(parts[1])
        parity = parts[2]
        if cmd == "first":
            first(nums, count, parity)
        else:
            last(nums, count, parity)

print(nums)
