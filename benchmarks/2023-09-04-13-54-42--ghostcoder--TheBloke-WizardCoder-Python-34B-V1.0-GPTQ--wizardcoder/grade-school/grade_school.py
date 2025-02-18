from collections import defaultdict

class School:
    def __init__(self):
        self._roster = defaultdict(set)
        self._added = set()

    def add_student(self, name, grade):
        if name not in self._added:
            self._roster[grade].add(name)
            self._added.add(name)
        else:
            raise ValueError(f"{name} has already been added.")

    def roster(self):
        return sorted([name for grade in sorted(self._roster.keys()) for name in sorted(self._roster[grade])])

    def grade(self, grade_number):
        return sorted(self._roster[grade_number])

    def added(self):
        return self._added
