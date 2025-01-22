def the_function(n):
    return n % 2 == 0


sequence_of_numbers = map(int, input().split())

result = list(filter(the_function, sequence_of_numbers))

print(result)
