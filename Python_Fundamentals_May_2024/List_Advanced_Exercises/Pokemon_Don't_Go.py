def processing(our_list, removed):
    for el in range(len(our_list)):
        if our_list[el] <= removed:
            our_list[el] += removed
        else:
            our_list[el] -= removed

    return our_list


sequence_of_integers = [int(x) for x in input().split()]
removed_elements = []

while sequence_of_integers:
    index = int(input())
    if index < 0:
        removed_element = sequence_of_integers[0]
        removed_elements.append(removed_element)
        del sequence_of_integers[0]
        sequence_of_integers.insert(0, sequence_of_integers[-1])
        sequence_of_integers = processing(sequence_of_integers, removed_element)

    elif index > len(sequence_of_integers) - 1:
        removed_element = sequence_of_integers[-1]
        removed_elements.append(removed_element)
        del sequence_of_integers[-1]
        sequence_of_integers.append(sequence_of_integers[0])
        sequence_of_integers = processing(sequence_of_integers, removed_element)

    else:
        removed_element = sequence_of_integers[index]
        removed_elements.append(removed_element)
        sequence_of_integers = sequence_of_integers[:index] + sequence_of_integers[index + 1:]
        sequence_of_integers = processing(sequence_of_integers, removed_element)

print(sum(removed_elements))
