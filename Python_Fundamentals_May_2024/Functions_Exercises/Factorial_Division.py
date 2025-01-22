import math


def factorial_division(num1, num2):
    factorial1 = math.factorial(num1)
    factorial2 = math.factorial(num2)

    result = factorial1 / factorial2

    print(f"{result:.2f}")


n1 = int(input())
n2 = int(input())
factorial_division(n1, n2)
