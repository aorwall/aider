class School:
    def __init__(self):
        self.roster = {}

    def add_student(self, name, grade):
        if grade not in self.roster:
            self.roster[grade] = []
        if name not in self.roster[grade]:
            self.roster[grade].append(name)
        else:
            return "Student already enrolled in grade"

    def roster(self):
        return self.roster

    def grade(self, grade_number):
        if grade_number not in self.roster:
            return []
        return sorted(self.roster[grade_number])

    def added(self):
        return sorted([student for grade in self.roster.values() for student in grade])
