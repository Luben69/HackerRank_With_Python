our_dic = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity = int(input())
    if resource not in our_dic:
        our_dic[resource] = quantity
    else:
        our_dic[resource] += quantity

for k, v in our_dic.items():
    print(f"{k} -> {v}")
