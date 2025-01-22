employees = input().split()
happiness_factor = int(input())
employees_thing = list(map(lambda x: int(x) * happiness_factor, employees))
filtered = list(filter(lambda x: x >= sum(employees_thing) / len(employees_thing), employees_thing))
if len(filtered) >= len(employees_thing) / 2:
    print(f"Score: {len(filtered)}/{len(employees_thing)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees_thing)}. Employees are not happy!")
