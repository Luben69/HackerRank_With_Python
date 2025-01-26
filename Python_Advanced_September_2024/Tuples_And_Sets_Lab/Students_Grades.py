number_of_students = int(input())

occ = {}

for _ in range(number_of_students):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in occ:
        occ[name] = []
    occ[name].append(grade)


for student_name, grades in occ.items():
    avg_grade = sum(grades) / len(grades)

    print(f"{student_name} -> {' '.join([f'{el:.2f}' for el in grades])} (avg: {avg_grade:.2f})")
