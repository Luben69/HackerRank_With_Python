# LOGIC
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# READ USER INPUT
number = int(input())

# OUTPUT
print(factorial(number))
