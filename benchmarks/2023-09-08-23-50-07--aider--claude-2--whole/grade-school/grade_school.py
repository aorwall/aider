class School:
    def __init__(self):
        self.rosters = {}

    def add_student(self, name, grade):
        if grade not in self.rosters:
            self.rosters[grade] = []
        if name not in self.rosters[grade]:
            self.rosters[grade].append(name)
            return True
        else:
            print(f"{name} is already enrolled in grade {grade}")
            return False

    def roster(self):
        return [name for names in self.rosters.values() for name in names]

    def grade(self, grade_number):
        return sorted(self.rosters.get(grade_number, []))

    def added(self):
        return self.roster()
