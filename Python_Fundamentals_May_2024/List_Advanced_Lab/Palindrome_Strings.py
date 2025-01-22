string = [x for x in input().split() if x == x[::-1]]
our_palindrome = input()
print(string)
print(f"Found palindrome {string.count(our_palindrome)} times")
