# LOGIC
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        mid_idx = (left + right) // 2
        mid_el = numbers[mid_idx]

        if mid_el == target:
            return mid_idx
        if mid_el < target:
            left = mid_idx + 1
        else:
            right = mid_idx - 1

    return -1

# READ USER INPUT


nums = [int(num) for num in input().split()]
target = int(input())

# OUTPUT
print(binary_search(nums, target))
