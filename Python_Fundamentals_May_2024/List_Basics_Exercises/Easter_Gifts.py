gift_for_buying = input().split()
said = input()

while said != 'No Money':
    cmd = said.split()
    if cmd[0] == 'OutOfStock':
        for x in range(len(gift_for_buying)):
            if gift_for_buying[x] == cmd[1]:
                gift_for_buying[x] = 'None'
    elif cmd[0] == 'Required':
        if 0 <= int(cmd[2]) < len(gift_for_buying):
            gift_for_buying[int(cmd[2])] = cmd[1]
    elif cmd[0] == 'JustInCase':
        gift_for_buying[-1] = cmd[1]
    said = input()

gift_for_buying = [gift for gift in gift_for_buying if gift != 'None']
print(*gift_for_buying)
