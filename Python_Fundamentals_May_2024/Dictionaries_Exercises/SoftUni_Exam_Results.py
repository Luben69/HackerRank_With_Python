user_points_dic = {}
courses_dic = {}
while True:
    current_result = input().split("-")
    if len(current_result) == 1:
        break

    elif len(current_result) == 2:
        name = current_result[0]
        del user_points_dic[name]
    else:
        name, course, points = current_result[0], current_result[1], int(current_result[2])
        if name not in user_points_dic.keys():
            user_points_dic[name] = 0
        if user_points_dic[name] < points:
            user_points_dic[name] = points
        if course not in courses_dic.keys():
            courses_dic[course] = 0
        courses_dic[course] += 1
print("Results:")
for name, max_points in user_points_dic.items():
    print(f"{name} | {max_points}")
print("Submissions:")
for course, number_of_students in courses_dic.items():
    print(f"{course} - {number_of_students}")
