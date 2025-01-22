our_dic = {}
while True:
    command = input()
    if command == "Lumpawaroo":
        break
    if "|" in command:
        force_side, force_user = command.split(" | ")
        force_boolean = False
        for list_of_users in our_dic.values():
            if force_user in list_of_users:
                force_boolean = True
                break
        if not force_boolean:
            if force_side not in our_dic.keys():
                our_dic[force_side] = []
            our_dic[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")
        for list_of_users in our_dic.values():
            if force_user in list_of_users:
                list_of_users.remove(force_user)
                break
        if force_side not in our_dic.keys():
            our_dic[force_side] = []
        our_dic[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for force_side, list_of_users in our_dic.items():
    if list_of_users:
        print(f"Side: {force_side}, Members: {len(list_of_users)}")
        for force_user in list_of_users:
            print(f"! {force_user}")
