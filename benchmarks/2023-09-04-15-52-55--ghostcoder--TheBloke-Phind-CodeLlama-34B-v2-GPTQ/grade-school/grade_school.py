class School:
    def __init__(self):
        self._students = {}

    def add_student(self, name, grade):
        if not name in self._students:
            self._students[name] = grade
            return True
        else:
            return False

    def roster(self):
        roster = []
        for name, grade in self._students.items():
            roster.append((grade, name))

        roster.sort()
        return ', '.join([name for _, name in roster])

    def grade(self, grade_number):
        grade = []
        for name, g in self._students.items():
            if g == grade_number:
                grade.append(name)

        grade.sort()
        return ', '.join(grade) or 'No students found'

    def added(self):
        return list(map(lambda x: True if x > 0 else False, self._students))
