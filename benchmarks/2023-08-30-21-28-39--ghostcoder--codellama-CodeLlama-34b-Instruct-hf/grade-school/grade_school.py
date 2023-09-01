class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []
        self.students[grade].append(name)

    def roster(self):
        return self.students

    def grade(self, grade_number):
        return self.students[grade_number]

    def added(self):
        return [True if name in self.students[grade] else False for grade in self.students for name in self.students[grade]]
