def rectangle(length, width):
    if type(length) == int and type(width) == int:
        def area(a, b):
            return a * b

        area(length, width)

        def perimeter(c, d):
            return (c + d) * 2

        perimeter(length, width)

        return f"Rectangle area: {area(length,width)}\n"\
            f"Rectangle perimeter: {perimeter(length, width)}"

    else:
        return "Enter valid values!"
