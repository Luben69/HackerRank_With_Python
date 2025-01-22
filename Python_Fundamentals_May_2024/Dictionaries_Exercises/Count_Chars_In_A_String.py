the_string = input()
our_dic = {}

for el in the_string:
    if el != ' ':
        if el not in our_dic:
            our_dic[el] = 1
        else:
            our_dic[el] += 1

for k, v in our_dic.items():
    print(f"{k} -> {v}")
