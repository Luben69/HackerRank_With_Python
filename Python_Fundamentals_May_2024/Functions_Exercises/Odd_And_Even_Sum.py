def odd_and_even_sum(y):
    sum_of_odd = 0
    sum_of_even = 0

    for char in y:
        if int(char) % 2 == 0:
            sum_of_even += int(char)
        else:
            sum_of_odd += int(char)

    return f"Odd sum = {sum_of_odd}, Even sum = {sum_of_even}"


single_number = input()
print(odd_and_even_sum(single_number))
