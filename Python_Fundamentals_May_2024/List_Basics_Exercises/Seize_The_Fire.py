fires_wth_their_cells = input().split('#')
water = int(input())
effort = 0
fires_off = []
for x in fires_wth_their_cells:
    cell = x.split(' = ')
    name = cell[0]
    temp = int(cell[1])
    if name == 'High':
        if 81 <= temp <= 125:
            if water >= temp:
                water -= temp
                fires_off.append(temp)
                effort += temp * 0.25
            else:
                continue
        else:
            continue
    elif name == 'Medium':
        if 51 <= temp <= 80:
            if water >= temp:
                water -= temp
                fires_off.append(temp)
                effort += temp * 0.25
            else:
                continue
        else:
            continue

    elif name == 'Low':
        if 1 <= temp <= 50:
            if water >= temp:
                water -= temp
                fires_off.append(temp)
                effort += temp * 0.25
            else:
                continue
        else:
            continue

print('Cells:')
print("\n".join([f" - {el}" for el in fires_off]))
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(fires_off)}")

