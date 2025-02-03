# LOGIC
def choice_coins(coins, remain):
    coins.sort(reverse=True)
    returned_count = {}

    idx = 0

    while idx < len(coins) and remain != 0:
        returned = remain // coins[idx]
        remain %= coins[idx]
        if returned > 0:
            returned_count[coins[idx]] = returned

        idx += 1

    if remain != 0:
        return "Error"
    result = f"Number of coins to take: {sum(returned_count.values())}\n"
    for k, v in returned_count.items():
        result += f"{v} coin(s) with value {k}\n"

    return result


# READ USER INPUT
coins_list = [int(num) for num in input().split(", ")]
change = int(input())

# OUTPUT
print(choice_coins(coins_list, change))
