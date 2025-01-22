def our_func(n):
    percentage = int(n / 10)

    result = f"[{'%'* percentage}{'.'* (10 - percentage)}]"
    if percentage == 10:
        print(f"{n}% Complete!")
        return result
    else:
        print(f"{n}% {result}")
        return "Still loading..."


number = int(input())
print(our_func(number))
