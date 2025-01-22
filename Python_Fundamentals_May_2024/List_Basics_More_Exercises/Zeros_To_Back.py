single_string = input().split(", ")
numbers = [int(num) for num in single_string]
non_zeros = [nm for nm in numbers if nm != 0]
zeros = [0] * numbers.count(0)
result = non_zeros + zeros
print(result)
