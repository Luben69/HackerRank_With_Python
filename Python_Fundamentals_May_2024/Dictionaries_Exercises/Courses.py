courses = {}
while True:
    cmd = input()
    if cmd == 'end':
        break

    course_name, user = cmd.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(user)


for k, v in courses.items():
    print(f"{k}: {len(v)}")
    for el in v:
        print(f"-- {el}")