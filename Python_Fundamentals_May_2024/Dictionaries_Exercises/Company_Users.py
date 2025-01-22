our_dic = {}
while True:
    our_string = input()
    if our_string == "End":
        break
    company_name, employee_id = our_string.split(" -> ")
    if company_name not in our_dic:
        our_dic[company_name] = []
    if employee_id not in our_dic[company_name]:
        our_dic[company_name].append(employee_id)

for k, v in our_dic.items():
    print(k)
    for els in v:
        print(f"-- {els}")
