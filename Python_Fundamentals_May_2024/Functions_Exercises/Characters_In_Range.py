def characters_in_between(char1, char2):
    # Get ASCII values of the characters
    ascii1 = ord(char1)
    ascii2 = ord(char2)

    result = [chr(i) for i in range(ascii1 + 1, ascii2)]

    return ' '.join(result)


a = input()
b = input()

print(characters_in_between(a, b))
