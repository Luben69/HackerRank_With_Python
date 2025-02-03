from core import execute


expression = input()

num1, sign, num2 = expression.split()

num1 = float(num1)
num2 = float(num2)

print(execute(num1, sign, num2))
