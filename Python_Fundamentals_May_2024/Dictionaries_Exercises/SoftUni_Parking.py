our_dic = {}
n = int(input())
for _ in range(n):
    whole_string = input().split()
    cmd = whole_string[0]
    username = whole_string[1]
    license_plate = whole_string[2] if len(whole_string) > 2 else None
    # cmd, username, license_plate = whole_string.split()
    if cmd == 'register':
        if username in our_dic:
            print(f"ERROR: already registered with plate number {license_plate}")
        else:
            our_dic[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
    elif cmd == 'unregister':
        if username not in our_dic:
            print(f"ERROR: user {username} not found")
        else:
            our_dic.pop(username)
            print(f"{username} unregistered successfully")

for k, v in our_dic.items():
    print(f"{k} => {v}")