from errors import UnknownSignError


def sum_nums(num1, num2):
    return num1 + num2


def subtract_nums(num1, num2):
    return num1 - num2


def multiply_nums(num1, num2):
    return num1 * num2


def divide_nums(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "Cannot divide by zero!"


def power(num1, num2):
    return num1 ** num2


mapper = {
    "+": sum_nums,
    "-": subtract_nums,
    "*": multiply_nums,
    "/": divide_nums,
    "^": power
}


def execute(num1, sign, num2):
    if sign in mapper:
        respective_function = mapper[sign]
        return respective_function(num1, num2)
    raise UnknownSignError("Please provide a valid sign !")
