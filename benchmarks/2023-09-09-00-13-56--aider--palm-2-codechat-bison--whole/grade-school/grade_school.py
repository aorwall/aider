class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if name in self.students:
            raise ValueError("Student already added")
        self.students[name] = grade

    def roster(self):
        return sorted(self.students.keys())

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))

    def added(self):
        return len(self.students)
