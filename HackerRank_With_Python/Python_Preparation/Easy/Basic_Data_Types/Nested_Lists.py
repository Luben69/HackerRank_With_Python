if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])

    students_sorted = sorted(students, key=lambda x: x[1])
    grades = sorted(set([x[1] for x in students]))
    second_lowest_grade = grades[1]

    result = [student[0] for student in students_sorted if student[1] == second_lowest_grade]
    result.sort()

    print("\n".join(result))
