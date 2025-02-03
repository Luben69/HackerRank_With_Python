# LOGIC
def calc_sum(nums, idx):
    if idx == len(nums) - 1:
        return nums[idx]
    return nums[idx] + calc_sum(nums, idx + 1)


# READ USER INPUT
n = [int(num) for num in input().split()]

# OUTPUT
print(calc_sum(n, 0))
