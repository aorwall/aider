class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if grade in self.students:
            self.students[grade].append(name)
            self.students[grade].sort()
        else:
            self.students[grade] = [name]

    def roster(self):
        all_students = []
        for grade in sorted(self.students.keys()):
            all_students.extend(self.students[grade])
        return all_students

    def grade(self, grade_number):
        if grade_number in self.students:
            return self.students[grade_number]
        else:
            return []

    def added(self):
        added_list = []
        for grade in self.students:
            added_list.extend([True] * len(self.students[grade]))
        return added_list