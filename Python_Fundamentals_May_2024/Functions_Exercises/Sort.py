def the_function(y):
    numbs_as_int = []

    for char in y:
        numbs_as_int.append(int(char))

    return sorted(numbs_as_int)


sequence_of_numbers = input().split()
print(the_function(sequence_of_numbers))
