students = []

while True:
    command = input()
    if ":" not in command:
        course_name = command.replace("_", " ")
        break

    name, student_id, course = command.split(":")
    students.append((name, student_id, course))

for n, s_id, course_taken in students:
    if course_taken == course_name:
        print(f"{n} - {s_id}")
