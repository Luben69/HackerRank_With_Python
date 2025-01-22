our_dic = {}
n = int(input())

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in our_dic:
        our_dic[name] = []
    our_dic[name].append(grade)

for k, v in our_dic.items():
    if sum(v) / len(v) >= 4.50:
        print(f"{k} -> {sum(v) / len(v):.2f}")