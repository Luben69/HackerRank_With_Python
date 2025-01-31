from functools import reduce

def operate(sign, *args):
    def summ():
        return reduce(lambda x, y: x + y, args)

    def subtract():
        return reduce(lambda x, y: x - y, args)

    def multiply():
        return reduce(lambda x, y: x * y, args)

    def divide():
        return reduce(lambda x, y: x / y, args)

    if sign == "+":
        return summ()
    elif sign == "-":
        return subtract()
    elif sign == "*":
        return multiply()
    elif sign == "/":
        return divide()
