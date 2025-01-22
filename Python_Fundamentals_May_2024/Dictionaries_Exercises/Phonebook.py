our_dic = {}
n = 0

while True:
    our_string = input()
    if "-" not in our_string:
        n = int(our_string)
        break
    origin_name, origin_number = our_string.split("-")
    if origin_name not in our_dic:
        our_dic[origin_name] = origin_number
    else:
        our_dic[origin_name] = origin_number

for _ in range(n):
    search = input()
    if search in our_dic:
        print(f"{search} -> {our_dic[search]}")
    else:
        print(f"Contact {search} does not exist.")