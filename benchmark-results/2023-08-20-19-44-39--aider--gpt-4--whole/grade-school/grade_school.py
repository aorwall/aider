class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []
        if name in self.students[grade]:
            return "This student is already added."
        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self):
        roster = []
        for grade in sorted(self.students):
            roster.extend(self.students[grade])
        return roster

    def grade(self, grade_number):
        if grade_number in self.students:
            return self.students[grade_number]
        return []

    def added(self):
        return self.students
