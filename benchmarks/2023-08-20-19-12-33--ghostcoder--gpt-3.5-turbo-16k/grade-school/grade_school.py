class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            self.students[grade].append(name)
        else:
            self.students[grade] = [name]

    def roster(self):
        sorted_students = []
        for grade in sorted(self.students.keys()):
            sorted_students.extend(sorted(self.students[grade]))
        return sorted_students

    def grade(self, grade_number):
        if grade_number in self.students:
            return sorted(self.students[grade_number])
        else:
            return []

    def added(self):
        return [True] * sum(len(names) for names in self.students.values())