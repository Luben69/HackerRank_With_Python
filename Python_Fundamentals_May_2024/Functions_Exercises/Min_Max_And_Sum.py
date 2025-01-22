def the_functions(i):
    numbs_as_int = []

    for char in i:
        numbs_as_int.append(int(char))

    print(f'The minimum number is {min(numbs_as_int)}')
    print(f'The maximum number is {max(numbs_as_int)}')
    print(f'The sum number is: {sum(numbs_as_int)}')


sequence_of_numbers = input().split()
the_functions(sequence_of_numbers)
