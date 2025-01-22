def is_perfect_number(number):
    if number < 1:
        return "It's not so perfect."

    # Find the sum of all proper divisors of the number
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)

    # Check if the sum of divisors equals the number
    if divisors_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


output = int(input())
print(is_perfect_number(output))