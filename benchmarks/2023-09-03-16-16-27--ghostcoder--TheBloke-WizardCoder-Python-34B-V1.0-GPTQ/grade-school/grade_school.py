class School:
    def __init__(self):
        self._roster = {}

    def add_student(self, name, grade):
        if name in [item for sublist in self._roster.values() for item in sublist]:
            return f"{name} is already in our records."
        else:
            self._roster.setdefault(grade, []).append(name)
            return "OK"

    def roster(self):
        result = ""
        for grade in sorted(self._roster.keys()):
            students = ", ".join(sorted(self._roster[grade]))
            result += f"Students in grade {grade}: {students}\n"
        return result

    def grade(self, grade_number):
        try:
            students = self._roster[grade_number]
            return ", ".join(sorted(students)) + f"\n{len(students)} students in total"
        except KeyError:
            return "No students found in grade {grade_number}"

    def get_added(self):
        return "\n".join([f"{key}: {', '.join(value)}" for key, value in self._roster.items()])
