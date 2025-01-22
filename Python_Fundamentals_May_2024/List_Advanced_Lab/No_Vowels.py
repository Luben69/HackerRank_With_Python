def remove_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = ''.join([ch for ch in text if ch.lower() not in vowels])
    return result


our_string = input()
print(remove_vowels(our_string))
