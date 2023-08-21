class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []
        if name not in self.students[grade]:
            self.students[grade].append(name)

    def roster(self):
        roster = []
        for grade in sorted(self.students):
            roster.extend(sorted(self.students[grade]))
        return roster

    def grade(self, grade_number):
        if grade_number in self.students:
            return sorted(self.students[grade_number])
        return []

    def added(self):
        return {grade: sorted(names) for grade, names in self.students.items()}
