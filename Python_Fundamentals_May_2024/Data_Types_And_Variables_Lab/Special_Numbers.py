n = int(input())

for num in range(1, n + 1):
    digit_sum = sum(int(digit) for digit in str(num))
    special = digit_sum in {5, 7, 11}
    print(f"{num} -> {special}")