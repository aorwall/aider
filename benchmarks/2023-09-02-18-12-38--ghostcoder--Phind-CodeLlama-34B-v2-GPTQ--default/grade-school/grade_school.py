class School:
    def __init__(self):
        self._roster = {}

    def add_student(self, name, grade):
        if name in self._roster.get(grade, []):
            return "Student already exists in this grade."
        else:
            if grade in self._roster:
                self._roster[grade].append(name)
            else:
                self._roster[grade] = [name]
            return "OK."

    def roster(self):
        return {grade: sorted(students) for grade, students in self._roster.items()}

    def grade(self, grade_number):
        if grade_number in self._roster:
            return sorted(self._roster[grade_number])
        else:
            return []

    def added(self):
        return "\n".join([f"{name} in grade {grade}" for grade in sorted(self._roster) for name in sorted(self._roster[grade])])
