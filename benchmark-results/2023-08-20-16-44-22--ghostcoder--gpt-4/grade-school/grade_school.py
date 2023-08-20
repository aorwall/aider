class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade not in self.students:
            self.students[grade] = []
        if name not in self.students[grade]:
            self.students[grade].append(name)
            self.students[grade].sort()
        else:
            return "Student already added."

    def roster(self):
        roster = []
        for grade in sorted(self.students.keys()):
            for student in self.students[grade]:
                roster.append(student)
        return roster

    def grade(self, grade_number):
        if grade_number in self.students:
            return self.students[grade_number]
        else:
            return []

    def added(self):
        added_students = []
        for grade in sorted(self.students.keys()):
            added_students.append(self.students[grade])
        return added_students