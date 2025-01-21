class Class:
    __students_count = 22

    def __init__(self, name: str):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if 1 + len(self.students) <= Class.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        return sum(self.grades) / len(self.grades)

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. " \
               f"Average grade: {self.get_average_grade():.2f}"
