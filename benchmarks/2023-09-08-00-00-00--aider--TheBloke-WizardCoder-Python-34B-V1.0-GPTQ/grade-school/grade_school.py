class School:
    def __init__(self):
        self.roster = {}

    def add_student(self, name, grade):
        if grade not in self.roster:
            self.roster[grade] = []
        if name in self.roster[grade]:
            raise ValueError("Student already in grade.")
        self.roster[grade].append(name)

    def get_roster(self):
        return self.roster

    def get_students_in_grade(self, grade_number):
        if grade_number not in self.roster:
            return []
        return sorted(self.roster[grade_number])

    def get_all_students(self):
        all_students = []
        for grade in sorted(self.roster.keys()):
            for student in self.roster[grade]:
                all_students.append(student)
        return all_students
