class School:
    def __init__(self):
        self._db = {}

    def add(self, name, grade):
        if not grade in self._db:
            self._db[grade] = []

        if name not in self._db[grade]:
            self._db[grade].append(name)

        self._db[grade] = sorted(self._db[grade])

    def roster(self, grade):
        if grade in self._db:
            return ", ".join(self._db[grade])
        else:
            return ""

    def grade(self, grade):
        if grade in self._db:
            return f"There are {len(self._db[grade])} students enrolled in that grade."
        else:
            return "No students enrolled in that grade."

    def added():
        total_added = sum([len(students) for students in self._db.values()])
        return f"Total students added so far: {total_added}."
