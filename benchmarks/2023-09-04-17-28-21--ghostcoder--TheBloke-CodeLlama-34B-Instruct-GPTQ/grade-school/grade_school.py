from collections import defaultdict

class School:
    def __init__(self):
        self._roster = defaultdict(list)

    def add_student(self, name, grade):
        if name in self._roster[grade]:
            raise ValueError('Student already exists')

        self._roster[grade].append(name)
        self._roster[grade].sort()

    def roster(self):
        result = []
        for grade in sorted(self._roster.keys()):
            result += self._roster[grade]
        return result

    def grade(self, grade_number):
        if grade_number not in self._roster:
            return []
        else:
            return self._roster[grade_number]

    def added(self):
        return len(self._roster) > 0
