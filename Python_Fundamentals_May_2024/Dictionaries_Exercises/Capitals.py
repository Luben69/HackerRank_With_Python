our_dic = {}

countries = input().split(", ")
capitals = input().split(", ")

for country, capital in zip(countries, capitals):
    our_dic[country] = capital

for k, v in our_dic.items():
    print(f"{k} -> {v}")