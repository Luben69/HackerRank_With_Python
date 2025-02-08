def swap_case(s):
    our_element = ""
    for ch in s:
        if ch == ch.lower():
            our_element += ch.upper()
        elif ch == ch.upper():
            our_element += ch.lower()
        else:
            our_element += ch
    return our_element

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)